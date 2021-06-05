#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import sys
import os
import torch
from IPython.display import Image  # for displaying images
print('torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))
torch.cuda.is_available()
torch.cuda.get_device_name(0)


# In[2]:


cd yolov5


# In[33]:


get_ipython().system('python detect.py --source 0 --weights personhelmet.pt --conf 0.55')

