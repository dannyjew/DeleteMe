word = "youu"
word_is_iso = True

# for letter in word.replace(" ", "").replace("-", ""):
#     if word.count(letter) > 1:
#         word_is_iso = False
#         break
#
# if word_is_iso:
#     print("Word is an isogram")
# else:
#     print("Word is not an isogram")

set_word = set(word.replace(" ", "").replace("-", ""))
print(set_word)
print(list(word.replace(" ", "").replace("-", "")))
if len(set_word) == len(word.replace(" ", "").replace("-", "")):
    print("Word is isogram")
else:
    print("word is not an isogram")

