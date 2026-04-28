
from Practice.calc import Calc

calc_obj = Calc()
print(calc_obj.add(10,4))
print(calc_obj.subtract(10,4))
print(calc_obj.multiply(10,4))

numbers = [10,20,30,40]

count = len(numbers)
print('Count is: ',count)

try:
    results = calc_obj.fdivide(10,4)
    for i in range(0,count+1):
        print(numbers[i])
except IndexError:
    print("Index out of range !!!")

except ZeroDivisionError:
    print('Division by zero')

except:
    print('Oops, something went wrong !!!')
else:
    print(results)
finally:
    print('Completed !!')