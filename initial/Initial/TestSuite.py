import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):

    def test_0(self):
        input = ["INSERT a1 number", "INSERT b2 string"]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 0))


    def test_1(self):
        input = ["INSERT x number", "INSERT y string", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]

        self.assertTrue(TestUtils.check(input, expected, 1))

    def test_2(self):
        input = ["INSERT var1 number", "INSERT var2 string", "INSERT var3 number"]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 2))

    def test_3(self):
        input = ["INSERT x number", "INSERT y string", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]

        self.assertTrue(TestUtils.check(input, expected, 3))

    def test_4(self):
        input = ["INSERT a number", "INSERT b", "INSERT c string"]
        expected = ["Invalid: INSERT b"]
        
        self.assertTrue(TestUtils.check(input, expected, 4))
    
    def test_5(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 17",
            "ASSIGN x 'abc'",
        ]
        expected = ["TypeMismatch: ASSIGN y 17"]

        self.assertTrue(TestUtils.check(input, expected, 5))

    def test_6(self):
        input = ["INSERT x number", 
                 "INSERT y string", 
                 "ASSIGN x 15",
                 "ASSIGN y x",]
        expected = ["TypeMismatch: ASSIGN y x"]

        self.assertTrue(TestUtils.check(input, expected, 6))

    def test_7(self):
        input = ["INSERT x number",
                 "INSERT y string",
                 "ASSIGN z 3",]
        
        expected = ["Undeclared: ASSIGN z 3"]

        self.assertTrue(TestUtils.check(input, expected, 7))
        
    """
    def test_8(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "END",
            "END",
        ]
        expected = ["success", "success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 8))

    def test_9(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "LOOKUP x",
            "LOOKUP y",
            "END",
        ]
        expected = ["success", "success", "success", "1", "0"]

        self.assertTrue(TestUtils.check(input, expected, 9))

    def test_10(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "y//0 x//1 z//1"]

        self.assertTrue(TestUtils.check(input, expected, 10))

    def test_11(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "RPRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "z//1 x//1 y//0"]

        self.assertTrue(TestUtils.check(input, expected, 11))
    
    """
    
