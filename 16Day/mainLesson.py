from turtle import Turtle, Screen

# import another_module
#
# print(another_module.another_variable)

# timmy = Turtle()
# print(timmy.shape("turtle"))
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)
table.clear()
