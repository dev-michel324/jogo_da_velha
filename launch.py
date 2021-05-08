from function import func

f = func()
while True:
    while True:
        print(f.show_tab())
        print("Vez do jogador 1:\n")
        x = int(input("Digite uma posição na horizontal:\n"))
        y = int(input("Digite uma posição na vertical:\n"))
        if x>0 and x<4 and y>0 and y<4:
            if f.tab[x-1][y-1]==" ":
                f.tab[x-1][y-1] = "X"
                break
            else:
                print("A posição selecionada está ocupada!")
        else:
            print("Digite uma posição válida!")
            continue
    if f.evaluate()!=0:
        print(f.evaluate())
        break
    while True:
        print(f.show_tab())
        print("Vez do jogador 2:\n")
        x = int(input("Digite uma posição na horizontal:\n"))
        y = int(input("Digite uma posição na vertical:\n"))
        if x>0 and x<4 and y>0 and y<4:
            if f.tab[x-1][y-1]==" ":
                f.tab[x-1][y-1] = "O"
                break
            else:
                print("A posição selecionada está ocupada!")
        else:
            print("Digite uma posição válida!")
            continue
    if f.evaluate()!=0:
        print(f.evaluate())
        break