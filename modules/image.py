from os import getcwd, listdir, remove
from requests import post, exceptions
from datetime import datetime

url_api = 'http://localhost:9000/api/images'
path = f'{getcwd()}/temp'
dir_path = ''

async def validate_dir():
  dir_path = listdir(path)
  if len(dir_path) < 0:
    return False
  return dir_path

async def send_image(id_vendedor):
  validate = await validate_dir()
  last_image = ''
  date_now = datetime.now()
  date_str = date_now.strftime("%d_%m_%Y_%H_%M_%S")
  if(validate):
    last_image = f'{path}/{validate[0]}'
    try:
      file = {'image': (f'{id_vendedor}-{date_str}.jpg',open(last_image, 'rb'))}
      response = post(url=f'{url_api}/get-image', files=file)
      #remove(last_image)
      return response
    except exceptions.ConnectionError as errc:
      print({'Error Connection' : errc})