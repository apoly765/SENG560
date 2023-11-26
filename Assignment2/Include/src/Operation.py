from typing import Any
from .utl import set_logger
from ast import literal_eval

LOG = set_logger()

class Operation:
    def __init__(self, input) -> None:
        if not isinstance(input, list):
            raise Exception(f"Input must be of type list")
        self._setattr("result", None)
        self._setattr("input", [literal_eval(x) if not isinstance(x, int) else x for x in input])
        LOG.info = f"Inputs ingested and converted to int for calculation"
    def __str__(self):
        return int(self.result)
    def _setattr(self, __name, __value):
        super().__setattr__(__name,__value) 
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "input":
            self.__init__(__value)
        elif __name== "result":
            raise Exception(f"Cannot directly set the value of result, use one of the functions in class Operations")
        else:
            self._setattr(self, __name, __value)
    def add(self):
        LOG.info = f"Inputs are being added"
        self._setattr("result", sum(self.input))
        return self
    def subtract(self):
        LOG.info = f"Inputs are being subtracted"
        result = self.input[0]
        for elem in self.input[1:]:
            result -= elem
        self._setattr("result", result)
        return self
    def multiply(self):
        LOG.info = f"Inputs are being multiplied"
        result = 1
        for elem in self.input:
            result = result * elem
        self._setattr("result", result)
        return self
    def divide(self):
        LOG.info = f"Inputs are being divided"
        result = self.input[0]
        for elem in self.input[1:]:
            result = result/elem
        self._setattr("result", int(result))
        return self
    def as_int(self):
        return int(self.result)
    def as_hex(self):
        return hex(self.result)
    def as_oct(self):
        return oct(self.result)
    def as_bin(self):
        return bin(self.result)
    

