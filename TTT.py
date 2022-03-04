pboard = {
    'P1':' ', 'P2':' ', 'P3':' ',
    'P4':' ', 'P5':' ', 'P6':' ',
    'P7':' ', 'P8':' ', 'P9':' '
}

player = 1
total_moves = 0
end_check = 0

def check():
    #Player-1 Condition checking
    #Horizontal Check
    if board['P1']=='X' and board['P2']=='X' and board['P3']=='X':
        print('Player-1 has WON!!!!!!')
        return 1
    if board['P4']=='X' and board['P5']=='X' and board['P6']=='X':
        print('Player-1 has WON!!!!!!')
        return 1
    if board['P7']=='X' and board['P8']=='X' and board['P9']=='X':
        print('Player-1 has WON!!!!!!')
        return 1
    
    #vertical Check
    if board['P1']=='X' and board['P4']=='X' and board['P7']=='X':
        print('Player-1 has WON!!!!!!')
        return 1
    if board['P2']=='X' and board['P5']=='X' and board['P8']=='X':
        print('Player-1 has WON!!!!!!')
        return 1
    if board['P3']=='X' and board['P6']=='X' and board['P9']=='X':
        print('Player-1 has WON!!!!!!')
        return 1
    
    #Diagonal Check
    if board['P1']=='X' and board['P5']=='X' and board['P9']=='X':
        print('Player-1 has WON!!!!!!')
        return 1
    if board['P3']=='X' and board['P5']=='X' and board['P7']=='X':
        print('Player-1 has WON!!!!!!')
        return 1
    
    #Player-2 Condition checking
    #Horizontal Check
    if board['P1']=='O' and board['P2']=='O' and board['P3']=='O':
        print('Player-2 has WON!!!!!!')
        return 1
    if board['P4']=='O' and board['P5']=='O' and board['P6']=='O':
        print('Player-2 has WON!!!!!!')
        return 1
    if board['P7']=='O' and board['P8']=='O' and board['P9']=='O':
        print('Player-2 has WON!!!!!!')
        return 1
    
    #vertical Check
    if board['P1']=='O' and board['P4']=='O' and board['P7']=='O':
        print('Player-2 has WON!!!!!!')
        return 1
    if board['P2']=='O' and board['P5']=='O' and board['P8']=='O':
        print('Player-2 has WON!!!!!!')
        return 1
    if board['P3']=='O' and board['P6']=='O' and board['P9']=='O':
        print('Player-2 has WON!!!!!!')
        return 1
    
    #Diagonal Check
    if board['P1']=='O' and board['P5']=='O' and board['P9']=='O':
        print('Player-2 has WON!!!!!!')
        return 1
    if board['P3']=='O' and board['P5']=='O' and board['P7']=='O':
        print('Player-2 has WON!!!!!!')
        return 1
    return 0


# To make users familiar about positions
print('P1 | P2 | P3')
print('-- | -- | --')
print('P4 | P5 | P6')
print('-- | -- | --')
print('P7 | P8 | P9')
print('**')

while True:
    #To see how the game Updates
    print(board['P1']+'|'+board['P2']+'|'+board['P3'])
    print('------')
    print(board['P4']+'|'+board['P5']+'|'+board['P6'])
    print('------')
    print(board['P7']+'|'+board['P8']+'|'+board['P9'])
    end_check = check()
   
    if total_moves == 9 or end_check == 1:
        break
    while True:
        if player == 1:
            p1_input = input('Player One:')
            if p1_input in board and board[p1_input] == ' ':
                board[p1_input] = 'X'
                player = 2
                break
            else:
                print('Wrong Move, Please eneter valid position..')
                continue
            
        if player == 2:
            p2_input = input('Player Two:')
            if p2_input in board and board[p2_input] == ' ':
                board[p2_input] = 'O'
                player = 1
                break
            else:
                print('Wrong Move, Please eneter valid position...')
                continue
    total_moves+=1
    print('*****')