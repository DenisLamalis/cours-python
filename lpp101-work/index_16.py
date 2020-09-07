# Lists - exercise

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

# Input

day_7 = input('What is the last number ? ')
sales_w2.append(int(day_7))

# create a unique list

sales = sales_w1.copy() + sales_w2.copy()

# Calculation

best_day_w1 = max(sales_w1)
best_day_w2 = max(sales_w2)
best_day_total = max(sales)

index_best_day_w1 = sales_w1.index(int(best_day_w1)) + 1
index_best_day_w2 = sales_w2.index(int(best_day_w2)) + 1

worst_day_w1 = min(sales_w1)
worst_day_w2 = min(sales_w2)
worst_day_total = min(sales)

index_worst_day_w1 = sales_w1.index(int(worst_day_w1)) + 1
index_worst_day_w2 = sales_w2.index(int(worst_day_w2)) + 1

# Print

print(f'The best day of week 1 : the day {index_best_day_w1} with {best_day_w1*1.5}$')
print(f'The best day of week 2 : the day {index_best_day_w2} with {best_day_w2*1.5}$')
print(f'The best day of the 2 weeks : {best_day_total*1.5}$')

print(f'The worst day of week 1 : the day {index_worst_day_w1} with {worst_day_w1*1.5}$')
print(f'The worst day of week 2 : the day {index_worst_day_w2} with {worst_day_w2*1.5}$')
print(f'The worst day of the 2 weeks : {worst_day_total*1.5}$')

# Solution

# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2.append(int(new_day))
# #sales.extend(sales_w1)
# #sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
# sales.sort()
# worst_day_prof = sales[0] * 1.5
# best_day_prof = sales[-1] * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2.append(int(new_day))
# #sales.extend(sales_w1)
# #sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
# #sales.sort()
# worst_day_prof = min(sales) * 1.5
# best_day_prof = max(sales) * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')


