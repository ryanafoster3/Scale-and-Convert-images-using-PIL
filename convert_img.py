#!/usr/bin/env python3

import os
from PIL import Image

# assigning input and output directories
input_dir = 'images/'
out_dir = '/opt/icons/'

# determine image size, format, and rotation direction
size = 128, 128
ext = 'JPEG'
rotation = -90

# iterate over the files from input directory
for filename in os.listdir(input_dir):
    # ensures item is a file and that files starting
    # with 'ic_' are edited
    f = os.path.join(input_dir, filename)
    if os.path.isfile(f) and filename.startswith('ic_'):
        # creates output directory path and new file name
        # opens image, rotates (rotation), resizes (size), and saves
        # as a desired file type (ext)
        n = os.path.join(out_dir, filename)
        im = Image.open(f)
        im.rotate(rotation).resize(size).convert('RGB').save(n, ext)

        # reports where the new image is stored as well as
        # displaying the new format and image size
        img = Image.open(n)
        img_format = str(img.format)
        img_size = str(img.size)
        print("Processed image: " + f)
        print('New image saved as: ' + n)
        print('Format: ' + img_format + "  //  Size: " + img_size)
