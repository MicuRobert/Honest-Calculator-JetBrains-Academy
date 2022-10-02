# write your code here
import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'], type=str)
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

stop = False
if len(sys.argv) < 5:
    stop = True
for k in vars(args):
    if type(vars(args)[k]) == float and vars(args)[k] < 0:
        stop = True
        
if stop == False:
    if args.type == 'diff':
        nominal_interest = args.interest / (12 * 100)
        total_pay = 0
        for x in range(int(args.periods)):
            repayment = math.ceil(args.principal / args.periods + nominal_interest * (args.principal - args.principal * (x) / args.periods))
            total_pay += repayment
            print(f'Month {x+1}: payment is {repayment}')
        print(f'Overpayment = {total_pay - args.principal}')
    elif args.type == 'annuity': 
        if args.periods == None:
            principal = args.principal
            monthly_pay = args.payment
            interest = args.interest
            nominal_interest = interest / (12 * 100)
            months = math.ceil(math.log(monthly_pay / (monthly_pay - nominal_interest * principal) , 1 + nominal_interest))
            months_remained = months % 12
            years = (months - months_remained) / 12
            total_pay = months * monthly_pay
            if years < 1:
                print(f'It will take {months_remained} months to repay this loan!')
                print(f'Overpayment = {total_pay - principal}')
            else:
                print(f'It will take {years} years and {months_remained} months to repay this loan!')
                print(f'Overpayment = {total_pay - principal}')
        elif args.payment == None:
            principal = args.principal
            period = args.periods
            interest = args.interest
            nominal_interest = interest / (12 * 100)
            payment = math.ceil(principal * (nominal_interest * math.pow(1 + nominal_interest, period)) / (math.pow(1 + nominal_interest, period) - 1))
            total_pay = period * payment
            print(payment)
            print(f'Overpayment = {total_pay - principal}')
        elif args.principal == None:
            annuity = args.payment
            period = args.periods
            interest = args.interest
            nominal_interest = interest / (12 * 100)
            print(annuity / ((nominal_interest * math.pow(1 + nominal_interest, period)) / (math.pow(1 + nominal_interest, period) - 1)))
    else:
        print('Incorrect parameters.')
elif stop == True:
    print('Incorrect parameters.')
