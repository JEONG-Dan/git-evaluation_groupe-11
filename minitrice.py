import sys

def repl():
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

if __name__ == "__main__":
    sys.exit(repl())
