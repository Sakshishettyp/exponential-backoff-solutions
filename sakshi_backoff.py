import time
import random
import requests


def backoff(url, max_retries, base_delay, jitter, timeout):
    for i in range(max_retries):
        try:
            r = requests.get(url, timeout=timeout)
            if r.status_code == 200:
                print("Success")
                return r.text
        except Exception as e:
            wait = base_delay * (2**i)
            wait += random.uniform(-jitter, jitter)

            if wait < 0:
                wait = 0
            print(f"Try {i + 1}")
            print(f"waiting {wait:.2f}s")
            time.sleep(wait)


if __name__ == "__main__":
    backoff("aa", 3, 1.0, 0.25, 3.0)
# https://httpstat.us/503
# https://google.com
