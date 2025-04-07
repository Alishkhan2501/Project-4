
import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40  
ERASER_SIZE = 20  
def erase_cells(canvas, eraser):
    """Erase cells that are in contact with the eraser"""

    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()

    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE


    for item in canvas.find_overlapping(left_x, top_y, right_x, bottom_y):
        canvas.itemconfig(item, fill='white')

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Calculate the number of rows and columns based on the canvas size and cell size
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')

    
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')

    def move_eraser(event):
        mouse_x = event.x
        mouse_y = event.y
        canvas.coords(eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
        
        erase_cells(canvas, eraser)


    canvas.bind('<Motion>', move_eraser)
    root.mainloop()


if __name__ == '__main__':
    main()
