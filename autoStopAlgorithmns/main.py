import time
import multiprocessing


def approximation_algorithm_a():
    counter = 0
    while True:
        print(f'Counter: {counter}')
        counter += 1


def approximation_algorithm_b():
    counter = 0
    while True:
        print(f'Counter: {counter}')
        counter += 2
        time.sleep(0.2)


if __name__ == '__main__':
    process = multiprocessing.Process(target=approximation_algorithm_b)

    start = time.perf_counter()
    process.start()

    time.sleep(5)

    process.terminate()
    end = time.perf_counter()

    print(end-start)

    process.join()