from collections import Counter

counter = Counter(["red", "red", "blue", "red", "blue", "green"])

print(counter["red"], counter["blue"], counter["green"])
print(dict(counter))
