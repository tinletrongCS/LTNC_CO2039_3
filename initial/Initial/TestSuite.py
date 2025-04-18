import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):

    def test_001(self):
        input = ["INSERT a1 number", "INSERT b2 string"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 1)) 

    def test_002(self):
        input = ["INSERT x number", "INSERT y string", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 2)) 

    def test_003(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 17",
            "ASSIGN x 'abc'",
        ]
        expected = ["TypeMismatch: ASSIGN y 17"]
        self.assertTrue(TestUtils.check(input, expected, 3)) 

    def test_004(self):
        input = [
            "INSERT x number",
            "ASSIGN y 17",
        ]
        expected = ["Undeclared: ASSIGN y 17"]
        self.assertTrue(TestUtils.check(input, expected, 4)) 

    def test_005(self):
        input = [
            "INSERT x number",
            "ASSIGN x y",
        ]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 5)) 
    
    def test_006(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x y",
        ]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 6)) 

    def test_007(self):
        input = [
            "INSERT x number",
            "ASSIGN x 15",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "ASSIGN x 23",
            "BEGIN",
            "INSERT y string",
            "END",
            "END",
        ]
        expected = [
            "success",
            "success",
            "success",
            "success",
            "success",
            "success"
                    ]

        self.assertTrue(TestUtils.check(input, expected, 7)) 

    def test_008(self):
        input = [
            "END",
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 8)) 

    def test_009(self):
        input = [
            "BEGIN",
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 9)) 
    
    def test_010(self):
        input = [
            "BEGIN",
            "BEGIN",
            "END",
            "BEGIN",
        ]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10)) 

    def test_011(self):
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
        self.assertTrue(TestUtils.check(input, expected, 11)) 
