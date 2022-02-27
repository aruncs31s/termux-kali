import  sys
from os import system
from time import sleep as waite
from colorama import *
import os

RED         = Fore.RED
GREEN       = Fore.GREEN
BLUE        = Fore.BLUE
YELLOW      = Fore.YELLOW
MAGENTA     = Fore.MAGENTA
CYAN        = Fore.CYAN

BOLD        = '\033[1m'
BRIGHT      = Style.BRIGHT

BACKRED     = Back.RED
BACKGREEN   = Back.GREEN
BACKYELLOW  = Back.YELLOW
BACKMAGENTA = Back.MAGENTA

RESET      = Style.RESET_ALL
#

#
interface = BRIGHT + MAGENTA + "Termux-kali "
print(interface.center(60))
#sleep(1)
#print(BRIGHT + MAGENTA + "  Enviornment  :" + RESET + BRIGHT + CYAN + " LXQT ")
#sleep(0.2)
#print(BRIGHT + MAGENTA + "  Auther  :" + RESET + BRIGHT + YELLOW + " aruncs31s")
#sleep(1)

def vnc_setup():
   xx


#print(BRIGHT + MAGENTA + "REMOVING OLD FILES IF EXISTS" + RESET)
setting_desktop()


def write(in_text):
 for char in in_text:
  waite(0.05)
  sys.stdout.write(char)
  sys.stdout.flush()
 
write(f"{CYAN}[+]{GREEN} Installing Xfce4 ...")
print("\t")
