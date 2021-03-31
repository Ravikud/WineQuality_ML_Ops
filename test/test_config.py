import pytest

class NotInRange(Exception):
def __init__(self,message="value not in range"):
    self.message=message
    #Inheriting from init constructor
    super().__init__(self.message)


def test_generic():
    a=5
    with pytest.raises(NotInRange):
        if a NotInRange(10,20):
            raise NotInRange
