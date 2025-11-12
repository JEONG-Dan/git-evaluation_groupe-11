import sys, re

EXPR = re.compile(r'^\s*(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)\s*$')

def eval_expr(line: str):
    m = EXPR.match(line)
    if not m:
        return None, "Erreur: syntaxe invalide"
    a_s, op, b_s = m.groups()
    a = float(a_s); b = float(b_s)
    if op == '/' and b == 0.0:
        return None, "Erreur: division par zéro"
    res = {'+': a+b, '-': a-b, '*': a*b, '/': a/b}[op]
    if res.is_integer():
        return str(int(res)), None
    s = f"{res:.10f}".rstrip('0').rstrip('.')
    return s, None

def main():
    if sys.stdin.isatty():
        try:
            while True:
                try:
                    line = input("> ")
                except EOFError:
                    print("Fin des calculs")
                    return 0
                out, err = eval_expr(line)
                print(out if err is None else err)
        except KeyboardInterrupt:
            return 130
    else:
        for raw in sys.stdin:
            line = raw.rstrip('\r\n')
            if not line:
                print("Erreur: syntaxe invalide")
                continue
            out, err = eval_expr(line)
            print(out if err is None else err)
        return 0

if __name__ == "__main__":
    sys.exit(main())
