# Task 6: Count occurrences of a word in a file.

def numOcc(path, word):
    file = open(path, 'r')
    text = file.read()
    list_words = text.split(" ")
    oc_word = 0
    for elt in list_words:
        if elt == word:
            oc_word += 1
    return oc_word

print(numOcc("text.txt", "Nobel")) 