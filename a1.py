"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Author: Oscar So (ons4), Jee-In Lee (jl3697)
Date:   September 11, 2019
"""


import json
import introcs


#Part A#
def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    return s[:s.find(" ")]


def after_space(s):
    """
    Returns a copy of s after the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    return s[s.find(" ")+1:]


#Part B#
def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quotes    
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C' 
    because it only picks the first such substring.
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters
    inside.
    """
    return s[s.find('"')+1:s.find('"',s.find('"')+1)]


def get_lhs(js):
    """
    Returns the lhs value in the response to a currency query
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    #unsure how to use first_inside_quotes
    y = json.loads(js)
    x = first_inside_quotes('"lhs"')
    return y[x]
    


def get_rhs(js):
    """
    Returns the rhs value in the response to a currency query
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    y = json.loads(js)
    x = first_inside_quotes('"rhs"')    
    return y[x]

def has_error(js):
    """
    Returns True if the query has an error; False otherwise.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    y = json.loads(js)
    return "invalid" in y["err"]


#Part C#
def currency_response(currency_from, currency_to, amount_from):
    """
    Returns: Returns a JSON string that is a response to a currency query.
    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string with no spaces

    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string with no spaces

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    return introcs.urlread('http://cs1110.cs.cornell.edu/2019fa/a1?src=' +
            currency_from + '&dst=' + currency_to + '&amt=' + str(amount_from))


#Part D#
def is_currency(currency):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.
    Parameter currency: the currency code to verify
    Precondition: currency is a string.
    """
    return (not (has_error(currency_response(currency, currency, 1.0))))


def exchange(currency_from, currency_to, amount_from):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in currency 
    currency_from to the currency currency_to. The value returned 
    represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand (the SRC)
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to (the DST)
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    return float(
            before_space(get_rhs(
                currency_response(currency_from,currency_to,amount_from))))
