# -*- coding: utf-8 -*-

from .context import enigma

import unittest


class EncryptionSuite(unittest.TestCase):
    """Encryption test cases."""


    def test_enc_ENIGMA(self):
        plugboard = None
        rotors = ['I','II','III']
        machine = enimga.Machine(
            plugboard=plugboard,
            rotors=rotors,
            reflector=reflector
            )

if __name__ == '__main__':
    unittest.main()