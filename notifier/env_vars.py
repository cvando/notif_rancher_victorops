import os
from dotenv import load_dotenv

path = "/env/"
dir_list = os.listdir(path) 

def env_files():
  for envfile in dir_list:
    pathfile = path+envfile
    load_dotenv(pathfile)
    print("Env vars loaded from "+pathfile)