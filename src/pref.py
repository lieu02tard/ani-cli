# Preferences file for ani-cli.py

player_fn   = "mpv"     #Any media player capable of playing URLs
prog        = "ani-cli"

#Color code
c_red       = "\033[1;31m]"
c_green     = "\033[1;32m]"
c_yellow    = "\033[1;33m]"
c_blue      = "\033[1;34m]"
c_magenta   = "\033[1;35m]"
c_cyan      = "\033[1;36m]"
c_reset     = "\033[0m"

def print_help():
    import sys
    print(
f"USAGE: ${prog} <query>\
    -h:     show this help text\
    -d:     download episode\
    -H:     continue where you left of\
    -q:     set video quality (best/worst/360/480/720", file = sys.stderr)
    return

