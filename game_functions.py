
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


def MM(board,player_turn_id,alpha,beta,depth,nodeIndex,isMaximizingPlayer,move):
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

