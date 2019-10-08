
mancala = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]

def rules(pos, state, turn):
  # No seleccionar area de puntos
  if pos % 7 == 0:
    return False

  # Posiciones para jugador 1
  if turn == 0 and pos < 7:
    print("turno valido")

  # Posiciones para jugador 2
  elif turn == 1 and pos > 7:
    print('turno valido')

  else:
    return False

def move(pos, state):
  moves = mancala[pos]
  mancala[pos] = 0
  
  
if __name__ == "__main__":
  print(move(8, mancala, 0))