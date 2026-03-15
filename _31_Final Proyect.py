# Jesus Antonio Baez Ortega 23310372 6E
# LAB#31 Final Project - Tic-Tac-Toe

from random import randrange

def display_board(board):
    """Dibuja el tablero en la consola con un formato visual limpio."""
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            # Imprime el valor de la celda (número, X u O)
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    """Solicita y valida el movimiento del usuario."""
    ok = False 
    while not ok:
        move = input("Ingresa tu movimiento (1-9): ") 
        # Validación: ¿Es un solo dígito entre 1 y 9?
        ok = len(move) == 1 and '1' <= move <= '9'
        if not ok:
            print("¡Movimiento inválido! Intenta de nuevo.")
            continue
        
        # Convertimos el número 1-9 a coordenadas de matriz 0-2
        move = int(move) - 1 
        row = move // 3      # División entera para la fila
        col = move % 3       # Módulo para la columna
        
        # Verificamos si la casilla ya está ocupada
        sign = board[row][col]
        ok = sign not in ['O', 'X'] 
        if not ok:
            print("¡Campo ocupado! Elige otro número.")
            continue
            
    board[row][col] = 'O'