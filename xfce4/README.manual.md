## Mnual Installition of Xfce4
### main
```
apt update 
apt  install nano -y 
apt install -y kali-themes kali-menu
apt install -y xfce4 xfce4-goodies tigervnc
```
### vnc
```
vncpasswd
```
### vnc-configs
``` 
echo "#!/usr/bin/bash
xfce4-session & " >> ~/.vnc/xstartup

chmod +x ~/.vnc/xstartup
```
