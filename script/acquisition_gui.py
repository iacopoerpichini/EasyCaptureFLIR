import EasyPySpin
import cv2
import os
from datetime import datetime


DIRETORY_PATH = "~/PycharmProjects/EasyCaptureFLIR"

def main(saving_path):
    cap = EasyPySpin.VideoCapture(0)

    if not cap.isOpened():
        print("Camera can't open\nexit")
        return -1

    cap.set(cv2.CAP_PROP_EXPOSURE, -1)  # -1 sets exposure_time to auto
    cap.set(cv2.CAP_PROP_GAIN, -1)  # -1 sets gain to auto

    #set fps to 25Hz
    cap.set(cv2.CAP_PROP_FPS, 25)  # led light frequence lab
    # print camera parameters
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print('camera w,h:', width, ',', height)

    # not used
    # cap.set(cv2.CAP_PROP_BRIGHTNESS, )
    # cap.set(cv2.CAP_PROP_GAMMA, )
    # cap.set(cv2.CAP_PROP_TEMPERATURE, )


    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    if not os.path.exists(os.path.join(output_dir, date)):
        os.makedirs(os.path.join(output_dir, date))
    count = 0
    while True:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BayerBG2BGR)  # for RGB camera demosaicing

        img_show = cv2.resize(frame, None, fx=0.25, fy=0.25)

        cv2.imshow("Press x to save, q to quit", img_show)

        key = cv2.waitKey(30)
        if key == ord("q"):
            break
        if key == ord("x"):
            # Save them
            print("Saving images to: %s" % saving_path)
            filename = '%08d.png' % count
            path = os.path.join(output_dir, date, filename)
            count += 1
            # cv2.imwrite(os.path.join(saving_path, path),frame)
            cv2.imwrite(path, frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Make a directory to save some images
    output_dir = 'acquisition_gui'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    main(saving_path=output_dir)
