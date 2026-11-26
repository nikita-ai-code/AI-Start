def multiply(a,b):
    return a * b
result = multiply(7,6)
print(result)


def calculate_average(a,b,c):
    return (a + b + c) / 3
result = calculate_average(10,20,30)
print(result)


def power(number,exponent=2):
    return number ** exponent
result = power(5)
result2 = power(5,3)
print(result, result2)


def calculate_discount(price,discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount            
    return final_price
result = calculate_discount(1000,20)
print(result)


def calculate_discount(price,discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount            
    return final_price

def calculate_tax(price,tax=20):
    tax_amount = price * tax / 100
    return tax_amount

def calculate_total(price,discount):
    discounted_price = calculate_discount(price,discount)
    tax_amount = calculate_tax(discounted_price)
    total = discounted_price + tax_amount
    return total
price = float(input("Enter price:"))
discount = float(input("Enter discount:"))
total_result = calculate_total(price,discount)
print(total_result)