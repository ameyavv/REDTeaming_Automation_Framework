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

script_paths = {"$script1_metasploit", "$script2_nikto", "$script3_unix_privesc_check", "$script4_LinEnum", "$script5_sql", "$script6_LinPEAS", "$script7_Bettercap", "$script8_Responder", "$script9_Beef", "$script10_Acunetix", "$script11_pwndrop", "$script12_Impacket", "$script13_Dirb", "$script14_Sherlock", "$script15_Spiderfoot", "$script16_Steghide", "$script17_theHarvester", "$script18_Linux_Exploit_Suggester", "$script19_Linux_Smart_Enumeration"}

# Function to execute each script one at a time
execute_scripts() {
    local script_paths=("$@")  # Get all script paths passed as arguments
    for script_path in "${script_paths[@]}"; do
        echo "Executing script: $script_path"
        bash "$script_path"
        echo "Script execution completed."
    done
}

# Call the function with all script paths
execute_scripts "${script_paths[@]}"
