from betterconcurrent import ThreadPoolExecutor

def wait_on_future(executor):
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())

with ThreadPoolExecutor(max_workers=2) as executor:
    f = executor.submit(wait_on_future, executor)
    f.result()

print('now for the hard part...')

with ThreadPoolExecutor(max_workers=1) as executor:
    f = executor.submit(wait_on_future, executor)
    f.result()
