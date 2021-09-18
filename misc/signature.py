import cv2
import numpy as np

def signature(pic_in, png_out, bgr_color=[127,0,0], lightness_scale=1):
  img = cv2.imread(pic_in)
  
  # mask
  thr = 150
  mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  mask[mask>thr] = 255
  mask[mask<=thr] = 0

  # color removal
  out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float)
  out = np.stack((out,)*3, axis=-1)
  # colorize
  for i in range(3):
    out[mask>0, i] = 255
    out[mask==0,i] += bgr_color[i]
  out[out>255] = 255
  # darken
  out[mask==0,:] *= lightness_scale
  # background removal
  out[mask>0,:] = 255
  out = out.astype(np.uint8)
  
  # set background to transparent
  out = cv2.cvtColor(out, cv2.COLOR_BGR2BGRA)
  out[mask>0,3] = 0
  out[mask==0,3] = 255
  cv2.imwrite(png_out, out)
  

if __name__=='__main__':
  import argparse 
  import os
  parser = argparse.ArgumentParser(description='signature processor')
  parser.add_argument('--pic', type=str, default='')
  args = parser.parse_args()

  png_out = os.path.splitext(args.pic)[0] + '.png'
  signature(args.pic, png_out)


