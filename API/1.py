from currency_converter import CurrencyConverter

c = CurrencyConverter()

# แปลง 100 USD เป็น THB
result = c.convert(100, 'USD', 'THB')
print(f'100 USD = {result:.2f} THB')
