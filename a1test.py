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
    #test procedure for a1.before_space: the function a1.before_space returns the substring of the string s; up to, but not including the first space. For example, s is "0.863569 Euros". The function a1.before_space returns '0.863569', the first substring of s up to but not including the first space.
   introcs.assert_equals('0.863569', a1.before_space("0.863569 Euros"))
      
   #test procedure for a1.after_space: the function a1.after_space returns the substring of s after the first space. For example, s is "0.863569 Euros". The function a1.after_space returns 'Euros', the substring of s after the first space.
  introcs.assert_equals('Euros', a1.after_space("0.8663569 Euros"))
   
  #test procedure for a1.before_space: the function a1.before_space returns the substring of the string s; up to, but not including the first space. For example, s is "1.012324 HKD". The function a1.before_space returns '1.012324', the first substring of s up to but not including the first space. 
   introcs.assert_equals('1.012324', a1.before_space("1.012324 HKD"))
        
  #test procedure for a1.after_space: the function a1.after_space returns the substring of s after the first space. For example, s is "1.012324 HKD". The function a1.after_space returns 'HKD', the substring of s after the first space.
  introcs.assert_equals('HKD', a1.after_space("1.012324 HKD"))
     

def testB():
    """
    Test procedure for Part B
    """
     #test procedures for a1.first_inside_quotes: the function a1.first_inside_quotes returns the first substring of s between two double quote characters. For example, if s is 'A "B C" D', the function first_inside_quotes returns 'B C'. If s is '"A" "B" C "D"', the function first_inside_quotes returns 'A'. If s is " ", the function first_inside_quotes returns ' '.
    introcs.assert_equals('B C', a1.first_inside_quotes('A "B C" D'))
    introcs.assert_equals('A', a1.first_inside_quotes('"A" "B" C "D"'))
    introcs.assert_equals(' ', a1.first_inside_quotes('" "'))
   
   #test procedure for a1.get_lhs: a1.get_src returns the string inside double quotes immediately following the keyword "lhs". If JSON is '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }', the function a1.get_lhs returns '2 United States Dollars' (not '"2 United States Dollars"'). 
   introcs.assert_equals('2 United States Dollars', a1.get_lhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : false, "err" : "" }'))
    
    #test procedure for a1.get_rhs: a1.get_rhs returns the string inside double quotes immediately following the keyword "rhs". If JSON is '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }', the function returns '2 United States Dollars' (not '"2 United States Dollars"').
   introcs.assert_equals('1.727138 Euros', a1.get_rhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'))
    
    #test procedure for a1.has_error: a1.get_src returns True if the query has an error. Since the query is not valid, the function returns True (it does NOT return "Source currency code is invalid").
    introcs.assert_equals(True, a1.has_error( '{ "lhs" : "", "rhs" : "", "valid" : false, "err" : "Source currency code is invalid." }'))
    
    #test procedure for a1.get_lhs: a1.get_src returns the string inside double quotes immediately following the keyword "lhs". If JSON is '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }', the function returns "2 United States Dollars".
    introcs.assert_equals("2 United States Dollars", a1.get_lhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : false, "err" : "" }'))
    
    #test procedure for a1.get_lhs: a1.get_src returns the string inside double quotes immediately following the keyword "lhs". If JSON is '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }', the function a1.get_lhs returns "2 United States Dollars". 
    introcs.assert_equals("1.727138 Euros", a1.get_dst('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "error" : "" }'))
     
     #test procedure for a1.has_error: a1.has_error returns False since the query does not have an error and is thus "valid".
    introcs.assert_equals(False, a1.has_error('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : false, "error" : "" }'))
    
    #test procedure for a1.has_error: a1.has_error returns True since the query has an error. The function does NOT return "Source currency code is invalid".
    introcs.assert_equals(True, a1.has_error('{ "lhs" : "", "rhs" : "", "valid" : false, "err" : "Source currency code is invalid." }'))
   
   #test procedure for a1.get_lhs: a1.get_lhs returns the string inside double quotes immediately following the keyword "lhs". If JSON is '{ "ok":true, "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "err" : "" }', the function a1.get_lhs returns '2 United States Dollars'.
    introcs.assert_equals('2 United States Dollars', a1.get_lhs('{ "ok":true, "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "err" : "" }'))

    #test procedure for a1.get_rhs: a1.get_rhs returns the string inside double quotes immediately following the keyword "rhs". If JSON is '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }', the function a1.get_rhs returns '1.727138 Euros'.
    introcs.assert_equals('1.727138 Euros', a1.get_rhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'))
    
    #test procedure for a1.has_error: a1.has_error returns True if the query has an error. If JSON is '{ "lhs" : "", "rhs" : "", "valid" : false, "err" : "Source currency code is invalid." }' the function a1.has_error returns True, since the query has an error (it does NOT return "Source currency code is invalid").
    introcs.assert_equals(True, a1.has_error( '{ "lhs" : "", "rhs" : "", "valid" : false, "err" : "Source currency code is invalid." }'))

    #test procedure for a1.get_lhs: a1.get_lhs returns the string inside double quotes immediately following "lhs". If JSON is '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }' the function a1.get_lhs returns "2 United States Dollars".
    introcs.assert_equals("2 United States Dollars", a1.get_lhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'))

    #test procedure for a1.get_rhs: a1.get_rhs returns the string inside double quotes immediately following "rhs". If JSON is '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }', the function a1.get_rhs returns "1.727138 Euros".
    introcs.assert_equals("1.727138 Euros", a1.get_rhs('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'))

    #test procedure for a1.has_error: a1.has_error returns False if the query is "valid". It does NOT return "valid".
    introcs.assert_equals(False, a1.has_error('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : false, "err" : "" }'))

    #test procedure for a1.has_error: a1.has_error returns True if the query has an error. It does NOT return "Source currency code is invalid".
    introcs.assert_equals(True, a1.has_error('{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : false, "err" : "Source currency code is invalid." }'))

    
def testC():
    """
    Test procedure for Part C
    """
    #test procedure for a1.currency_response: a1.currency_response returns the response to a currency query. The query converts amount_from money in currency currency_from to the currency currency_to. The query is "valid", with the old amount ("lhs") displaying 2.5 United States Dollars and the new converted amount ("rhs") 64.375 Cuban Pesos.
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }', a1.currency_response("USD","CUP",2.5))

    #test procedure for a1.currency_response: a1.currency_response returns the response to a currency query. The query converts amount_from money in currency currency_from to the currency currency_to. The query is "valid", with the old amount ("lhs") displaying 2.5 United States Dollars and the new converted amount ("rhs") 2.2160175 Euros.
    introcs.assert_equals('{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"2.2160175 Euros", "err":"" }', a1.currency_response("USD","EUR",2.5))
   
    #test procedure for a1.currency_response: a1.currency_response returns the response to a currency query. The query converts amount_from money in currency currency_from to the currency currency_to. The query is "valid", with the old amount ("lhs") displaying 100 United States Dollars and the new converted amount ("rhs") 782.455 Hong Kong Dollars.
   introcs.assert_equals('{ "ok":true, "lhs":"100 United States Dollars", "rhs":"782.455 Hong Kong Dollars", "err":"" }', a1.currency_response("USD","HKD",100))


def testD():
    """
    Test procedure for Part D
    """
    #test procedures for a1.is_currency: a1.is_currency returns True if currency is a valid (3 letter code for a currency. It returns False otherwise. For example, for the strings "USD", "HKD", "EUR", they are valid three letter, all capitalized abbreviations of currency, so the function a1.is_currency returns True. For the strings "ABC", "usd", "Euros", they are not valid forms of currency, not properly capitalized, nor abbreviated properly, respectively.
    introcs.assert_equals(True, a1.is_currency("USD"))
    introcs.assert_equals(True, a1.is_currency("HKD"))
    introcs.assert_equals(True, a1.is_currency("EUR"))
    introcs.assert_equals(False, a1.is_currency("ABC"))
    introcs.assert_equals(False, a1.is_currency("usd"))
    introcs.assert_equals(False, a1.is_currency("Euros"))  

    #test procedures for a1.exchange: a1.exchange returns the amount of currency received in the given exchange. The user is changing amount_from money in currency currency_from to the currency currency_to. The float value returned represents the amount in currency currency_to. When exchanging 100.0 Euros to Hong Kong Dollars, the function a1.exchange returns 882.72655789045 Hong Kong Dollars. When exchanging 100.0 United States Dollars to Hong Kong Dollars, the function a1.exchange returns 782.455 Hong Kong Dollars.
    introcs.assert_equals(882.72655789045, a1.exchange("EUR", "HKD", 100.0))
    introcs.assert_equals(782.455, a1.exchange("USD", "HKD", 100.0))
    
    
testA()
testB()
testC()
testD()
print("Module a1 passed all tests")
