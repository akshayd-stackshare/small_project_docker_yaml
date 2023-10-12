import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill_time = time.time()

    def refill(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_refill_time

        # Calculate the number of tokens to add, based on the refill_rate and time_elapsed
        new_tokens = time_elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill_time = current_time

    def can_consume(self, amount=1):
        self.refill()  # First, add tokens to the bucket based on time since last refill
        if self.tokens >= amount:
            self.tokens -= amount
            return True
        return False


if __name__ == '__main__':
    # Example of using the TokenBucket in a Python service:
    bucket = TokenBucket(10, 1)  # 10 tokens capacity, and refills at 1 token per second

    def handle_request():
        if bucket.can_consume():
            print("Request processed")
        else:
            print("Rate limit exceeded")

    # Simulating incoming requests
    for _ in range(15):
        handle_request()
        time.sleep(0.5)  # Sleep for 0.5 seconds between requests to simulate incoming request patterns
