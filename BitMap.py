from PIL import Image

def calculate_dx_dy(x0, y0, x1, y1, size_x, size_y):
    dx = x1 - x0 / size_x
    dy = y1 - y0 / size_y
    return dx, dy

def calculate_xy_prime(x, y, dx, dy, cx, cy, loop_count):
    x_prime = (x * dx) * (x * dx) - (y * dy) * (y * dy) + cx
    y_prime = 2*(x * dx) * (y * dy) + cy

    for i in range(0, loop_count):
        x_prime = (x_prime * dx) * (x_prime * dx) - (y_prime * dy) * (y_prime * dy) + cx
        y_prime = 2*(y_prime * dx) * (y * dy) + cy
        i += 1

    return x_prime, y_prime

def prime_number_cases(x_prime, y_prime, loop_count):
    red = green = blue = 0
    if x_prime >= 0:
        if x_prime == float("inf"):
            red = 255
        elif x_prime > loop_count:
            red = 128
        elif x_prime <= loop_count:
            red = 64
        elif x_prime < .005:
            red = 0

    if x_prime < 0:
        if x_prime == float("-inf"):
            blue = 255
        elif x_prime < -1 * loop_count:
            blue = 255
        elif x_prime >= -1 * loop_count:
            blue = 64
        elif x_prime < -.005:
            blue = 0

    if y_prime >= 0:
        if y_prime == float("inf"):
            green = 255
        elif y_prime > loop_count:
            green = 200
        elif y_prime <= loop_count:
            green = 200
        elif y_prime < .005:
            green = 0

    if y_prime < 0:
        if y_prime == float("-inf"):
            green = 128
        elif y_prime < -1 * loop_count:
            green = 90
        elif y_prime >= -1 * loop_count:
            green = 64
        elif y_prime < -.005:
            green = 0

    return red, green, blue

def alter_pixels(img, pixels, loop_count, dx, dy, cx, cy):
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            x_prime, y_prime = calculate_xy_prime(i, j, dx, dy, cx, cy, loop_count)
            red, green, blue = prime_number_cases(x_prime, y_prime, loop_count)
            pixels[i,j] = (red, green, blue)

def main():
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

    # Create image using the prime number cases and corresponding RGB values
    img = Image.new("RGB", (size_x, size_y), (0,0,0))
    pixels = img.load()
    alter_pixels(img, pixels, loop_count, dx, dy, cx, cy)
    img.show()

if __name__ == "__main__":
    main()
    
