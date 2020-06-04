def ContarPuntos(board):
	acumuladorPuntos= 0
	N = 6
	EMPTY = 99
	acumulador = 0
	contador = 0
	for i in range(len(board[0])):
		if ((i +1) % 6) != 0:
			if board[0][i] != EMPTY and board[0][i + 1] != EMPTY and board[1][contador + acumulador] != EMPTY and board[1][contador + acumulador + 1] != EMPTY:
				acumuladorPuntos = acumuladorPuntos + 1
			acumulador = acumulador + N
		else: 
			contador = contador + 1
			acumulador = 0
	return acumuladorPuntos

def direction_move(board, player_turn_id):
	free = []
	free = FreeSpace(board)

	quality = -10000
	nextMove = []
	for i in free:
		
		score = MM(board, player_turn_id, -100000, +100000, 0, 0, False, i)
		if (score > quality):
			nextMove.clear()
			quality = score			
			nextMove.append(i)

	return [nextMove[0][0],nextMove[0][1]]


def MinMx(board,player_turn_id,alpha,beta,depth,nodeIndex,isMaximizingPlayer,move):
	player = player_turn_id if isMaximizingPlayer else (player_turn_id % 2) + 1
	_,validate = LookAhead(board, player_turn_id, move, not isMaximizingPlayer)
	
	
	if (depth == 0 or validate != 0):
		return validate
	
	free = []
	free = space_available(board)
	
	if (isMaximizingPlayer):
		quality = -100000
		for i in free:
			board = LookAhead(board,player,move,isMaximizingPlayer)
			
			score = MM(board, player, alpha, beta, depth + 1, 0, False, i)
			quality = max(quality, score)
			alpha = max(alpha, score)
			if (beta <= alpha):
				break

		board[move[0]][move[1]] = 99
		return quality

	
	if (not(isMaximizingPlayer)):
		quality = 100000
		for j in free:
			board = LookAhead(board,player,move,isMaximizingPlayer)
			
			score = MM(board, player, alpha, beta, depth + 1, 0, True, j)
			quality = min(quality,score)
			beta = min(beta, score)

		board[move[0]][move[1]] = 99
		return quality

	return 0
    
def space_available(board):
    free = []
    for i in range(len(board)):
	    for j in range(len(board[0])):
		    if board[i][j] == 99:
			    free.append((i,j))
    return free


def look_ahead(board, player_turn, move, isMAx):

	board = list(map(list,board))
	acumuladorPuntos = ContarPuntos(board)

	board[move[0]][move[1]] = 0
	board = list(map(list,board))
	acumuladorPuntos2 = ContarPuntos(board)

	diferencia = acumuladorPuntos2 - acumuladorPuntos
	if (acumuladorPuntos < acumuladorPuntos2):
		if (player_turn == 1):
			board[move[0]][move[1]] = 2 if diferencia == 2 else 1
		elif (player_turn == 2):
			board[move[0]][move[1]] = -2 if diferencia == 2 else -1

	if (isMAx):
		return (board,diferencia)
	else:
		return (board, diferencia * -1)

