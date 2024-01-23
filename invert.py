from MatrixMonday import MatrixMonday

trixie = MatrixMonday(3, 3)
trixie.set_entry(0, 0, 1)
trixie.set_entry(0, 1, 2)
trixie.set_entry(0, 2, 3)
trixie.set_entry(1, 0, 0)
trixie.set_entry(1, 1, 1)
trixie.set_entry(1, 2, 4)
trixie.set_entry(2, 0, 5)
trixie.set_entry(2, 1, 6)
trixie.set_entry(2, 2, 0)


trixie.invert()
trixie.print()