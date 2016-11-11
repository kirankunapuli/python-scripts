var = 1
while var == 1:

    bs = float(input('Enter basic salary: '))
    print('Entered basic salary is Rs.', bs)

    # when basic is less than 2500
    if (bs < 2500):
        hra = bs * 0.1
        da = bs * 0.9
        gs = bs + hra + da

    # when basic is greater than 2500
    else:
        hra = 500
        da = bs * 0.98
        gs = bs + hra + da
    print('Gross Salary is Rs.', gs)
