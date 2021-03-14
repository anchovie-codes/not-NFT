import numpy as np
import matplotlib.pyplot as plt

#visibility of embedded encoding (1-255, higher = brighter)
#increase this value if decoded QR is too noisy when testing
QR_BRIGHTNESS = 1

#imports file & removes alpha channel
img = plt.imread("input.png")
img = img[:,:,:3]

#clips the array so the max value is (255 - QR_BRIGHTNESS)
img = (img * 255).astype(np.uint8)
img = np.clip(img, 0, 255 - QR_BRIGHTNESS)

#create an empty array the size of img
#read in the QR code
#pad every pixel in the QR code with zeros
embed_mask = np.zeros_like(img)
qr = plt.imread("QR_in.png")
qr = qr[:,:,:3]
qr = (qr * QR_BRIGHTNESS).astype(np.uint8)
spaced_qr = np.zeros(((qr.shape[0] * 2), (qr.shape[1] * 2), 3)).astype(np.uint8)
spaced_qr[::2, ::2] = qr

#embeds and tesselates spaced_qr across img
#stops before the edges of img, when spaced_qr can't fully fit
qrgrid = np.copy(spaced_qr)

for i in range((img.shape[0] // spaced_qr.shape[0]) - 1):
    qrgrid = np.concatenate((qrgrid, spaced_qr), 0)

qrgrid_row = np.copy(qrgrid)

for j in range((img.shape[1] // spaced_qr.shape[1]) - 1):
    qrgrid = np.concatenate((qrgrid, qrgrid_row), 1)

embed_mask[:qrgrid.shape[0], :qrgrid.shape[1]] = qrgrid
encoded_img = embed_mask + img

#saves the encoded image
plt.imsave("encode.png", encoded_img)
print("encoded image saved!")