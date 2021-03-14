# not-NFT
a simple Python steganography tool for individualizing artwork without (much of) a trace!

# ABOUT
any questions about this project can be directed to my twitter, @anchoviedraws.

inspired by the growing trend of using NFTs (non-fungible tokens) as unique identifiers for digital artwork, `not-NFT` explores an alternate approach that isn't tied to the pyramid scheme of cryptocurrency. NFTs are minted with monopoly money on a blockchain, and are primarily sold for speculative value rather than artistic/emotional/spiritual value. `not-NFT` offers a free, creative alternative that preserves an emphasis on artistic value. it uses simple image processing to encode an image with a QR code. on the decoding side, it can extract that QR code from an encoded image for someone to scan and "prove" it is individualized with whatever content was put on the QR code. in terms of protecting the encoding from replication, if someone uploads (say, accidentally) an encoded image to a service that compresses the upload (literally every major social media platform afaik), the encoding will be destroyed by the compression and it will become a non-unique copy.

this is far from a complete or perfect solution, nor do i plan on making it one. i'm not a software developer, and i'm solely interested in personalizing visually-identical images for the novelty of my clients owning digital artifacts that are similar, yet unique. my hope is that people who actually know how to code could use this as a basis for other NFT alternatives, e.g. embedding QR codes with private-public keys for secure unique identification. or embedding something else entirely! have fun, be creative, make art <3.

# HOW TO USE
1. MAKE A QR CODE
* visit https://www.qrstuff.com/ (or other such free QR builder)
  * i just make plaintext QR codes with personalized notes, but the sky's the limit. put whatever you want on it!
* size & resolution: 100px @ 72dpi
* file type: png
* error correction: level H (30%)

2. EDIT THE GENERATED QR CODE
* crop out precisely the white border around the QR code
* divide resulting image size by # of pixels that are in 1 of the smallest black squares
  * (e.g. if a black square takes up 7x7px, divide image dimensions by 7
* double check that the QR code still scans properly after shrinking

3. ENCODE
* rename QR code as “QR_in.png”
* rename source image as “input.png”
* change QR_BRIGHTNESS, if desired (Default = 1, min = 1, max = 255, higher = more visible encoding)

4. DECODE
* image file being decoded should be named “encode.png”
* ensure QR_BRIGHTNESS is the same value that was used for encoding the image
* set QR_SIZE to the height of the QR code that was encoded in the image
