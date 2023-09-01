from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
VELOCITY = 10
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = 0
    start_y = 0
    right_x = start_x + SIZE 
    bottom_y = start_y + SIZE
    player = canvas.create_rectangle(start_x, start_y, right_x, bottom_y, 'Blue')
    
    goal_start_x = SIZE * 18
    goal_start_y = SIZE * 18
    goal_right_x = goal_start_x + SIZE
    goal_bottom_y = goal_start_y + SIZE
    goal = canvas.create_rectangle(goal_start_x , goal_start_y, goal_right_x, goal_bottom_y, 'salmon')
    
    x_direction = 20
    y_direction = 0
    
    score = 0
    
    score_text = canvas.create_text(10, 10, text="Score: 0", anchor="nw")
    
    game_over_text = None  # Placeholder for game over text
    
    while True:
        key = canvas.get_last_key_press()
        
        if key == 'ArrowLeft':
            x_direction = -20
            y_direction = 0

        if key == 'ArrowRight':
            x_direction = +20
            y_direction = 0
        
        if key == 'ArrowUp':
            x_direction = 0
            y_direction = -20

        if key == 'ArrowDown':
            x_direction = 0
            y_direction = +20
  
        canvas.move(player, x_direction, y_direction)
        time.sleep(DELAY)
    
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        
        if player_x < 0 or player_x >= CANVAS_WIDTH or player_y < 0 or player_y >= CANVAS_HEIGHT:
            if game_over_text is None:
                game_over_text = canvas.create_text(CANVAS_WIDTH // 2,CANVAS_HEIGHT // 2,text="Game Over",anchor="center",color="red")
            break

        if player_x == goal_start_x and player_y == goal_start_y:
            canvas.delete(goal)  # Delete the old goal
            goal_start_x, goal_start_y, goal = move_goal(canvas)  # Create a new goal
            score += 1
            canvas.delete(score_text)  # Remove old text
            score_text = canvas.create_text(10, 10, text=f"Score: {score}", anchor="nw")  # Create new text

def move_goal(canvas):
    goal_start_x = random.randint(0, CANVAS_WIDTH // SIZE - 1) * SIZE
    goal_start_y = random.randint(0, CANVAS_HEIGHT // SIZE - 1) * SIZE
    goal = canvas.create_rectangle(goal_start_x , goal_start_y, goal_start_x + SIZE, goal_start_y + SIZE, 'salmon')
    return goal_start_x, goal_start_y, goal

if __name__ == '__main__':
    main()
