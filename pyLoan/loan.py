
# what we need? detials: money owed, annual % rate, montly payment, how many months for result?

money_owed = float(input('How much money do you owe, in dollars?\n')) # 50k
apr = float(input('what is the annual persentage rate of the loan, in percentage?\n')) # 3
payment = float(input('How much will you pay off each month, in dollars?\n')) # 1k
months = int(input('How many months do you want to see the results for?\n')) # 24

montyly_rate = apr/100/12

# added as 2nd ->before this line it only calculated for 1 month
for i in range(months):


    # calculate interest to pay
    interest_paid = money_owed*montyly_rate

    # add in interest
    money_owed = money_owed + interest_paid

    # added as 3rd
    if (money_owed - payment) < 0:
        print('the last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break

    # make payment
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    print('Now I owe', money_owed)