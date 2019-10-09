
mancala = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]


def rules(pos, state, turn):
  print("turno ", turn)
  if state[pos] == 0:
    print("pos en 0")
    return state, turn

  sub_one = state[0:6]
  sub_two = state[7:13]

  # Check if someone won
  if sum(sub_one) == 0 or sum(sub_two) == 0:
    new_state = state.copy()
    new_state[6] = sum(sub_one)
    new_state[13] = sum(sub_two)
    i = 0
    while i < 6:
      new_state[i] = 0
      new_state[i + 7] = 0
      i += 1
    return new_state, 3

  # Not available move
  if pos % 7 == 6:
    return state, turn

  # Posiciones para jugador 1
  if turn == 0 and pos < 7:
    new_state, last = move(pos, state, turn)
    if last % 7 == 6:
      pass
    else:
      turn = (turn + 1) % 2
    if new_state[last] == 1:
      new_state[6] =  new_state[6] + new_state[(7+last)%14]
      new_state[(last+7)%14] = 0
    return new_state, turn

  # Posiciones para jugador 2
  elif turn == 1 and pos > 6:
    new_state, last = move(pos, state, turn)
    if last % 7 == 6:
      pass
    else:
      turn = (turn + 1) % 2
    if new_state[last] == 1:
      new_state[13] = new_state[(13-last)%14] + new_state[13]
      new_state[(13-last)%14] = 0
    return new_state, turn
  else:
    return (state, turn)


# Movement in the board
def move(pos, state, turn):
  moves = state[pos]
  state[pos] = 0
  new_state = state.copy()
  x = 1
  while x<=moves:
    if pos + x == 6 and turn == 0:
      new_state[(pos+x) % 14] = state[(pos + x) % 14] + 1
    elif pos + x == 13 and turn == 1:
      new_state[(pos+x) % 14] = state[(pos+x) % 14] + 1
    elif pos + x == 6 and turn != 0:
      moves += 1
    elif pos + x == 13 and turn != 1:
      moves +=1
    else:
      new_state[(pos+x) % 14] = state[(pos+x) % 14] + 1
    x += 1
  return (new_state, (pos + x - 1) % 14) 


# Function for printing the board
def for_print(board):
  for x in range(6):
    print("   ", board[12-x], end = "")
  print("")
  print(board[13], "                              ", board[6])
  x = 0
  for x in range(6):
    print("   ", board[x], end = "")
  print("")

def monte_carlo():
  return 10

def juego():
  board = mancala
  turn = 0
  for_print(board)
  while True:
    if turn == 0:
      pos = input("Ingrese su movimiento ")
    else:
      pos = monte_carlo()
    board, turn = rules(int(pos), board, turn)
    for_print(board)
    if turn == 3:
      break
      
    
    

  
if __name__ == "__main__":
  juego()
  # board , turn = rules(4, mancala, 0)
  # for_print(board)
  # if  not turn:
  #   print("gano alguien")