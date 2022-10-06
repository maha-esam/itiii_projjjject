text = "are u a fool guy"
word = "fool"
string_words_list = text.split()
result =''
stars = "*" * len(word)
count = 0
index = 0
for i in string_words_list:
    if i == word:
        string_words_list[index] = stars
    index += 1
result = ' '.join(string_words_list)
print(result)