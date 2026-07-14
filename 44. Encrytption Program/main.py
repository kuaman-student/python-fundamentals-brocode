import string
import random
non_hashed = list(string.punctuation + string.digits + string.ascii_letters + " ")
hashed = non_hashed.copy()
random.shuffle(hashed)


print(hashed)
print(non_hashed)
def crack(sentence, tohash):
    newword =""
    if tohash:
        for word in sentence:
            newword = newword + hashed[non_hashed.index(word)]
        return newword
    else:
        for word in sentence:
            newword = newword + non_hashed[hashed.index(word)]
        return newword


print(crack(crack("ABCD", True), False))