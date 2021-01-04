import random, string
from pathlib import Path
length = int(input('Enter the length of the password '))
letters = string.ascii_letters
nums = string.digits
chars = letters + nums + '!@:%#)('
rnd = random.SystemRandom()
print(''.join(rnd.choice(chars)
                    for i in range(length)))


