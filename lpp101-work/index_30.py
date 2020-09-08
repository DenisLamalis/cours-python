# conditionals - exercise improve

def num_days(month):

    months_31 = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
    months_30 = ['apr', 'jun', 'sep', 'nov']
    months_28 = ['feb']

    if month in months_31:
        print('number of days in',month,'is',31)
    elif month in months_30:
        print('number of days in',month,'is',30)
    elif month in months_28:
        print('number of days in',month,'is',28)

    # if month == 'jan':
    #     print('number of days in',month,'is',31)
    # elif month == 'feb':
    #     print('number of days in',month,'is',28)
    # elif month == 'mar':
    #     print('number of days in',month,'is',31)
    # elif month == 'apr':
    #     print('number of days in',month,'is',30)
    # elif month == 'may':
    #     print('number of days in',month,'is',31)
    # elif month == 'jun':
    #     print('number of days in',month,'is',30)
    # elif month == 'jul':
    #     print('number of days in',month,'is',31)
    # elif month == 'aug':
    #     print('number of days in',month,'is',31)
    # elif month == 'sep':
    #     print('number of days in',month,'is',30)
    # elif month == 'oct':
    #     print('number of days in',month,'is',31)
    # elif month == 'nov':
    #     print('number of days in',month,'is',30)
    # elif month == 'dec':
    #     print('number of days in',month,'is',31)

num_days('nov')

# optimize/shorten the code in the function
# try to reduce the number of conditionals 


# Solution

# def num_days(month):

#     if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
#         print('number of days in',month,'is',31)
#     elif month == 'feb':
#         print('number of days in',month,'is',28)
#     elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
#         print('number of days in',month,'is',30)

# num_days('jul')


# def num_days(month):

#     if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
#         print('number of days in',month,'is',31)
#     elif month == 'feb':
#         print('number of days in',month,'is',28)
#     else:
#         print('number of days in',month,'is',30)

# num_days('jul')


# def num_days(month):
#     days = 31
#     if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
#         days = 30
#     elif month == 'feb':
#         days = 28
#     print('number of days in',month,'is',days)

# num_days('jul')


# def num_days(month):
#     days = 31
#     if month in {'apr','jun','sep','nov'}:
#     #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
#         days = 30
#     elif month == 'feb':
#         days = 28
#     print('number of days in',month,'is',days)
    

# num_days('jan')