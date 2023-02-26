from betterconcurrent import ThreadPoolExecutor

def wait_on_future(executor):
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    yield from f.yield_until_done()
    print(f.result())

with ThreadPoolExecutor(max_workers=1) as executor:
    f = executor.submit(wait_on_future, executor)
    executor.join()
