from CRDTs import LWWRegister
from typing import TypeVar, Generic, Tuple, Dict


T = TypeVar('T')
Value = Dict[str, T]
State = Dict[str,LWWRegister[T|None].state]
class LWWMap(Generic[T]):
    id: str
    _data: State

    def __init__(self,id: str, state: State):
        self.id=id
        #self.state=state
        self._data = {key: LWWRegister(self.id, register) for key, register in state.items()}
    @property
    def id(self):
        return self.id

    @id.setter
    def id(self,id: str) -> id:
        pass

    @property
    def state(self):
        return self.state
    
    @state.setter
    def set(self,value: T) -> Tuple:
        pass

    def getAllState(self) -> State:
        return {key: register.state for key, register in self._data.items()}

    def setAllState(self, state: State):
        self._data = {key: LWWRegister(self.id, register) for key, register in state.items()}
        return self._data
    
    def getValue(self,key: str) -> T:
        return self._data[key].value()
    
    def getAllValues(self) -> Value:
        return {key: register.value() for key, register in self._data.items()}
    
    
    def set(self,key: str, value: T):
        if self._data[key]:
            self._data[key].set(value)
        else:
            self._data[key] = LWWRegister(self.id,(self.id,1,value))
        return self._data[key].state
    
    def get(self,key: str) -> LWWRegister[T]:
        return self._data[key]
    
    def has(self,key: str) -> bool:
            if key in self._data and self._data[key] is not None:
                return True
            return False
    
    def remove(self,key: str):
        if key in self._data:
            self._data[key] = None
        return self._data
    
    def clear(self):
        self._data.clear()
        return self._data
    
    def size(self) -> int:
        return len(self._data)
    
    def isEmpty(self) -> bool:
        return len(self._data) == 0
    
    def getId(self,key: str) -> str:
        return self._data[key].id
    
    def getState(self,key: str) -> LWWRegister[T].state:
        return self._data[key].state
    
    def getTimestamp(self,key: str) -> int:
        return self._data[key].state[1]
    
    def merge(self, state: State):
        for key, register in state.items():
            if key in self._data:
                self._data[key].merge(register)
            else:
                self._data[key] = LWWRegister(self.id, register)
        return self._data

