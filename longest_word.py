def longest_word(word):
    word=max(word,key=len)
    print("longest word:",word)
    print("its length is:",len(word))
a=["book","pen","pencil","bag","calculator"]
longest_word(a)

output:
longest word: calculator
its length is: 10
