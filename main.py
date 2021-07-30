import pygame
from tkinter import *
from screen import ScreenVisual
from settings import *


def bubbleSort(arr):    #Bubble Sort Technique
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw.dispSort(arr,j,j+1)               
    draw.drawArr(arr,GREEN,1)

def insertionSort(arr): #Insertion Sort Technique
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j] :
                arr[j + 1] = arr[j]
                draw.dispSort(arr,j+1,j)
                j -= 1
        arr[j + 1] = temp
        draw.dispSort(arr,j+1,j)
    draw.drawArr(arr,GREEN,1)

def selectionSort(arr): #Selection Sort Technique
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                draw.dispSort(arr,j)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw.dispSort(arr,min_idx,i)
    draw.drawArr(arr,GREEN,1)

def closeWindow():  #This function helps to quit the while loop when Tkinter screen is closed
    global f 
    f = 1
    root.destroy()

run = True
clock = pygame.time.Clock()
drawing_color = BLACK

while run:

    f = 0

    root = Tk()
    root.wm_title('Sorting Visualizer')
    root.resizable(0,0)

    Label(text="SIZE").grid(row=0, column=0)

    size = IntVar(value=20)
    Entry(root, textvariable = size).grid(row=0,column=1)

    Label(text="Sorting Technique").grid(row=1, column=0)
    sortType = StringVar(value="Bubble Sort")
    OptionMenu(root, sortType, "Bubble Sort", "Insertion Sort","Selection Sort").grid(row=1, column=1)

    Label(text="Speed").grid(row=2, column=0)
    speed = IntVar(value=20)
    Entry(root, textvariable = speed).grid(row=2,column=1)

    gridLines = BooleanVar(value=True)
    Checkbutton(root, text='Show Grid Lines', onvalue=True, offvalue=False, variable=gridLines).grid(row=3)

    Button(root,bg="green",fg = "white",text = "Start",command=closeWindow,anchor=CENTER,relief=GROOVE).grid(row=4,column=0)

    Button(root,bg="red",fg = "white",text = "Quit",command=root.destroy,anchor=CENTER,relief=GROOVE).grid(row=4,column=1)

    root.mainloop()

    if f == 0:
        break
    
    sortMethod = sortType.get() #Getting values from Tk interface
    COLS = ROWS = size.get()
    delay = speed.get()
    drawGridLines = gridLines.get()

    WIN = pygame.display.set_mode((WIDTH,HEIGHT))   #Pygame screen
    pygame.display.set_caption( sortMethod+" Visualizer")
    draw = ScreenVisual(COLS,sortMethod,delay,drawGridLines,WIN)

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        arr = []
        draw.empGrids()
        arr = draw.generate_arr()
        draw.drawArr(arr,PURPLE)

        if sortMethod == "Bubble Sort":
            bubbleSort(arr)
        elif sortMethod == "Insertion Sort":
            insertionSort(arr)
        elif sortMethod == "Selection Sort":
            selectionSort(arr)
        break