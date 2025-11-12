import sys

def repl():
    if sys.stdin.isatty():
        try:
            while True:
                try:
                    line = input("> ")
                except EOFError:
                    print("Fin des calculs")
                    return 0
                print(line)
        except KeyboardInterrupt:
            return 130
    else:
        for line in sys.stdin:
            print(line.rstrip("\n"))
        return 0

if __name__ == "__main__":
    sys.exit(repl())
