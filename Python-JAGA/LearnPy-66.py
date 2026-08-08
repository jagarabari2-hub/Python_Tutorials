print("|========================================|"
      "| Illustrating the concept of Multithreading "
      "||========================================|")
print()
import threading
def print_area(s):
    """ Function to print perimeter of side 's' """
    print("Area of square: {}".format(s * s))
def print_perimeter(s):
    """ Function to print perimeter of side 's' """
    print("Perimeter of square: {}".format(4 * s))
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_area, args=(5,))
    t2 = threading.Thread(target=print_perimeter, args=(5,))
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # thread completly executed
print("Multithreading Successfully executed")
print("|========================================|"
      "| Illustrating the concept of Single Threading "
      "||========================================|")
print()
def print_note():
    """ Function to print note """
    print("Thread function execution\n")
    return
if __name__=='__main__':
    for flag in range(16):
        t = threading.Thread(target=print_note)
        t.start()