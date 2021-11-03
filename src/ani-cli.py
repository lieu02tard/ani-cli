# nekopv - The anime pre
import os, sys
import subprocess
import json

import gganime

import pref     # Preferences
import fnparse  # Argument parsing

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
ngin = {"gganime": gganime}

    #Error reporter
def prerr(s: str, code:int):
    print(f"{c_red}{s}{c_reset}\n", file  = sys.stderr)
    if code == 0:
        sys.exit(1)
    return

def print_help():
    print("\
nekopv - CLI anime player\
Usage: nekoplayer [OPTIONS] [anime]\
\
Options:\
-h,             : Print help\
--help\
-H,             : Request history\
--history\
-d,             : Download\
--download\
-q <quality>    : Quality\
--quality\
-Q, --query     : Query certain anime\
    ")
    sys.exit(0)

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
    terminate = False
    while not terminate:
        if sysstt["anime_quest"] == "" or sysstt["anime_quest"] == None:
            # Quest anime name
            print(f"{c_blue}Search anime{c_reset}: ", end='')
            sysstt["anime_quest"] = input()
        main_ngin = ngin["gganime"]
        search_results = main_ngin.search_anime(sysstt["anime_quest"])
        if search_results == None:
            print("No search results found, continue (Y/N): ")
            inp = input().lower()
            if inp == "y":
                continue
            else:
                break
        
        #Anime selection section
        count = 0
        for animeid in search_results:
            print(f"[{c_blue}{count}{c_reset}]{c_magenta}{animeid}{c_reset}") if count % 2 == 0 else print(f"[{c_blue}{count}{c_reset}]{c_yellow}{animeid}{c_reset}")
            count += 1
        print(f"{c_blue}Select anime [0-{len(search_results) - 1}]: ", end='')
        epno = main_ngin.search_eps(sysstt["anime_quest"])
        print(f"{c_blue}Choose episode {c_cyan}[1-{epno}]{c_reset}: {c_green}")
        choices = input().split()
        if len(choices) >= 2 or len(choices) == 0:
            prerr("Maloformed input", 0)
        if len(choices) == 1:
            try:
                ep_choice_start = ep_choice_end = int(choices[0])
            except Exception as e:
                raise e
        else:
            try:
                ep_choice_start  = int(choices[0])
                ep_choice_end   = int(choices[1])
            except Exception as e:
                raise e

        for i in range(ep_choice_start, ep_choice_end + 1):
            main_ngin.open_episode(sysstt["anime_quest"], i, sysstt["is_download"], sysstt["quality"])




if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        #if ani_verbal or ani_debug:
        #    print(e)
        raise e
        if ani_fatal:
            sys.exit(1)
