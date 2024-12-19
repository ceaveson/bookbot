with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def word_count(file):
    lines = []
    words = []
    for line in file.split("\n"):
        lines.append(line)
    for line in lines:
        for word in line.split(" "):
            if word != "":
                words.append(word)
    return len(words)

def num_of_chars(file):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v" ,"w", "x", "y", "z"]
    chars = []
    chars_dict = {}
    for i in file:
        if i.lower() in alphabet:
            chars.append(i.lower())
    for char in set(chars):
        chars_dict[char] = 0
    for char in chars:
        chars_dict[char] += 1
    return chars_dict



print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count(file_contents)} words found in the document")
for k,v in num_of_chars(file_contents).items():
    print(f"The '{k}' character was found {v} times")