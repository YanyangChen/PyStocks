import threading
import time
from StockObj import StockObj


exitFlag = 0


class myThread (threading.Thread):

    def __init__(self, period1, period2):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = counter
        self.period1 = period1
        self.period2 = period2

    def run(self):
        print("Starting " + self.name)
        run_this(self.period1, self.period2)
        print("Exiting " + self.name)

#
# def run_this(period1, period2):
#   print("threads running")
#   with open('./hkstks') as f:
#      lines = f.read().splitlines()
#   print(lines)
#
#  # there may be some stocks left before index 534
#   for line in lines[period1:period2]:
#      print("threads running ---------------" + str(line))
#      abc = StockObj("abc", str(line))
#      abc.main()


def run_this(period1, period2):

 # there may be some stocks left before index 534
    for line in lines[period1:period2]:
        print("threads running ---------------" + str(line))
        abc = StockObj("abc", str(line)+".SZ")
        abc.main()


with open('./SZtks') as f:
    lines = f.read().splitlines()
print(len(lines)/4*2)

def thread_run(start, end):
    length = int(end - start)
    portion = int(length/4)
    thread1 = myThread(int(start), int(start)+portion)
    thread2 = myThread(int(start)+portion + 1, int(start) + portion*2)
    thread3 = myThread(int(start) + portion*2 + 1, int(start) + portion*3)
    thread4 = myThread(int(start) + portion*3 + 1, int(end))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


# thread1 = myThread(0, int(len(lines) / 4))
# thread2 = myThread(int(len(lines) / 4) + 1, int(len(lines) / 4) * 2)
# thread3 = myThread(int(len(lines) / 4) * 2 + 1, int(len(lines) / 4) * 3)
# thread4 = myThread(int(len(lines) / 4) * 3 + 1, len(lines))
#
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
thread_run(765, 1000)
