import random
number = random.randint(1,100)
print(number)
print(number ** 2)


from random import randint
number = randint(1,50)
number2 = randint(1,50)
print(number)
print(number2)
print(number + number2)


import math
number = 81
print(math.sqrt(number))
number2 = 7.8
print(math.ceil(number2))
print(math.floor(number2))


from random import randint
import math
number = randint(1,100)
print(number)
print(math.sqrt(number))
print(math.ceil(math.sqrt(number)))


import random as r
import math as m
number = r.randint(1,100)
number2 = r.randint(1,100)
print(number)
print(number2)
sum_numbers = number + number2
print(sum_numbers)
sqrt_sum = m.sqrt(sum_numbers)
print(sqrt_sum)
print(m.ceil(sqrt_sum))
print(m.floor(sqrt_sum))


import calculator
print(calculator.add(5, 3))
print(calculator.multiply(5, 3))
print(calculator.subtract(10, 2))
print(calculator.divide(10, 2))
print(calculator.divide(10, 0))