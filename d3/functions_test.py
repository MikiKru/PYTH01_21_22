from d3.functions import *
# ALT + Enter -> auto-import

hello()
hello()
hello()

hello_me("Michał")
hello_me("Adam")

print(division(1, 3))
result = division(4, 0)
print(result)

print(get_normalized_random())
print(get_normalized_random())
print(get_normalized_random())

print(get_unique_value_upper_tresh([4,3,2,4,5,3,2,1], treshold=4))
print(get_unique_value_upper_tresh([4,-3,2,-4,5,3,2,1]))

print(get_avg_from_grades(3, 5, 4))
print(get_avg_from_grades(5, 5, 5, 5, 5))
print(get_avg_from_grades(3, 3))

print(get_avg_from_grades_named(grade1=3, grade2=5, grade3=4))
print(get_avg_from_grades_named(g1=3, g2=5, g3=4))