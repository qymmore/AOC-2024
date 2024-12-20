with open('input.txt', 'r') as file:
    lines = file.readlines()
    
# initialize lists
list_1 = []
list_2 = []

for line in lines:
    values = line.strip().split()
    if len(values) == 2:
        list_1.append(int(values[0]))
        list_2.append(int(values[1]))

list_1.sort()
list_2.sort()

list_sums = [abs(a - b) for a,b in zip(list_1, list_2)]
total_sums = sum(list_sums)

print("Total sum of differences: ", total_sums)