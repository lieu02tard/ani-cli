# nekopv - The CLI anime manager
import os, sys
import subprocess
import json

import gganime

import pref     # Preferences
import fnparse  # Argument parsing
import wharg
    # Note that with the amount of hard code and assets, the program will not run on Windows or will not function correctly

    ##Global settings
ani_verbal  = False
ani_quiet   = False
ani_debug   = False
ani_fatal   = True      # Shutdown program when exception
is_download = False
quality     = "best"
scrape      = "query"

    #Importation
player_fn   = pref.player_fn
prog        = pref.prog

c_red       = pref.c_red
c_green     = pref.c_green
c_yellow    = pref.c_yellow
c_blue      = pref.c_blue
c_magenta   = pref.c_magenta
c_cyan      = pref.c_cyan
c_reset     = pref.c_reset
#
#
greet_string = "Welcome to nekopv !"
ngin = {"gganime": gganime}

    #Error reporter
def prerr(s: str, code:int):
    print(f"{c_red}{s}{c_reset}\n", file  = sys.stderr)
    if code == 0:
        sys.exit(1)
    return

def print_help():
    print("""
nekopv - CLI anime player
Usage: nekoplayer [OPTIONS] [anime]

Options:
-h,             : Print help
--help
-H,             : Request history
--history
-d,             : Download
--download
-q <quality>    : Quality
--quality
-Q, --query     : Query certain anime
    """)
    sys.exit(0)
class nekopvRunning(wharg.argparser):
    async def begin(self):
        return

    async def unknown(self, arg):
        print(f"Argument '{arg}' unexpected!")
        self.printHelp()
        return
    async def printHelp(self):
        printHelp()
        return
    async def usage(s: str):
        self.argStack.append(s)
        return
    async def repop(s: str, is_long:bool):
        if is_long:
            if s == "quality":
                if cmdStack != "play":
                    self.unknown(s)
                    return
                self.expect_arg = True
                self.opStack.append(s)
                return
            if s == "verbal":
                sysstt["verbal"] = True
                sysstt["quiet"] = False
                self.optStack.append(s)
                return
            if s == "quiet":
                sysstt["quiet"] = True
                sysstt["verbal"] = False
                sysstt["debug"] = False
                self.optStack.append(s)
                return
            if s == "debug":
                sysstt["quiet"] = False
                sysstt["debug"] = True
                sysstt["verbal"] = True
                return

        else:
            for c in s:
                if c == "Q": # If a value-request option is read, other following option are set aside
                    if cmdStack != "play":
                        self.unknown(c)
                        return
                    self.expect_arg = True
                    self.optStack.append(s)
                    return
                if c == "v":
                    sysstt["verbal"] = True
                    sysstt["quiet"] = False
                    self.optStack.append(c)
                    continue
                if c == "q":
                    sysstt["quiet"] = True
                    sysstt["verbal"] = False
                    self.optStack.append(c)
                    continue
                if c == "g":
                    sysstt["debug"] = True
                    sysstt["quiet"] = False
                    sysstt["verbal"] = True
                    return

    async def exe(self):
        if commandARG == "save":
            #[FIXME]
            return
        if commandARG = "play":
            #[FIXME]
            return
        if commandARG = "save":
            #[FIXME]
            return
        if commandARG == "export":
            #[FIXME]
            return
        if commandARG == "import":
            #[FIXME]
            return
        if commandARG == "help":
            self.printHelp()
            return
        if commandARG == "manual":
            print_manual()
            return
        if commandARG == "plman":
            #[FIXME]
            return

##### Start-up ######
def main():

    import fnparse

    sysstt = {"scrape": "", "is_download": False, "quality": "best", "anime_quest": ""}
    ## Parsing argument
    prev_pos    = 0
    fnreturn    = {}

    while True:
        argc = len(sys.argv)
        if argc == 1:
            break
        fnreturn = fnparse.fnparse(sys.argv, prev_pos)
        if fnreturn == fnparse.null_p:
            break
        prev_pos = fnreturn.get("pos")
        curpos  = prev_pos
        if fnreturn.get("is_short") == True:
            for c in sys.argv[curpos][1:]:
                if c == '-h':
                    print_help()
                if c == 'd':
                    sysstt["is_download"]
                if c == 'H':
                    sysstt["scrape"] = "history"
                if c == 'q':
                    if curpos >= argc - 1:
                        prerr("Expected argument unprovided", 0)
                        sys.exit(1)
                    sysstt["quality"] = sys.argv[curpos + 1]
                    #if not valid_vidqual(vidqual):
                    #    fnerr(f"Argument ''{vidqual}' invalid")
                    #    sys.exit(1)
                    prev_pos += 1
                    break
                #Default case
                prerr("Argument '{c}' unexpected", 0)
                sys.exit(0)
                break
        else:
            s = sys.argv[curpos][2:]
            if s == "help":
                print_help()
                sys.exit(0)

            if s == "download":
                #if curpos >= argc - 1:
                #    fnerr("Expected argument unprovided")
                #    sys.exit(1)
                #download_ep = sys.argv[curpos + 1]
                #prev_pos += 1
                sysstt["is_download"] = True

            if s == "recent":
                sysstt["scrape"] = "query"
            if s == "quality":
                if curpos >= argc - 1:
                    prerr("Expected argument unprovided", 0)
                    sys.exit(1)
                sysstt["quality"] = sys.argv[curpos + 1]
                #if not valid_vidqual(vidqual):
                #    prerr(f"Argument '{vidqual}' invalid", 0)
                #    sys.exit(1)
                prev_pos += 1
            if s == "quality=":
                sysstt["quality"] =sys.argv[curpos + 1][9:]


            ##Default
            prerr(f"Argument '{s}' unexpected", 0)
            sys.exit(1)
            break

    #Main program
    wharg.argparser main_argparser(greetString = f"Welcome to {program_name} {program_version}", opa)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        #if ani_verbal or ani_debug:
        #    print(e)
        raise e
        if ani_fatal:
            sys.exit(1)
