"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Oscar So (ons4), Jee-In Lee (jl3697)
Date:   September 11, 2019
"""

"""
Examples for a1app:
3-letter code for original currency: USD
3-letter code for the new currency: EUR
Amount of the original currency: 2.5
You can exchange 2.5 USD for 2.158923 EUR.
"""
import a1
currency_from = input("3-letter code for original currency: ")
currency_to = input("3-letter code for the new currency: ")
amount_from = float(input("Amount of the original currency: "))
print("You can exchange " + str(amount_from) + " " + currency_from 
        + " for " + str(a1.exchange(currency_from, currency_to, amount_from))
        + " " + currency_to + ".")
