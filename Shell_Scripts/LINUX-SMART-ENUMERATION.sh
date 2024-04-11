#!/bin/bash
# Clone the lse repository from GitHub
git clone https://github.com/diego-treitos/linux-smart-enumeration.git

# Navigate to the directory
cd linux-smart-enumeration

# To check the directory
Ls

# Make the lse.sh script executable
chmod +x lse.sh

echo "Installation completed."
echo "You can now run Linux Smart Enumeration (lse) by executing './lse.sh' or 'bash lse.sh' in the 'linux-smart-enumeration' directory."

To use this script:
1.	Open a text editor on your Kali Linux system.
2.	Copy and paste the above script into the text editor.
3.	Save the file with a name like install_lse.sh.
4.	Open a terminal and navigate to the directory where you saved the script.
5.	Make the script executable using the command chmod +x install_lse.sh.
6.	Run the script with ./install_lse.sh.
This script will automatically clone the lse repository, navigate into the directory, make the lse.sh script executable, and provide instructions on how to run it. After running the script, you can execute ./lse.sh or bash lse.sh within the linux-smart-enumeration directory to run Linux Smart Enumeration.
