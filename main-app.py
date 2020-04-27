from calculator import Calculator
import decimal
import math

global mem
mem = 0


def getFirstNumber():
    a = input("First Input? ")
    while type(a) == str:
        try:
            a = float(a)
        except ValueError:
            print('Error: Please Enter Valid Number\n')
            a = getFirstNumber()
    return a

def getSecondNumber():
    b = input('Second Input?')
    while type(b) == str:
        try:
            b = float(b)
        except ValueError:
            print('Error: Please Enter Valid Number\n')
            b = getSecondNumber()
    return b


def getTwoNumbers():
    a = getFirstNumber()
    b = getSecondNumber()
    return a, b


def displayResult(x: float):
    print(x, "\n")
    return x


def choose_op():
    print("List of choice")
    print("-" * 50)
    print('1 Add                2 Subtract          3 Multiply              4 Divide')
    print('5 Power              6 Square            7 Square Root           8 Inverse')
    print('9 Sinrad             10 Cosrad           11 Tanrad               12 Cotrad')
    print('13 Sindeg            14 Cosdeg           15 Tandeg               16 Cotdeg')
    print('17 Factorial         18 Log 10           19 10^x                 20 Ln ')
    print('21 e^x               22 Log base         23 Binary               24 Octal')
    print('25 Decimal           26.Hexidecimal      27.Switch Sign          28 Degree' )
    print('29 Radian            30 M+               31 MRC                  32 MC' )
    print(' ')
    # op = int(input('Choose an operation: '))


def performCalcLoop(calc):
    while True:
        choose_op()
        print("press 'q' to quit")
        print('-' * 50)
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.

        elif choice == '1': #'Add'
            a, b = getTwoNumbers()
            x = displayResult(calc.add(a, b))
        elif choice == '2': #'Subtract':
            a, b = getTwoNumbers()
            x = displayResult(calc.subtract(a, b))

        elif choice == '3': #'Multiply'
            a, b = getTwoNumbers()
            x = displayResult(calc.multiply(a, b))

        elif choice == '4': #'Division'
            a, b = getTwoNumbers()
            if b != 0:
                x = displayResult(calc.divide(a, b))
            else:
                print('invalid input')
                performCalcLoop(calc)

        elif choice == '5': #'Power'
            print("1st num: base, 2nd num: Exponent")
            a, b = getTwoNumbers()
            x = displayResult(calc.powerof(a, b))
        elif choice == '6': #'Square'
            a = getFirstNumber()
            x = displayResult(calc.square(a))
        elif choice == '7': #'Square Root'
            a = getFirstNumber()
            x = displayResult(calc.squareroot(a))
        elif choice == '8': #'Inverse'
            a = getFirstNumber()
            x = displayResult(calc.squareroot(a))

        elif choice == '9': #'Sine in radians':
            a = getFirstNumber()
            x = displayResult(calc.sinrad(a))
        elif choice == '10': #'Cosine in radians':
            a = getFirstNumber()
            x = displayResult(calc.cosrad(a))
        elif choice == '11': #'Tangent in radians':
            a = getFirstNumber()
            x = displayResult(calc.tanrad(a))
        elif choice == '12': #'Costangent in radians':
            a = getFirstNumber()
            x = displayResult(calc.cosecrad(a))
        # elif choice == '13': #'Secant in radian':
        #     a = getFirstNumber()
        #     x = displayResult(calc.secrad(a))
        # elif choice == '14': #'Cotangent in radian':
        #     a = getFirstNumber()
        #     x = displayResult(calc.cotrad(a))

        elif choice == '13': #'Sine in degrees':
            a = getFirstNumber()
            x = displayResult(calc.sindeg(a))
        elif choice == '14': #'Cosine in degrees':
            a = getFirstNumber()
            x = displayResult(calc.cosdeg(a))
        elif choice == '15': #'Tangent in degrees':
            a = getFirstNumber()
            x = displayResult(calc.tandeg(a))
        elif choice == '16': #'Cosecant in degrees':
            a = getFirstNumber()
            x = displayResult(calc.cosecdeg(a))
        # elif choice == 'Secant in degrees':
        #     a = getFirstNumber()
        #     x = displayResult(calc.secdeg(a))
        # elif choice == 'Cotangent in degrees':
        #     a = getFirstNumber()
        #     x = displayResult(calc.cotdeg(a))

        elif choice == '17': #'Factorial':
            a = getFirstNumber()
            x = displayResult(calc.factorial(a))
        elif choice == '18': #'Log 10':
            a = getFirstNumber()
            x = displayResult(calc.logten(a))
        elif choice == '19': #'10^x' inverse log
            a = getFirstNumber()
            x = displayResult(calc.inv_logten(a))
        elif choice == '20': #'Natural log':
            a = getFirstNumber()
            x = displayResult(calc.ln(a))
        elif choice == '21': #Inverse Natural log, e^x':
            a = getFirstNumber()
            x = displayResult(calc.inv_ln(a))

        elif choice == '22': #'log base x':
            a, b = getTwoNumbers()
            x = displayResult((calc.log_base_x(a,b)))

        elif choice == '23': #'Binary':
            a = getFirstNumber()
            x = displayResult(bin(int(a)))
            x = a
        elif choice == '24': #Octal':
            a = getFirstNumber()
            x = displayResult(oct(int(a)))
            x = a
        elif choice == '25': #'Decimal':
            a = getFirstNumber()
            x = displayResult(decimal(int(a)))
            x = a
        elif choice == '26': #Hexidecimal':
            a = getFirstNumber()
            x = displayResult(decimal.Decimal(int(a)))
            x = a

        elif choice == '27': #'Switch Sign':
            a = getFirstNumber()
            x = displayResult(calc.switchsign(a))

        elif choice == '28': #'Degree':
            a = getFirstNumber()
            x = displayResult(math.degrees(a))
        elif choice == '29': #Radian':
            a = getFirstNumber()
            x = displayResult(math.radian(a))

        elif choice == '30': #'M+':
            global mem
            mem = x
        elif choice == '31': #'"MRC":
            x = mem
        elif choice == '32': #"MC":
            mem = 0

        else:
            print("That is not a valid input.")
            performCalcLoop(calc)

        performCalcLoop(a)

def performaCalcLoop(calc, a):
    x = a
    while True:
        choose_op()

        print("clear bottom: c")
        print('~' * 50)
        print("Your first number: " + str(a) + "\n")
        choice = input("Which Operation?")

        if choice == 'c':
            break

        elif choice == 'Add':
            b = getSecondNumber()
            x = displayResult(calc.add(a, b))
        elif choice == 'Subtract':
            a, b = getTwoNumbers()
            x = displayResult(calc.subtract(a, b))
        elif choice == 'Multiply':
            b = getSecondNumber()
            x = displayResult(calc.multuply(a, b))
        elif choice == 'Divide':
            b = getSecondNumber()
            if b != 0:
                x = displayResult(calc.divide(a, b))
            else:
                print("Cannot Divide by Zero")
                performCalcLoop(calc, a)

        elif choice == 'Power':
            print("1st num: base, 2nd num: Exponent")
            b = getSecondNumber()
            x = displayResult(calc.powerof(a, b))
        elif choice == 'Square':
            x = displayResult(calc.square(a))
        elif choice == 'Square root':
            a = getFirstNumber()
            x = displayResult(calc.squareroot(a))
        elif choice == 'Inverse':
            x = displayResult(calc.inverse(a))

        elif choice == 'Sine in radians':
            x = displayResult(calc.sinrad(a))
        elif choice == 'Cosine in radians':
            x = displayResult(calc.cosrad(a))
        elif choice == 'Tangent in radians':
            x = displayResult(calc.tanrad(a))
        elif choice == 'Cotangent in radians':
            x = displayResult(calc.cosecrad(a))
        elif choice == 'Secant in radians':
            x = displayResult(calc.secrad(a))
        elif choice == 'Cotangent in radians':
            x = displayResult(calc.cotrad(a))

        elif choice == 'Sine in degrees':
            x = displayResult(calc.sindeg(a))
        elif choice == 'Cosine in degrees':
            x = displayResult(calc.cosdeg(a))
        elif choice == 'Tangent in degrees':
            x = displayResult(calc.tandeg(a))
        elif choice == 'Cosecant in degrees':
            x = displayResult(calc.cosecdeg(a))
        elif choice == 'Secant in degrees':
            x = displayResult(calc.secdeg(a))
        elif choice == 'Cotangent in degrees':
            x = displayResult(calc.cotdeg(a))

        elif choice == 'Factorial':
            x = displayResult(calc.factorial(a))
        elif choice == 'Base 10 log':
            x = displayResult(calc.logten(a))
        elif choice == 'inverse log, 10^x':
            a = getFirstNumber()
            x = displayResult(calc.inv_logten(a))
        elif choice == 'Natural log':
            x = displayResult(calc.ln(a))
        elif choice == 'Inverse Natural log, e^x':
            a = getFirstNumber()
            x = displayResult(calc.inv_ln(a))

        elif choice == 'Log base x':
            print("Second number is log base")
            b = getSecondNumber()
            x = displayResult(calc.logbasex(a, b))

        elif choice == 'Binary':
            x = displayResult(bin(int(a)))
            x = a
        elif choice == 'Octal':
            x = displayResult(oct(int(a)))
            x = a
        elif choice == 'Decimal':
            x = displayResult(decimal.Decimal(a))
            x = a
        elif choice == 'Hexidecimal':
            x = displayResult(hex(int(a)))
            x = a

        elif choice == 'Switch sign':
            x = displayResult(calc.switchsign(a))

        elif choice == 'Degree':
            x = displayResult(math.degrees(a))
        elif choice == 'Radian':
            x = displayResult(math.radians(a))

        elif choice == 'M+':
            global mem
            mem = x
        elif choice == "MC":
            mem = 0
        elif choice == "MRC":
            x = mem

        else:
            print ('Invalid input')

        performCalcLoop(calc, x)


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()