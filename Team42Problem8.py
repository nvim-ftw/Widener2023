user_in = input().split(" ")
start_word = user_in[0]
goal_word = user_in[1]

start_word = "".join([i for i in start_word if i in goal_word])

prev_done = []
for letter in goal_word:
    if letter in prev_done: continue
    prev_done.append(letter)
    how_many = start_word.count(letter)
    how_many_needed = goal_word.count(letter)
    if how_many < how_many_needed:
        print("NO")
        exit()
    if how_many == how_many_needed: continue
    for i in range(how_many - how_many_needed):
        f_index = start_word.find(letter)
        if f_index == 0:
            start_word = start_word[1:]
        else:
            start_word = start_word[0:f_index] + start_word[f_index + 1:]

if start_word == goal_word: print("YES")
else: print("NO")
