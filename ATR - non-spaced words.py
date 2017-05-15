import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)

img = cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)
text = np.array([[0,0,0]])
words = np.array([[[0,0],[0,0]]])




isPrevPart = False  # is previous column connected part of a word

#img[columns, width]
# searching pixels
# 1 . upside down   >>    range(148)
# 2 . right to left     >>      range(281 - 1, -1, -1)

for x in range(281 - 1, -1, -1):
    isColumnEmpty = True    # assume every column is empty
    for y in range(148):

        # check if it is is character (recognize non whited spaces)
        if img[y, x] != 255:

            # store characters
            text = np.append(text, [[y,x,img[y, x]]], axis=0)

            # non-spaced word start
            if isPrevPart == False:

                # store where the word start
                words = np.append(words, [[[y,x],[0,0]]], axis=0) # [0,0] later will be modified to store the where the word ends

                # is previous column connected part of a word : yes now it does
                isPrevPart = True


            words[-1][-1] = [y, x]
            isColumnEmpty = False

    if (isColumnEmpty == True):
        isPrevPart = False


text = np.delete(text, 0, 0)
words = np.delete(words, 0, 0)


print(words)
#print(text)
#print(text.size)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()