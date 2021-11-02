import EasyPySpin
import cv2
import os
from datetime import datetime

def main():
    cap = EasyPySpin.VideoCapture(0)

    if not cap.isOpened():
        print("Camera can't open\nexit")
        return -1

    cap.set(cv2.CAP_PROP_EXPOSURE, -1)  # -1 sets exposure_time to auto
    cap.set(cv2.CAP_PROP_GAIN, -1)  # -1 sets gain to auto

    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    count = 0
    while True:
        ret, frame = cap.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_RGB)  # for RGB camera demosaicing

        img_show = cv2.resize(frame, None, fx=0.25, fy=0.25)
        cv2.imshow("Press x to save, q to quit", img_show)

        key = cv2.waitKey(30)
        if key == ord("q"):
            break
        if key == ord("x"):
            # Save them
            print("Saving images to: %s" % output_dir)
            path = os.path.join(date, '%08d.jpg' % count)
            count += 1
            cv2.imwrite(os.path.join(output_dir, path),frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Make a directory to save some images
    output_dir = 'acquisition_gui'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    main()
