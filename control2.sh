#!/bin/bash

# Add paths to all your shell scripts
script1_metasploit=Shell_Scripts/Metasploit.sh
script2_nikto=Shell_Scripts/Nikto.sh
script3_unix_privesc_check=Shell_Scripts/Unix_Privesc_Check.sh
script4_LinEnum=Shell_Scripts/LinEnum.sh
script5_sql=Shell_Scripts/sql.sh
script6_LinPEAS=Shell_Scripts/LinPEAS.sh
script7_Bettercap=Shell_Scripts/Bettercap.sh
script8_Impacket=Shell_Scripts/Impacket.sh
script9_Dirb=Shell_Scripts/Dirb.sh
script10_Sherlock=Shell_Scripts/Sherlock.sh
script11_Spiderfoot=Shell_Scripts/Spiderfoot.sh
script12_theHarvester=Shell_Scripts/theHarvester.sh
script13_Linux_Exploit_Suggester=Shell_Scripts/Linux-Exploit-Suggester.sh
script14_Linux_Smart_Enumeration=Shell_Scripts/LINUX-SMART-ENUMERATION.sh
script15_nmap=Shell_Scripts/nmap.sh
script16_hping3=Shell_Scripts/hping3.sh
script17_Netcat=Shell_Scripts/Netcat.sh
script18_pspy=Shell_Scripts/pspy.sh
script19_dirsearch=Shell_Scripts/dirsearch.sh

# Array of script variables
scripts=( script1_metasploit
    script2_nikto
    script3_unix_privesc_check
    script4_LinEnum
    script5_sql
    script6_LinPEAS
    script7_Bettercap
    script8_Impacket
    script9_Dirb
    script10_Sherlock
    script11_Spiderfoot
    script12_theHarvester
    script13_Linux_Exploit_Suggester
    script14_Linux_Smart_Enumeration
    script15_nmap
    script16_hping3
    script17_Netcat
    script18_pspy
    script19_dirsearch
)

# Loop through each script
for script_var in "${scripts[@]}"; do
    script_path="${!script_var}"  # Get the value of the variable
    echo "Executing script: $script_path"
    
    # Run the installation script
    bash "$script_path"
    
    # Check the exit status of the script
    if [ $? -eq 0 ]; then
        echo "Script executed successfully."
    else
        echo "Error executing script: $script_path"
        exit 1  # Exit the main script if any installation script fails
    fi
done

echo "All installation scripts have been executed successfully."
