# AI Traffic Management System

This repository represents an ongoing open source research into utilizing different object detection algorithims like YOLO and hardcode designs in IoT systems using softwares like Wokwi and Adurino which provide an intelligent and adaptive traffic light control system. All the code and models are under research and development and subject to change. 

The AI based Traffic Light Control System is an inteligent embedded system which applies computer vision to determine the density of cars at each lane on a traffic intersection so as to generate adaptive duration for green and red traffic light at each lane.

Yolov5s is selected for this project due to its speed, lightness and accuracy. The yolov5s model can be found from https://github.com/ultralytics/yolov5 

## Features

- Detect and counts vehicles from a camera feed on each lane
- Determine a green and red light duration based on comparison of each lanes vehicle density
- Displays a simulation

## Devices Used

- Nvidia Jetson Nano
- Ip camera

## How to run

For CPU and GPU environments...
The Onnx implementation can run both on CPU and GPU
```sh
$ cd implementation_with_yolov5s_onnx_model 
$ python3 main.py  --sources video1.mp4,video2.mp4,video3.mp4,video5.mp4
```

Only for GPU environments...
The Tensorrt based implementation runs only on GPU
```sh
$ cd implementation_with_yolov5s_tensorrt_model
$ python3 main.py --sources video1.mp4,video2.mp4,video3.mp4,video5.mp4
```

A simulation developed from scratch using Pygame to simulate the movement of vehicles across a traffic intersection having traffic lights with a timer. Additional features added to existing basic simulation to take it closer to real-life scenarios and use it effectively in Data Analysis tasks or AI applications.


Features added:
Vehicle Turning Functionality - Unlike the previous simulation where all the vehicles went straight through the intersection, some of the vehicles will be turning left, some right, and some will go straight in the modified simulation.
Vehicle Type Controller - This feature lets us choose which vehicle types among car, bus, truck and bike we want in our simulation.
Random Green Signal Timer - If enabled, this feature sets the green signal time equal to a random number generated within a given range.

## References
 1. How to export yolov5s model to onnx:
   https://github.com/ultralytics/yolov5
 2.  How to export onnx model to tensorrt:
   https://github.com/SeanAvery/yolov5-tensorrt
    

