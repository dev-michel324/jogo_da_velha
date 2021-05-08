class func:
    def __init__(self):
        self.tab = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    def show_tab(self):
        output = "   1 2 3\n"
        for i in range(len(self.tab)):
            output += "{} |{}|{}|{}|\n".format((i+1), self.tab[i][0], self.tab[i][1], self.tab[i][2])
        return output

    def evaluate(self):
        for i in range(len(self.tab)):
            if self.tab[i][0]!=" " and self.tab[i][1]==self.tab[i][0] and self.tab[i][2]==self.tab[i][0]:
                if self.tab[i][0]=="X":
                    return "Jogador 1 venceu!"
                else:
                    return "Jogador 2 venceu!"
        
        for i in range(len(self.tab)):
            if self.tab[0][i]!=" " and self.tab[1][i]==self.tab[0][i] and self.tab[2][i]==self.tab[0][i]:
                if self.tab[0][i]=="X":
                    return "Jogador 1 venceu!"
                else:
                    return "Jogador 2 venceu!"

        if self.tab[0][0]!=" " and self.tab[1][1]==self.tab[0][0] and self.tab[2][2]==self.tab[0][0]:
            if self.tab[0][0]=="X":
                return "Jogador 1 venceu!"
            else:
                return "Jogador 2 venceu!"
        
        if self.tab[0][2]!=" " and self.tab[1][1]==self.tab[0][2] and self.tab[2][0]==self.tab[0][2]:
            if self.tab[0][2]=="X":
                return "Jogador 1 venceu!"
            else:
                return "Jogador 2 venceu!"
        
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                if self.tab[i][j]==" ":
                    return 0
        
        return "Empate"