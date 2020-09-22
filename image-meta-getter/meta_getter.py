import sys

from PIL import Image

from PIL.ExifTags import TAGS

# Get image from CLI arg
image = sys.argv[1]

# get the image iteratable data
image_meta = Image.open(image)._getexif()

#iterate over the data 
for tag in image_meta:
    tag = TAGS.get(tag, tag)
    data = image_meta.get(tag)
    if isinstance(data, bytes):
        #decode the data
        data = data.decode()
    print(f"{tag:25}: {data}")

