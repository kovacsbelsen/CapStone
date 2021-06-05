import cv2
import os
import torch
import subprocess
from IPython.display import Image  # for displaying images
print('torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))
torch.cuda.is_available()
torch.cuda.get_device_name(0)

print(os.getcwd())

os.system("python ./CapStone/yolov5/detect.py --source 0 --weights personhelmet.pt --conf 0.55")


#subprocess.run("python ./CapStone/yolov5/detect.py --source 0 --weights personhelmet.pt --conf 0.55")