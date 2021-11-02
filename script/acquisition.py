from simple_pyspin import Camera
from PIL import Image
import os
from datetime import datetime

NUM_IMAGES = 10

def acquire():
    with Camera() as cam: # Initialize Camera
        # Set the area of interest (AOI) to the middle half
        cam.Width = cam.SensorWidth // 2
        cam.Height = cam.SensorHeight // 2
        cam.OffsetX = cam.SensorWidth // 4
        cam.OffsetY = cam.SensorHeight // 4

        # If this is a color camera, get the image in RGB format.
        if 'Bayer' in cam.PixelFormat:
            cam.PixelFormat = "RGB8Packed"
            #  - possible values: `'Mono8'`, `'Mono12Packed'`, `'Mono16'`, `'RGB8Packed'`,
            #  `'YUV422Packed'`, `'BayerGR8'`, `'BayerRG8'`, `'BayerGB8'`, `'BayerBG8'`,
            #  `'CbYCrY'`


        # To change the frame rate, we need to enable manual control
        # TODO See the generated documentation
        # cam.AcquisitionFrameRateAuto = 'Off'
        # cam.AcquisitionFrameRateEnabled = True
        # cam.AcquisitionFrameRate = 20

        # To control the exposure settings, we need to turn off auto
        cam.GainAuto = 'Off'
        # Set the gain to 20 dB or the maximum of the camera.
        gain = min(20, cam.get_info('Gain')['max'])
        print("Setting gain to %.1f dB" % gain)
        cam.Gain = gain
        cam.ExposureAuto = 'Off'
        cam.ExposureTime = 10000 # microseconds

        # If we want an easily viewable image, turn on gamma correction.
        # NOTE: for scientific image processing, you probably want to _disable_ gamma correction!
        try:
            cam.GammaEnabled = True
            cam.Gamma = 2.2
        except:
            print("Failed to change Gamma correction (not avaiable on some cameras).")

        cam.start() # Start recording
        imgs = [cam.get_array() for n in range(NUM_IMAGES)]
        cam.stop() # Stop recording

    return imgs


if __name__ == '__main__':
    # Make a directory to save some images
    output_dir = 'test_images'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    imgs = acquire()

    # Save them
    print("Saving images to: %s" % output_dir)
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    for n, img in enumerate(imgs):
        date = os.path.join(date, '%08d.jpg' % n)
        Image.fromarray(img).save(os.path.join(output_dir, date))