import enigma.core as core
import enigma.rotors as erotors
import enigma.reflectors as reflectors  
import random, string
from random import randint
import cProfile

rotors = [erotors.M3_I,erotors.M3_II,erotors.M3_III,erotors.M3_IV,erotors.M3_V]

def random_pair():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

def random_char():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(1))

def performance_test():
    for i in range(1000):
        e1 = core.Machine(plugboard=[random_pair(), random_pair(), random_pair(), random_pair(), random_pair(), random_pair(), random_pair(), random_pair(), random_pair(), random_pair()], settings=[random_char(),random_char(),random_char()],rotors=[rotors[randint(0, 4)],rotors[randint(0, 4)],rotors[randint(0, 4)]], offsets=[random_char(),random_char(),random_char()], reflector=reflectors.B)

        e1.encrypt(''.join(random.choice(string.ascii_uppercase) for _ in range(25)))
        
pr = cProfile.Profile()
pr.enable()

performance_test()

pr.disable()
 
pr.print_stats(sort='time')