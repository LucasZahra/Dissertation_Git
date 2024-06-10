import torch
import torchvision
import cv2

# This script is to test that the install have all been installed correctly
# and also that the versions are compatible with each other

x = torch.rand(5, 3)
print(x)

print("PyTorch Version:", torch.__version__)
print("TorchVision Version:", torchvision.__version__)
print("OpenCV Version:", cv2.__version__)