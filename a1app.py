"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Oscar So (ons4), Jee-In Lee (jl3697)
Date:   September 11, 2019
"""

import a1
currency_from = input("Enter source currency: ")
currency_to = input("Enter target currency: ")
amount_from = float(input("Enter original amount: "))
print("You can exchange " + str(amount_from) + " " + currency_from 
        + " for " + str(a1.exchange(currency_from, currency_to, amount_from))
        + " " + currency_to + ".")
