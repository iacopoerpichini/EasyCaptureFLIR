from simple_pyspin import Camera, list_cameras
import os
import time

output_dir = os.path.join('docs', 'cameras')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with Camera() as cam:
    print('Resetting camera...')
    cam.DeviceReset()


print('Waiting...')
time.sleep(1)

for n in range(10):
    cl = list_cameras()
    n_cam = cl.GetSize()
    cl.Clear()
    if n_cam:
        break
    time.sleep(1)

print('Reconnecting camera...')
with Camera() as cam:
    cam_name = cam.DeviceVendorName.strip() + ' ' + cam.DeviceModelName.strip()
    ofn = os.path.join(output_dir, cam_name.replace(' ', '_') + '.md')
    print('Generating documentation in file: %s' % ofn)

    with open(ofn, 'wt') as f:
        f.write(cam.document())
