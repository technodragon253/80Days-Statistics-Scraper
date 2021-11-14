import time
import threading
import sys

class loading_animation():
    animation = 0
    def __init__(self):
        self.loading = True
    def loading_animation(self):
        if self.animation == 0:
            print("-\r", end="")
            sys.stdout.flush()
            time.sleep(0.1)
            while self.loading:
                time.sleep(0.1)
                if self.loading:
                    print("\\\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("|\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("/\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("-\r", end="")
                    sys.stdout.flush()
        if self.animation == 1:
            print("o\r", end="")
            sys.stdout.flush()
            time.sleep(0.1)
            while self.loading:
                time.sleep(0.1)
                if self.loading:
                    print(".\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("o\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("O\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("*\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("°\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("*\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("O\r", end="")
                    sys.stdout.flush()
                time.sleep(0.1)
                if self.loading:
                    print("o\r", end="")
                    sys.stdout.flush()

    def start(self):
        self.thread = threading.Thread(target=self.loading_animation)
        self.thread.daemon = True
        self.thread.start()
        time.sleep(0.1)
    def stop(self):
        self.loading = False
        print("\r", end="")