from calculator import Calculator
import decimal
import math

global mem


def getFirstNumber():
    a = input("first Number? ")
    while type(a) == str:
        try:
            a = float(a)
        except ValueError:
            print('Error: Please Enter Valid Number\n')
            a = getFirstNumber()
    return a

def getSecondNumber():
    b = input('Second Number?')
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


def choose_op():
    print("List of choice")
    print("-" * 50)
    print('1 Addition           2 Subtraction       3 Multiplication        4 Division')
    print('5 Power              6 Square            7 Square Root           8 Inverse')
    print('9 Sin                10 Cos              11 Tan                  12 cot')
    print('13 invSin            14 invCos           15 invTan               16 Factorial')
    print('17 Factorial         18 Log 10           19 10^x                 20 Ln ')
    print('21 e^x               22 Log base         23 Binary               24 Octal')
    print('25 Decimal           26.Hexidecimal      27.Switch Sign          28 Degree' )
    print('30 Radian            31 M+               31 MRC                  32 MC' )
    print('35. Exit')
    print(' ')
    op = int(input('Choose an operation: '))


def performCalcLoop(calc):
    while True:
        choose_op()
        print("press 'q' to quit")
        print('-' * 50)
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.

        elif choice == 'Add':
            a, b = getTwoNumbers()
            x = displayResult(calc.add(a, b))
        elif choice == 'Subtract':
            a, b = getTwoNumbers()
            x = displayResult(calc.sub(a, b))

        elif choice == 'Multiply':
            a, b = getTwoNumbers()
            x = displayResult(calc.mul(a, b))

        elif choice == 'Division':
            a, b = getTwoNumbers()
            if b != 0:
                x = displayResult(calc.div(a, b))
            else:
                print('invalid input')
                performCalcLoop(calc)

        elif choice == 'Exponent':
            print("1st num: base, 2nd num: Exponent")
            a, b = getTwoNumbers()
            x = displayResult(calc.powerof(a, b))
        elif choice == 'Square':
            a = getFirstNumber()
            x = displayResult(calc.square(a))
        elif choice == 'Square Root':
            a = getFirstNumber()
            x = displayResult(calc.squareroot(a))
        elif choice == 'Inverse':
            a = getFirstNumber()
            x = displayResult(calc.squareroot(a))

        elif choice == 'Sine in radians':
            a = getFirstNumber()
            x = displayResult(calc.sinrad(a))
        elif choice == 'Cosine in radians':
            a = getFirstNumber()
            x = displayResult(calc.cosrad(a))
        elif choice == 'Tangent in radians':
            a = getFirstNumber()
            x = displayResult(calc.tanrad(a))
        elif choice == 'Costangent in radians':
            a = getFirstNumber()
            x = displayResult(calc.cosecrad(a))
        elif choice == 'Secant in radian':
            a = getFirstNumber()
            x = displayResult(calc.secrad(a))
        elif choice == 'Cotangent in radian':
            a = getFirstNumber()
            x = displayResult(calc.cotrad(a))


        elif choice == 'Sine in degrees':
            a = getFirstNumber()
            x = displayResult(calc.sindeg(a))
        elif choice == 'Cosine in degrees':
            a = getFirstNumber()
            x = displayResult(calc.cosdeg(a))
        elif choice == 'Tangent in degrees':
            a = getFirstNumber()
            x = displayResult(calc.tandeg(a))
        elif choice == 'Cosecant in degrees':
            a = getFirstNumber()
            x = displayResult(calc.cosecdeg(a))
        elif choice == 'Secant in degrees':
            a = getFirstNumber()
            x = displayResult(calc.secdeg(a))
        elif choice == 'Cotangent in degrees':
            a = getFirstNumber()
            x = displayResult(calc.cotdeg(a))

        elif choice == 'Factorial':
            a = getFirstNumber()
            x = displayResult(calc.factorial(a))
        elif choice == 'Base 10 log':
            a = getFirstNumber()
            x = displayResult(calc.logten(a))
        elif choice == 'inverse log, 10^x':
            a = getFirstNumber()
            x = displayResult(calc.inv_logten(a))
        elif choice == 'Natural log':
            a = getFirstNumber()
            x = displayResult(calc.ln(a))
        elif choice == 'Inverse Natural log, e^x':
            a = getFirstNumber()
            x = displayResult(calc.inv_ln(a))

        elif choice == 'log base x':
            a, b = getTwoNumbers()
            x = displayResult((calc.log_base_x(a,b)))

        elif choice == 'Binary':
            a = getFirstNumber()
            x = displayResult(bin(int(a)))
            x = a
        elif choice == 'Octal':
            a = getFirstNumber()
            x = displayResult(oct(int(a)))
            x = a
        elif choice == 'decimal':
            a = getFirstNumber()
            x = displayResult(decimal(int(a)))
            x = a
        elif choice == 'Hexidecimal':
            a = getFirstNumber()
            x = displayResult(decimal.Decimal(int(a)))
            x = a

        elif choice == 'Switch Sign':
            a = getFirstNumber()
            x = displayResult(calc.switchsign(a))

        elif choice == 'Degree':
            a = getFirstNumber()
            x = displayResult(math.degrees(a))
        elif choice == 'Radian':
            a = getFirstNumber()
            x = displayResult(math.radian(a))

        elif choice == 'M+':
            global mem
            mem = x
        elif choice == "MRC":
            x = mem
        elif choice == "MC":
            mem = 0

        else:
            print("That is not a valid input.")
            performCalcLoop(calc)

        performCalcLoop(calc, a)

def performaCalcLoop(calc, a):
    x =a
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
            x = displayResult(calc.sub(a, b))
        elif choice == 'Multiply':
            b = getSecondNumber()
            x = displayResult(calc.mul(a, b))
        elif choice == 'Division':
            b = getSecondNumber()
            if b != 0:
                x = displayResult(calc.div(a, b))
            else:
                print("Cannot Divide by Zero")
                performCalcLoop(calc, a)

        elif choice == 'Exponent':
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