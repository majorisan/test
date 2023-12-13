a=input("введите выражение")

def calculate(expression):
    try:
        resulut=eval(expression)
        return resulut
    except Exception :
        return "впишите число!"

print(calculate(a))





