from typing import Generic, TypeVar, Optional
from datetime import datetime

T = TypeVar('T')

class LWWRegister(Generic[T]):
    def __init__(self, value: Optional[T] = None, timestamp: Optional[datetime] = None):
        self.value = value
        self.timestamp = timestamp or datetime.now()

    def assign(self, value: T, timestamp: Optional[datetime] = None):
        timestamp = timestamp or datetime.now()
        if self.timestamp is None or timestamp > self.timestamp:
            self.value = value
            self.timestamp = timestamp

    def get(self) -> Optional[T]:
        return self.value

    @property
    def state(self) -> dict:
        return {'value': self.value, 'timestamp': self.timestamp}

    def merge(self, other: 'LWWRegister[T]'):
        if other.timestamp > self.timestamp:
            self.value = other.value
            self.timestamp = other.timestamp