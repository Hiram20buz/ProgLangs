import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data, img_as_float
#
from skimage.segmentation import slic
from skimage.data import astronaut
from skimage.color import label2rgb
#
fig, axes = plt.subplots(1, 3, figsize=(10, 10))

# Sample Image of scikit-image package
astronaut = data.astronaut()
gray_astronaut = rgb2gray(astronaut)

astronaut_segments = slic(astronaut,n_segments=50,compactness=10)

# Computing the Chan VESE segmentation technique
#chanvese_gray_astronaut = chan_vese(gray_astronaut,max_iter=100,extended_output=True)

ax = axes.flatten()

# Plotting the original image
ax[0].imshow(gray_astronaut, cmap="gray")
ax[0].set_title("Original Image")

# Plotting the original image
ax[1].imshow(label2rgb(astronaut_segments,astronaut,kind = 'avg'))
ax[1].set_title("Original Image")

plt.show()

