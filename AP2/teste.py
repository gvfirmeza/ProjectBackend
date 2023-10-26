import os
import numpy as np
import torch
import pydicom
import matplotlib.pyplot as plt
from tcia_utils import nbia
from monai.transforms import LoadImage, Orientation, EnsureChannelFirst, Compose
from monai.config import print_config

datadir = 'C:\\Users\\202301135737\\AP2\\imgs'
CT_folder = os.path.join(datadir, 'CT_1h.dcm')

ds = pydicom.read_file(CT_folder)

image = ds.pixel_array
image = ds.RescaleSlope * image + ds.RescaleIntercept

plt.pcolormesh(image, cmap='Greys_r')
plt.colorbar(label='HU')
plt.axis('off')
plt.show()

image_loader = LoadImage(image_only=True)
CT = image_loader(CT_folder)

CT_coronal_slice = CT[0,:,256].cpu().numpy()

plt.figure(figsize=(3,8))
plt.pcolormesh(CT_coronal_slice.T, cmap='Greys_r')
plt.colorbar(label='HU')
plt.axis('off')
plt.show()

channel_transform = EnsureChannelFirst()
CT = channel_transform(CT)

orientation_transform = Orientation(axcodes=('LPS'))
CT = orientation_transform(CT)

CT_coronal_slice = CT[0,:,256].cpu().numpy()

plt.figure(figsize=(3,8))
plt.pcolormesh(CT_coronal_slice.T, cmap='Greys_r')
plt.colorbar(label='HU')
plt.axis('off')
plt.show()

preprocessing_pipeline = Compose([
    LoadImage(image_only=True),
    EnsureChannelFirst(),
    Orientation(axcodes='LPS')
])

CT = preprocessing_pipeline(CT_folder)
CT_coronal_slice = CT[0,:,256].cpu().numpy()

plt.figure(figsize=(3,8))
plt.pcolormesh(CT_coronal_slice.T, cmap='Greys_r')
plt.colorbar(label='HU')
plt.axis('off')
plt.show()

print_config()
