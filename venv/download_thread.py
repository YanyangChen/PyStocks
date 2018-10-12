import threading
import time
from StockObj import StockObj


exitFlag = 0

class myssThread (threading.Thread):

    def __init__(self, period1, period2):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = counter
        self.period1 = period1
        self.period2 = period2

    def run(self):
        print("Starting " + self.name)
        run_ss(self.period1, self.period2)
        print("Exiting " + self.name)

class myusThread (threading.Thread):

    def __init__(self, period1, period2):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = counter
        self.period1 = period1
        self.period2 = period2

    def run(self):
        print("Starting " + self.name)
        run_us(self.period1, self.period2)
        print("Exiting " + self.name)

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
        run_sz(self.period1, self.period2)
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


def run_sz(period1, period2):

 # there may be some stocks left before index 534
    for line in lines[period1:period2]:
        print("threads running ---------------" + str(line)+ ".SZ")
        abc = StockObj("abc", str(line) + ".SZ")
        abc.main()

def run_ss(period1, period2):

 # there may be some stocks left before index 534
    for line in lines[period1:period2]:
        print("threads running ---------------" + str(line)+ ".SS")
        abc = StockObj("abc", str(line) + ".SS")
        abc.main()


def run_us(period1, period2):
    # there may be some stocks left before index 534
    for line in lines[period1:period2]:
        print("threads running ---------------" + str(line) + ".US")
        abc = StockObj("abc", str(line))
        abc.main()


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


def ssthread_run(start, end):
    length = int(end - start)
    portion = int(length/4)
    thread1 = myssThread(int(start), int(start)+portion)
    thread2 = myssThread(int(start)+portion + 1, int(start) + portion*2)
    thread3 = myssThread(int(start) + portion*2 + 1, int(start) + portion*3)
    thread4 = myssThread(int(start) + portion*3 + 1, int(end))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


def usthread_run(start, end):
    length = int(end - start)
    portion = int(length/4)
    thread1 = myusThread(int(start), int(start)+portion)
    thread2 = myusThread(int(start)+portion + 1, int(start) + portion*2)
    thread3 = myusThread(int(start) + portion*2 + 1, int(start) + portion*3)
    thread4 = myusThread(int(start) + portion*3 + 1, int(end))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


def us3thread_run(start, end):
    length = int(end - start)
    portion = int(length/3)
    thread1 = myusThread(int(start), int(start)+portion)
    thread2 = myusThread(int(start)+portion + 1, int(start) + portion*2)
    thread3 = myusThread(int(start) + portion*2 + 1, int(end))

    thread1.start()
    thread2.start()
    thread3.start()


def us8thread_run(start, end):
    length = int(end - start)
    portion = int(length/8)
    thread1 = myusThread(int(start), int(start)+portion)
    thread2 = myusThread(int(start)+portion + 1, int(start) + portion*2)
    thread3 = myusThread(int(start) + portion*2 + 1, int(start) + portion*3)
    thread4 = myusThread(int(start) + portion*3 + 1, int(start) + portion*4)
    thread5 = myusThread(int(start) + portion*4 + 1, int(start) + portion*5)
    thread6 = myusThread(int(start) + portion*5 + 1, int(start) + portion*6)
    thread7 = myusThread(int(start) + portion*6 + 1, int(start) + portion*7)
    thread8 = myusThread(int(start) + portion * 7 + 1, int(end))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
# thread1 = myThread(0, int(len(lines) / 4))
# thread2 = myThread(int(len(lines) / 4) + 1, int(len(lines) / 4) * 2)
# thread3 = myThread(int(len(lines) / 4) * 2 + 1, int(len(lines) / 4) * 3)
# thread4 = myThread(int(len(lines) / 4) * 3 + 1, len(lines))
#
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread_run(0, int(765/3))
# thread_run(int(765/3)+1, int(765/3)*2)
# thread_run(int(765/3)*2+1, 765)
# thread_run(765, 1000)
# thread_run(1001, 1500)
# thread_run(1501, 2000)

#run this tomorrow
# thread_run(2001, 2500)
# thread_run(2501, 3000)

# with open('./SStks') as f:
#     lines = f.read().splitlines()
# ssthread_run(1, 1971)


with open('./tks/USAtks') as f:
    lines = f.read().splitlines()
us3thread_run(int(len(lines)/2)+1, int(len(lines)))
