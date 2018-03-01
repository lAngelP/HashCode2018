import csv

MODE = "a_example"

with open('data/'+MODE+'.in') as f:
    input_reader = csv.reader(f, delimiter=' ')
    (ROWS, COLUMNS, VH, RIDES, BONUS, STEPS) = (int(x) for x in next(input_reader))
    rides = [[int(element) for element in line] for line in input_reader]

print(ROWS, COLUMNS, VH, RIDES, BONUS, STEPS)
print(rides)
