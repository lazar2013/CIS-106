def CompSqFt(length, width, height):
    floor_ceiling = 2 * (length * width)
    walls = 2 * (length * height) + 2 * (width * height)
    SqFt = floor_ceiling + walls
    return SqFt

r = input("Do you want to calculate the gallons of paint needed (yes or no)?")
while r == "yes":
    length = float(input("Enter the length of the room:"))
    width = float(input("Enter the width of the room:"))
    height = float(input("Enter the height of the room:"))

    SqFt = CompSqFt(length, width, height)
    gallons = SqFt / 50
    print(f"Gallons of paint needed: {gallons:.2f}")

    r = input("Do you want to calculate the gallons of paint needed (yes or no)?")