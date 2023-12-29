#Perimeter of a rectangle

length = int(input("Enter the longest size indicated: "))
width = int(input("Enter the shortest size indicated: "))

perimeter = (length + width + length + width)

#or

perimeter = (length + width) * 2

print("The perimeter of the rectangle is", perimeter,".")