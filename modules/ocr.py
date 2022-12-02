import cv2
import easyocr
from os import getcwd, listdir
#from pathlib import Path

reader = easyocr.Reader(lang_list=['es'], gpu=False, verbose=False)

def validate_folder():
  path = f'{getcwd()}/assets/'
  dir = listdir(path)
  
  if len(dir) > 0:
    print('El directorio tiene archivos', len(dir))
    print(dir)
    #print(f'{path}{dir[0]}')
    read_image(f'{path}{dir[0]}')
  else:
    print('El directorio esta vacio')
  

def read_image(image_path):
  voucher = cv2.imread(image_path)
  result = reader.readtext(voucher)
  
  for res in result:
    print('result:', res)
