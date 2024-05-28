from sudoku import Sudoku

game = Sudoku()
with open('medium.txt', 'r') as file:
    file_contents = file.read()
for i in range(9):
    for j in range(9):
        digit = file_contents[i * 9 + j]
        if digit != ' ':
            game.insert(i, j, int(digit))

game.show_display()
##solution
game.scan_single()
#game.scan_must()
#game.scan_single()

game.show_display()
if game.remaining != 0:
    game.show_candidate()