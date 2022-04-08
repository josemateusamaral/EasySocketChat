import os
from threading import Thread
from functools import partial
import time
Thread(target=partial(os.system,'python EasyChat.py')).start()
time.sleep(1)
Thread(target=partial(os.system,'python EasyChat.py')).start()