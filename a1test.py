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
    introcs.assert_equals('1.012324', a1.before_space("1.012324 HKD"))
    introcs.assert_equals('HKD', a1.after_space("1.012324 HKD"))
    

def testB():
    """
    Test procedure for Part B
    """
    introcs.assert_equals('B C', a1.first_inside_quotes('A "B C" D'))
    introcs.assert_equals('A', a1.first_inside_quotes('"A" "B" C "D"'))
    introcs.assert_equals(' ', a1.first_inside_quotes('" "'))
    introcs.assert_equals('2 United States Dollars', a1.get_src('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals('1.727138 Euros', a1.get_dst('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals(True, a1.has_error( '{ "src" : "", "dst" : "", "valid" : false, "error" : "Source currency code is invalid." }'))
    introcs.assert_equals("2 United States Dollars", a1.get_src('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals("1.727138 Euros", a1.get_dst('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals(False, a1.has_error('{ "src" : "2 United States Dollars", "dst" : "1.727138 Euros", "valid" : true, "error" : "" }'))
    introcs.assert_equals(True, a1.has_error('{ "src" : "2 United Stats Dollars", "dst" : "1.727138 Euros", "valid" : false, "error" : "Source currency code is invalid." }'))

    
def testC():
    """
    Test procedure for Part C
    """
    #introcs.assert_equals('{"currency_from": "3.673096 United Arab Emirates Dirham", "currency_to": "1 United States Dollars", "amount_from": "1 United States Dolalrs"}', a1.currency_response("3.673096 United Arab Emirates Dirham", "1 United States Dollars", 1.0))
    
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
    
    

testA()
testB()
testC()
testD()
print("Module a1 passed all tests")
