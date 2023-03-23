import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder_to_track = "C:/Users/sahil/OneDrive/Desktop/New folder/to track"
folder_destination = "C:/Users/sahil/OneDrive/Desktop/ACLib/to track"

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith('.txt'):
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)
                print(f"File moved from {src} to {new_destination}")


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
