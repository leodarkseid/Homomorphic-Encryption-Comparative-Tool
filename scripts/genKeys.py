import threading
import time
from bfvKeyGen import keyGen as bfvGen
from bgvKeyGen import keyGen as bgvGen
from ckksKeyGen import keyGen as ckksGen


def genAllkeys():
    start_time = time.time()

    # threads = []

    # t1 = threading.Thread(target=bfvGen)
    # t2 = threading.Thread(target=bgvGen)
    # t3 = threading.Thread(target=ckksGen)

    # threads.append(t1)
    # threads.append(t2)
    # threads.append(t3)

    # for thread in threads:
    #     thread.start()

    # for thread in threads:
    #     thread.join()

    bfvGen()
    bgvGen()
    ckksGen()
    end_time = time.time()
    print("end", end_time - start_time)


if __name__ == '__main__':
    genAllkeys()
