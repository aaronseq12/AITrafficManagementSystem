# AI Traffic Management System

This repository represents an ongoing open source research into utilizing different object detection algorithims like YOLO and hardcode designs like IoT systems using softwares like Tinkercad and Adurino which provide an inteligent and adaptive traffic light control system. All the code and models are under research and development and subject to change.

The AI based Traffic Light Control System is an inteligent embedded system which applies computer vision to determine the density of cars at each lane on a traffic intersection so as to generate adaptive duration for green and red traffic light at each lane. 

Yolov5s is selected for this project due to its speed, lightness and accuracy. The yolov5s model can be found from https://github.com/ultralytics/yolov5      |

## Features

- Detect and counts vehicles from a camera feed on each lane
- Determine a green and red light duration based on comparison of each lanes vehicle density
- Displays a simulation

## Work flow

<p float="left">
  <img src="Internet Pic/Smart+and+Safe+Crosswalk.png" width="600" height=400 />

</p>


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

## References
 1. How to export yolov5s model to onnx:
   https://github.com/ultralytics/yolov5
 2.  How to export onnx model to tensorrt:
   https://github.com/SeanAvery/yolov5-tensorrt
    

