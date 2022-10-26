a1 = " "
a2 = " "
a3 = " "
b1 = " "
b2 = " "
b3 = " "
c1 = " "
c2 = " "
c3 = " "

board = a1 + '|' + a2 + '|' + a3 + "\n" + b1 + '|' + b2 + '|' + b3 + "\n" + c1 + '|' + c2 + '|' + c3

choosing = True

while choosing:
        chooser = input("Would player one like to be X's or O's?")

        if chooser.upper() == "X":
                player1 = "X"
                player2 = "O"
                print("Ok, then player two will be O's")
        elif chooser.upper() == "O":
                player1 = "O"
                player2 = "X"
                print("Ok, then player two will be X's")
        else:
                continue
        choosing = False