import time


class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.water = 0  # This represents the current water (or request) level in the bucket
        self.last_request_time = time.time()

    def can_consume(self, amount=1):
        current_time = time.time()
        time_elapsed = current_time - self.last_request_time

        # Simulate the leak over the elapsed time
        leaked_amount = time_elapsed * self.leak_rate
        self.water = max(0, self.water - leaked_amount)

        # Check if adding the new request would overflow the bucket
        if self.water + amount <= self.capacity:
            self.water += amount
            self.last_request_time = current_time
            return True
        return False


# Example of using the LeakyBucket in a Python service:
if __name__ == '__main__':
    bucket = LeakyBucket(10, 1)  # 10 requests capacity, and it leaks at 1 request per second


    def handle_request():
        if bucket.can_consume():
            print("Request processed")
        else:
            print("Rate limit exceeded")


    # Simulating incoming requests
    for _ in range(15):
        handle_request()
        time.sleep(0.5)  # Sleep for 0.5 seconds between requests to simulate incoming request patterns
