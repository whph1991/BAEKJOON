#2920
ascending = 0
descending = 0

N = list(map(int, input().split()))

for i in range(len(N)):
  if N[i] == (i+1):
    ascending = ascending + 1
  elif N[i] == (8-i):
    descending = descending + 1

if ascending == 8:
  print("ascending")
elif descending == 8:
  print("descending")
else:
  print("mixed")