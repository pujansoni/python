from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.split()
    for word in line_words:
        story_words.append(word)

print(story_words)
print('------------------')
# Generally the http returns the encoded byte array so we need to decode it in order to get the string data
story1 = urlopen('http://sixty-north.com/c/t.txt')
story_words1 = []
for line in story1:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words1.append(word)

print(story_words1)