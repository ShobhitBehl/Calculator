import logging

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    oprnd = "+";
    a = 2
    b = 3
    if oprnd == "+":
        summ = add(a, b)

    oprnd = "-"
    if oprnd == "-":
        diff = sub(a, b)

    logging.basicConfig(filename="logFile.txt",
                filemode='a',
                format='%(asctime)s %(levelname)s-%(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)
    logging.info(summ)