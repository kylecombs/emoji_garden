import random


class Plot:

  dirt = "🟫"
  seedling = "🌱"
  plants = ["🌿", "🌿", "🌿", "🌾", "🌷", "🌹", "🌺", "🌸", "🌼", "🌻"]
  wilted = ["🥀", "🍂"]

  def __init__(self, plant_num):
    self.state = self.dirt
    self.plant = self.plants[plant_num]
    self.day_to_germ = random.randint(1, 7)
    self.day_to_mature = self.day_to_germ + random.randint(1, 3)
    self.day_to_wilt = self.day_to_mature + random.randint(7, 10)
    self.day_to_decomp = self.day_to_wilt + random.randint(1, 3)
  def grow(self, day):
    if(day == self.day_to_germ):
      self.state = self.seedling
    elif(day == self.day_to_mature):
      self.state = self.plant
    elif(day == self.day_to_wilt):
      if self.state == self.plants[0] or self.state == self.plants[1] or self.state == self.plants[2] or self.state == self.plants[3]:
        self.state = self.wilted[1]
      else:
        self.state = self.wilted[0]
    elif(day == self.day_to_decomp):
      self.state = self.dirt
