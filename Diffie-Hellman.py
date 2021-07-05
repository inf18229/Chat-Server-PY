import random
MAX_PRIME = 10000
MAX_BASE = 1000
class DiffieHellman:
    def __init__(self):
       print("New Deffie Hellman class")
       self.sharedPrime = self.createRandomPrime()
       self.sharedBase = random.randint(0,MAX_BASE)
       self.secret = 0
       print("Shared Prime: ",self.sharedPrime)
       print("Shared Base: ",self.sharedBase)
    def isPrime(self,num)->bool:
        if num > 1:
            # check for factors
            for i in range(2,num):
                if (num % i) == 0:
                    return False
                else:
                    return True 
        else:
            return False
    def createRandomPrime(self)->int:
        primes = [i for i in range(0,MAX_PRIME) if self.isPrime(i)]
        return random.choice(primes)
    def setSecret(self):
        self.secret = random.randint(0,MAX_BASE)
    def sendValue(self)->int:
        return (self.sharedBase ** self.secret) % self.sharedPrime
    def sharedSecret(self,recievedValue)->int:
        return (recievedValue ** self.secret) % self.sharedPrime

Test1 = DiffieHellman()
Test2 = Test1
Test1.setSecret()
print(Test1.secret)

Test2.setSecret()
print(Test2.secret)
print("Es wird ",Test1.sendValue()," von Test 1 gesendet")
print("Es wird ",Test2.sendValue()," von Test 2 gesendet")
print("Public Secret von Test 1: ",Test1.sharedSecret(Test2.sendValue()))
print("Public Secret von Test 2: ",Test2.sharedSecret(Test1.sendValue()))