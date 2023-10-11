import time


class FixedDelay:
    def __init__(self, delay_seconds):
        self.delay_seconds = delay_seconds
        self.last_request_time = 0

    def can_proceed(self):
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time

        if time_since_last_request < self.delay_seconds:
            return False
        else:
            self.last_request_time = current_time
            return True


if __name__ == '__main__':
    def handle_request():
        if limiter.can_proceed():
            print("Request processed")
        else:
            print("Waiting for delay")


    # Usage:
    limiter = FixedDelay(1)  # 1 second delay between requests

    # Simulating incoming requests
    for _ in range(5):
        handle_request()
        time.sleep(0.5)
