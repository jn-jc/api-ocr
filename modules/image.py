from os import getcwd, listdir, remove
from requests import post, HTTPError

url_api = 'http://localhost:9000/api/images'
path = f'{getcwd()}/temp'
dir_path = ''

async def validate_dir():
  dir_path = listdir(path)
  if len(dir_path) < 0:
    return False
  return dir_path

async def send_image():
  validate = await validate_dir()
  last_image = ''
  if(validate):
    last_image = f'{path}/{validate[0]}'
    try:
      file = {'image': open(last_image, 'rb')}
      response = post(url=f'{url_api}/get-image', files=file)
      remove(last_image)
      return response
    except HTTPError:
      raise HTTPError