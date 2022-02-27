#!/data/data/com.termux/files/usr/bin/python

#
from os import system
from time import sleep
from colorama import *
import os
#
init(autoreset=True)
#
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

class pkgs:
	X11      = 'pkg install -y x11-repo'
	PKGS     = 'pkg install -y xfce4 tigervnc '
	UNSTABLE = 'pkg install -y gobject-introspection at-spi2-atk '
	

class extra:
	def access_storage():
		system('termux-setup-storage')

	def symbolic_link():
		system('ln -s $HOME/storage/music $HOME/Music')
#	
def vnc():


def folders():
	system('mkdir $HOME/Desktop')
	system('mkdir $HOME/Downloads')
	system('mkdir $HOME/Templates')
	system('mkdir $HOME/Public')
	system('mkdir $HOME/Documents')
	system('mkdir $HOME/Video')
	system('chmod +x ~/.vnc/xstartup')
	
def exit_py():
	pass
#

def main():
	pass

os.chdir(r'/data/data/com.termux/files/home')
interface = BRIGHT + MAGENTA + "Termux-kali "
print(interface.center(60))
sleep(1)

print(BRIGHT + MAGENTA + "\n\t Push " + BRIGHT + YELLOW + "ENTER " + BRIGHT + MAGENTA + "to continue ... ")
input(BRIGHT + GREEN + " >> ")


sleep(0.5)
system(pkgs.X11)
system(pkgs.PKGS)
system(pkgs.UNSTABLE)
