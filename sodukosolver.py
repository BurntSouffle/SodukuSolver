#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:42:57 2021
Project: Automated Soduku Solver
Website: https://sudoku.com/expert/
@author: sufian
"""
import pyautogui as pg
import time

board = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    board.append(ints)

    if len(board) == 9:
        break
    print('Row ' + str(len(board)) + ' Complete')

time.sleep(2)

def print_board(board):
  
  for i in range(len(board)):

    #When we hit the 3 row we print a line
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - - - ")

    #When we hit 3 column we add a '|'
    for j in range(len(board[0])):
        if j % 3 == 0 and j != 0 :
          print(" | ", end = "")

        #Prints actual items in list to the board    
        if j == 8:
          print(board[i][j])
        else:
          print(str(board[i][j]) + " ", end = "")

#Function finds position of empty box in board denoted as 0
def find_empty(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return (i, j) #returns position of empty box as tuple (row, coloumn)
  return None 

#Function checks if number passed to the borad is valid
def valid_num(board, num, pos):
  #Check if num is in the same row 
  for i in range(len(board[0])):
    if board[pos[0]][i] == num and pos[1] != i:
      return False
  
  #Check if num is in same column 
  for i in range(len(board)):
    if board[i][pos[1]] == num and pos[0] != i:
      return False
  
  #Check if num is in the same box 
  box_x = pos[1] // 3
  box_y = pos[0] // 3 #gives us which square we are on

  for i in range(box_y * 3, box_y*3 + 3):
    for j in range(box_x * 3, box_x*3 +3):
      if board[i][j] == num and (i,j) != pos:
        return False
  
  return True

def weboutput(board):
    final_board = []
    str_board = []
    
    for i in range(9):
        final_board.append(board[i])
    
    for lists in final_board:
        for num in lists:
            str_board.append(str(num))
    
    counter = []
    
    for num in str_board:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            for i in range(8):
                pg.hotkey('left')

def solve(board):
  
  empty_square = find_empty(board)
  if not empty_square:
    return True
  else:
    erow, ecol = empty_square

  for i in range(1,10):
    if valid_num(board, i, (erow, ecol)):
      board[erow][ecol] = i

      if solve(board):
        return True
      
      board[erow][ecol] = 0
  return False

solve(board)
weboutput(board)
'''
print("Soduku board: \n")
print_board(board)
print("")
solve(board)
print("Your solved board: \n")
print_board(board)
'''
