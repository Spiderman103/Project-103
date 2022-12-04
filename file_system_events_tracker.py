import sys
import time
import random
import os
import shutil
from watchdog.observers import Obsever
from watchdog.events import FileSystemEventHandler


from_dir  "C:\Users\sahil\OneDrive\Documents\C-102 Project - BYJU"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")

    
    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src.path}!")

    def on_modified(self,event):
        print(f"Hey, {event.src_path} has been modified!")
    
    def on_moved(self,event):
        print(f"Hey {event.src_path} has been moved")
    

    observer = Observer
    observer.Observer()
    observer.schedule()


    try:
        while true:
            time.sleep(2)
            print("running...")
    except KeyboardInterrupt:
        print("stopped!")
        observer.stop()


    