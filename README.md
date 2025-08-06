# AI-Powered Traffic Management System

![Simulation Screenshot](https://raw.githubusercontent.com/aaronseq12/AITrafficManagementSystem/master/peek.jpg)

This project is an AI-driven traffic management system that uses real-time vehicle detection to optimize traffic flow at a four-way intersection. It combines computer vision for vehicle counting with a dynamic traffic simulation to adjust signal timings based on traffic density. An optional hardware component allows the system to control physical traffic light LEDs using an Arduino.

---

## 🌟 Features

-   **Real-time Vehicle Detection**: Utilizes the YOLO (You Only Look Once) object detection model via the Darkflow framework to identify and count vehicles in images of an intersection.
-   **Dynamic Traffic Simulation**: A Pygame-based simulation of a four-way intersection where traffic signal timings are dynamically adjusted based on the detected number of vehicles.
-   **Intelligent Signal Control**: The system calculates green signal durations proportionally to the traffic density in each lane, minimizing congestion and wait times.
-   **Hardware Integration (Optional)**: Includes an Arduino sketch to control a physical model of the traffic light system via serial communication.
-   **Modular and Extensible**: The codebase has been refactored into a modular, object-oriented structure, making it easy to understand, modify, and extend.

---

## 🏛️ System Architecture

The system operates in two main stages:

1.  **Vehicle Detection**:
    * The `vehicle_detector.py` script takes an image of the intersection as input.
    * It uses a pre-trained YOLO model to detect vehicles (cars, buses, trucks, motorcycles).
    * It outputs the number of detected vehicles for each of the four lanes (right, left, up, down).

2.  **Traffic Simulation & Control**:
    * The `main.py` script launches the Pygame simulation.
    * It calls the vehicle detection script to get the current traffic density.
    * The `TrafficManager` class uses this data to calculate the optimal green light duration for each lane.
    * The simulation visually represents the traffic flow, with vehicles moving according to the smart traffic signals.
    * If an Arduino is connected, the system sends commands via a serial port to update the physical LEDs.

---

## 🔧 Setup and Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Python 3.7+
-   Git
-   (Optional) Arduino IDE for the hardware component.

### 1. Clone the Repository

```bash
git clone [https://github.com/aaronseq12/AITrafficManagementSystem.git](https://github.com/aaronseq12/AITrafficManagementSystem.git)
cd AITrafficManagementSystem
```

### 2. Set up a Python Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

The project uses several Python libraries. The `darkflow` library requires manual setup.

First, install the libraries from `requirements.txt`:
```bash
pip install -r requirements.txt
```

Next, build the Cython components for `darkflow`:
```bash
cd darkflow
python setup.py build_ext --inplace
cd ..
```
This command compiles the necessary Cython extensions within the `darkflow` directory.

### 4. Download YOLOv2 Weights

The vehicle detection model requires pre-trained weights. Download the `yolov2.weights` file and place it in a `bin` directory inside the root of the project.

1.  Create the `bin` directory:
    ```bash
    mkdir bin
    ```
2.  Download the weights file from the official YOLO website (or a mirror): [yolov2.weights](https://pjreddie.com/media/files/yolov2.weights)
3.  Move the downloaded `yolov2.weights` file into the `bin/` directory.

### 5. (Optional) Arduino Setup

If you want to use the physical traffic light model:
1.  Connect your Arduino to your computer.
2.  Open `Traffic_signal/Traffic_signal.ino` in the Arduino IDE.
3.  Upload the sketch to your Arduino board.
4.  Make sure to note the COM port your Arduino is connected to (e.g., `COM3` on Windows, `/dev/ttyUSB0` on Linux). You will need to update this in the `config.py` file.

---

## 🚀 Usage

The project can be run in two modes: simulation-only or with vehicle detection.

### Running the Full System (Detection + Simulation)

To run the complete system, where vehicle detection determines the signal timings:

```bash
python main.py --use-detection --image-path test_images/1.jpg
```

-   `--use-detection`: This flag tells the system to run the vehicle detector.
-   `--image-path`: Specify the path to the intersection image you want to analyze. You can use any of the images in the `test_images` folder.

The system will first process the image, print the detected vehicle counts, and then launch the simulation with timings adjusted for that traffic scenario.

### Running the Simulation Standalone

To run the simulation with default, fixed signal timings (without running the vehicle detector):

```bash
python main.py
```

---

## 📁 Project Structure

The repository has been restructured for clarity and maintainability:

```
AITrafficManagementSystem/
│
├── bin/                      # To store model weights (e.g., yolov2.weights)
├── cfg/                      # YOLO model configuration files
├── darkflow/                 # Darkflow submodule for YOLO inference
├── images/                   # Assets for the Pygame simulation
├── test_images/              # Sample images of intersections for detection
├── Traffic_signal/           # Arduino sketch for hardware integration
│
├── .gitignore                # Specifies files for Git to ignore
├── config.py                 # Central configuration for paths and settings
├── main.py                   # Main entry point to run the simulation
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── simulation_gui.py         # Handles all Pygame rendering and GUI
├── traffic_manager.py        # Core logic for traffic simulation and signal control
├── vehicle.py                # Vehicle sprite class for the simulation
├── vehicle_detector.py       # Class for detecting and counting vehicles
└── arduino.py                # Handles serial communication with Arduino
```

---

## 💡 Future Improvements

-   **Real-time Video Processing**: Adapt the system to process a live video feed from a traffic camera instead of static images.
-   **Advanced Traffic Algorithms**: Implement more sophisticated algorithms, such as reinforcement learning, to predict traffic flow and prevent congestion proactively.
-   **Emergency Vehicle Detection**: Add a feature to detect emergency vehicles (ambulances, fire trucks) and turn all signals green for their path.
-   **Pedestrian Detection**: Integrate pedestrian detection to manage crosswalk signals, ensuring pedestrian safety.
-   **Web-based Dashboard**: Create a web interface to monitor traffic conditions and control the system remotely.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
