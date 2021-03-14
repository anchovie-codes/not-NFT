# not-NFT
a simple Python steganography tool for individualizing artwork without (much of) a trace!

# ABOUT
this project is licensed under a Creative Commons Attribution-Share-Alike 4.0 International License.
you can create derivative work and share or sell it! but you must attribute me (anchovie) and my partner (marzz) as the source creators, and publish your work under a similar license. questions can be directed to my twitter, @anchoviedraws.

inspired by the growing trend of using NFTs (non-fungible tokens) as unique identifiers for digital artwork, `not-NFT` explores an alternate approach that isn't tied to the pyramid scheme that is cryptocurrency. unlike NFTs, which are minted with monopoly money on a blockchain and are primarily sold for speculative value rather than artistic/emotional/spiritual value, `not-NFT` offers a free, creative alternative. it uses simple image processing techniques to subtley encode images with a QR code, and can extract the QR code from an encoded image for a user to scan and "prove" it is individualized.

this is far from a complete solution, nor do i plan on making it one. i'm solely interested in making visually-identical images personalized for the novelty of having an artifact that is both similar and unique. my hope is people who actually know how to code could use this as a basis for other NFT alternatives, e.g. embedding QR codes with private-public keys for secure unique identification. or embed something else entirely! have fun, be creative, make art <3

# HOW TO USE
1. MAKE A QR CODE
visit https://www.qrstuff.com/ (or other such free QR builder)
i just make plaintext QR codes with personalized notes, but the sky's the limit. put whatever you want on it!

size & resolution: 100px @ 72dpi
file type: png
error correction: level H (30%)

2. EDIT THE GENERATED QR CODE
*crop out precisely the white border around the QR code
*divide resulting image size by # of pixels that are in 1 of the smallest black squares
  *(e.g. if a black square is 7 * 7px, divide image dimensions by 7
*double check that the QR code still scans properly after shrinking

3. ENCODE
*rename QR code as “QR_in.png”
*rename source image as “input.png”
*change QR_BRIGHTNESS, if desired (Default = 1, min = 1, max = 255, higher = more visible encoding)

4. DECODE
-image file being decoded should be named “encode.png”
-ensure QR_BRIGHTNESS is the same value that was used for encoding the image
-set QR_SIZE to the height of the QR code that was encoded in the image
