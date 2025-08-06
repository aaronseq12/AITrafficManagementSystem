# main.py

import argparse
import json
import os
import sys
from vehicle_detector import VehicleDetector
from traffic_manager import TrafficManager
from simulation_gui import SimulationGUI
from arduino import ArduinoConnector
import config

def main():
    """
    The main entry point for the AI Traffic Management System.
    It parses command-line arguments, runs vehicle detection if requested,
    and starts the traffic simulation.
    """
    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(description="AI Traffic Management System")
    parser.add_argument(
        '--use-detection',
        action='store_true',
        help="Run vehicle detection on an image to determine traffic density."
    )
    parser.add_argument(
        '--image-path',
        type=str,
        default=os.path.join('test_images', '1.jpg'),
        help="Path to the intersection image for vehicle detection."
    )
    args = parser.parse_args()

    vehicle_counts = {'right': 10, 'left': 10, 'up': 10, 'down': 10} # Default counts

    # --- Vehicle Detection Stage ---
    if args.use_detection:
        # Check if model weights exist
        if not os.path.exists(config.MODEL_WEIGHTS):
            print("Error: Model weights not found!")
            print(f"Please download 'yolov2.weights' and place it in the '{os.path.basename(config.BASE_DIR)}/bin/' directory.")
            sys.exit(1)
            
        # Check if the image path exists
        if not os.path.exists(args.image_path):
            print(f"Error: Image file not found at '{args.image_path}'")
            sys.exit(1)

        print("--- Starting Vehicle Detection ---")
        detector = VehicleDetector()
        vehicle_counts = detector.detect_vehicles(args.image_path)
        print("\n--- Detection Complete ---")
        print("Detected Vehicle Counts:")
        print(json.dumps(vehicle_counts, indent=4))
        print("--------------------------\n")

    # --- Simulation Stage ---
    print("--- Starting Traffic Simulation ---")
    
    # Initialize Arduino connection (if enabled)
    arduino_comm = ArduinoConnector() if config.ENABLE_ARDUINO else None

    # Initialize the core logic and GUI
    traffic_manager = TrafficManager(vehicle_counts)
    gui = SimulationGUI()

    # Run the main game loop
    gui.run_game_loop(traffic_manager, arduino_comm)
    
    # Clean up
    if arduino_comm:
        arduino_comm.close()
        
    print("Simulation finished. Exiting.")

if __name__ == '__main__':
    main()
