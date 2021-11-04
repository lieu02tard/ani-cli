# fwharg - Improved wharg.py
import sys
import asyncio
class argparser:
    # commandARG must be a dict with properly format:
    # {bool is_singular, str opt}
    # Command line interface
    # search <anime_name>   : Search for anime
    # play <anime_name>     : Play anime
        [episode]
    # save [anime_name]     : Save anime to playlist
    # export [address]      : Export playlist
    # import [address]      : Import playlist
    # help                  : Print quick manual
    # manual                : Print full manual
    # plman <playlist>      : Manage playlist
    def __init__ (self,commandARG, defaultCMD, pref,  greetString: str = "Welcome !"):
        self.greetString    = greetString   # Greet string to be print at the beginning of the program
        self.commandARG     = commandARG
        self.pref           = pref
        self.cmdStack       = ""
        self.optStack       = []
        self.argStack       = []
        self.defaultCMD     = defaultCMD
        self.expect_arg     = False
        self.expected_arg   = ""

    async def begin(self):
        print("Begin argparser command line", file = sys.stderr)
        return
    async def unknown(self,s:str):      # What to do when face unexpected parameter
        return

    async def exe (self):               # Execute code
        return

    async def usage(self,s:str):
        #Register argument
        return

    async def repop(self,s:str, is_long:bool):
        # Register option
        return

    #process and return argument(s)
    def process(self,s: str):
        #Fix. Need to have more sophisphicated method of analyzing command
        return s.strip().split()
    def clear_at_end(self):
        self.optid = 0
    async def run(self):
        await self.begin()
        print(self.greetString)
        toContinue=True
        while toContinue:
            print('>>> ',end='')
            cmd=input()
            args = self.process(cmd)
            argc=len(args)
            if argc==0:
                continue
            elif argc==1:
                if args[0] in [s.get("opt") if s.get("is_singular") == True for s in commandARG]:
                    self.cmdStack = args[0]
                    await self.exe()
                else:
                    a = await self.usage(args[0])
                    if a==False:
                        continue
                    await self.exe()

            elif argc > 1:
                for i in range(0,argc):
                    if i == 0:
                        if not args[i] in [s.get("opt") for s in self.commandARG]:
                            self.cmdStack = self.defaultCMD
                        else:
                            self.cmdStack = args[i]
                            continue
                    if args[i][0] == '-':
                        if len(args[i]) == 1:
                            self.usage(args[i])
                            continue
                        if args[i][1] == '-':
                            if len(args[i]) == 2:
                                self.usage(args[i])
                                continue
                            else:
                                self.repop(args[i][2:], True)
                                continue
                        else:
                            self.repop(args[i][1:], False)
                            continue
                    self.usage(args[i])
                    if i == argc - 1:
                        if self.expect_arg:
                            self.unknown(args[i])
                        await self.exe()
            self.clear_at_end()
            await self.ending()

    async def ending(self): #Overwrite this
        return
    def start(self):
        asyncio.run(self.run())
        #I still want to have a event loop here
    def stop(self,return_code: int = 0):
        self.ending()
        print("Exiting")
        sys.exit(return_code)
