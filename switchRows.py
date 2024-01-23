from  MatrixMonday import MatrixMonday

alice = MatrixMonday(2, 3)
alice.set_entry(0, 0, 1)
alice.set_entry(0, 1, 2)
alice.set_entry(0, 2, 3)
alice.set_entry(1, 0, 4)
alice.set_entry(1, 1, 5)
alice.set_entry(1, 2, 6)
alice.switchRows(1, 2)
alice.print()