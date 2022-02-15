import random
from termcolor import colored
from noise import pnoise2
from Plot import Plot

def generate_garden(cols=16, rows=16, noise=100):
  seed = random.randint(0, 100)
  land = []

  for row in range(rows):

    for col in range(cols):
      n = pnoise2(row / rows, col / cols, base=seed, octaves=5)
      n *= noise
      n = round(n)
      n = n % len(Plot.plants)
      land.append(Plot(n))

  print("finished generating landscape")
  return land

def ask_for_number(question):
  tries = 0
  while tries < 3:
    answer = input(colored(question, "green"))

    if answer == "quit":
      quit()
    if answer.isnumeric():
      return int(answer)
    else:
      tries += 1
      print(colored("this doesn't make sense", "yellow"))
  print(colored("sorry please try again", "red"),)
  quit()


if __name__ == "__main__":
  rows = ask_for_number("how many rows? ")
  cols = ask_for_number("how many columns? ")

  garden = generate_garden(cols, rows)
  grid = ""
  for i in range(len(garden)):
    grid += garden[i].state + " "
    if(i % cols == cols - 1):
      grid += "\n"
  print(grid)