from MatrixMonday import MatrixMonday


trixe = MatrixMonday(2, 3)
trixe.set_entry(0, 0, 1)
trixe.set_entry(0, 1, 2)
trixe.set_entry(0, 2, 3)
trixe.set_entry(1, 0, 4)
trixe.set_entry(1, 1, 5)
trixe.set_entry(1, 2, 6)

alice = MatrixMonday(2, 3)
alice.set_entry(0, 0, 7)
alice.set_entry(0, 1, 8)
alice.set_entry(0, 2, 9)
alice.set_entry(1, 0, 10)
alice.set_entry(1, 1, 11)
alice.set_entry(1, 2, 12)

trixe.plus(alice)
trixe.print()
