import logging

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__ == "__main__":
    oprnd = "+";
    a = 5
    b = 3
    if oprnd == "+":
        summ = add(a, b)
        print(summ)

    oprnd = "-"
    if oprnd == "-":
        diff = sub(a, b)
        print(diff)

    oprnd = "*"
    if oprnd == "*":
        prod = mul(a, b)
        print(prod)

    oprnd = "/"
    if oprnd == "/":
        q = div(a, b)
        print(q)

    logging.basicConfig(filename="logFile.txt",
                filemode='a',
                format='%(asctime)s %(levelname)s-%(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)
    logging.info(summ)
    logging.info(diff)
    logging.info(prod)
    logging.info(q)