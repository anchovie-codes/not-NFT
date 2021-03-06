# not-NFT
a simple Python steganography tool for individualizing artwork without (much of) a trace!

# ABOUT
`not-NFT` is a project by anchovie and marzz. any questions can be directed to my twitter, @anchoviedraws.

inspired by the growing trend of using NFTs (non-fungible tokens) as unique identifiers for digital artwork, `not-NFT` explores an alternate approach that isn't tied to the pyramid scheme of cryptocurrency. NFTs are minted with monopoly money on a blockchain, and are primarily sold for speculative value rather than artistic/emotional/spiritual value. `not-NFT` offers a free, creative alternative that preserves an emphasis on artistic value. it uses simple image processing methods to encode an image with a QR code. then on the decoding side, it can extract that QR code from an encoded image. someone can scan this and "prove" it is individualized with whatever content was put on the QR code. to protect the encoding from replication, if someone uploads (say, accidentally) an encoded image to a service that compresses the upload (literally every major social media platform afaik), the encoding will be destroyed by the compression and it will become a non-unique copy.

this is far from a complete or perfect solution, nor do i plan on making it one. maintenance of this project is subject to our interest in it, there are no guarantees. i'm not a software developer. i'm just interested in personalizing images for the novelty of my clients owning digital artifacts that are visually-identical, yet unique. my hope is that people who actually know how to code could use this as a basis for other NFT alternatives, e.g. embedding QR codes with private-public keys for secure unique identification, or embedding something else entirely! have fun, be creative, make art <3.

# WHAT YOU NEED
* Python 3
* numpy
* matplotlib
* scipy
* PIL

# HOW TO USE
1. MAKE A QR CODE
* visit https://www.qrstuff.com/ (or other such free QR builder)
  * i just make plaintext QR codes with personalized notes, but the sky's the limit. put whatever you want on it!
* my settings: 
  * size & resolution: 100px @ 72dpi
  * file type: png
  * error correction: level H (30%)

2. EDIT THE GENERATED QR CODE
* crop out precisely the white border around the QR code
* divide resulting image size by # of pixels that are in 1 of the smallest black squares
  * (e.g. if a black square takes up 7x7px, divide image dimensions by 7
* double check that the QR code still scans properly after shrinking

NOTE:  if you want to change what you're embedding, you'll need to alter the image processing methods in `encoder.py` and `decoder.py` that are currently configured to modify and embed a QR code with the specific properties listed above. if you have a general understanding of `numpy` and `scipy` you'll be fine! seriously, if i can do it then anyone can. my only suggestion is that whatever signal you embed should have some amount of redundancy (e.g. a high error correction level on a QR code). that way, it's still legible if the decoding side ends up a bit noisy.

3. ENCODE
* rename QR code as ???QR_in.png???
* rename source image as ???input.png???
* change QR_BRIGHTNESS, if desired (default = 1, range = 1-255, higher value = more visible encoding)

4. DECODE
* rename image file being decoded to ???encode.png???
* set QR_BRIGHTNESS to the same value that was used for encoding the original image
* set QR_SIZE to the height of the QR code that was encoded in the original image

# TUNING THE SETTINGS
this project hasn't been tested comprehensively, but i've put it through a stress test of a variety of images: graphite sketches, dithered grayscale manga, dithered color art, film photos, and digital photos. the global variables are commented with explanations of how to tune them for a good output, but here are some additional comments:
* `QR_BRIGHTNESS` is very sensitive. i never needed to turn it up past `4` to get a clear result on even the noisiest images (film photo with strong grain). if you change this value on the encoding side, you must make it identical on the decoding side as well.
* `THRESHOLD` is used to increase the contrast of the output to pure white on pure black. if you're testing a decode and want to see what the grayscale QR_out looks like without this adjustment, comment out lines 49 and 50.

# FOR ARTISTS
this is my process for using this tool:
* put the original QR code and a text file with the encoding settings in the same folder as the original artwork, for safekeeping/reference.
* when the time comes to decode, those important parameters (such as `QR_BRIGHTNESS` and `QR_SIZE`,  will be easy to set!
* this isn't a "set it and forget it" tool, it will demand fine-tuning and a bit of trial and error. writing down your settings and your tweaking process will serve as a good reference point, and increase your familiarity with the tool over time.
* this tool's effectiveness is largely dependent upon the dimensions of the original image. bigger is better! i recommend at least 2000x2000px if you're going to use a `QR_BRIGHTNESS` value lower than 3, but this is obviously dependent on how noisy the image is. experiment and see what works!
