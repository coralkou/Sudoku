class Sudoku:
    def __init__(self):
        self.display = [[None for col in range(9)] for row in range(9)]
        self.candidate = [[set() for col in range(9)] for row in range(9)]
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    self.candidate[i][j].add(k + 1)
        self.remaining = 81
        self.queue = []

    def insert(self, row, col, num):
        if (row < 0 or row >= 9 or col < 0 or row  >= 9 or not isinstance(row, int) or not isinstance(col, int)):
            print("invalid cooridinates")
            return
        if (self.remaining == 0):
            print("The matrix is full")
            return
        if (num < 1 or num > 9 or not isinstance(num, int)):
            print("Invalid input")
            return
        self.remaining -= 1
        self.display[row][col] = num
        for c in range(9):
            if num in self.candidate[row][c]:
                self.candidate[row][c].remove(num)
                if len(self.candidate[row][c]) == 1:
                    self.queue.append([row, c, list(self.candidate[row][c])[0]])
        for r in range(9):
            if num in self.candidate[r][col]:
                self.candidate[r][col].remove(num)
                if len(self.candidate[r][col]) == 1:
                    self.queue.append([r, col, list(self.candidate[r][col])[0]])
        base_r = (row //3) * 3
        base_c = (col //3) * 3
        for r in range(3):
            for c in range(3):
                if num in self.candidate[base_r + r][base_c + c]:
                    self.candidate[base_r + r][base_c + c].remove(num)
                    if len(self.candidate[base_r + r][base_c + c]) == 1:
                        self.queue.append([base_r + r, base_c + c, list(self.candidate[base_r + r][base_c + c])[0]])
        self.candidate[row][col] = set()
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
                row += " |"
                for n in self.candidate[r][c]:
                    row += f"{n}"
            print(row)
        return
    
    def scan_single(self):
        while self.queue:
            r, c, num = self.queue.pop(0)
            self.insert(r, c, num)
            # print("Scanning singles...")
            # before = self.remaining
            # for r in range(9):
            #     for c in range(9):
            #         if len(self.candidate[r][c]) == 1:
            #             num = list(self.candidate[r][c])[0]
            #             print(f"row {r} col {c} add {num}")
            #             self.insert(r, c, num)
            # if self.remaining == before or self.remaining == 0:
            #     break
            # else:
            #     before = self.remaining
        return

    def scan_must(self):
        print("scanning must")
        for r in range(9):
            count = [0 for x in range(9)]
            for c in range(9):
                for num in self.candidate[r][c]:
                    count[num - 1] += 1
            for i in range(9):
                if count[i] == 1:
                    for c in range(9):
                        if i + 1 in self.candidate[r][c]:
                            print(f"row {r} col {c} add {i + 1}")
                            self.insert(r, c, i + 1)
                            break
        for c in range(9):
            count = [0 for x in range(9)]
            for r in range(9):
                for num in self.candidate[r][c]:
                    count[num - 1] += 1
            for i in range(9):
                if count[i] == 1:
                    for r in range(9):
                        if i + 1 in self.candidate[r][c]:
                            print(f"row {r} col {c} add {i + 1}")
                            self.insert(r, c, i + 1)
                            break
        for start in [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]:
            count = [0 for x in range(9)]
            for delta in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]:
                for num in self.candidate[start[0]+ delta[0]][start[1] + delta[1]]:
                    count[num - 1] += 1
            for i in range(9):
                if count[i] == 1:
                    for delta in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]:
                        if i + 1 in self.candidate[start[0]+ delta[0]][start[1] + delta[1]]:
                            print(f"row {start[0]+ delta[0]} col {start[1] + delta[1]} add {i + 1}")
                            self.insert(start[0]+ delta[0], start[1] + delta[1], i + 1)
                            break
        return