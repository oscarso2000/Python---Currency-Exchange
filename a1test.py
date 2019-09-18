"""
Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Author: Oscar So (ons4)
Date:   September 11, 2019
"""
import introcs
import a1

def testA():
    """
    Test procedure for Part A
    """
    introcs.assert_equals('0.863569', a1.before_space("0.863569 Euros"))
    introcs.assert_equals('Euros', a1.after_space("0.8663569 Euros"))
    #introcs.assert_equals(...)
    

def testB():
    """
    Test procedure for Part B
    """
    introcs.assert_equals('B C', a1.first_inside_quotes('A "B C" D'))
    introcs.assert_equals('A', a1.first_inside_quotes('"A" "B" C "D"'))
    introcs.assert_equals(' ', a1.first_inside_quotes('" "'))
<<<<<<< HEAD
    introcs.assert_equals('2 United States Dollars', a1.get_src('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals('1.727138 Euros', a1.get_dst('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals(True, a1.has_error( '{ "src" : "", "dst" : "", "valid" : false, "error" : "Source currency code is invalid." }'))
=======
    introcs.assert_equals("2 United States Dollars", a1.get_src('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals("1.727138 Euros", a1.get_dst('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals(False, a1.has_error('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals(True, a1.has_error('{ "src" : "", "dst" : "", "valid" : false, "error" : "Source currency code is invalid." }'))

>>>>>>> 92ba6a4b24a0fbff5ec92fe312fda467f38c6a01
    
def testC():
    """
    Test procedure for Part C
    """
    

def testD():
    """
    Test procedure for Part D
    """
    pass

testA()
testB()
testC()
testD()
print("Module a1 passed all tests")
