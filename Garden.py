from generate_garden import generate_garden

class Garden:

  def __init__(self, cols, rows):
    self.day = 0
    self.garden_plots = generate_garden(cols ,rows, 20)
    self.grid = ""
    self.rows = rows
    self.cols = cols

  def nextDay(self):
    self.day += 1
    for plot in self.garden_plots:
      plot.grow(self.day)
    
  def generate_grid(self):
    grid = ""
    for i in range(len(self.garden_plots)):
      grid += self.garden_plots[i].state + " "
      if(i % self.cols == self.cols - 1):
        grid += "\n"
    self.grid = grid
  
  def print_grid(self):
    self.generate_grid()
    print(self.grid)

  def validate_end(self):
    if self.day > 0:
      for plot in self.garden_plots:
        if plot.state != "🟫":
          return False
      return True
    else:
      return False

  def render(self):
    self.generate_grid()
    return self.grid

if __name__ == "__main__":
  new_garden = Garden(5, 5)

  while new_garden.validate_end() == False:
    new_garden.print_grid()
    new_garden.nextDay()

  new_garden.print_grid()