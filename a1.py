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
    Returns: Substring of s; up to, but not including, the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    return s[:s.find(" ")]


def after_space(s):
    """
    Returns: Substring of s after the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it
    """
    return s[s.find(" ")+1:]


#Part B#
def first_inside_quotes(s):
    """
    Returns: The first substring of s between two (double) quote characters
    A quote character is one that is inside a string, not one that delimits it. 
    We typically use single quotes (') to delimit a string if want to use a
    double quote character (") inside of it.
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C' 
    because it only picks the first such substring.
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside.
    """
    return s[s.find('"')+1:s.find('"',s.find('"')+1)]


def get_lhs(js):
    """
    Returns: The SRC value in the response to a currency query.
    Given a JSON response to a currency query, this returns the string inside double quotes (") 
    immediately following the keyword "lhs". For example, if the JSON is
    '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'
    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    It returns the empty string if the JSON is the result of on invalid query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    y = json.loads(js)
    return y["lhs"]


def get_rhs(js):
    """
    Returns: The DST value in the response to a currency query.
    Given a JSON response to a currency query, this returns the string inside double quotes (") 
    immediately following the keyword "rhs". For example, if the JSON is
    '{ "lhs" : "2 United States Dollars", "rhs" : "1.727138 Euros", "valid" : true, "err" : "" }'
    then this function returns '1.727138 Euros' (not '"1.727138 Euros"').
    It returns the empty string if the JSON is the result of on invalid query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    y = json.loads(js)
    return y["rhs"]


def has_error(js):
    """
    Returns: True if the query has an err; False otherwise.
    Given a JSON response to a currency query, this returns the opposite of 
    the value following the keyword "valid". For example, if the JSON is
    '{ "lhs" : "", "rhs" : "", "valid" : false, "err" : "Source currency code is invalid." }'
    then the query is not valid, so this function returns True
    (It does NOT return the message 'Source currency code is invalid').
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    y = json.loads(js)
    return "invalid" in y["err"]


#Part C#
def currency_response(currency_from, currency_to, amount_from):
    """
    Returns: a JSON string that is a response to a currency query.
    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form
    '{ "lhs" : "<old-amt>", "rhs" : "<new-amt>", "valid" : true, "err" : "" }'
    where the values old-amount and new-amount contain the value and name for
    the original and new currencies. If the query is invalid, both old-amount 
    and new-amount will be empty, while "valid" will be followed by the value false.

    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string with no spaces

    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string with no spaces

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    return introcs.urlread('http://cs1110.cs.cornell.edu/2019fa/a1?src=' + currency_from + '&dst=' + currency_to + '&amt=' + str(amount_from))


#Part D#
def is_currency(currency):
    """
    Returns: True if currency is a valid (3 letter code for a)
    currency. It returns False otherwise.
    Parameter currency: the currency code to verify
    Precondition: currency is a string.
    """
    return (not (has_error(currency_response(currency, currency, 1.0))))


def exchange(currency_from, currency_to, amount_from):
    """
    Returns: amount of currency received in the given exchange.

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
    return float(before_space(get_rhs(currency_response(currency_from,currency_to,amount_from))))
