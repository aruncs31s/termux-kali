#most of the parts of this script is made by https://github.com/EXALAB/AnLinux-App
#!/data/data/com.termux/files/usr/bin/bash
kalidir=termux-kali
PREFIX=/data/data/com.termux/files/usr
if [ -d "$kalidir" ]; then
	first=1
	printf "kali linux is alredy installed\nIf not remove the $kalidir"
fi
kalitar="kali-rootfs.tar.xz"
if [[(-f ~/$kalidir)]]; then
	if [ ! -f $kalitar ]; then
		echo "Download Rootfs, this may take a while base on your internet speed."
		case `dpkg --print-architecture` in
		aarch64)
			archurl="arm64" ;;
		arm)
			archurl="armhf" ;;
		amd64)
			archurl="amd64" ;;
		x86_64)
			archurl="amd64" ;;	
		i*86)
			archurl="i386" ;;
		x86)
			archurl="i386" ;;
		*)
			echo "unknown architecture"; exit 1 ;;
		esac
		wget "https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Rootfs/Kali/${archurl}/kali-rootfs-${archurl}.tar.xz" -O $kalitar
	fi
	cur=`pwd`
	mkdir -p "$kali"
	cd "$kali"
	echo "Decompressing Rootfs, please be patient."
	proot --link2symlink tar -xJf ${cur}/${kalitar}||:
	cd "$cur"
fi
mkdir -p kali-binds
bin=kali
echo "writing launch script"
cat > $bin <<- EOM
#!/bin/bash
cd \$(dirname \$0)
## unset LD_PRELOAD in case termux-exec is installed
unset LD_PRELOAD
command="proot"
command+=" --link2symlink"
command+=" -0"
command+=" -r $kalidir"
if [ -n "\$(ls -A kali-binds)" ]; then
    for f in kali-binds/* ;do
      . \$f
    done
fi
command+=" -b /dev"
command+=" -b /proc"
command+=" -b kali-fs/root:/dev/shm"
## uncomment the following line to have access to the home directory of termux
#command+=" -b /data/data/com.termux/files/home:/root"
## uncomment the following line to mount /sdcard directly to / 
command+=" -b /sdcard"
command+=" -w /root"
command+=" /usr/bin/env -i"
command+=" HOME=/root"
command+=" PATH=/usr/local/sbin:/usr/local/bin:/bin:/usr/bin:/sbin:/usr/sbin:/usr/games:/usr/local/games"
command+=" TERM=\$TERM"
command+=" LANG=C.UTF-8"
command+=" /bin/bash --login"
com="\$@"
if [ -z "\$1" ];then
    exec \$command
else
    \$command -c "\$com"
fi
EOM

termux-fix-shebang $bin
echo "making $bin executable"
chmod +x $bin
cp $bin $PREFIX/bin/
echo "removing image for some space"
rm -rf $kalitar
printf "\nkali linux is now installed\n"
echo "You can now launch Kali by typing \"kali\" or \"./kali\""
