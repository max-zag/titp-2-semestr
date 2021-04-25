from sorts.sorts import SortClass
from analyzer.analyzer import Analyzer

sort = SortClass()

# Bubble sort
sort.bubble_sort()
Analyzer(sort.get_result_list('bubble_sort'))

# Discarded Sort (Linear Sort)
# sort.linear_sort()
