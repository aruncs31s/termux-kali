## Mnual Installition of Xfce4
### main
```
apt update 
apt  install nano -y 
apt install -y kali-themes kali-menu
apt install -y xfce4 xfce4-goodies tightvncserver
```
### vnc
```
vncpasswd
```
### vnc-configs
``` 
nano ~/.vnc/xstartup
** #!/usr/bin/bash
** xfce4-session & 

chmod +x ~/.vnc/xstartup
```
