candidates = input().split(" ")

votes = []

while True:
    user_in = input()
    if user_in[0] == ".":
        break
    votes.append(user_in)

c_winner = "0"

for candidate in candidates:
    good = True

    for opp in candidates:
        if opp == candidate: continue
        score = 0

        for vote in votes:
            cand_rank = vote.find(candidate)
            opp_rank = vote.find(opp)

            if cand_rank == -1 and opp_rank == -1:
                continue
            if cand_rank == -1:
                score -= 1
                continue
            if opp_rank == -1:
                score += 1
                continue

            if cand_rank < opp_rank: score += 1
            else: score -= 1

        if not score > 0: good = False
    if good: c_winner = candidate


print(c_winner)
