import random

# print(dir(random))
# 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'main', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'

# print(random.randbytes(2))
print(random.randint(1,3))

print(random.random())

print(random.randrange(1,10,2))

hello = ["h", "e", "l", "l", "o"]
random.shuffle(hello)
print(hello)

print(random.uniform(2.1, 2.3))

print(random.choice(hello))