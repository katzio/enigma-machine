Enigma Machine Simulator
========================

Software Security 2018 - A - Assignment 


# Example

```
# test machine
e1 = core.Machine(rotors=[erotors.M3_III, erotors.M3_II, erotors.M3_I], offsets=['V', 'D', 'F'], reflector=reflectors.B)

# set state
e1.encrypt('ENIGMA')

# assert encryption output
self.assertEqual(e1._buffer.decode(), 'QGELID')
```
