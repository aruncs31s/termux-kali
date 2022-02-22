#!/data/data/com.termux/files/usr/bin/bash
sudo apt update 
sudo apt install fluxbox tightvncserver -y
mkdir ~/.vnc &>/dev/null
wget https://raw.githubusercontent.com/aruncs31s/termux-kali/main/fluxbox/vncstart -P /usr/local/bin
wget https://raw.githubusercontent.com/aruncs31s/termux-kali/main/fluxbox/xstartup -P ~/.vnc/
wget https://raw.githubusercontent.com/aruncs31s/termux-kali/main/fluxbox/vncstop -P /usr/local/bin

chmod +x /usr/local/bin/vncstart
chmod +x /usr/local/bin/vncstop

printf "\nFluxbox wm is now installed  is now installed\n\nYou can start the vnc by typing vncstart \n vncstop to stop the vnc server\n"
