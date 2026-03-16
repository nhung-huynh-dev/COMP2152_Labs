import threading
import time


def simulate_task(name, duration, lock):

    lock.acquire()
    print(f"[START] {name}")
    lock.release()

    time.sleep(duration)

    lock.acquire()
    print(f"[DONE]  {name} ({duration}s)")
    lock.release()


def run_sequential(tasks, lock):

    for name, duration in tasks:
        simulate_task(name, duration, lock)


def run_threaded(tasks, lock):

    threads = []

    for name, duration in tasks:
        t = threading.Thread(target=simulate_task, args=(name, duration, lock))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def main():

    tasks = [
        ("Brew Coffee", 3),
        ("Toast Bread", 2),
        ("Fry Eggs", 4)
    ]

    lock = threading.Lock()

    print("=" * 60)
    print("  SEQUENTIAL vs THREADED EXECUTION")
    print("=" * 60)

    print("\n--- Running SEQUENTIALLY ---")

    start = time.time()
    run_sequential(tasks, lock)
    seq_time = time.time() - start

    print(f"Sequential time: {seq_time:.2f} seconds")

    print("\n--- Running with THREADS ---")

    start = time.time()
    run_threaded(tasks, lock)
    thread_time = time.time() - start

    print(f"Threaded time: {thread_time:.2f} seconds")

    speedup = seq_time / thread_time
    print(f"\nSpeedup: {speedup:.2f}x faster with threads!")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()