#!/usr/bin/python3

import random
from rich.console import Console
import random
import json
import os

#$$$$$$$$$$#

class PYQR :
    def __init__(self) -> None :
        self.BANNER = ["██████╗ ██╗   ██╗ ██████╗ ██████╗ ",
                       "██╔══██╗╚██╗ ██╔╝██╔═══██╗██╔══██╗",
                       "██████╔╝ ╚████╔╝ ██║   ██║██████╔╝",
                       "██╔═══╝   ╚██╔╝  ██║▄▄ ██║██╔══██╗",
                       "██║        ██║   ╚██████╔╝██║  ██║",
                       "╚═╝        ╚═╝    ╚══▀▀═╝ ╚═╝  ╚═╝"]

        self.CONSOLE = Console()

        self.UPI_STR = "upi://pay?pa={0}&pn={1}&am={2}&cu={3}&tn={4}&"

        with open("/home/{0}/.config/PYQR/config.json".format(os.getlogin()),
                  "r") as file :
            self.DATA = json.load(file)
            self.KEYS = list(self.DATA.keys())

        self.menu_run()

    def menu_run(self) -> None :
        printable = "\n"
        for _ in self.BANNER :
            printable += _+"\n"
        os.system("clear")
        self.CONSOLE.print("[bold bright_white]"+
                           printable+
                           "[/ bold bright_white]")
        count = 0
        for _ in self.DATA :
            self.CONSOLE.print("[bold bright_white][ {0} ] {1}[/ bold bright_white]".format(count,
                                                                                            _))
            self.CONSOLE.print("")
            count += 1

        self.CONSOLE.print("[bold bright_white][()>] What You Want To Do ? :[/ bold bright_white]",
                           end="")
        choice  = input()

        if choice == "0" :
            self.CONSOLE.print("[bold bright_white]Enter Amount :[/ bold bright_white]",
                               end="")
            amount = input()
            self.CONSOLE.print("[bold bright_white]Enter Transaction Note :[/ bold bright_white]",
                               end="")
            tn = input()

            try :
                amount = round(float(amount), 2)
            except :
                self.CONSOLE.print("\n[bold deep_pink2][ * ] Amount Invalid[/ bold deep_pink2]")
                input()
                exit()

            upi_url = self.UPI_STR.format(self.DATA["UPI"]["UPI_ID"],
                                          self.DATA["UPI"]["PAYEE_NAME"],
                                          amount,
                                          self.DATA["UPI"]["CURRENCY"],
                                          tn)
            print()
            os.system("segno \"{0}\" --border 3 -p 6 | lolcat -F {1} -p {2}".format(upi_url,
                                                                                    random.randint(1, 200)/1000,
                                                                                    random.randint(1, 40)))
            input()
        else :
            try :
                choice = int(choice)
                os.system("segno \"{0}\" --border 3 -p 6 | lolcat -F {1} -p {2}".format(self.DATA[self.KEYS[choice]],
                                                                                        random.randint(1, 200)/1000,
                                                                                        random.randint(1, 40)))
                input()
            except :
                self.CONSOLE.print("\n[bold deep_pink2][ * ] Choice Invalid[/ bold deep_pink2]")
                input()
                exit()

if __name__ == "__main__" :
    OBJ = PYQR()
