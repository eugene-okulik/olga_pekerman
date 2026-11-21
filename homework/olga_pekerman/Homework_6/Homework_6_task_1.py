text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

words = text.split()
words_ing = []

for word in words:
    if ',' in word:
        word = word.strip(',') + 'ing,'
    elif '.' in word:
        word = word.strip('.') + 'ing.'
    else:
        word = word + 'ing'

    words_ing.append(word)

print(' '.join(words_ing))
