import re

maxPercent = -1
maxWord = ""
full = []

file = open("words.txt", "r")
for word in file:
    percent = 0
    word = re.sub('[^0-9a-zA-Z]+', '', word)
    for letter in word:
        percent += ord(letter.lower()) - 96
    if percent > maxPercent:
        maxPercent = percent
        maxWord = word
    if percent == 100:
        full.append(word)

print(f"The word with the highest percentage of letters is {maxWord} with a percentage of {maxPercent}")

f = open('f1.txt','w')
for ele in full:
    f.write(ele+'\n')