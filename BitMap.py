from PIL import Image

def calculate_dx_dy(x0, y0, x1, y1, size_x, size_y):
    dx = x1 - x0 / size_x
    dy = y1 - y0 / size_y
    return dx, dy

def main():
    file_name = input("Enter the file name: ")
    # Get valid x and y coordinates
    while True:
        x0 = int(input("Enter x0: "))
        y0 = int(input("Enter y0: "))
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        if x0 != x1 and y0 != y1:
            break
        else:
            print("Error: x0 and y0 must be different from x1 and y1")
            continue
    # Swap values 
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0

    # Get cx and cy constants
    cx = int(input("Enter cx: "))
    cy = int(input("Enter cy: "))

    # Get size x and y
    size_x = int(input("Enter size x: "))
    size_y = int(input("Enter size y: "))

    # Get loop_count
    while True:
        loop_count = int(input("Enter loop count: "))
        if loop_count <= 9:
            print("Error: loop count must be >+9")
            continue
        else:
            break

    # Get dx and dy
    dx, dy = calculate_dx_dy(x0, y0, x1, y1, size_x, size_y)

    pixels = [[0 for x in range(x1-x0)] for y in range(y1-y0)]
