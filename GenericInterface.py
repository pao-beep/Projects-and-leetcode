from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# Define type variables
T = TypeVar('T')
U = TypeVar('U')

class MyGenericInterface(ABC, Generic[T, U]):
    @property
    @abstractmethod
    def prop1(self) -> T:
        pass

    @prop1.setter
    @abstractmethod
    def prop1(self, value: T):
        pass

    @property
    @abstractmethod
    def prop2(self) -> U:
        pass

    @prop2.setter
    @abstractmethod
    def prop2(self, value: U):
        pass

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self, param: T):
        pass

# Example implementation of the generic interface
class MyClass(MyGenericInterface[int, str]):
    def __init__(self):
        self._prop1 = 0
        self._prop2 = ""

    @property
    def prop1(self) -> int:
        return self._prop1

    @prop1.setter
    def prop1(self, value: int):
        self._prop1 = value

    @property
    def prop2(self) -> str:
        return self._prop2

    @prop2.setter
    def prop2(self, value: str):
        self._prop2 = value

    def method1(self):
        print("Method1 implementation")

    def method2(self, param: int):
        print(f"Method2 implementation with param: {param}")

# Usage
obj = MyClass()
obj.prop1 = 42
print(obj.prop1)  # Output: 42
obj.prop2 = "Hello"
print(obj.prop2)  # Output: Hello
obj.method1()  # Output: Method1 implementation
obj.method2(100)  # Output: Method2 implementation with param: 100