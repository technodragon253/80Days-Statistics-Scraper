import time
import threading

class loading_animation():
    def __init__(self):
        self.loading = True
    def loading_animation(self):
        print("-", end="")
        while self.loading:
            time.sleep(0.1)
            print("\r\\", end="")
            time.sleep(0.1)
            print("\r|", end="")
            time.sleep(0.1)
            print("\r/", end="")
            time.sleep(0.1)
            print("\r-", end="")
            time.sleep(0.1)
            print("\r\\", end="")
            time.sleep(0.1)
            print("\r|", end="")
            time.sleep(0.1)
            print("\r/", end="")
            time.sleep(0.1)
            print("\r-", end="")
    def start(self):
        thread = threading.Thread(target=self.loading_animation)
        thread.daemon = True
        thread.start()