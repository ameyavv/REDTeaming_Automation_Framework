#!/bin/bash

# Add paths to all your shell scripts
script1_metasploit=Shell_Scripts/Metasploit.sh
script2_nikto=Shell_Scripts/Nikto.sh
script3_unix_privesc_check=Shell_Scripts/Unix_Privesc_Check.sh
script4_LinEnum=Shell_Scripts/LinEnum.sh
script5_sql=Shell_Scripts/sql.sh
script6_LinPEAS=Shell_Scripts/LinPEAS.sh
script7_Bettercap=Shell_Scripts/Bettercap.sh
script8_Responder=Shell_Scripts/Responder.sh
script9_Beef=Shell_Scripts/Beef.sh
script10_Acunetix=Shell_Scripts/Acunetix.sh
script11_pwndrop=Shell_Scripts/pwndrop.sh
script12_Impacket=Shell_Scripts/Impacket.sh
script13_Dirb=Shell_Scripts/Dirb.sh
script14_Sherlock=Shell_Scripts/Sherlock.sh
script15_Spiderfoot=Shell_Scripts/Spiderfoot.sh
script16_Steghide=Shell_Scripts/Steghide.sh
script17_theHarvester=Shell_Scripts/theHarvester.sh
script18_Linux_Exploit_Suggester=Shell_Scripts/Linux-Exploit-Suggester.sh
script19_Linux_Smart_Enumeration=Shell_Scripts/LINUX-SMART-ENUMERATION.sh
script20_nmap=Shell_Scripts/nmap.sh
script21_hping3=Shell_Scripts/hping3.sh
script22_Netcat=Shell_Scripts/Netcat.sh
script23_dirsearch=Shell_Scripts/dirsearch.sh

# Add more paths if you have additional shell scripts

# Run each shell script
bash "$script1_metasploit" &
bash "$script2_nikto" &
bash "$script3_unix_privesc_check" &
bash "$script4_LinEnum" &
bash "$script5_sql" &
bash "$script6_LinPEAS" &
bash "$script7_Bettercap" &
bash "$script8_Responder" &
bash "$script9_Beef" &
bash "$script10_Acunetix" &
bash "$script11_pwndrop" &
bash "$script12_Impacket" &
bash "$script13_Dirb" &
bash "$script14_Sherlock" &
bash "$script15_Spiderfoot" &
bash "$script16_Steghide" &
bash "$script17_theHarvester" &
bash "$script18_Linux_Exploit_Suggester" &
bash "$script19_Linux_Smart_Enumeration" &
bash "$script20_nmap" &
bash "$script21_hping3" &
bash "$script22_Netcat" &
bash "$script23_dirsearch"

echo "ALl scripts have been completed"

# Run additional shell scripts if needed
