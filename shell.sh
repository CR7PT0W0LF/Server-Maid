
clear
sudo apt install figlet -y
clear
figlet Server Maid
echo "this might take a minute. go grab a Dr. Pepper or something"
sleep 3
#Minecraft server install
mkdir Minecraft
sudo apt update -y && sudo apt upgrade -y 
clear
#this is some security stuff to get rid of some programs that are a risk
sudo apt-get --purge remove xinetd nis yp-tools tftpd atftpd tftpd-hpa telnetd rsh-server rsh-redone-server -y
#normal utils for seeing system resources and changing config files
 sudo apt install screen -y
 sudo apt install htop -y
 sudo apt install neovim -y
 sudo apt install net-tools -y
 sudo apt install speedtest-cli -y
 sudo apt install curl -y 
 sudo apt install snapd =y
 sudo snap install core -y 
 sudo apt install git -y
 clear
  
  cd Minecraft
   sudo apt install openjdk-21-jre-headless -y
   sudo wget https://piston-data.mojang.com/v1/objects/e6ec2f64e6080b9b5d9b471b291c33cc7f509733/server.jar
chmod +x ServerJars-3 
     
    #This is a program that allows you TCP Tunnel your Servers so you don't have to port foward. Make sure to setup a accout 
     cd -
     mkdir TCP-Tunnel
     cd TCP-Tunnel
     #playit system
      curl -SsL https://playit-cloud.github.io/ppa/key.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/playit.gpg >/dev/null
      if [ $? -ne 0 ]; then
          echo "Error: Failed to download or process the GPG key."
          exit 1
      fi
echo "deb [signed-by=/etc/apt/trusted.gpg.d/playit.gpg] https://playit-cloud.github.io/ppa/data ./" | sudo tee /etc/apt/sources.list.d/playit-cloud.list
sudo apt update
sudo apt install playit

       sudo add-apt-repository multiverse
 sudo dpkg --add-architecture i386
 sudo apt update
 sudo apt install lib32gcc-s1 steamcmd
 sudo apt install steamcmd
cd
clear

 figlet Complete
 
sleep 5
  sudo apt purge figlet -y 
  clear




     


