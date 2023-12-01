from tkinter import*
import random
window=Tk()
window.title("Snake Game")
score=0
direction="down"
game_width=700
game_height=700
speed=200
space_size=30
Body_parts=2
snake_color="#8E7618"
food_color="#DC143C"
background_color="#FFFFC2"
l=Label(window,text="Score:{}".format(score),font="Arial 20")
l.pack()
c=Canvas(window,bg=background_color,height=game_height,width=game_width)
c.pack()
class Snake:
    def __init__(self):
        self.body_size=Body_parts
        self.squares=[]
        self.coordinates=[]
        for i in range(0,Body_parts):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square=c.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color,tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        x=random.randint(0,(game_width//space_size)-1)*space_size
        y=random.randint(0,(game_height//space_size)-1)*space_size
        self.coordinates=[x,y]
        c.create_oval(x,y,x+space_size,y+space_size,fill=food_color,tag="food")
def next_turn(snake,food):
    x,y=snake.coordinates[0]
    if direction=="up":
        y-=space_size
    elif direction=="down":
        y+=space_size
    elif direction=="left":
        x-=space_size
    elif direction=="right":
        x+=space_size
    snake.coordinates.insert(0,(x,y))
    square=c.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color)
    snake.squares.insert(0,square)
    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        l.config(text="Score:{}".format(score))
        c.delete("food")
        food=Food()
    else:
        del snake.coordinates[-1]
        c.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(speed,next_turn,snake,food)
def change_direction(new_direction):
    global direction
    if new_direction=="left":
        if direction!="right":
            direction=new_direction
    elif new_direction=="right":
        if direction!="left":
            direction=new_direction
    elif new_direction=="up":
        if direction!="down":
            direction=new_direction
    elif new_direction=="down":
        if direction!="up":
            direction=new_direction
def check_collisions(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>=game_width:
        return True
    elif y<0 or y>=game_height:
        return True
    for body_parts in snake.coordinates[1:]:
        if x==body_parts[0] and y==body_parts[1]:
            return True
    return False
def game_over():
    c.delete(ALL)
    c.create_text(c.winfo_width()/2,c.winfo_height()/2,fill="red",font=("consolas", 70),text='GAME OVER',tag="gameover")
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_height}x{window_width}+{x}+{y}")
window.bind("<Left>",lambda event:change_direction("left"))
window.bind("<Right>",lambda event:change_direction("right"))
window.bind("<Up>",lambda event:change_direction("up"))
window.bind("<Down>",lambda event:change_direction("down"))
snake=Snake()
food=Food()
next_turn(snake,food)
window.mainloop()