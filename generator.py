import random

OPS = ['+', '-', '*', '/']

def random_number():
    if random.random() < 0.7:
        return str(random.randint(0, 100))
    else:
        return f"{random.randint(0,100)}.{random.randint(0,99)}"

def random_expr():
    a = random_number()
    b = random_number()
    op = random.choice(OPS)
    if op == '/' and float(b) == 0.0:
        b = '1'
    return f"{a}{op}{b}"

def main():
    for _ in range(100):
        print(random_expr())

if __name__ == "__main__":
    main()
