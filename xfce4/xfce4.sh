#!/bin/bash

clear
cd $HOME
#
printf "\nInstalling dependencies ... "
apt  install python wget -y 
python -m pip install --upgrade pip
pip install colorama

python ~/termux-kali/xfce4/xfce4.py 

printf "\n  To start the vnc server Type start-xfce4\n   To stop the vnc server Type stop-xfce4\n"
