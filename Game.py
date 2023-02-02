import random

class Player:

    def __init__(self, name, ai = False):
        self.name = name
        self.store = 0
        self.currentSelection = ""
        self.ai = ai

    def AddPoint(self):
        self.store =+ 1
        print(111)

def ChoiceToString(intParam):
    if intParam == 1:
        return "папір"
    elif intParam == 2:
        return "камінюка"
    elif intParam == 3:
        return "ножиці"

def DefinitionWinner(player1, player2):

    if player1.currentSelection == player2.currentSelection:
        return ""
    elif player1.currentSelection == 'ножиці' and player2.currentSelection == 'папір':
        return player1
    elif player1.currentSelection == 'папір' and player2.currentSelection == 'ножиці':
        return player2
    elif player1.currentSelection == 'папір' and player2.currentSelection == 'камінюка':
        return player1
    elif player1.currentSelection == 'камінюка' and player2.currentSelection == 'папір':
        return player2
    elif player1.currentSelection == 'камінюка' and player2.currentSelection == 'ножиці':
        return player1
    elif player1.currentSelection == 'ножиці' and player2.currentSelection == 'камінюка':
        return player2

def AlreadyAdded(analyzedPlayers, player):
    
    if len(analyzedPlayers) > 0:
            try:
                if  analyzedPlayers.index(player) == 0 or analyzedPlayers.index(player) > 0:
                    return True
                else:
                    return False
            except:
                return False
    return False       
    
realPlayer = Player("Реальний гравець")
aiPlayer1 = Player("AI гравець 1", ai=True)

players = list()
players.append(realPlayer)
players.append(aiPlayer1)

winStore = 5
endGame = False
winner = ""

while endGame != True:

    for player in players:
        
        if player.ai:
            choiceInt = random.randint(1, 3)
        else: 
            choiceInt = int(input("Введіть число : папір = 1, ножиці = 2, камінюка = 3 \n"))
        
        player.currentSelection = ChoiceToString(choiceInt)

    analyzedPlayers = [] #Теж list

    currentPlayer = players[0]

    for playerX in players:

        if currentPlayer != playerX:
           analyzedPlayers.append(currentPlayer)
           currentPlayer = playerX

        for playerY in players:
            if playerX == playerY:
                continue
            elif AlreadyAdded(analyzedPlayers, playerY):
                continue                
            else:
                print(f"Гравець {playerX.name} обрав {playerX.currentSelection} та Гравець {playerY.name} обрав {playerY.currentSelection}\n")
                result = DefinitionWinner(playerX,playerY)
                if result != "":
                    print(f"{result.name} виграв цей бій \n")
                    result.store =+ 1
                    #result.AddPoint()

    print("*************************************************")
    for player in players:
        print(f"Рахунок {player.name} : {player.store} \n")
    print("*************************************************")

    for player in players:
        if player.store >= winStore:
            endGame = True
            winner = player

print(f"---Гравець {playerX.name} переможець---\n")


