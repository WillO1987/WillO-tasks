
def calculate_score(rolls):
    total = 0
    go = 1
    roll_index = 0

    while go <= 10:
        if rolls[roll_index] == 10:  # Strike meaning first go == 10 
            total += 10 + rolls[roll_index + 1] + rolls[roll_index + 2] # adds the total of the next 2 turns
            roll_index += 1
        elif rolls[roll_index] + rolls[roll_index + 1] == 10:  # Spare
            total += 10 + rolls[roll_index + 2] # adds the total of the next turn
            roll_index += 2
        else:
            total += rolls[roll_index] + rolls[roll_index + 1]
            roll_index += 2
        go += 1
    return total

def play_bowling():
    rolls = []
    go = 1

    while go <= 10:
        print("Turn: {go}")
        roll1 = int(input("Enter the score on the first go: "))

        if roll1 == 10:  # Strike
            rolls.append(roll1)
            go += 1
            continue

        roll2 = int(input("Enter the score on the second go: "))

        if roll1 + roll2 > 10:
            print("Invalid input")
            continue

        rolls.append(roll1)
        rolls.append(roll2)
        go += 1

    total = calculate_score(rolls)
    print("\nYour final score is: {total}")


play_bowling()
