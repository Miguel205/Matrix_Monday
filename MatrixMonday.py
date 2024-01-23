class MatrixMonday:
    def __init__(self, rows, columns):
        self.m1 = [[0 for j in range(columns)] for i in range(rows)]
        self.columns = columns
        self.rows = rows
    def print(self):
        if isinstance(self.m1, str):
            print(self.m1)
            return ()
            print("The object is a string.")
        for i in range(self.rows):
            for j in range(self.columns):
                if self.m1[i][j] == -0:
                    self.m1[i][j] = 0
                print(self.m1[i][j], end="\t")
            print()
    def set_entry(self, row, column, value):
        self.m1[row][column] = value
    def get_entry(self, row, column):
        return self.m1[row][column]
    def plus(self, alice):
        trixie_rows, trixie_columns = self.rows, self.columns
        alice_rows, alice_columns = alice.rows, alice.columns

        trixie = self.m1
        sunny = []  # holds the output

        if trixie_rows != alice_rows or trixie_columns != alice_columns:
            self.m1 = ("Matrices cannot be added. Dimensions are different.")
            return ("Matrices cannot be added. Dimensions are different.")

        # uses nested for loops to add each value
        for (trix, al) in zip(trixie, alice.m1):
            filler = []  # holds the rows before adding them to the 2d array
            for (a, b) in zip(trix, al):  # for each number in x row of trixie and alice
                filler.append(a + b)  # add the sum to filler list
            sunny.append(filler)  # add filler to sunny

        self.m1 = sunny
        return sunny
    def times(self,alice):
        '''
        :param alice: other matrices
        :return: function takes two matrices and returns the product
        '''
        trixie = self.m1
        alice= alice.m1
        cloudy = []                     # alice converted into columns
        sunny = []                      # final return value
        'checks if matrices can be multiplied '
        if len(trixie[0]) != len(alice):
            self.m1=("Matrices cannot be multiplied. Inner dimensions are different.")
            return ("Matrices cannot be multiplied. Inner dimensions are different.")
        "converts alice's rows to columns and columns to rows so they can be multiplied with trixie"
        for i in range(len(alice[0])):  # for item in the row of alice
            rainy = []                  # holder for columns/ truncates rainy
            for row in alice:
                rainy.append(row[i])    # append the number to rainy
            cloudy.append(rainy)        # append list of numbers(column) to cloudy
        "then uses nested for loops to multiply the numbers"
        for collum in trixie:
            pos = 0
            hail = []
            for row in cloudy:
                pointer = 0
                holder = []                                        # holds the numbers that have to be added
                for item in range(len(alice)):                     # run the loop for as many columns are in alice
                    holder.append(collum[pointer] * row[pointer])  # append the multiplied numbers to holder
                    pointer += 1                                   # changes position of the numbers
                hail.append(sum(holder))
            pos += 1
            sunny.append(hail)
            self.m1=sunny
        return sunny
    def scalarTimesRow(self, scalar, row):
        '''
        :param scalar: number that row will be multiplied
        :param row: row that will be multiplied
        :return: matrix with new row
        '''
        trixie = self.m1
        row -= 1                #subtract one to avoid out of range list index
        'multiples each item in a row by a number'
        for column in range(len(trixie[row])):
            trixie[row][column] = (trixie[row][column] * scalar)    #multiples each item in row by scalar
        self.m1=trixie
        return trixie
    def switchRows(self,row1, row2):
        '''
        :param row1: row to by switched
        :param row2: row to by switched
        :return:matrix with switch rows
        '''
        row1-=1                                                 #subtract one to avoid out of range list index
        row2-=1
        trixie = self.m1
        trixie[row1],trixie[row2]=trixie[row2],trixie[row1]     #make row 1 equal to row2 and row2 equal to row1
        self.m1=trixie
        return trixie
    def linearCombRows(self,scalar,firstrow,secondrow):
        '''
        :param scalar: number first row will be multiplied by
        :param firstrow: row scalar will multiply
        :param secondrow:row the product of first row and scalar will be added to
        :return:
        '''
        firstrow-=1
        secondrow-=1
        trixie=self.m1
        multiplier=[]
        for number in range(len(trixie[firstrow])-1):
            multiplier.append(scalar*trixie[firstrow][number])              #multiply each number in first row by scalar and append to multiplier
        for pos in range(len(trixie[secondrow]) - 1):
            trixie[secondrow][pos]=multiplier[pos]+trixie[secondrow][pos]   #add each number in secondrow to each number in multiplier
        self.m1=trixie
        return trixie
    def rref(self):
        trixie = self.m1
        trixie = self.ref()
        pivits = 0
        rainy = []
        for row in trixie:
            if all(x == 0 for x in row):
                break
            else:
                #creats 1s in matrix
                divider = trixie[pivits][pivits]                      #number needed to for the pivot to be 1 when dived
                for number in range(len(row)):                        #for every number in row
                    trixie[pivits][number] = row[number] / divider    #replace number in trixie by number dived by divder
                for i in reversed(range(pivits)):
                    multiplier = trixie[i][pivits]
                    for number in range(len(row)):
                        output=trixie[i][number]- (multiplier * trixie[pivits][number])
                        trixie[i][number]=output
            pivits += 1
        trixie=self.remove_floats(trixie)
        self.m1=trixie
        return trixie
    def refstart(self, trixie, sunny):
        '''
        :param trixie: matrix that will be turned to ref
        :param sunny: ref of trixie
        :return:function generates all the rows of ref matrix except for the first row
        '''
        'function uses recursion to shrink matrix down ex(3x3 to 2x2 then break at 1x1)'
        if len(trixie) == 1:            #if the matrix is a 1x1 matrix return sunny
            return sunny
        else:
            pos = 1
            crate = []
            for number in range(len(trixie) - 1):
                basket = []                         # basket is where the outputs go
                pivot = trixie[0][0]                # pivot is the pivot point of the function
                axle = trixie[pos][0]
                multiplier = (-1 * axle) / pivot    # multiplier is the number needed for this equation to be true
                # (multiplier * pivot - axle = 0)
                for (trix, al) in zip(trixie[0], trixie[pos]):
                    output = (trix * multiplier) + al
                    basket.append(output)
                if pos == 1:
                    sunny.append(basket)
                pos += 1
                crate.append(basket)
            crate2 = []
            for row in crate:
                row = row[1:]
                crate2.append(row)

            return self.refstart(crate2, sunny)
    def ref(self):
        '''
        :return:function converts matrix to ref
        '''
        trixie=self.m1
        'function generates all the rows of ref matrix exept for the first row'
        cloudy = self.refstart(trixie, sunny=[])
        cloudy.insert(0, trixie[0])                 #add the first row to the matrix
        rainy = []
        'coverts floats to ints'
        for row in cloudy:
            holder = []
            for number in row:
                if number == int(number):           #only convert number to int if it has no decmial points
                    holder.append(int(number))
                else:
                    holder.append(number)
            rainy.append(holder)
        'fill the empty spaces of the matrix with zeros'
        max_length = max(len(row) for row in rainy)
        for item in range(len(rainy)):
            while len(rainy[item]) < max_length:    #if the row is not full
                rainy[item].insert(0, 0)            #add 0s to the start of the row
        self.m1 = rainy  # convert matrix to instance
        return rainy
    def identity(self):
        '''
        function returns an identity matrix the same size as the input matrix
        uses nested for loops to create a matrix of zeros
        then adds 1s to diagonals
        '''
        matrix=self.m1
        blank = []
        'creates a matrix of zeros'
        for row in matrix:
            filler=[]                   #hold the row before adding it to blank
            for number in row:
                filler.append(0)        #and zeros to filler
            blank.append(filler)
        'adds 1s two the diagonals '
        for pos in range(len(matrix)):  #for row in matrix
            blank[pos][pos]=1           #add 1 to the digaonals
        return blank
    def invert(self):
        '''
        :return:the function uses the jordan gauss elimination to invert the matrix given
        '''
        trixie=self.m1
        if len(trixie)== len(trixie[0]):
            identity= self.identity()                                       #create identity of matrix
            try:
                for row in range(len(trixie)):
                    pivot = trixie[row][row]                                    #middle digonal values  of trixie
                    'turns middle digonals into 1s'
                    for number in range(len(trixie)):
                        trixie[row][number]=trixie[row][number] /pivot          #divid each number by pivot then replace that number in the matrix
                        identity[row][number] =identity[row][number] /pivot     #do the same for the identity matrix
                    "gets rid of 0s above and bellow 1s"
                    for row2 in range(len(trixie)):
                        if row2 != row:                                         #skips the row2 if it is the same as row
                            factor = trixie[row2][row]                          #number bellow/ubove the digainals
                            for collum in range(len(trixie)):
                                trixie[row2][collum]  = trixie[row2][collum]  -(factor * trixie[row][collum])     #replace trixie[row2][collum] with the new number that has been subrated by the
                                identity[row2][collum]=identity[row2][collum] -(factor * identity[row][collum])
                inverted_matrix = self.remove_floats(identity)
                self.m1=inverted_matrix
                return (inverted_matrix)
            except:
                self.m1=("matrix has no inverse")
                return("matrix has no inverse")
        else:
            self.m1=("matrix not square")
            return ("matrix not square")
    def remove_floats(self,matrix):
        'coverts floats to ints '
        new_matrix = []
        for row in matrix:  #
            holder = []
            for number in row:
                if number == int(number):  # only convert number to int if it has no decimal points
                    holder.append(int(number))
                else:
                    number = round(number, 2)  # round to hundredth
                    holder.append(number)
            new_matrix.append(holder)
        return new_matrix
