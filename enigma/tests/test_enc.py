# -*- coding: utf-8 -*-
import unittest
import enigma.core as core
import enigma.rotors as erotors
import enigma.reflectors as reflectors  

class EncryptionSuite(unittest.TestCase):
    """Encryption test cases."""

    def test_enc_ENIGMA_QGELID(self):
        # test machine
        e1 = core.Machine(rotors=[erotors.M3_III, erotors.M3_II, erotors.M3_I], offsets=['V', 'D', 'F'], reflector=reflectors.B)

        # set state
        e1.encrypt('ENIGMA')
        
        # assert encryption output
        self.assertEqual(e1._buffer.decode(), 'QGELID')


    def test_enc_KAXMNF_ENIGMA(self):
        # test machine
        e1 = core.Machine(rotors=[erotors.M3_III, erotors.M3_II, erotors.M3_I], offsets=['V', 'E', 'Q'], reflector=reflectors.B)

        # set state
        e1.encrypt('KAXMNF')
        
        # assert encryption output
        self.assertEqual(e1._buffer.decode(), 'ENIGMA')

    
    def test_enc_TURING_ACELKT(self):
        # test machine
        e1 = core.Machine(rotors=[erotors.M3_III, erotors.M3_II, erotors.M3_I], offsets=['Y', 'E', 'X'], reflector=reflectors.B)

        # set state
        e1.encrypt('TURING')
        
        # assert encryption output
        self.assertEqual(e1._buffer.decode(), 'ACELKT')


    def test_enc_AAAAA_EWTYX(self):
        # test machine
        e1 = core.Machine(settings=['B','B','B'],rotors=[erotors.M3_III,erotors.M3_II, erotors.M3_I], offsets=['A','A','A'], reflector=reflectors.B)

        # set state
        e1.encrypt('AAAAA')
        
        # assert encryption output
        self.assertEqual(e1._buffer.decode(), 'EWTYX')


    def test_enc_PEACE_IRJZU(self):
        # test machine
        e1 = core.Machine(plugboard=['AT', 'CE', 'RL'], settings=['F','H','C'],rotors=[erotors.M3_IV,erotors.M3_II, erotors.M3_I], offsets=['I','D','S'], reflector=reflectors.B)

        # set state
        e1.encrypt('PEACE')
        
        # assert encryption output
        self.assertEqual(e1._buffer.decode(), 'IRJZU')


    def test_enc_PEACE_IRJZU(self):
        # test machine
        e1 = core.Machine(plugboard=['ZU', 'HL', 'CQ', 'WM', 'OA', 'PY', 'EB', 'TR', 'DN', 'VI'], settings=['X','I','S'],rotors=[erotors.M3_IV,erotors.M3_V, erotors.M3_II], offsets=['N','O','C'], reflector=reflectors.B)

        # set state
        e1.encrypt('DOR')
        
        # assert encryption output
        self.assertEqual(e1._buffer.decode(), 'MLD')


    def test_enc_PEACE_IRJZU(self):
        # test machine
        e1 = core.Machine(plugboard=['ZU', 'HL', 'CQ', 'WM', 'OA', 'PY', 'EB', 'TR', 'DN', 'VI'], settings=['X','I','S'],rotors=[erotors.M3_IV,erotors.M3_V, erotors.M3_II], offsets=['N','O','C'], reflector=reflectors.B)

        # set state
        e1.encrypt('MLD')
        
        # assert encryption output
        self.assertEqual(e1._buffer.decode(), 'DOR')



    def test_enc_FOR_MOTHER_RUSSIA(self):
        """
        decipher 

        RNYHP UMDPQ CUAQN LVVSP IARKC TTRJQ KCFPT OKRGO ZXALD RLPUH AUZSO SZFSU GWFNF DZCUG VEXUU LQYXO TCYRP SYGGZ HQMAG PZDKC KGOJM MYYDD H
        """
        # test machine
        e1 = core.Machine(plugboard=['ZU', 'HL', 'CQ', 'WM', 'OA', 'PY', 'EB', 'TR', 'DN', 'VI'], settings=['X','I','S'],rotors=[erotors.M3_IV,erotors.M3_V, erotors.M3_II], offsets=['N','O','C'], reflector=reflectors.B)

        # set state
        e1.encrypt('MLD')
        
        # assert encryption output
        self.assertEqual(e1._buffer.decode(), 'DOR')


        e1 = core.Machine(plugboard=['ZU', 'HL', 'CQ', 'WM', 'OA', 'PY', 'EB', 'TR', 'DN', 'VI'], settings=['X','I','S'],rotors=[erotors.M3_IV,erotors.M3_V, erotors.M3_II], offsets=['R','O','D'], reflector=reflectors.B)


        # set state
        e1.encrypt('UMDPQ CUAQN LVVSP IARKC TTRJQ KCFPT OKRGO ZXALD RLPUH AUZSO SZFSU GWFNF DZCUG VEXUU LQYXO TCYRP SYGGZ HQMAG PZDKC KGOJM MYYDD H')

        print(e1._buffer.decode())

        self.assertEqual(e1._buffer.decode(), "GROUP SOUTH COMMA NDFRO MGENP AULUS XSIXT HARMY ISENC IRCLE DXOPE RATIO NBLAU FAILE DXCOM MENCE RELIE FOPER ATION IMMED IATEL Y")

if __name__ == '__main__':
    unittest.main()