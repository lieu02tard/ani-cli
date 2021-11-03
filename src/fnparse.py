#!/usr/bin/python3
# Parse the `sys.argv` list
# pos is the last returned position

null_p  = {"pos": None, "is_short": None}

def fnparse(argv: list, pos: int):
    argc = len(argv)
    if pos >= argc:
        return null_p
    for i in (pos + 1, argc):
        if argv[i][0] == '-':
            if len(argv[i]) == 1:
                continue
            if argv[i][1] == '-':
                if len(argv[i]) == 2:
                    continue
                return {"pos": i, "is_short": False}
            return {"pos": i, "is_short": True}
        continue

# Sample usage
def sample_main():
    def printhelp():
        print("\
    Sample fnparse program\
              ", file = sys.stderr)
    def fnerr(s: str):
        print(s)
        sys.exit(1)
    if len(sys.argv) == 1:
        print("No argument provided !", file=sys.stderr)
    prev_pos    = 0
    isshort     = False
    fnreturn    = {}
    while True:
        fnreturn = fnparse(sys.argv, prev_pos)
        if fnreturn == null_p:
            break
        curpos  = fnreturn.get("pos")
        if fnreturn.get("is_short") == True:
            for c in sys.argv[curpos][1:]:
                if c == 'h':
                    printhelp()
                    sys.exit(0)
                else:
                    fnerr(f"Unknown argument: '{c}'")
        else:
            if sys.argv[curpos][2:] == "help":
                printhelp()
                sys.exit(0)
            else:
                fnerr(f"Unknown argument: '{sys.argv[curpos][2:]}'")

if __name__ == "__main__":
    import os, sys
    try:
        sample_main()
    except Exception as e:
        print(e)
        sys.exit(1)

