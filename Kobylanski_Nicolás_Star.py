import turtle
import random

def main():
    # Input del usuario (número de puntas)
    try:
        points = int(input("Enter the number of points of the star (> 5 and odd number): "))
    except ValueError:
        print("Please enter a valid input.")
        return
    
    turtle.setup(600, 600)      # Tamaño ventana
    turtle.bgcolor("white")     # Color fondo
    turtle.speed(4)             # Velocidad lápiz
    turtle.shape("turtle")      # Icono lápiz
    
    turtle.pensize(4)           # Tamaño lápiz

    # Establece la posición del lápiz
    turtle.penup()
    turtle.goto(-200, 60)
    turtle.pendown()

    # Dibujo de la estrella
    for _ in range(points):
        turtle.pencolor(random.random(), random.random(), random.random())  # Color aleatorio
        turtle.forward(400)             # Longitud de línea
        angle = 180 - (180 / points)    # Cálculo del ángulo
        turtle.right(angle)             # Giro lápiz

    turtle.mainloop()               

if __name__ == "__main__":  # LLamo función
    main()
