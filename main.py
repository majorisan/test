def calculate(expression):
    try:
        operands=expression.split()
        if len(operands) !=3:
            raise ValueError("Неправильный формат выражения")
        num1=int(operands[0])
        operator=operands[1]
        num2=int(operands[2])
        if num1 < 1 or num1 > 10 or num2 < 1 or num2 > 10:
            raise ValueError("число должно быть от 1 до 10")
        if operator not in ["+","-",":","/"]:
            raise ValueError("не верная операция")
        elif operator =="+":
            result=num1+num2
        elif operator =="-":
            result=num1 - num2
        elif operator =="*":
            result=num1 * num2
        elif operator =="/":
            result=num1//num2
        return result
    except ValueError as e:
        return str(e)

def main():
    user_input=input("введите выражение:")
    print(calculate(user_input))
if __name__== "__main__":
    main()