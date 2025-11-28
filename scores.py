import sys
if len(sys.argv) > 1:
    scores = list(map(float, sys.argv[1:]))
    print("User provided scores:")
else:
    # Default values
    scores = [12, 24, 36, 42, 60]
    print("No input given - using default scores:")

script_name = sys.argv[0]

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Script Name:", script_name)
print("Scores:", scores)
print("Sum of Scores:", total)
print("Average Score:", average)
print("Maximum Score:", maximum)
print("Minimum Score:", minimum)
