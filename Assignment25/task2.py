import threading
import queue

def process_queue(q):
    while not q.empty():
        try:
            number = q.get_nowait()
            is_even = 'even' if number % 2 == 0 else 'odd'
            print(f"Thread: {threading.current_thread().name}, Number: {number}, Even: {is_even}")
        except queue.Empty:
            break

# Create a FIFO queue
num_queue = queue.Queue()

# Create and start three threads
threads = []
for i in range(3):
    thread = threading.Thread(target=process_queue, args=(num_queue,), name=f'Thread-{i}')
    threads.append(thread)
    thread.start()

# Fill the queue with numbers
for number in range(10):
    num_queue.put(number)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All tasks are done.")
