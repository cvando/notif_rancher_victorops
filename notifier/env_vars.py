import os
from dotenv import load_dotenv

def init_env_vars():
  path = '/env/'
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
    for file in f:
      if '.env' in file:
        files.append(os.path.join(r, file))
  for f in files:
    load_dotenv(dotenv_path=f)
    print("Env vars loaded from "+f)

    