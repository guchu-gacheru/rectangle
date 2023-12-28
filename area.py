# Area of a Rectangle

length = int(input("Enter the longest size indicated: "))
width = int(input("Enter the shortest size indicated: "))

area = length * width

print("Area of the rectangle is", area, ".")


# Area of a rectangle as a function
def area():
    return (length * width)


print("Area of the rectangle is", area(), ".")
