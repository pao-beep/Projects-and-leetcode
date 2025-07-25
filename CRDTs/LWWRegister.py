from CRDTs import CRDTInterface

from typing import Generic, TypeVar, Tuple

T = TypeVar('T')
class LWWRegister(Generic[T]):
    id: str
    state: Tuple[str, int, T]  # (peerId, timestamp, value)
    # state: Tuple[str, int, T]  # (peerId, timestamp, value)

    def __init__(self,id: str, state: Tuple[str,int, T]):
        self.id=id
        self.state=state

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self,id: str) -> id:
        self.id = id
        return self.id

    @property
    def state(self):
        return self.state

    @state.setter
    def set(self,value: T) -> Tuple:
        self.state = [self.id, self.state[1]+1,value]

    def value(self):
        return self.state[2]

    def merge(self,state: Tuple[str,int,T]):
        remotePeer, remoteTimestamp,remoteValue = state
        localPeer,localTimeStamp,localValue = self.state

        if localTimeStamp > remoteTimestamp:
            return

        if (localTimeStamp == remoteTimestamp)  and  (localPeer > remotePeer):
            return

        self.state = state