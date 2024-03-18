def find_runner_up_score(scores):
    unique_scores = set(scores)
    unique_scores.remove(max(unique_scores))
    return max(unique_scores)

# Prompt user to enter the number of participants
n = int(input("Enter the number of participants: "))

# Prompt user to enter the scores separated by spaces
scores = list(map(int, input("Enter the scores separated by spaces: ").split()))

if len(scores) != n:
    print("Number of scores entered does not match the number of participants.")
else:
    runner_up_score = find_runner_up_score(scores)
    print("The runner-up score is:", runner_up_score)