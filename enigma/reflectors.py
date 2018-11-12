from .rotors import _RotorBase

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class _ReflectorBase(_RotorBase):
    '''Simple adapter to the Rotor base class for defining reflectors'''

    _wiring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def invalid(self):
        """Used to nerf invalid methods"""
        pass

    step = invalid
    translateReverse = invalid

class B(_ReflectorBase):
    _wiring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'