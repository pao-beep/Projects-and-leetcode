"""
There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads to form water molecules.

There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given releaseHydrogen and releaseOxygen methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it must wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present, it must wait for an oxygen thread and another hydrogen thread.
We do not have to worry about matching the threads up explicitly; the threads do not necessarily know which other threads they are paired up with. The key is that threads pass the barriers in complete sets; thus, if we examine the sequence of threads that bind and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

 

Example 1:

Input: water = "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
Example 2:

Input: water = "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
 

Constraints:

3 * n == water.length
1 <= n <= 20
water[i] is either 'H' or 'O'.
There will be exactly 2 * n 'H' in water.
There will be exactly n 'O' in water."""

import threading

class H2O:
    def __init__(self):
        self.h_sem = threading.Semaphore(2)  # Allows up to 2 H threads to proceed
        self.o_sem = threading.Semaphore(1)  # Allows 1 O thread to proceed
        self.barrier = threading.Barrier(3)  # Synchronizes exactly 3 threads (2H + 1O)
        self.h_queue = 0
        self.o_queue = 0
        self.lock = threading.Lock()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.lock:
            self.h_queue += 1
            if self.h_queue >= 2 and self.o_queue >= 1:
                self.h_queue -= 2
                self.o_queue -= 1
                self.h_sem.release(2)
                self.o_sem.release(1)
        
        self.h_sem.acquire()
        releaseHydrogen()
        try:
            self.barrier.wait()
        except threading.BrokenBarrierError:
            pass

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.lock:
            self.o_queue += 1
            if self.h_queue >= 2 and self.o_queue >= 1:
                self.h_queue -= 2
                self.o_queue -= 1
                self.h_sem.release(2)
                self.o_sem.release(1)
        
        self.o_sem.acquire()
        releaseOxygen()
        try:
            self.barrier.wait()
        except threading.BrokenBarrierError:
            pass


"""How threading.Barrier(3) Works:
Initialization: When you create a barrier with threading.Barrier(3), it is set to wait for exactly 3 threads.

Waiting at the Barrier: Each thread that reaches the barrier calls the wait() method. The thread is then blocked until the total number of threads that have called wait() reaches 3.

Release: Once 3 threads have called wait(), all 3 threads are unblocked and can continue their execution. The barrier is then reset and can be used again for the next set of threads.

Example Usage:
Here’s a simple example to illustrate how threading.Barrier(3) works:
"""
"""import threading

def worker(barrier, name):
    print(f"{name} is waiting at the barrier.")
    barrier.wait()
    print(f"{name} passed the barrier.")

barrier = threading.Barrier(3)

threads = [
    threading.Thread(target=worker, args=(barrier, "Thread 1")),
    threading.Thread(target=worker, args=(barrier, "Thread 2")),
    threading.Thread(target=worker, args=(barrier, "Thread 3"))
]

for t in threads:
    t.start()

for t in threads:
    t.join()"""


"""Condition Variables in Thread Synchronization
A condition variable (threading.Condition) is a synchronization primitive that allows threads to wait until a certain condition is met. It is always associated with a lock (typically the same lock used to protect shared data). The key methods are:

wait(): Releases the lock and blocks until another thread calls notify() or notify_all().

notify(): Wakes up one waiting thread.

notify_all(): Wakes up all waiting threads.

How Condition Variables Could Be Used in the H2O Problem
Instead of semaphores, we could use:

A lock (threading.Lock) to protect shared counters (h_count and o_count).

A condition variable (threading.Condition) to make threads wait until the correct number of H and O threads are available.
"""
"""
import threading

class H2O:
    def __init__(self):
        self.lock = threading.Lock()
        self.h_count = 0  # Number of waiting H threads
        self.o_count = 0  # Number of waiting O threads
        self.condition = threading.Condition(self.lock)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.lock:
            self.h_count += 1
            # Notify waiting O threads if enough H threads are available
            if self.h_count >= 2 and self.o_count >= 1:
                self.condition.notify_all()  # Wake up waiting threads
            else:
                self.condition.wait()  # Wait until 2H + 1O are available
            releaseHydrogen()
            self.h_count -= 1

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.lock:
            self.o_count += 1
            # Notify waiting H threads if enough O threads are available
            if self.h_count >= 2 and self.o_count >= 1:
                self.condition.notify_all()  # Wake up waiting threads
            else:
                self.condition.wait()  # Wait until 2H + 1O are available
            releaseOxygen()
            self.o_count -= 1
"""