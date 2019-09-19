"""
Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Author: Oscar So (ons4), Jee-In Lee (jl3697)
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
    introcs.assert_equals('1.012324', a1.before_space("1.012324 HKD"))
    introcs.assert_equals('HKD', a1.after_space("1.012324 HKD"))
    

def testB():
    """
    Test procedure for Part B
    """
    introcs.assert_equals('B C', a1.first_inside_quotes('A "B C" D'))
    introcs.assert_equals('A', a1.first_inside_quotes('"A" "B" C "D"'))
    introcs.assert_equals(' ', a1.first_inside_quotes('" "'))
    introcs.assert_equals('2 United States Dollars', a1.get_lhs('{ "ok":true, "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "err" : "" }'))
    introcs.assert_equals('1.727138 Euros', a1.get_rhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'))
    introcs.assert_equals(True, a1.has_error( '{ "lhs" : "", "rhs" : "", "valid" : false, "err" : "Source currency code is invalid." }'))
    introcs.assert_equals("2 United States Dollars", a1.get_lhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'))
    introcs.assert_equals("1.727138 Euros", a1.get_rhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'))
    introcs.assert_equals(False, a1.has_error('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'))
    introcs.assert_equals(True, a1.has_error('{ "lhs" : "2 United Stats Dollars", "rhs" : "1.727138 Euros", "valid" : false, "err" : "Source currency code is invalid." }'))

    
def testC():
    """
    Test procedure for Part C
    """
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }', a1.currency_response("USD","CUP",2.5))
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"2.2160175 Euros", "err":"" }', a1.currency_response("USD","EUR",2.5))
    introcs.assert_equals('{ "ok":true, "lhs":"100 United States Dollars", "rhs":"782.455 Hong Kong Dollars", "err":"" }', a1.currency_response("USD","HKD",100))


def testD():
    """
    Test procedure for Part D
    """
    introcs.assert_equals(True, a1.is_currency("USD"))
    introcs.assert_equals(True, a1.is_currency("HKD"))
    introcs.assert_equals(True, a1.is_currency("EUR"))
    introcs.assert_equals(False, a1.is_currency("ABC"))
    introcs.assert_equals(False, a1.is_currency("usd"))
    introcs.assert_equals(False, a1.is_currency("Euros"))    
    introcs.assert_equals(882.72655789045, a1.exchange("EUR", "HKD", 100.0))
    introcs.assert_equals(782.455, a1.exchange("USD", "HKD", 100.0))
    
    
testA()
testB()
testC()
testD()
print("Module a1 passed all tests")
