from MatrixMonday import MatrixMonday

trixe = MatrixMonday(2, 3)
trixe.set_entry(0, 0, 1)
trixe.set_entry(0, 1, 2)
trixe.set_entry(0, 2, 3)
trixe.set_entry(1, 0, 4)
trixe.set_entry(1, 1, 5)
trixe.set_entry(1, 2, 6)

trixe.linearCombRows(2, 1, 2)
trixe.print()