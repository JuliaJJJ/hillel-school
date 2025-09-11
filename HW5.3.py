import string

text = input("Введіть текст: ")

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()
capitalized_words = [word.capitalize() for word in words]

hashtag = '#' + ''.join(capitalized_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print("Хештег:", hashtag)
