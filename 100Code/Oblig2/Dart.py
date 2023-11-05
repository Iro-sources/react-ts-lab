import random

players = int(input("How many players?\n"))
rounds = int(input("How many throws?\n"))
dars = int(input("How many pillars?\n"))

total_score = []

for i in range(players):
    player_score = []
    sum = 0

    for j in range(rounds):
        round_sum = 0
        for dart in range(dars):
            score = random.randrange(0, 60)
            player_score.append(score)
            round_sum += int(score.split()[-2])
        player_score.append(f"Round {i+1}got total of: {round_sum}")
        sum += round_sum

    player_score.append(f"Total: {sum}")
    total_score.append(player_score)

for x in total_score:
    print(*x)

#print(f"{i+1} got {sum} total of points and won the game")



