# config.py

"""
Central configuration file for the AI Traffic Management System.
"""

import os

# --- Project Root ---
# Get the absolute path of the directory where this file is located.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Model Configuration ---
# Path to the YOLOv2 configuration file.
MODEL_CFG = os.path.join(BASE_DIR, "cfg", "yolo-voc.cfg")

# Path to the pre-trained YOLOv2 weights file.
# Make sure you have downloaded this file and placed it in the 'bin' directory.
MODEL_WEIGHTS = os.path.join(BASE_DIR, "bin", "yolov2.weights")

# Path to the class names file (e.g., coco.names).
# This is not strictly required by darkflow for inference but is good practice.
MODEL_NAMES = os.path.join(BASE_DIR, "cfg", "coco.names")

# Detection threshold for the model.
# Detections with a confidence score below this value will be ignored.
DETECTION_THRESHOLD = 0.4

# --- Simulation Configuration ---
# Screen dimensions for the Pygame simulation window.
SIM_WIDTH = 1400
SIM_HEIGHT = 800

# Time settings for the simulation (in milliseconds).
GREEN_SIGNAL_BASE_TIME = 10000  # Base time for a green signal (10 seconds).
YELLOW_SIGNAL_TIME = 2000     # Duration of a yellow signal (2 seconds).

# --- Arduino Configuration (Optional) ---
# Set to True if you have an Arduino connected for the hardware component.
ENABLE_ARDUINO = False

# The serial port your Arduino is connected to.
# Examples: 'COM3' on Windows, '/dev/ttyUSB0' or '/dev/tty.usbmodem1421' on Linux/macOS.
ARDUINO_PORT = 'COM3'

# The baud rate for serial communication. Must match the rate in the Arduino sketch.
ARDUINO_BAUD_RATE = 9600

# --- Asset Paths ---
# Directory containing images for the simulation GUI.
ASSETS_DIR = os.path.join(BASE_DIR, "images")
