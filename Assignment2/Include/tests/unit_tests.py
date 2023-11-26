import unittest
from reuse_math.Operation import Operation

class TestReuseMath(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        test_inputs = [1, 2, 3]
        self.operations = []
        for inp in test_inputs:
            self.operations.append(Operation([int(x) for x in range(inp)]))
            self.operations.append(Operation([hex(x) for x in range(inp)]))
            self.operations.append(Operation([bin(x) for x in range(inp)]))
        self.operations.append(Operation([1, hex(2), oct(3), bin(4)]))
    def test_define_operations(self):
        for operation in self.operations:
            self.assertIsInstance(operation, Operation, f"Operation not parsing input")
    def test_add(self):
        for operation in self.operations:
            self.assertIsInstance(operation.add().as_int(), int, f"Addition not working for int return for operation input {operation.input}")
            self.assertIsInstance(operation.add().as_hex(), str, f"Addition not working for hex return for operation input {operation.input}")
            self.assertIsInstance(operation.add().as_bin(), str, f"Addition not working for bin return for operation input {operation.input}")
            self.assertIsInstance(operation.add().as_oct(), str, f"Addition not working for oct return for operation input {operation.input}")
    def test_sub(self):
        for operation in self.operations:
            self.assertIsInstance(operation.subtract().as_int(), int, f"Subtract not working for int return for operation input {operation.input}")
            self.assertIsInstance(operation.subtract().as_hex(), str, f"Subtract not working for hex return for operation input {operation.input}")
            self.assertIsInstance(operation.subtract().as_bin(), str, f"Subtract not working for bin return for operation input {operation.input}")
    def test_mult(self):
        for operation in self.operations:
            self.assertIsInstance(operation.multiply().as_int(), int, f"Multiply not working for int return for operation input {operation.input}")
            self.assertIsInstance(operation.multiply().as_hex(), str, f"Multiply not working for hex return for operation input {operation.input}")
            self.assertIsInstance(operation.multiply().as_bin(), str, f"Multiply not working for bin return for operation input {operation.input}")
    def test_divide(self):
        for operation in self.operations:
            self.assertIsInstance(operation.divide().as_int(), int, f"Divide not working for int return for operation input {operation.input}")
            self.assertIsInstance(operation.divide().as_hex(), str, f"Divide not working for hex return for operation input {operation.input}")
            self.assertIsInstance(operation.divide().as_bin(), str, f"Divide not working for bin return for operation input {operation.input}")
    def test_basic_add(self):
        self.assertEquals(Operation([8,9]).add().as_int(), 17)
        self.assertEquals(Operation([8,9]).add().as_hex(), hex(17))
        self.assertEquals(Operation([8,9]).add().as_oct(), oct(17))
        self.assertEquals(Operation([8,9]).add().as_bin(), bin(17)) 
    def test_basic_sub(self):
        self.assertEquals(Operation([8,9]).subtract().as_int(), -1)
        self.assertEquals(Operation([8,9]).subtract().as_hex(), hex(-1))
        self.assertEquals(Operation([8,9]).subtract().as_oct(), oct(-1))
        self.assertEquals(Operation([8,9]).subtract().as_bin(), bin(-1))
    def test_basic_mult(self):
        self.assertEquals(Operation([8,9]).multiply().as_int(), 72)
        self.assertEquals(Operation([8,9]).multiply().as_hex(), hex(72))
        self.assertEquals(Operation([8,9]).multiply().as_oct(), oct(72))
        self.assertEquals(Operation([8,9]).multiply().as_bin(), bin(72))
    def test_basic_divide(self):
        self.assertEquals(Operation([2,1]).divide().as_int(), 2)
        self.assertEquals(Operation([2,1]).divide().as_hex(), hex(2))
        self.assertEquals(Operation([2,1]).divide().as_oct(), oct(2))
        self.assertEquals(Operation([2,1]).divide().as_bin(), bin(2))

if __name__ == "__main__":
    unittest.main()