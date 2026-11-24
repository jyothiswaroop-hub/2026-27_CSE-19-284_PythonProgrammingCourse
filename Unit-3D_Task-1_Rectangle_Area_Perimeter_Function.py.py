def rectangle_area_perimeter(l, b):
    a = l * b
    p = 2 * (l + b)
    
    return a, p

length = 5
breadth = 6
area, perimeter = rectangle_area_perimeter(length, breadth)

print("Area:", area)
print("Perimeter:", perimeter)
