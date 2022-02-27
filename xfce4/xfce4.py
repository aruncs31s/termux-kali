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

#//BACKRED     = Back.RED
#//BACKGREEN   = Back.GREEN
#//BACKYELLOW  = Back.YELLOW
#//BACKMAGENTA = Back.MAGENTA

#//RESET      = Style.RESET_ALL
#
def update_kali():
	system('apt update')


class kali:
	theme = 'apt install -y kali-themes kali-menu'
	basic = 'apt install -y xfce4 xfce4-goodies tigervnc '
	clean = 'ff'

class extra:
	def access_storage():
		system('termux-setup-storage')

	def symbolic_link():
		system('ln -s $HOME/storage/music $HOME/Music')
#	
def vnc_setup():
 	system('mkdir $HOME/.vnc')
    system('vncpasswd')
	system('cp -rf $HOME/termux-kali/xfce4/start-xfce4 $PREFIX/bin')
	system('cp -rf $HOME/termux-kali/xfce4/stop-xfce4 PREFIX/bin')
	system('cp -rf $HOME/termux-kali/xfce4/xstartup $HOME/.vnc')


def user_folders():
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



#os.chdir(r'/data/data/com.termux/files/home')
interface = BRIGHT + MAGENTA + "Termux-kali"
print(interface.center(60))
sleep(0.1)
def write(in_text):
 for char in in_text:
  waite(0.05)
  sys.stdout.write(char)
  sys.stdout.flush()
 
write(f"{CYAN}[+]{GREEN} Installing Xfce4 ...")
print("\t")
system(kali.update_kali)
system(kali.basic)
system(kali.theme)

print(BRIGHT + MAGENTA + "\n\t Push " + BRIGHT + YELLOW + "ENTER " + BRIGHT + MAGENTA + "to continue ... ")
input(BRIGHT + GREEN + " >> ")


sleep(0.5)
