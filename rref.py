from MatrixMonday import MatrixMonday


trixie_custom = MatrixMonday(3,4)
trixie_custom.set_entry(0, 0, 11)
trixie_custom.set_entry(0, 1, 41)
trixie_custom.set_entry(0, 2, 2)
trixie_custom.set_entry(0, 3, 12)
trixie_custom.set_entry(1, 0, 9)
trixie_custom.set_entry(1, 1, 25)
trixie_custom.set_entry(1, 2, 34)
trixie_custom.set_entry(1, 3, 23)
trixie_custom.set_entry(2, 0, 42)
trixie_custom.set_entry(2, 1, 53)
trixie_custom.set_entry(2, 2, 18)
trixie_custom.set_entry(2, 3, 17)

trixie_custom.rref()
trixie_custom.print()