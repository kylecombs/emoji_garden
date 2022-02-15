import os
from Garden import Garden

os.makedirs("outputs", exist_ok=True)

new_garden = Garden(5, 5)

i = 0

while new_garden.validate_end() == False:
  output = new_garden.render()
  filename = os.path.join("outputs", f"test-{i}.text")

  with open(filename, "w") as f:
    f.write(output)

  new_garden.nextDay()
  i += 1

# final output file
new_garden.nextDay()
final_output = new_garden.render()
filename = os.path.join("outputs", f"test-{i + 1}.text")
with open(filename, "w") as f:
    f.write(final_output)