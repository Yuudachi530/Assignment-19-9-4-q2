TextFile = open("hamlet.txt", "r")
TextFile = TextFile.read()

for i in "!'#$%&()*+,-./:;<=>?@[\\]^_‘{|}~" :
    TextFile = TextFile.replace(i, ' ')

TextFile = TextFile.replace('"', ' ')
    
TextFile = TextFile.lower()
words = TextFile.split()

for word in words:
    if word == 's' or word == 't':
        words.remove(word)

WordsCounter = {}

for word in words:
    WordsCounter[word] = WordsCounter.get(word, 0) + 1

WordList = list(WordsCounter.items())
WordList.sort(key = lambda x:x[1], reverse = True)

OutFile = open("OutputFile.txt", 'w')

for i in range(len(WordList)):
    word, value = WordList[i]
    line = '{0:<10}{1:>5}'.format(word, value)
    print(line)
    print()
    OutFile.write(line + '\n')

OutFile.close()

    

    
    

    
    
