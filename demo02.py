from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, song, sec):
        super().__init__()
        self.song = song
        self.sec = sec

    def run(self):
        for i in range(3):
            print("playing %s : %s") % (self.song, time.ctime())
            time.sleep(self.sec)


t = MyThread("mysong", 2)
t.start()
t.join()
