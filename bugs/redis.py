import redis
from django.conf import settings
import redis.lock

client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
)


class RedisBugStore:
    def __init__(self, application_token: str) -> None:
        self.application_token = application_token

    def get_number_key(self) -> str:
        return f"application_last_number_{self.application_token}"

    def get_last_number(self) -> int:
        key = self.get_number_key()
        number = client.get(key)
        return int(number) if number else 0

    def update_last_number(self, number: int):
        key = self.get_number_key()
        client.set(key, number)

    def get_lock_key(self) -> str:
        return f"application_lock_{self.application_token}"

    def lock(self):
        key = self.get_lock_key()
        self.lock_obj = client.lock(key, 10, blocking=True, sleep=0.001)
        return self.lock_obj.acquire(blocking=True)

    def unlock(self):
        if not hasattr(self, "lock_obj") or not self.lock_obj:
            return
        client.delete(self.lock_obj.name)

    def __enter__(self):
        self.lock()

    def __exit__(self, exc_type, exc_value, traceback):
        self.unlock()
