from random_word import RandomWords
import string as str
import random
from graphics import *



coords1 = []

ltrs = list(str.ascii_lowercase)
for i in range(1, 5):
    word = ""
    for i in range(0, random.randint(1, 10)):
        word = word + ltrs[random.randint(0, len(ltrs)-1)]
    coords1.append(len(word))

    print(word)

window1 = GraphWin(width = 500, height = 1000)
window1.setCoords(0, 0, 10, 10)
wordSquare1 = Rectangle(Point(coords1[0], coords1[1]), Point(coords1[2], coords1[3]))
wordSquare1.draw(window1)
window1.getMouse()




coords2 = []

r = RandomWords()
for i in range(1, 5):
    try:
        word = r.get_random_word()
    except Exception:
        word = "FAILURE"
        print(failure)
        continue
    print(word)
    coords2.append(len(word))

if len(coords2) < 4:
    failedWord = [10, 20, 30 ,40]
    coords2 = failedWord

window2 = GraphWin(width = 1000, height = 500)
window2.setCoords(0, 0, 10, 10)
wordSquare2 = Rectangle(Point(coords2[0], coords2[1]), Point(coords2[2], coords2[3]))
wordSquare2.draw(window2)
window2.getMouse()
