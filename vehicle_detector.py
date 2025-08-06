# vehicle_detector.py

import cv2
import json
from darkflow.net.build import TFNet
import config

class VehicleDetector:
    """
    A class to detect vehicles in an image using a pre-trained YOLO model.
    It identifies vehicles in four specific regions of interest (ROIs)
    corresponding to a four-way intersection.
    """

    def __init__(self):
        """
        Initializes the VehicleDetector by loading the YOLO model with
        pre-trained weights using the Darkflow framework.
        """
        # Define model options based on the configuration file
        options = {
            "model": config.MODEL_CFG,
            "load": config.MODEL_WEIGHTS,
            "threshold": config.DETECTION_THRESHOLD,
            "gpu": 0.7  # Use 70% of GPU memory, if available
        }
        
        # Load the TensorFlow model
        print("Loading vehicle detection model...")
        self.tfnet = TFNet(options)
        print("Model loaded successfully.")

        # Define the labels of vehicles we want to detect
        self.vehicle_labels = {'car', 'bus', 'truck', 'motorbike'}

    def detect_vehicles(self, image_path):
        """
        Detects vehicles in the given image and counts them per lane.

        Args:
            image_path (str): The path to the image file to be processed.

        Returns:
            dict: A dictionary containing the vehicle count for each of the four lanes
                  ('right', 'left', 'up', 'down').
        """
        try:
            # Read the image from the specified path
            image = cv2.imread(image_path)
            if image is None:
                raise FileNotFoundError(f"Image not found at path: {image_path}")

            # Get image dimensions
            height, width, _ = image.shape

            # Use the loaded model to get predictions from the image
            predictions = self.tfnet.return_predict(image)

            # Define the regions of interest (ROIs) for each lane
            # These ROIs are defined as percentages of the image dimensions
            # to remain scalable for different image sizes.
            # Format: (x_start, y_start, x_end, y_end)
            rois = {
                'right': (width // 2, 0, width, height // 2),
                'left': (0, height // 2, width // 2, height),
                'up': (0, 0, width // 2, height // 2),
                'down': (width // 2, height // 2, width, height)
            }

            # Initialize a dictionary to store the count of vehicles in each lane
            vehicle_counts = {lane: 0 for lane in rois}

            # Iterate through each prediction from the model
            for prediction in predictions:
                label = prediction['label']
                
                # Check if the detected object is a vehicle
                if label in self.vehicle_labels:
                    # Get the coordinates of the bounding box
                    top_x = prediction['topleft']['x']
                    top_y = prediction['topleft']['y']
                    bottom_x = prediction['bottomright']['x']
                    bottom_y = prediction['bottomright']['y']
                    
                    # Calculate the center of the bounding box
                    center_x = (top_x + bottom_x) / 2
                    center_y = (top_y + bottom_y) / 2

                    # Check which ROI the center of the vehicle falls into
                    for lane, (x1, y1, x2, y2) in rois.items():
                        if x1 < center_x < x2 and y1 < center_y < y2:
                            vehicle_counts[lane] += 1
                            break # Move to the next prediction once assigned to a lane

            return vehicle_counts

        except Exception as e:
            print(f"An error occurred during vehicle detection: {e}")
            # Return zero counts in case of an error
            return {'right': 0, 'left': 0, 'up': 0, 'down': 0}

if __name__ == '__main__':
    """
    Main execution block to allow this script to be run directly from the command line
    for testing purposes.
    """
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Detect vehicles in an image and return counts per lane.")
    parser.add_argument("image_path", type=str, help="Path to the input image file.")
    args = parser.parse_args()

    # Create a detector instance and run detection
    detector = VehicleDetector()
    counts = detector.detect_vehicles(args.image_path)

    # Print the results in a structured JSON format
    print("\n--- Detection Results ---")
    print(json.dumps(counts, indent=4))
    print("-------------------------")

