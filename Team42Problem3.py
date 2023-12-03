user_in = input()
vowels = ['A', 'E', 'I', 'O', 'U']

count = 0
for index, letter in enumerate(user_in):
    if index == len(user_in) - 1: break
    if letter.upper() in vowels and user_in[index + 1].upper() in vowels:
        count += 1

print(count)
