sudo apt install python3-segno
sudo apt install lolcat

pip install rich

if [ -d "/home/$USER/.config/PYQR" ]; then
	sudo rm /home/$USER/.config/PYQR -r
fi

sudo cp CONFIG/ /home/$USER/.config/PYQR -r

if [ -f "/usr/bin/pyqr" ]; then
	sudo rm /usr/bin/pyqr
fi

sudo cp PYQR/pyqr.py /usr/bin/pyqr

sudo chmod +x /usr/bin/pyqr
