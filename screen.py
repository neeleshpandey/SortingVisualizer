import pygame
from tkinter import *
from random import randint
from settings import *

class ScreenVisual():

    def __init__(self,COLS,sortMethod,delay,drawGridLines,WIN):
        
        self.PIXEL_SIZE = WIDTH // COLS
        self.ROWS = self.COLS = COLS
        self.sortMethod = sortMethod
        self.delay = delay
        self.drawGridLines = drawGridLines
        self.WIN = WIN
        self.grid = self.init_grid(BG_COLOR)

    def init_grid(self, color):
        """This function returns grids"""
        grid = []

        for i in range(self.ROWS):
            grid.append([])
            for _ in range(self.COLS):
                grid[i].append(color)

        return grid

    def draw_grid(self):
        """This function draws grids on pygame screen"""
        for i,row in enumerate(self.grid):
            for j,pixel in enumerate(row):
                pygame.draw.rect(self.WIN, pixel,(i * self.PIXEL_SIZE, j * self.PIXEL_SIZE, self.PIXEL_SIZE, self.PIXEL_SIZE))

        if self.drawGridLines:
            for i in range(self.ROWS + 1):
                pygame.draw.line(self.WIN, BLACK, (0, i* self.PIXEL_SIZE), (WIDTH, i * self.PIXEL_SIZE))

            for i in range(self.COLS + 1):
                pygame.draw.line(self.WIN, BLACK, (i* self.PIXEL_SIZE, 0), (i * self.PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

    def draw(self):
        """This function draws pygame screen"""
        self.WIN.fill(BG_COLOR)
        self.draw_grid()

        pygame.display.update()

    def generate_arr(self): 
        """This function generates a random array"""
        arr = []
        for _ in range(0, self.ROWS):
            arr.append(randint(1,self.COLS))
        return arr

    def drawArr(self,arr,colour,delay=-1):
        """This function draws the given array on pygame screen"""
        for i in range(0,len(arr)):
            for j in range(self.COLS-1,self.ROWS-arr[i],-1):
                self.grid[i][j] = colour
                if delay != -1:
                    self.slowExec(delay)

    def empGrids(self):
        """This function resets all the grids to white"""
        for i in range(self.ROWS):
            for j in range(self.COLS):
                self.grid[i][j] = WHITE
            
    def slowExec(self,delay):
        """This function slows the execution,
        to create animation on pygame screen"""
        self.draw()
        pygame.display.update() 
        pygame.time.delay(delay)

    def dispSort(self,arr,j):
        """This function displays realtime changes in array on pygame screen"""
        k1 = k2 = self.COLS-1
        self.empGrids()
        self.drawArr(arr,PURPLE)
        pygame.display.update()
        while k1 != self.ROWS - arr[j]-1 or k2 != self.ROWS - arr[j+1]-1:
            if k1 != self.ROWS - arr[j]-1:
                self.grid[j][k1] = RED
                k1 -= 1
            if k2 != self.ROWS - arr[j+1]-1:
                self.grid[j+1][k2] = GREEN
                k2 -= 1
            pygame.display.update()
            self.slowExec(self.delay)
        self.empGrids()
        self.drawArr(arr,PURPLE)
            
            