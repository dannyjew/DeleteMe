# single_quotes = 'Hello'
#
# double_quotes = "Hello"
#
# print(double_quotes)
# print(single_quotes)
#
# # string_failure = 'I said 'WOW''
# # print(string_failure)
#
# escape_example = 'I said \'WOW\''
# print(escape_example)
#
# quote_in_quote = 'I said "WOW"'
# print(quote_in_quote)
#
# hw = "Hello! World"
# print(hw[0:5])
# print(hw[3:4])
# print(hw[3:])
# print(len(hw[:7]))
# print(hw[1:3])
# print(len(hw))
#
# white_space = "hello          "
# print(len(white_space))
# print(len(white_space.strip()))

Example_Text = "here's some text with lot's of text"

print(Example_Text.count("e"))
print(Example_Text.lower())
print(Example_Text.upper())
print(Example_Text.capitalize())
print(Example_Text.replace(" ", ""))

x = 5
y = 2
print(str(x)+str(y))

int_string = "6"
print(type(int(int_string)))
print(float(int_string))

# F-Strings
name = "Lassie"
years = 7
height_cm = 60.2
print(f"{name} is {years} years old and {height_cm}cm tall")
print(f"{name.upper()} is {years*7} years old in dog years and {height_cm}cm tall")
