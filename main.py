
print('Starting program...')
raw_list = [25, 43, 79, 160, 362, 909, 245725, 43, 79, 160, 362, 909, 2457]
print(f'Raw list - {raw_list} \n')

# Bubble sort
print('Bubble sort')
bubble_list = raw_list.copy()
iterations_count = 0
for i in range(0, len(bubble_list) - 1):
    for j in range(1, len(bubble_list) - i -1):
        if bubble_list[j] > bubble_list[j + 1]:
            bubble_list[j], bubble_list[j + 1] = bubble_list[j + 1], bubble_list[j]
            iterations_count += 1
print('Bubble sort finished!', f'Result - {bubble_list}', f'Number of iterations - {iterations_count}', sep='\n', end='\n\n')

# Discarded Sort (Linear Sort)
print('Linear Sort')
linear_list = raw_list.copy()
iterations_count = 0
for i in range(len(linear_list) - 1):
    for j in range(i + 1, len(linear_list)):
        if linear_list[j] < linear_list[i]:
            linear_list[i], linear_list[j] = linear_list[j], linear_list[i]
            iterations_count += 1
print('Linear Sort finished!', f'Result - {linear_list}', f'Number of iterations - {iterations_count}', sep='\n', end='\n\n')

print('Program finished!')
