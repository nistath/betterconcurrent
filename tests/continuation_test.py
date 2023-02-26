from betterconcurrent import ThreadPoolExecutor


def wait_on_future(executor):
    f = executor.submit(pow, 5, 2)
    yield from f.yield_until_done()
    return f.result()


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=1) as executor:
        f = executor.submit(wait_on_future, executor)
        assert f.result() == 25
        executor.join()
