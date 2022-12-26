
import pygame

pygame.init()


#Creating the rows and columns
#0 represents no value in the matrix
#1 represents the player value in the matrix
#2 represent the computer value in the matrix
Board=[

    [1,2,1],
    [0,0,0],
    [0,0,0]
]


PlayerHasWon=0


def Update_Board(IndexOfCombination, All_List_Combinations, IndexOfValue):

    Row1=All_List_Combinations[0]#Storing the value of Row1 to the first list in the All_List_Combinations list
    Row2=All_List_Combinations[1]#Storing the value of Row2 to the second list in the All_List_Combinations list
    Row3=All_List_Combinations[2]#Storing the value of Row3 to the third list in the All_List_Combinations list
    Column1=All_List_Combinations[3]#Storing the value of Column1 to the fourth list in the All_List_Combinations list
    Column2=All_List_Combinations[4]#Storing the value of Column2 to the fifth list in the All_List_Combinations list
    Column3=All_List_Combinations[5]#Storing the value of Column3 to the sixth list in the All_List_Combinations list
    Diagnol1=All_List_Combinations[6]#Storing the value of Diagnol1 to the seventh list in the All_List_Combinations list
    Diagnol2=All_List_Combinations[7]#Storing the value of the Diagnol2 to the eighth list in the All_List_Combinations list

    
    if All_List_Combinations[IndexOfCombination]==Row1 and IndexOfCombination==0:#Checking to see if the index of the combination's value is equal to the list in Row1 and making sure the index of the combination is 0 to avoid scanning the wrong list
     
        Board[0][IndexOfValue]=Row1[IndexOfValue]#Setting either the first, second or third square of the board to the value in Row1 which is the compputer's selected square
        print("The combination is Row1")
    
    elif All_List_Combinations[IndexOfCombination]==Row2 and IndexOfCombination==1:#Checking to see if the index of the combinations value is equal to the list in Row2 and making sure the index of the combination is 1 to avoid scanning the wrong list      
        
        Board[1][IndexOfValue]=Row2[IndexOfValue]#Setting either the fourth, fifth or sixth square of the board to the value in Row2 which is the computer's selected square
        print("The combination is Row2 ")
    
    elif All_List_Combinations[IndexOfCombination]==Row3 and IndexOfCombination==2:#Checking to see if the index of the combination's value is equal to the list in Row3 and making sure the index of the combination is 2 to avoid scanning the wrong list
        
        Board[2][IndexOfValue]=Row3[IndexOfValue]#Setting either the seventh, eighth or ninth square of the board to the value in Row3 which is the computer's selected square
        print("The combination is Row3")
    
    elif All_List_Combinations[IndexOfCombination]==Column1 and IndexOfCombination==3:#Checking to see if the index of the combination's value is equal to the list in Column1 and making sure the index of the combination is 3 to avoid scanning the wrong list 

        Board[IndexOfValue][0]=Column1[IndexOfValue]#Setting either the first, fourth or seventh square of the board to the value in Column1 which is the computer's selected square
        print("The combination is Column1")

    elif All_List_Combinations[IndexOfCombination]==Column2 and IndexOfCombination==4:#Checking to see if the index of the combination's value is equal to the list in Column2 and making sure that the index of the combination is 4 to avoid scanning the wroing list 

        Board[IndexOfValue][1]=Column2[IndexOfValue]#Setting the second, fifth or eighth square of the board to the value in Column2 which is the computer's selected square                  
        print("The combination is Column2")
    
    elif All_List_Combinations[IndexOfCombination]==Column3 and IndexOfCombination==5:#Checking to see if the index of the combination's value is equal to the list in Column3 and making sure that the index of the combination is 5 to avoid scanning the wrong list 

        Board[IndexOfValue][2]=Column3[IndexOfValue]#Setting the third, sixth or ninth square of the board to the value in Column3 which is the computer's selected square
        print("The combination is Column3")
    
    elif All_List_Combinations[IndexOfCombination]==Diagnol1 and IndexOfCombination==6:#Checking to see if the index of the combination's value is equal to the list in Diagnol1 and making sure that the index of the combination is 6 to avoid scanning the wrong list

        Board[IndexOfValue][IndexOfValue]=Diagnol1[IndexOfValue]#Setting the first, fifth or ninth square of the board to the value in Diagnol1 which is the computer's selected square
        print("The combination is Diagnol1")
    
    elif All_List_Combinations[IndexOfCombination]==Diagnol2 and IndexOfCombination==7:#Checking to see if the index of the combination's value is equal to the list in Diagnol2 and making sure that the index of the combination is 7 to avoid scanning the wrong list

        if Diagnol2[0]==2:#Checking if the first value in Diagnol2 has the computer's input which is represented by '2'

            Board[2][0]=Diagnol2[0]#Setting the seventh square of Board to the first element of Diagnol2 
        
        elif Diagnol2[1]==2:#Checking if the second value in Diagnol2 has the computer's input which is represented by '2'

            Board[1][1]=Diagnol2[1]#Setting the fifth square of the Board to the second element in Diagnol2
        
        elif Diagnol2[2]==2:#Checking if the third value in Diagnol2 has the computer's input which is represented by '2'

            Board[0][2]=Diagnol2[2]#Setting the third square of the Board to the third element in Diagnol2
        print("The combination is Diagnol2")
    







def Check_For_Winner():#Function defined to check for the winner


    #Storing the row values in a list

    Row1=[Board[0][0], Board[0][1], Board[0][2]]
    Row2=[Board[1][0], Board[1][1], Board[1][2]]
    Row3=[Board[2][0], Board[2][1], Board[2][2]]

    #Storing the column values in a list
    Column1=[Board[0][0], Board[1][0], Board[2][0]]
    Column2=[Board[0][1], Board[1][1], Board[2][1]]
    Column3=[Board[0][2], Board[1][2], Board[2][2]]

    #Storing the diagnol values in a list
    Diagnol1=[Board[0][0], Board[1][1], Board[2][2]]
    Diagnol2=[Board[2][0], Board[1][1], Board[0][2]]

    All_List_Combinations=[Row1, Row2, Row3, Column1, Column2, Column3, Diagnol1, Diagnol2]#Storing all of the combination in a list


    #Checking for a winner
    for Combination in All_List_Combinations:#Looping through the possible combinations

        SumOfValues=sum(Combination)#Calculating the total value of the combination

        if SumOfValues==6:#If there are 3 values of '2' then the computer has won since 3 multiplied by the value 2 = 6

            PlayerHasWon=False
            #print("The computer has won")
        if SumOfValues==3:#If there are 3 values of '1' then the player has won since 3 multiplied by the value 1 = 3

            PlayerHasWon=True
            #print("The player has won")
    



    #Computer algorithm

    #Chooses the right square to win
    for Combination in All_List_Combinations:#Looping through the combinations 
        
        Computer_Can_Win=True#Setting the value of Computer_Can_Win to True
        SumOfValues=sum(Combination)#Finding the sum of the values in the combination

        for Value1 in Combination:#Looping through the values in the combination
            if Value1==1:#Checking if a player has entered a value in that combination 

                Computer_Can_Win=False#Setting the value of Computer_Can_Win to False if the player has entered a value
                break#Stopping the code
        
        if SumOfValues==4 and Computer_Can_Win==True:#Checking if the total value is 4 which means that 2 values of '2'= 4 and the computer can win

            IndexOfCombination=All_List_Combinations.index(Combination)#Finding the index of the combination

            for Value in Combination:#Looping through the values in the combination
                
                if Value==0:#Checking if there is an empty space in the combination to take over

                    IndexOfValue=Combination.index(Value)#Finding the index of the Value in the Combination
                    All_List_Combinations[IndexOfCombination][IndexOfValue]=2#Setting the value of the empty space to '2' 
                    Update_Board(IndexOfCombination, All_List_Combinations, IndexOfValue)   
                    print(Board[0])
                    print(Board[1])
                    print(Board[2])
        
    
    #Block user from winning 

    for Combination in All_List_Combinations:#Looping through all of the possible combinations

        SumOfValues=sum(Combination)#Findind the sum of all the values in the combination
        if SumOfValues==2:#Checking if the sum is 2 which could mean that there are 2 values of '1' meaning that there could be 2 values of the player 
            
            #This loop is being ran to check if there are 2 values of '1' which would mean that the computer could block the player from winning

            NumberOfPlayerValue=0#Setting the NumberOfPlayerValue to 0

            for Value in Combination:#Looping through all of the values in the combination

                if Value==1:#Checking if the value is 1 which means that there is a player value 
                    NumberOfPlayerValue=NumberOfPlayerValue+1#incrementing the NumberOfPlayerValues by 1 to see if there are 2 values of '1' in the combination
            
            if NumberOfPlayerValue==2:#Checking if there are 2 player values in the combination
               
                for Value in Combination:#Looping through the values in the combination

                    if Value==0:#Checking if the value is '0' which would mean that there is an empty space for the computer to occupy

                        IndexOfCombination=All_List_Combinations.index(Combination)#Finding the index of the combination
                        IndexOfValue=Combination.index(Value)#Finding the index of the empty value in the combination
                        All_List_Combinations[IndexOfCombination][IndexOfValue]=2#Changing the empty value to '2' which would mean that the computer has occupied the value
                        Update_Board(IndexOfCombination, All_List_Combinations, IndexOfValue)
                        print(Board[0])
                        print(Board[1])
                        print(Board[2])
                        
    """
    #Updating the Board matrix        

    Board[0][0]=Row1[0]#Changing the value of the first square in Board to the first element in Row1- This is applying all of the Row1 values to the Board matrix
    Board[0][1]=Row1[1]#Changing the value of the second square in Board to the second element in Row1
    Board[0][2]=Row1[2]#Changing the value of the third square in Board to the third element in Row1

    Board[1][0]=Row2[0]#Changing the value of the fourth square in Board to the first element in Row2- This is applying all of the Row2 values to the Board matrix
    Board[1][1]=Row2[1]#Changing the value of the fifth square in Board to the second element in Row2
    Board[1][2]=Row2[2]#Changing the value of the sixth square in Board to the third element in Row2

    Board[2][0]=Row3[0]#Changing the value of the seventh square in Board to the first element in Row3- This is applying all of the Row3 values to the Board matrix
    Board[2][1]=Row3[1]#Changing the value of the eighth square in Board to the second element in Row3
    Board[2][2]=Row3[2]#Changing the value of the ninth square in Board to the third element in Row3

    Board[0][0]=Column1[0]#Changing the value of the first square to the first element in Column1- This is applying all of the Column1 values to the Board matrix
    Board[1][0]=Column1[1]#Changing the value of the fourth square to the second element in Column1
    Board[2][0]=Column1[2]#Changing the value of the seventh square to the third element in Column1

    Board[0][1]=Column2[0]#Changing the value of the second square to the first element in Column2- This is applying all of the Column2 values to the Board matrix
    Board[1][1]=Column2[1]#Changing the value of the fifth square to the second element in Column2
    Board[2][1]=Column2[2]#Changing the value of the eighth square to the third element in Column2

    Board[0][2]=Column3[0]#Changing the value of the third square to the first element in Column3- This is applying all of the Column3 values to the Board matrix
    Board[1][2]=Column3[1]#Changing the value of the sixth square to the second element in Column3
    Board[2][2]=Column3[2]#Changing the value of the ninth square to the third element in Column3

    Board[0][0]=Diagnol1[0]#Changing the value of the first square to the first element in diagnol1- This is applying all of the Diagnol1 values to the Board matrix
    Board[1][1]=Diagnol1[1]#Changing the value of the fifth square to the second element in diagnol1
    Board[2][2]=Diagnol1[2]#Changing the value of the ninth square to the third element in diagnol1

    Board[2][0]=Diagnol2[0]#Changing the value of the seventh square to the first element in diagnol2-This is applying all of the Diagnol2 values to the Board matrix
    Board[1][1]=Diagnol2[1]#Changing the value of the fifth square to the second element in diagnol2
    Board[0][2]=Diagnol2[2]#Changing the value of the third square to the third element in diagnol2

    print(All_List_Combinations)
    print(Board)
  """






    







ScreenSize=pygame.display.Info()
Screen=pygame.display.set_mode((ScreenSize.current_w-80,ScreenSize.current_h-80),pygame.RESIZABLE)
pygame.display.set_caption("Tic Tac Toe Game")
Screen.fill((255,255,255))
pygame.display.flip()

#Uploading the board template
TicTacToeTemplate=pygame.image.load("C:\\Users\\rjini\\Downloads\\TicTacToeTemplate.png").convert()#Uploading image
TicTacToeTemplate=pygame.transform.scale(TicTacToeTemplate,(500,500))#Resizing
Screen.blit(TicTacToeTemplate,(0,0))#Displaying

#Uploading the x and o 
GamePieceX=pygame.image.load("C:\\Users\\rjini\\Downloads\\TicTacToeX.png").convert()#Uploading image
GamePieceX=pygame.transform.scale(GamePieceX,(150,150))#Resizing
GamePieceO=pygame.image.load("C:\\Users\\rjini\Downloads\\TicTacToeO.png").convert()#Uploading image
GamePieceO=pygame.transform.scale(GamePieceO,(120,120))#Reziing


pygame.display.flip()









#Function to check which square was clicked
def CheckSquare():

    if MousePosition[0]<150 and MousePosition[0]>0 and MousePosition[1]<=175 and MousePosition[1]>=0:#Checking if the first square was clicked
        Board[0][0]=1
        #print("The first square was clicked")
    
    if MousePosition[0]>150 and MousePosition[0]<330 and MousePosition[1]<=175 and MousePosition[1]>=0:#Checking if the second square was clicked
        Board[0][1]=1
        #print("The second square was clicked")
    
    if MousePosition[0]>330 and MousePosition[0]<495 and MousePosition[1]<=175 and MousePosition[1]>=0:#Checking if the third square was clicked
        Board[0][2]=1
        #print("The third square was clicked")

    if MousePosition[0]<155 and MousePosition[0]>0 and MousePosition[1]<=345 and MousePosition[1]>=180:#Checking if the fourth square was clicked
        Board[1][0]=1
        #print("The fourth square was clicked")
    
    if MousePosition[0]>155 and MousePosition[0]<332 and MousePosition[1]>180 and MousePosition[1]<347:#Checking if the fifth square was clicked
        Board[1][1]=1
        #print("The fifth square was clicked")
    
    if MousePosition[0]<495 and MousePosition[0]>332 and MousePosition[1]>180 and MousePosition[1]<345:#Checking if the sixth square was clicked
        Board[1][2]=1
        #print("the sixth square was clicked")

    if MousePosition[0]>0 and MousePosition[0]<150 and MousePosition[1]>350 and MousePosition[1]<498:#Checking if the seventh square was clicked
        Board[2][0]=1
        #print("The seventh square was clicked")
    
    if MousePosition[0]>150 and MousePosition[0]<331 and MousePosition[1]<498 and MousePosition[1]>350:#Checking if the eighth square was clicked
        Board[2][1]=1
        #print("The eighth square was clicked")

    if MousePosition[0]>331 and MousePosition[0]<498 and MousePosition[1]<498 and MousePosition[1]>350:#Checking if the ninth square was clicked
        Board[2][2]=1
        #print("The ninth square was clicked")











#Game loop
RunGame=True
while RunGame:
    MousePosition=pygame.mouse.get_pos()#Checking the mouse position
    Screen.fill((255,255,255))#Display
    Screen.blit(TicTacToeTemplate,(0,0))#Display

    if Board[0][0]==1:#Checking if the first square was pressed
        Screen.blit(GamePieceX,(0,20))#Displaying the X

    if Board[0][1]==1:#Checking if the second square was pressed
        Screen.blit(GamePieceX,(170,20))#Displaying the X

    if Board[0][2]==1:#Checking if the third square was pressed
        Screen.blit(GamePieceX,(340,20))#Displaying the X

    if Board[1][0]==1:#Checking if the fourth square was pressed
        Screen.blit(GamePieceX,(0,190))#Displaying the X

    if Board[1][1]==1:#Checking if the fifth square was pressed
        Screen.blit(GamePieceX,(170,190))#Displaying the X

    if Board[1][2]==1:#Checking if the sixth square was pressed
        Screen.blit(GamePieceX,(340,190))#Displaying the X
        
    if Board[2][0]==1:#Checking if the seventh square was pressed
        Screen.blit(GamePieceX,(0,352))#Displaying the X

    if Board[2][1]==1:#Checking if the eighth square was pressed
        Screen.blit(GamePieceX,(170,352))#Displaying the X

    if Board[2][2]==1:#Checking if the ninth square was pressed
        Screen.blit(GamePieceX,(340,352))#Displaying the X

    

    pygame.display.update()#Updating the display

    for event in pygame.event.get():
        if event.type==pygame.QUIT:#Checking if the window was closed
            RunGame=False#Ending the game loop

        if event.type==pygame.MOUSEBUTTONDOWN:#Checking if a square was clicked
            CheckSquare()#Calling the CheckSquare function
            Check_For_Winner()#Calling the Check_For_Winner function