import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from PIL import Image

#visibility of embedded encoding (must match encoding value)
QR_BRIGHTNESS = 1
#dimension (px) of original QR code
QR_SIZE = 42
#threshold for QR_out pixels to be pure black vs. pure white (0-255)
THRESHOLD = 153

#imports the encoded image
encoded_img = plt.imread("encode.png")
encoded_img = encoded_img[:,:,:3].astype(np.float64)

#builds the weights for the convolution
w = np.ones((3, 3, 1), np.float64)
w /= 8
w[1, 1, 0] = 0

#creates a gradient map of the encoded image
#this finds the difference between the signal pixels and their surrounding pixels
#across the entire image, the gradient will be strongest where the signal is embedded
avg_map = convolve(encoded_img.astype(np.float64), w, mode="mirror")
gradient_map = encoded_img - avg_map
gradient_map = np.clip(gradient_map, 0., QR_BRIGHTNESS / 255)

#tetris time
#rearranges and slices the gradient map array such that the QR code data is stacked
#signal becomes stronger, noise stays the same
#or None in the slicing operation accounts for when the gradient map array is the same size as the encoded image array
gradient_map = np.sum(gradient_map, 2)
gradient_map = gradient_map[:(gradient_map.shape[0] % (QR_SIZE * 2) * -1) or None, :(gradient_map.shape[1] % (QR_SIZE * 2) * -1) or None]
gradient_map = np.reshape(gradient_map, (gradient_map.shape[0], QR_SIZE * 2, -1), order="F")
gradient_map = np.transpose(gradient_map, (1, 0, 2))
gradient_map = np.reshape(gradient_map, (gradient_map.shape[0], QR_SIZE * 2, -1), order="F")
gradient_map = np.transpose(gradient_map, (1, 0, 2))

#pieces the QR code together from the reshaped gradient map
#converts datatype so PIL is happy
#gets rid of padding around signal pixels
#darkens noise pixels to black (0) and signal pixels to white (255) for better contrast when scanning
qr_decode = np.sum(gradient_map, 2)
qr_decode /= np.amax(qr_decode)
qr_decode *= 255
qr_decode = qr_decode.astype(np.uint8)
qr_decode = qr_decode[::2, ::2]
qr_decode[np.where(qr_decode < THRESHOLD)] = 0
qr_decode[np.where(qr_decode >= THRESHOLD)] = 255
Image.fromarray(qr_decode).save("QR_out.png")
print("QR code extracted and saved!")