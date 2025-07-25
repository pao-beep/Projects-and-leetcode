from LWWRegister import LWWRegister
from LWWMap import LWWMap
from RGB import RBGColor
from typing import Generic, TypeVar, Dict

class PixelData:
    id: str
    _data: LWWMap[RBGColor]

    def __init__(self,id: str):
        self.id=id
        self._data = LWWMap(id, {})

    def key(self, x:str, y:str) -> str:
        return f"{x},{y}"
    
    def getValue(self, x: str, y: str) -> RBGColor:
        return self._data.getValue(self.key(x,y))
    
    def getAllValues(self) -> Dict[str, RBGColor]:
        return self._data.getAllValues()
    
    def set(self, x: str, y: str, value: RBGColor)-> LWWRegister[RBGColor]:
        if not self._data.has(self.key(x,y)):
            self._data.set(self.key(x,y), LWWRegister(self.id,(self.id,1,RBGColor(255,255,255))))
        #print(f"set {self._data.get(self.key(x,y))} to {value}")
        return self._data.get(self.key(x,y))
    
    def get(self, x:str, y: str) -> LWWRegister[RBGColor]:
        if not self._data.has(self.key(x,y)):
            self._data.set(self.key(x,y), LWWRegister(self.id,(self.id,1,RBGColor(255,255,255))))
        #print(f"get {self._data.get(self.key(x,y))}")
        return self._data.get(self.key(x,y))
    
    def has(self, x: str, y: str) -> bool:
        if self._data.has(self.key(x,y)):
            return True
        return False
    
    def delete(self, x: str, y: str):
        if self.has(x,y):
            self._data.remove(self.key(x,y))
        return self._data.get(self.key(x,y)).state[2]
    
    def merge(self,state: Dict[str,LWWRegister[RBGColor].state]):
        self._data.merge(state)
    

    