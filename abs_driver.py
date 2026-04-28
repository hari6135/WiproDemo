from Practice.rect_abs import Rectangle
from Practice.square_abs import Square

sq_obj = Square(10)

print(f'Area: {sq_obj.calculate_area()} \t Perimeter: {sq_obj.calculate_perimeter()}')

rect_obj = Rectangle(10,5)
print(f'Area: {rect_obj.calculate_area()} \t Perimeter: {rect_obj.calculate_perimeter()}')