# Safe of Site - Helmet detection with Yolo V5

![](site.gif)

## Introduction - Safet of Site

This repository contains a moded version of PyTorch YOLOv5 (https://github.com/ultralytics/yolov5).


Construction site object detection project, for predicting the proper use of safety helmets with two use cases.

The first use case can be initiated by running the detect.py script in jupyter notebook (see CapStone_SOS.ipynb) or terminal.
It detects people, helmets, or if helmets are not detected, heads.
All detected people are counted and compared to the amount of helmets detected. If it is not equal, an error message, "Incorrect" appears on the image / frame. 
In case any heads are detected without a helmet, the same "Incorrect" message appears, indicating danger.

The second use case can be initiated by running the detectgate.py script.
It is an automated gate entrance system for construction sites. 
A person is detected in the frame and we check for their helmet. If the helmet is not detected, the gate will remain closed.
Once it is detected, we count for 30 frames, if the person had the helmet on for 30 consecutive frames, we open the gate for 15 frames. 
If the count is disrupted before it reaches 30, it resets to 0
 


## Work in progress - People movement tracker

The detections of persons from Yolov5 are passed to a Deep Sort algorithm (https://github.com/ZQPei/deep_sort_pytorch) which tracks the persons. 
For each detection, the center of their bounding box is calculated, then the center's coordinate is passed to a dictionary each frame.
For each detection, we get all of the previous coordinate location and draw lines in consecutive order.


## Requirements

Python 3.8 or later with all requirements.txt dependencies installed, including torch>=1.7. To install run:

`pip install -U -r requirements.txt`

All dependencies are included in the associated docker images. Docker requirements are: 
- `nvidia-docker`
- Nvidia Driver Version >= 440.44

## Before you run the tracker

1. Clone the repository recursively:

`git clone --recurse-submodules https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch.git`

If you already cloned and forgot to use `--recurse-submodules` you can run `git submodule update --init`

2. Github block pushes of files larger than 100 MB (https://help.github.com/en/github/managing-large-files/conditions-for-large-files). Hence you need to download two different weights: the ones for yolo and the ones for deep sort

- download the yolov5 weight from the latest realease https://github.com/ultralytics/yolov5/releases. Place the downlaoded `.pt` file under `yolov5/weights/`
- download the deep sort weights from https://drive.google.com/drive/folders/1xhG0kRH1EX5B9_Iz8gQJb7UNnn_riXi6. Place ckpt.t7 file under`deep_sort/deep/checkpoint/`

## Tracking

Tracking can be run on most video formats

```bash
python3 track.py --source ...
```

- Video:  `--source file.mp4`
- Webcam:  `--source 0`
- RTSP stream:  `--source rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa`
- HTTP stream:  `--source http://wmccpinetop.axiscam.net/mjpg/video.mjpg`

MOT compliant results can be saved to `inference/output` by 

```bash
python3 track.py --source ... --save-txt
```

## Other information

For more detailed information about the algorithms and their corresponding lisences used in this project access their official github implementations.

