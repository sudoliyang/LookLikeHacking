import random
def randomascii():
  return random.randint(32,127)
while 1:
  for x in range(1,randomascii()):
    print(chr(randomascii())),
  print()