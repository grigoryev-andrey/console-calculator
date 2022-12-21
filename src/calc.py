def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a // b


def main():
    x = int(input())
    op = input()
    y = int(input())
    if op == "+":
        print(add(x, y))
    elif op == "-":
        print(sub(x, y))
    elif op == "*":
        print(mul(x, y))
    elif op == "/":
        if y != 0:
            print(div(x, y))
        else:
            print("Error")
    else:
        print("Error")


if __name__ == "__main__":
    main()
