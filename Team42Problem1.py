# p1

user_in = input("").split(" ")
user_in = [int(i) for i in user_in]

affordable = int(user_in[0] / user_in[1])
change = user_in[0] - (affordable * user_in[1])
cups = (user_in[2] * affordable) / 8

print(f"{affordable} {change} {cups}")
