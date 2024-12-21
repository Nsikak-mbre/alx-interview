#!/usr/bin/python3
"""
Module to solve the N Queens problem.
"""

import sys


def is_safe(board, row, col, N):
    """
    Check if placing a queen at (row, col) is safe.
    """
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonal (top-left to bottom-right)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check diagonal (top-right to bottom-left)
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(row, board, N, solutions):
    """
    Recursive backtracking function to solve the N Queens problem.
    """
    if row == N:
        # Found a solution
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(row + 1, board, N, solutions)
            # Backtrack
            board[row] = -1


def nqueens(N):
    """
    Solve the N Queens problem and print solutions.
    """
    board = [-1] * N  # Initialize the board
    solutions = []    # To store all solutions
    solve_nqueens(0, board, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Argument validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    nqueens(N)
