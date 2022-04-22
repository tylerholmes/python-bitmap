from PIL import Image

def calculate_dx_dy(x0, y0, x1, y1, size_x, size_y):
    dx = x1 - x0 / size_x
    dy = y1 - y0 / size_y
    return dx, dy

def fill_rectangle_array(x0, y0, x1, y1, dx, dy, size_x, size_y, pixels):
    

    return pixels

def main():
    file_name = input("Enter the file name: ")  

    # Get valid x and y coordinates
    while True:
        x0 = float(input("Enter x0: "))
        y0 = float(input("Enter y0: "))
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
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
    cx = float(input("Enter cx: "))
    cy = float(input("Enter cy: "))

    # Get size x and y
    while True:
        size_x = int(input("Enter size x: "))
        size_y = int(input("Enter size y: "))
        if size_x <= 0 and size_y <= 0:
            print("Error: size x and y must be greater than 0")
            continue
        else:
            break

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

    pixels = [[0 for x in range(size_x)] for y in range(size_y)]

    image = Image.new("RGB", (size_x, size_y), "black")
    image.save(file_name + ".bmp")

if __name__ == "__main__":
    main()
    
