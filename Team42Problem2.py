number = int(input())

square = str(number * number)

number = str(number)

user_in_len = len(number)
sqr_len = len(square)

if square[-user_in_len::] == number:
    print("automorphic")
else:
    print("not automorphic")
