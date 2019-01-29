words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#modify sequence
for w in words[:]:
    if len(w) > 5:
        words.insert(0, w)
print(words)

