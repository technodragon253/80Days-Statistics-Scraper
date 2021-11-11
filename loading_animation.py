import time
import threading
import sys

class loading_animation():
    def __init__(self):
        self.loading = True
    def loading_animation(self):
        print("-\r", end="")
        time.sleep(0.1)
        while self.loading:
            time.sleep(0.1)
            print("\\\r", end="")
            time.sleep(0.1)
            print("|\r", end="")
            time.sleep(0.1)
            print("/\r", end="")
            time.sleep(0.1)
            print("-\r", end="")

    def start(self):
        self.thread = threading.Thread(target=self.loading_animation)
        self.thread.daemon = True
        self.thread.start()
        print("Fetching Data")
    def stop(self):
        self.loading = False
        sys.stdout.flush()
        print("Done!")