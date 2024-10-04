import turtle

def draw_segment(t, line_length, recursion_level):
    if recursion_level == 0:
        t.forward(line_length)
    else:
        line_length /= 3.0
        draw_segment(t, line_length, recursion_level - 1)
        t.left(60)
        draw_segment(t, line_length, recursion_level - 1)
        t.right(120)
        draw_segment(t, line_length, recursion_level - 1)
        t.left(60)
        draw_segment(t, line_length, recursion_level - 1)

def draw_snowflake(t, line_length, recursion_level):
    for _ in range(3):
        draw_segment(t, line_length, recursion_level)
        t.right(120)

def main():
    level = int(input("Введіть рівень рекурсії (0-5): "))
    
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0) 
    t.penup()
    t.goto(-150, 100) 
    t.pendown()
    
    length = 200

    draw_snowflake(t, length, level)

    window.mainloop()

if __name__ == "__main__":
    main()
