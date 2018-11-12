# Aryeh Katz

import array
import enigma.helper as helper
from collections import deque

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CHARS_SET_LEN = len(ALPHABET)

class _RotorBase:
    '''Base rotor class. Inherited by all rotors'''

    _wiring = ALPHABET # Base wiring is 1:1
    _notches = 'A' # self.notches = [1,0,0,0,...,0]
    _offset = 'A' # self.offset = 0
    _setting = 'A' # self.setting = 0

    def __init__(self, offset='A', setting='A'):
        '''Instantiate a new {} with custom or default settings'''
        
        helper.log('Creating new {}: {}\nOffset: {}\nSetting: {}\nNotches: {}'.format(self.__class__,self.__class__.__name__, offset, setting, self._notches))
        # Relative node references
        self.next = None
        self.previous = None

        # Initial rotor offset, setting and notches
        self.setting = ALPHABET.index(setting)
        self._setting = self.setting
        self.offset = ALPHABET.index(offset)
        self._offset = self.offset

        helper.log('self.offset: ' + str(self.offset))
        
        # Initialize wiring tables
        self.wiring_forward = array.array('b', [0 for i in range(CHARS_SET_LEN)])
        self.wiring_reverse = array.array('b', [0 for i in range(CHARS_SET_LEN)])

        # program wiring tables
        for x in range(CHARS_SET_LEN):
            # map chars to wiring
            y = ALPHABET.index(self._wiring[x])
            self.wiring_forward[x] = y - x
            self.wiring_reverse[y] = x - y

        # Initial rotor setting, shift wiring
        helper.log('self._wiring shifting: ' + str(self.setting))
        helper.log('self.wiring_forward (before settings shift):\t' + str(self.wiring_forward))
        helper.log('self.wiring_reverse (before settings shift):\t' + str(self.wiring_reverse))

        self.wiring_forward = deque(self.wiring_forward)
        self.wiring_reverse = deque(self.wiring_reverse)

        self.wiring_forward.rotate(self.setting)
        self.wiring_reverse.rotate(self.setting)

        self.wiring_forward = array.array('b', list(self.wiring_forward))
        self.wiring_reverse = array.array('b', list(self.wiring_reverse))

        helper.log('self.wiring_forward (after settings shift):\t' + str(self.wiring_forward))
        helper.log('self.wiring_reverse (after settings shift):\t' + str(self.wiring_reverse))

        


        # Initialize the notch table
        self.notches = array.array('b', [0 for i in range(CHARS_SET_LEN)])
        for notch in self._notches:
            self.notches[ALPHABET.index(notch)] = 1

    def _modulo(self, n):
        return n % (CHARS_SET_LEN) # 0 to CHARS_SET_LEN

    def step(self):
        '''
        Step the rotor by one letter.
        Returns True if the rotor hit its notch
        '''

        # If a notch is hit, increment the next in the series
        if self.notches[self.offset] and self.next:        
            helper.log('{} notch riched'.format(self.__class__.__name__))
            self.next.step()

        elif self.next and self.next.notches[self.next.offset]:
            self.next.step()

        # step this rotor
        self.offset = self._modulo(self.offset + 1)
        self._offset = ALPHABET[(self.offset)]

        helper.log('STEPPING  {}!\n{} step to {}'.format(self.__class__.__name__, ALPHABET[(self.offset-1)], self._offset))


    def transalte(self, char_in):
        """ naming helper """
        return self.translateForward(char_in)

    def translateForward(self, char_in):
        '''Translate one char through the rotor in forword pass'''
        modifier = self.wiring_forward[self._modulo(char_in + self.offset)]
        char_out = self._modulo(char_in + modifier)

        helper.log('{} translating forword: {} ({}) -> {} ({})'.format(self.__class__.__name__, char_in, ALPHABET[self._modulo(char_in + self.offset)], ALPHABET[self._modulo(char_out + self.offset)], char_out))

        if self.next:
            helper.log('{} to next rotor forword: {}'.format(self.__class__.__name__, self.next.__class__.__name__))
            return self.next.translateForward(char_out)
        
        helper.log('{} returns to rotor revers: {}'.format(self.__class__.__name__, self.previous.__class__.__name__))
        return self.previous.translateReverse(char_out)

    def translateReverse(self, char_in):
        '''Translate one char through this rotor in reverse pass'''
        modifier = self.wiring_reverse[self._modulo(char_in + self.offset)]
        char_out = self._modulo(char_in + modifier)
    

        helper.log('{} translating revers: {} ({})-> {} ({})'.format(self.__class__.__name__, char_in, ALPHABET[self._modulo(char_in + self.offset)], ALPHABET[self._modulo(char_out + self.offset)] ,char_out))

        if self.previous:
            helper.log('{} returns to rotor revers: {}'.format(self.__class__.__name__, self.previous.__class__.__name__))
            return self.previous.translateReverse(char_out)
    
        helper.log('Last translation')
        return char_out


class M3_I(_RotorBase):
    _wiring = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    _notches = 'Q'

class M3_II(_RotorBase):
    _wiring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _wiring = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    _notches = 'E'

class M3_III(_RotorBase):
    _wiring = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    _notches = 'V'

class M3_IV(_RotorBase):
    _wiring = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
    _notches = 'J'

class M3_V(_RotorBase):
    _wiring = 'VZBRGITYUPSDNHLXAWMJQOFECK'
    _notches = 'Z'