from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')
S = TypeVar('S')
class CRDT(ABC, Generic[T,S]):

    @property
    @abstractmethod
    def state(self) -> S:
        pass

    @state.setter
    @abstractmethod
    def state(self, state: S) -> S:
        pass

    @property
    @abstractmethod
    def value(self) -> T:
        pass

    @value.setter
    @abstractmethod
    def value(self, value: T) -> T:
        pass


    @abstractmethod
    def merge(self,state: S):
        pass