from sudoku import Sudoku

game = Sudoku()
level = input("What is the level of the game? (easy, medium, hard, expert, master, extreme)"  )
with open(f"{level}.txt", 'r') as file:
    file_contents = file.read()
for i in range(9):
    for j in range(9):
        digit = file_contents[i * 9 + j]
        if digit != ' ':
            game.insert(i, j, int(digit))

game.show_display()


##solution
while game.remaining != 0:
    before = game.remaining
    game.scan_single()
    game.scan_row()
    game.scan_single()
    game.scan_column()
    game.scan_single()
    game.scan_square()
    game.scan_single()

    if game.remaining == before:
        print(f"Current method is not sufficient, remaining {game.remaining}")
        game.show_candidate()
        break


game.show_display()