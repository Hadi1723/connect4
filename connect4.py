# No boiler plate here... You are creating it all!
dollars = '$'
euros = '€'

class CurrencyPiece() :
    def __init__(self, team_name):
        if isinstance(team_name, int):
            if team_name == 0:
                self.team_name == "Dollars"
            elif team_name == 1:
                self.team_name = "Euros"
            else:
                raise ValueError
        elif isinstance(team_name, str):         
            noSpace = team_name.split()
            team_name = "".join(noSpace)
            
            if team_name.lower() == "Dollars".lower():
                self.team_name = "Dollars"
            elif team_name.lower() == "Euros".lower():
                self.team_name = "Euros"
            else:
                raise ValueError
        else:
            raise TypeError
    
    def __str__(self):
        if self.team_name == "Dollars":
            return dollars
        else:
            return euros

class Board:
    def __init__(self):
        self.board = [ [None,  None,  None, None,  None,  None, None]
                     , [None,  None,  None, None,  None,  None, None]
                     , [None,  None,  None, None,  None,  None, None]
                     , [None,  None,  None, None,  None,  None, None]
                     , [None,  None,  None, None,  None,  None, None]
                     , [None,  None,  None, None,  None,  None, None]
                    ]
        self.current = "Dollars"
        
    def addPiece(self, column):
        self.column = column - 1
        
        if not (self.column >= 0 and self.column <= 6):
            raise ValueError
        
        self.rowForColumn = []
        
        for i in range(len(self.board)):
            self.rowForColumn.append(self.board[i][self.column])
        
        if self.rowForColumn.count(None) == 0:
            return
        
        for j in range(len(self.rowForColumn)-1, -1, -1):
            if self.rowForColumn[j] == None:
                self.board[j][self.column] = CurrencyPiece(self.current)
                break
        
        if self.current == "Dollars":
            self.current = "Euros"
        else:
            self.current = "Dollars"
                    
    def checkWinner(self):
        #horizontal check loop
        for a in range(6):
            for ai in range(4):
                if str(self.board[a][ai]) == "$" and \
                    str(self.board[a][ai+1]) == "$" and \
                    str(self.board[a][ai+2]) == "$" and \
                    str(self.board[a][ai + 3]) == "$":
                        return "Dollars"
                elif str(self.board[a][ai]) == "€" and \
                    str(self.board[a][ai+1]) == "€" and \
                    str(self.board[a][ai+2]) == "€" and \
                    str(self.board[a][ai + 3]) == "€":
                        return "Euros" 
        #vertical check loop
        for a in range(6):
            for ai in range(2,-1,-1):
                if str(self.board[ai][a]) == "$" and \
                    str(self.board[ai+1][a]) == "$" and \
                    str(self.board[ai+2][a]) == "$" and \
                    str(self.board[ai+3][a]) == "$":
                        return "Dollars"
                if str(self.board[ai][a]) == "€" and \
                    str(self.board[ai+1][a]) == "€" and \
                    str(self.board[ai+2][a]) == "€" and \
                    str(self.board[ai+3][a]) == "€":
                        return "Euros"
                    
        #negative diagonal check
        for a in range(3):
            for ai in range(4):
                if str(self.board[a][ai]) == "$" and \
                    str(self.board[a+1][ai+1]) == "$" and \
                    str(self.board[a+2][ai+2]) == "$" and \
                    str(self.board[a+3][ai+3]) == "$":
                        return "Dollars"
                if str(self.board[a][ai]) == "€" and \
                    str(self.board[a+1][ai+1]) == "€" and \
                    str(self.board[a+2][ai+2]) == "€" and \
                    str(self.board[a+3][ai+3]) == "€":
                        return "Euros"
                    
        #positive diagonal check
        for a in range(5,2,-1):
            for ai in range(4):
                if str(self.board[a][ai]) == "$" and \
                    str(self.board[a-1][ai+1]) == "$" and \
                    str(self.board[a-2][ai+2]) == "$" and \
                    str(self.board[a-3][ai+3]) == "$":
                        return "Dollars"
                if str(self.board[a][ai]) == "€" and \
                    str(self.board[a-1][ai+1]) == "€" and \
                    str(self.board[a-2][ai+2]) == "€" and \
                    str(self.board[a-3][ai+3]) == "€":
                        return "Euros"
        
        return False         
    
    def parseMove(self, column, row = 1):
         return True 
    
    def __str__(self) -> str:
        """
        This function was created in collaboration with the teacher assistants from the COMPSCI 1MD3 course (from McMaster University) on December 2021
        """
        s = "╔" + ("══╦" * 6) + "═" * 3 + "╗\n"
        for row_index, row in enumerate(self.board):
            s += "║"
            for col_index, column in enumerate(row):
                s += f" {str(column if column != None else ' ')} ║"
            if row_index < 5:
                s += "\n╠" + ("═══╬" * 6) + "═══╣\n"
            else:
                s += '\n'
        return s + "╚" + "═══╩" * 6 + "═" * 3 + "╝\n"
