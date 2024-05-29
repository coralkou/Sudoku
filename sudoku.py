class Sudoku:
    def __init__(self):
        self.display = [[None for col in range(9)] for row in range(9)]
        self.candidate = [['' for col in range(9)] for row in range(9)]
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    self.candidate[i][j]+= str(k + 1)
        self.remaining = 81
        self.queue = []

    def insert(self, row, col, num):
        if (row < 0 or row >= 9 or col < 0 or row  >= 9 or not isinstance(row, int) or not isinstance(col, int)):
            print("invalid cooridinates")
            return
        if (self.remaining == 0):
            print(f"Trying to add {num} at row {row} col {col}")
            print("The matrix is full")
            return
        if (num < 1 or num > 9 or not isinstance(num, int)):
            print("Invalid input")
            return
        self.remaining -= 1
        self.display[row][col] = num
        self.candidate[row][col] = ''
        for c in range(9):
            if str(num) in self.candidate[row][c]:
                self.candidate[row][c] = self.candidate[row][c].replace(str(num), '')
                if len(self.candidate[row][c]) == 1:
                    self.queue.append([row, c, int(self.candidate[row][c])])
        for r in range(9):
            if str(num) in self.candidate[r][col]:
                self.candidate[r][col] = self.candidate[r][col].replace(str(num), '')
                if len(self.candidate[r][col]) == 1:
                    self.queue.append([r, col, int(self.candidate[r][col])])
        base_r = (row //3) * 3
        base_c = (col //3) * 3
        for r in range(3):
            for c in range(3):
                if str(num) in self.candidate[base_r + r][base_c + c]:
                    self.candidate[base_r + r][base_c + c] = self.candidate[base_r + r][base_c + c].replace(str(num), '')
                    if len(self.candidate[base_r + r][base_c + c]) == 1:
                        self.queue.append([base_r + r, base_c + c, int(self.candidate[base_r + r][base_c + c])])
        return
    
    def show_display(self):
        for r in range(9):
            row = ""
            for c in range(9):
                if self.display[r][c]:
                    row += f"| {self.display[r][c]} "
                else:
                    row += "| _ "
                if c in {2, 5, 8}:
                    row += "|"
            print(row)
            if r in {2, 5, 8}:
                print("------------------------------------")
        return
    
    def show_candidate(self):
        for r in range(9):
            row = ""
            for c in range(9):
                row += self.candidate[r][c] + " " * (10 - len(self.candidate[r][c])) + "|"
            print(row)
        return
    
    def scan_single(self):
        print("scanning single>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        while self.queue:
            r, c, num = self.queue.pop(0)
            print(f"Insert row {r} col {c} with {num}")
            self.insert(r, c, num)
        return

    def scan_row(self):
        print("scanning row>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
        for r in range(9):
            double = set()
            count = [0 for x in range(9)]
            for c in range(9):
                if self.candidate[r][c] in double:
                    for c2 in range(9):
                        if self.candidate[r][c2] != "" and self.candidate[r][c2] != self.candidate[r][c]:
                            for num in self.candidate[r][c2]:
                                if num in self.candidate[r][c]:
                                    self.candidate[r][c2] = self.candidate[r][c2].replace(num, '')
                else:
                    if len(self.candidate[r][c]) == 2:
                        double.add(self.candidate[r][c])
                for num in self.candidate[r][c]:
                    count[int(num) - 1] += 1
            for i in range(9):
                if count[i] == 1:
                    for c in range(9):
                        if str(i + 1) in self.candidate[r][c]:
                            print(f"row {r} col {c} add {i + 1}")
                            self.insert(r, c, i + 1)
                            break
        return
    
    def scan_column(self):
        print("scanning column>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        for c in range(9):
            double = set()
            count = [0 for x in range(9)]
            for r in range(9):
                if self.candidate[r][c] in double:
                    for r2 in range(9):
                        if self.candidate[r2][c] != "" and self.candidate[r2][c] != self.candidate[r][c]:
                            for num in self.candidate[r2][c]:
                                if num in self.candidate[r][c]:
                                    self.candidate[r2][c] = self.candidate[r2][c].replace(num, '')
                else:
                    if len(self.candidate[r][c]) == 2:
                        print(f"added double {self.candidate[r][c]}")
                        double.add(self.candidate[r][c])
                for num in self.candidate[r][c]:
                    count[int(num) - 1] += 1
            for i in range(9):
                if count[i] == 1:
                    for r in range(9):
                        if str(i + 1) in self.candidate[r][c]:
                            print(f"row {r} col {c} add {i + 1}")
                            self.insert(r, c, i + 1)
                            break
        return

    def scan_square(self):
        print("scanning square>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        for start in [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]:
            count = [0 for x in range(9)]
            double = set()
            for delta in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]:
                if self.candidate[start[0]+ delta[0]][start[1] + delta[1]] in double:
                    for delta2 in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]:
                        if self.candidate[start[0]+ delta2[0]][start[1] + delta2[1]] != "" and self.candidate[start[0]+ delta2[0]][start[1] + delta2[1]] != self.candidate[start[0]+ delta[0]][start[1] + delta[1]]:
                            for num in self.candidate[start[0]+ delta2[0]][start[1] + delta2[1]]:
                                if num in self.candidate[start[0]+ delta[0]][start[1] + delta[1]]:
                                    self.candidate[start[0]+ delta2[0]][start[1] + delta2[1]] = self.candidate[start[0]+ delta2[0]][start[1] + delta2[1]].replace(num, '')
                else:
                    if len(self.candidate[start[0]+ delta[0]][start[1] + delta[1]]) == 2:
                        double.add(self.candidate[start[0]+ delta[0]][start[1] + delta[1]])

                for num in self.candidate[start[0]+ delta[0]][start[1] + delta[1]]:
                    count[int(num) - 1] += 1
            for i in range(9):
                if count[i] == 1:
                    for delta in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]:
                        if str(i + 1) in self.candidate[start[0]+ delta[0]][start[1] + delta[1]]:
                            print(f"row {start[0]+ delta[0]} col {start[1] + delta[1]} add {i + 1}")
                            self.insert(start[0]+ delta[0], start[1] + delta[1], i + 1)
                            break
        return