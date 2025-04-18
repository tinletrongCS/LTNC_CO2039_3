"""
 * Initial code for Assignment 3
 * file : run.py
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 16.04.2025
 
 * install extension ANTLR4 grammar syntax support, Better Comments
 * run code
    Usage:
    python3 run.py [test_case]   # Run tests (test_case is optional)

    Notes:
    - Replace [test_case] with the specific test you want to run, e.g., test_1.
    - If [test_case] is not provided, all tests in the suite will be executed.
"""
import unittest
from TestUtils import TestUtils
import inspect

class TestSymbolTable(unittest.TestCase):

    def test_001(self):
        input = ["INSERT a1 number", "INSERT b2 string"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 

    def test_002(self):
        input = ["INSERT x number", "INSERT y string", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 

    def test_003(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 17",
            "ASSIGN x 'abc'",
        ]
        expected = ["TypeMismatch: ASSIGN y 17"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 

    def test_004(self):
        input = [
            "INSERT x number",
            "ASSIGN y 17",
        ]
        expected = ["Undeclared: ASSIGN y 17"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 

    def test_005(self):
        input = [
            "INSERT x number",
            "ASSIGN x y",
        ]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 
    
    def test_006(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x y",
        ]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 

    def test_007(self):
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
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 

    def test_008(self):
        input = [
            "END",
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 

    def test_009(self):
        input = [
            "BEGIN",
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 
    
    def test_010(self):
        input = [
            "BEGIN",
            "BEGIN",
            "END",
            "BEGIN",
        ]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 

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
        self.assertTrue(TestUtils.check(input, expected, inspect.stack()[0].function)) 
