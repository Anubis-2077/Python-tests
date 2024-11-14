# Function to rotate the image anticlockwise
def rotate_image(size, img):
    for layer in range(size // 2):
        first = layer
        last = size - layer - 1
        for i in range(first, last):
            # guardar el valor superior
            top = img[first][i]
            # mover el valor de la derecha a la perte superior
            img[first][i] = img[i][last]
            # mover el valor inferior a la derecha
            img[i][last] = img[last][size - i - 1]
            # mover el valor de la izquierda a la parte inferior
            img[last][size - i - 1] = img[size - i - 1][first]
            # mover el valor superior a la izquierda
            img[size - i - 1][first] = top


# Read input values from stdin
size = int(input().strip())

img = []
for _ in range(size):
    row = list(map(int, input().strip().split()))
    img.append(row)

# Call rotate_image and display the result
rotate_image(size, img)

# Print the rotated image without spaces after the last element
for row in img:
    print(" ".join(map(str, row)))

"""input:
3
8 2 3
2 9 1
9 0 6"""

""" output:
3 1 6
2 9 0
8 2 9"""

rotate_image(8, 2, 3)
