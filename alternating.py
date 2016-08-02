import os
import re

def AlternatingWords(wordPath):
    leftHanded = "[qwertasdfgzxcvb]"
    rightHanded = "[^qwertasdfgzxcvb]"
    alt = re.compile("^((({left}{right})+{left}?)|(({right}{left})+{right}?))$".format(left = leftHanded, right = rightHanded))
    with open(wordPath, 'r') as wordFile:
        for word in wordFile:
            match = alt.match(word)
            if match:
                yield word.strip()

if __name__ == "__main__":
    for word in AlternatingWords(os.path.expanduser(r'~/Dropbox/bin/words/english/words.txt')): print word
