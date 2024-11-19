#solution by chat gpt, with some corrections

def floodFill(image, sr, sc, newColor, oldColor):
    m, n = len(image), len(image[0])
    if sr < 0 or sr >= m or sc < 0 or sc >= n:
        return image

    # base case: return if the starting pixel is already the new color or if it is out of bounds
    if image[sr][sc] == newColor or image[sr][sc] != oldColor:
        return image

    # change the color of the starting pixel
    image[sr][sc] = newColor

    # recursively call floodFill on the surrounding pixels
    floodFill(image, sr+1, sc, newColor, oldColor)
    floodFill(image, sr-1, sc, newColor, oldColor)
    floodFill(image, sr, sc+1, newColor, oldColor)
    floodFill(image, sr, sc-1, newColor, oldColor)

    return image


image = [[1,1,1], [1,1,0], [1,0,1]]

sr = 1
sc = 1
clr = 2
oldColor = image[sr][sc]

img = floodFill(image, sr, sc, clr, oldColor)
print (img)