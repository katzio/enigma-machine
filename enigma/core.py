# -*- coding: utf-8 -*-
import array
import enigma.helper as helper
import enigma.rotors as erotors
import enigma.reflectors as reflectors

class Machine:
    def __init__(
            self,
            plugboard=[],
            rotors=[erotors.M3_III, erotors.M3_II,erotors.M3_I],  # Default Rotos, order is left to right
            offsets=['A','A','A'],
            settings=['A','A','A'],
            reflector=reflectors._ReflectorBase # Default Reflector, returns input
            ):

        """Initialize a new Enigma Machine."""
        self._plugboard = None
        self._rotors = []

        # Output buffer        
        self._buffer = bytearray()
        self._initPlugboard(plugboard)
        self._initRotors(rotors, offsets, settings)
        self._reflector = reflector()

        # Link all of the rotors and reflectors together
        self._link()

    def _initRotors(self,rotors, offsets, settings):
        helper.log("Initing rotors")
        for i, rotor in enumerate(rotors):
            helper.log("Initing rotor[{}] - {} - with setting={} offset={}".format(i, rotor, settings[i],offsets[i]))
            self._rotors.append(rotor(setting=settings[i], offset=offsets[i]))

    def _initPlugboard(self, plugboard):
        '''Initialize the plugboard'''
        helper.log("Initing plugboard")
        self._plugboard = array.array('b', [i for i in range(26)])

        # swap characters
        for pair in plugboard:
            x = pair[0]
            y = pair[1]
            x = erotors.ALPHABET.index(x.upper())
            y = erotors.ALPHABET.index(y.upper())
            self._plugboard[x] = y
            self._plugboard[y] = x

        helper.log("Plugboard: {}".format(self._plugboard))

    def _link(self):
        """Link the rotors and reflectors"""
        # Link the rotors forward
        for i in range(len(self._rotors))[:-1]: # loop all except the last
            self._rotors[i].next = self._rotors[i + 1]

        # Link the rotors backwards
        for i in range(len(self._rotors))[1:]: # loop all except the first
            self._rotors[i].previous = self._rotors[i - 1]

        self._rotors[-1].next = self._reflector # link last rotor to reflector
        self._reflector.previous = self._rotors[-1] # link reflector to last rotor

    def encrypt(self, str_in):
        """ Encrypt a string"""

        # Text modes
        for char in bytes(str_in, 'utf-8'):

            if char == 32: # space
                self._buffer.append(32)
                continue

            # Convert the char to a int
            char_in = char - 65

            # Run it through the machine
            char_out = self._translate_char(char_in)
            helper.log("\n\n#### TRANSALTED:\t{} -> {}\n\n".format(erotors.ALPHABET[char_in],erotors.ALPHABET[char_out]))

            # Convert it back into a char
            char_out += 65

            # Append it to the array
            self._buffer.append(char_out)

    def _translate_char(self, char):
        """
        Translate a singular char (as an integer) through the plugboard,
        rotors, reflector, and back again.
        """

        rotor = self._rotors[0]
        # Step the rotors
        rotor.step()


        helper.log('Plugboard forword: {} -> {} ({})'.format(char, erotors.ALPHABET[self._plugboard[char]], self._plugboard[char]))
        char = self._plugboard[char]
        char = rotor.transalte(char)

        helper.log('Plugboard backwords: {} -> {} ({})'.format(char, erotors.ALPHABET[self._plugboard[char]], self._plugboard[char]))
        char = self._plugboard[char]

        return char