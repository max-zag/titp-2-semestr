from random import randint


class SortClass:
    arrays_size = []
    # arrays_size = [25, 79, 160, 245, 362, 725, 909, 2457]
    results = {}

    def __init__(self, arrays_size):
        self.arrays_size = arrays_size
        print('Starting program...')

    def arrays_generator(self):
        raw_array = []
        for i in range(len(self.arrays_size)):
            raw_array.append([randint(1, 99999) for _ in range(self.arrays_size[i])])
        return raw_array

    def sort_init(self, sort_name):
        self.results[sort_name] = {}
        self.results[sort_name]['raw_arrays'] = self.arrays_generator()
        self.results[sort_name]['iterations_count'] = []
        self.results[sort_name]['comparison_count'] = []
        self.results[sort_name]['name'] = sort_name

    def bubble_sort(self):
        print('Bubble sort')
        sort_name = 'bubble_sort'
        self.sort_init(sort_name)

        for sort_cycle in range(len(self.results[sort_name]['raw_arrays'])):
            bubble_list = self.results[sort_name]['raw_arrays'][sort_cycle]
            print(f'Array - {sort_cycle + 1}. Len - {len(bubble_list)}')
            transposition_count = 0
            comparison_count = 0

            def swap(i, j):
                bubble_list[i], bubble_list[j] = bubble_list[j], bubble_list[i]

            n = len(bubble_list)
            swapped = True
            x = -1
            while swapped:
                swapped = False
                x = x + 1
                for i in range(1, n - x):
                    comparison_count += 1
                    if bubble_list[i - 1] > bubble_list[i]:
                        swap(i - 1, i)
                        transposition_count += 1
                        swapped = True
            print(f'Result - {bubble_list}', f'Number of transposition - {transposition_count}',
                  f'Number of comparison - {comparison_count}', sep='\n', end='\n\n')

    def linear_sort(self):
        print('Linear Sort')
        sort_name = 'linear_sort'
        self.sort_init(sort_name)

        for sort_cycle in range(len(self.results[sort_name]['raw_arrays'])):
            linear_list = self.results[sort_name]['raw_arrays'][sort_cycle]
            print(f'Array - {sort_cycle + 1}. Len - {len(linear_list)}')
            transposition_count = 0
            comparison_count = 0

            for i in range(len(linear_list)):
                minimum = i
                for j in range(i + 1, len(linear_list)):
                    comparison_count += 1
                    if linear_list[j] < linear_list[minimum]:
                        minimum = j

                transposition_count += 1
                linear_list[minimum], linear_list[i] = linear_list[i], linear_list[minimum]

            print(f'Result - {linear_list}', f'Number of transposition - {transposition_count}',
                  f'Number of comparison - {comparison_count}', sep='\n', end='\n\n')

    def get_result_list(self, sort_name):
        try:
            return self.results[sort_name]
        except KeyError:
            print(f"{sort_name} doesn't exist!")
