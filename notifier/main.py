import importlib
import os
import conf.default as cfg
import time
from env_vars import env_files
from http_server2 import listen

while "CHANNELS" not in os.environ:
  env_files()
  time.sleep(1)
importlib.reload(cfg)
print("Channels configured: "+cfg.channels, flush=True)
listen()