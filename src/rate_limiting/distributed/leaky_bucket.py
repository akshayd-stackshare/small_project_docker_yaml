import time
import redis


class RedisLeakyBucket:
    def __init__(self, redis_host, capacity, leak_rate, fqdn):
        self.redis = redis.StrictRedis(host=redis_host, port=6379, db=0)
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.fqdn = fqdn

    def _get_bucket_state(self):
        water = float(self.redis.hget(self.fqdn, 'water') or 0)
        last_request_time = float(self.redis.hget(self.fqdn, 'last_request_time') or 0)
        return water, last_request_time

    def can_consume(self, amount=1):
        water, last_request_time = self._get_bucket_state()
        current_time = time.time()
        time_elapsed = current_time - last_request_time

        # Calculate leaked amount
        leaked_amount = time_elapsed * self.leak_rate
        water = max(0, water - leaked_amount)

        if water + amount <= self.capacity:
            self.redis.hmset(self.fqdn, {
                'water': water + amount,
                'last_request_time': current_time
            })
            return True
        return False

    def process_request(self):
        while not self.can_consume():
            print('waiting...')
            time.sleep(0.1)
        print("Processing request for", self.fqdn)


if __name__ == '__main__':
    REDIS_HOST = 'localhost'
    bucket = RedisLeakyBucket(REDIS_HOST, 1, 1, "www.example.com")

    for _ in range(15):
        bucket.process_request()
        time.sleep(0.5)


    bucket = RedisLeakyBucket(REDIS_HOST, 5, 1, "www.example.com")

    for _ in range(15):
        bucket.process_request()
        time.sleep(0.5)


    bucket = RedisLeakyBucket(REDIS_HOST, 10, 1, "www.example.com")

    for _ in range(30):
        bucket.process_request()
        time.sleep(0.5)
