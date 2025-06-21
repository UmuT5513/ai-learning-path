import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', type=float)
parser.add_argument('-b', type=float)
parser.add_argument('-op', choices=['+', '-', '*', '/'])


args = parser.parse_args()

a = args.a
b = args.b
operator = args.op

match operator:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '/':
        try:
            print(a/b)
        except ZeroDivisionError:
            import logging
            logging.basicConfig(level=logging.DEBUG,
                                format="{asctime} - {levelname} - {name} - {message}", 
                                style="{", 
                                filename="calc.log",
                                filemode='a',
                                encoding='utf-8',
                                datefmt='%Y-%m-%d %H:%M:%S',
                                )
            logging.error('bölünen 0 olamaz', exc_info=True)
    case '*':
        print(a/b)


