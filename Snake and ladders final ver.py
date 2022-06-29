print("Welcome to Snakes and Ladders!")

def GetPlayerList():
    PlayerList = [] #An empty list
    FirstPlayer = str(input("Please enter First Player's name: "))
    PlayerList.append(FirstPlayer) #Append adds something to the list
    SecondPlayer = str(input("Please enter Second Player's name: "))
    PlayerList.append(SecondPlayer)
    return PlayerList, FirstPlayer, SecondPlayer #return recalls value back to reader.

PlayerList, FirstPlayer, SecondPlayer = GetPlayerList()
print("Current players are:", PlayerList)

def GenerateLadderPosition():
    import random
    LadderPositions=random.sample(range(5, 85),15)
    return LadderPositions

LadderPositions = GenerateLadderPosition()
print("Ladder cells: %s" %(LadderPositions))

def GenerateSnakePosition(): #This is so snake cells don't overlap with ladder cells, bootleg but it works
    import random
    SnakePositions = []
    count = 0
    while count <10:
        Generator=random.randint(5,85)
        if Generator not in LadderPositions:
            SnakePositions.append(Generator)
            count+=1
    return SnakePositions
        
SnakePositions = GenerateSnakePosition()
print("Snake cells: %s" %(SnakePositions))

def RollDice(CurrentPosition):
    import random
    roll = random.randint(1,6)
    CurrentPosition += roll
    print("You have rolled: %s," %(roll), "Your new position is: %s." %(CurrentPosition))
    return CurrentPosition

def CheckForLadder(r):
    if r in LadderPositions:
        r += 15
        print("Great %r! It's a ladder, climb up 15 cells. Your new position is: %s" %(CurrentPlayer, r))
        return r
    else:
        return r

def CheckForSnake(t):
    if t in SnakePositions:
        t -= 10
        print("Oops %r! You've been bitten, go down 10 cells. Your new position is: %s" %(CurrentPlayer, t))
        return t
    else:
        return t
    
FirstPlayerPosition = 1
SecondPlayerPosition = 1

while FirstPlayerPosition < 100 or SecondPlayerPosition < 100:
    
    CurrentPlayer = FirstPlayer
    print("\nIt's %s turn." %(FirstPlayer))
    input("Press enter to roll dice for first player %s: " %(FirstPlayer))
    FirstPlayerPosition = RollDice(FirstPlayerPosition)
    FirstPlayerPosition = CheckForLadder(FirstPlayerPosition)
    FirstPlayerPosition = CheckForSnake(FirstPlayerPosition)
    
    if FirstPlayerPosition > 99:
        print("\n%s is the Winner of the Game, Congratulations!" %(FirstPlayer))
        break
    
    CurrentPlayer = SecondPlayer
    print("\nIt's %s turn." %(SecondPlayer))
    input("Press enter to roll dice for second player %s: " %(SecondPlayer))
    SecondPlayerPosition = RollDice(SecondPlayerPosition)
    SecondPlayerPosition = CheckForLadder(SecondPlayerPosition)
    SecondPlayerPosition = CheckForSnake(SecondPlayerPosition)
    
    if SecondPlayerPosition > 99:
        print("\n%s is the Winner of the Game, Congratulations!" %(SecondPlayer))
        break

input("Press any key to exit.")
