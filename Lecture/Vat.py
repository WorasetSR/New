'''
Price = P
'''
P = float(input("Enter a price : "))
Vat = float(input("Enter a VAT : "))
result = ( P * Vat / 100) + P
print(result)