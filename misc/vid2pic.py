import os
import cv2

def get_frames(vid_file):
  cap = cv2.VideoCapture(vid_file)
  frame_list = []
  # iterate through the video file
  while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
      frame_list.append(frame)
    # Break the loop
    else: 
      break
  # everything done, release the handler
  cap.release()
  return frame_list

def write_images(target_path, frame_list, fmt='jpg'):
  # create target path
  if not os.path.exists(target_path):
    print('creating {}...'.format(target_path))
    os.makedirs(target_path, mode=0o755)
  # write frames
  for i in range(len(frame_list)):
    image_name = '{}.{}'.format(str(i).zfill(5), fmt)
    filename = os.path.join(target_path, image_name)
    cv2.imwrite(filename, frame_list[i])
  # write number of frames
  with open(os.path.join(target_path, 'n_frames'), 'w') as f:
    f.write('{}\n'.format(len(frame_list)))
  print('>> finished with {} frames'.format(len(frame_list)))

def get_video_list(root_path, fmt='avi'):
  assert(os.path.isdir(root_path))
  vid_list = []
  for dirpath, _, filenames in os.walk(root_path):
    relpath = os.path.relpath(dirpath, root_path)
    local_list = [(relpath, f) for f in filenames if f.endswith('.'+fmt)]
    vid_list.extend(local_list)
  return vid_list

def main(vid_root_path, pic_root_path):
  vid_list = get_video_list(vid_root_path)
  for (relpath, vid) in vid_list:
    vid_file = os.path.join(vid_root_path, relpath, vid)
    frame_list = get_frames(vid_file)
    img_path = os.path.join(pic_root_path, relpath, os.path.splitext(vid)[0])
    write_images(img_path, frame_list)


if __name__=='__main__':
  #create_folder('./d/a/d')
  #print(get_video_list('./'))
  main('./', 'xxx')
