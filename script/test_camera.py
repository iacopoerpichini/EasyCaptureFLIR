from simple_pyspin import Camera
from PIL import Image as im
import os

with Camera() as cam: # Initialize Camera
    cam.start() # Start recording
    imgs = [cam.get_array() for n in range(10)] # Get 10 frames
    cam.stop() # Stop recording

print(imgs[0].shape, imgs[0].dtype) # Each image is a numpy array!

data = im.fromarray(imgs[0])
# saving the final output
# as a PNG file
# Make a directory to save some images
output_dir = 'test_image_dummy'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
print("Saving images to: %s" % output_dir)
data.save(output_dir + '/dummy_pic.png')
