print("|========================================|"
      "| Multithreading by printing thread name"
      "||========================================|")
print()
import threading
import os

def job1():
    print("Job 1 assigned to thread: {} \n".format(threading.current_thread().name))
    print("ID of process running Job 1: {} \n".format(os.getpid()))

def job2():
    print("Job 2 assigned to thread: {} \n".format(threading.current_thread().name))
    print("ID of process running Job 2: {} \n".format(os.getpid()))

if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {} \n".format(os.getpid()))
    # print name of main thread
    print("Main thread name: {} \n".format(threading.current_thread().name))
    # creating threads
    t1 = threading.Thread(target=job1, name='Thread-1')
    t2 = threading.Thread(target=job2, name='Thread-2')
    # starting threads
    t1.start()
    t2.start()
    # wait for both threads to complete
    t1.join()
    t2.join()