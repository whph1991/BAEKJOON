#1963

def is_prime_number(x):
  """
  2부터 (x-1)까지의 모든 수를 확인하며 x가 해당 수로 나누어 떨어지면 소수가 아님

  :param x: 정수
  :return: True x가 소수인 경우, False 그 외

  Example Input:
    x = 3
  Output:
    True
  """
    
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

prime_number = []

for i in range(1033, 8179):
  if is_prime_number(i):
    prime_number.append(i)

print(prime_number)