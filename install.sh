#!/bin/bash
# ==========================================
# Variables
# ==========================================
RED=$'\e[0;31m'

# ==========================================
# LOGO
# ==========================================
cat << "EOF"

           il*%%%%*             i%%%%%%%           
          iiiI*%%%%%          .iii*%%%%*%          
         iiiiii%%%%%%▒       .iiiii%*%%%*%         
        iiiiiii %%%%%%<      iiiiii %*%%%%%        
       iiiiiii   *%%%%%%   ;iiiiii   **%%%%*       
      iiiiiii     %%%%%*% ;iiiiii     %*%%%%*      
     iiiiiii       **%%%**iiiiii       *%%%%*%     
    iiiiiii         *%%%%*<iiii         **%%%**    
   iiiiiii           %*%%%**ii           *%%%%*%   
  iiiiiiiiiiiiiiiiiiii%%%%%%*%%%%%%%%%%%%%%%%%%%*  
 iiiiiiiiiiiiiiiiiiiiii%*%%%%%%%%%%%%%%%%%%%%%%%%* 
iiiiiiiiiiiiiiiiiiiiiiii**%%%%%%%%%%%%%%%%%%%%%%%%%
                                                   
iiiii iiiiii iiiiii  iiiii iiiii:iiiiii  iii iiiiii
iiiiiiii  iiiii  iii ii:iiiiiiii   ii   iiii   ii  
iiiii iiiiiiiii  iii iiiii iiiiii  ii  iiiiii  ii  
ii    ii iii iiiiii  ii    iiiiii  ii iiiiiiii ii  

EOF

# ==========================================
# Copyright & License Warning
# ==========================================

date +"Copyright 2026 - YYYY by Propstat"
echo "Non commercial use is free of charge, please consult our license for commercial use."
echo "The license is available at https://github.com/propstat/ssldeploy"

# ==========================================
# Accept License
# ==========================================

while true; do
    echo "Do you accept the license?"
    echo "Type Y to continue or N to cancel the install."
    read -p "#? " reply

    case $reply in
        1 | Yes | yes | y | Y ) 
            make install
            break
            ;;
        2 | No | no | n | N ) 
            echo "Installation aborted."
            exit 0
            ;;
        * ) 
            echo "Invalid option. Please try again."
            echo ""
            ;;
    esac
done

# ==========================================
# Introduction and Warning
# ==========================================

cat << "EOF"
This tool allows you to request and deploy Let’s Encrypt™ Certificates among your services.

Currently following DNS providers are supported:
- Cloudflare

If you want to introduce support for an additional provider visit our repository at
https://github.com/propstat/ssldeploy
EOF
cat << EOF

${RED}==========================================${NC}
${RED}WARNING${NC}
${RED}==========================================${NC}
${RED}At the end of this process, this machine will hold credentials that allow to modify your DNS zone files. This system is meant for management networks and not for public access.${NC}
${RED}The software is provided "as is," meaning the original authors are not liable for any damages or bugs.${NC}
${RED}Proceed only if you know what you are doing.${NC}

Requirements:
1) This machine needs access to the internet to validate your certificate request.
2) You will subsequently need credentials to access the servers you want to deploy certificates on.
3) It will as first stept request a certificate for this server itself.
EOF

while true; do
    echo "Do you understand the risks and want to proceed?"
    echo "Type Y to continue or N to cancel the install."
    read -p "#? " reply

    case $reply in
        1 | Yes | yes | y | Y ) 
            make install
            break
            ;;
        2 | No | no | n | N ) 
            echo "Installation aborted."
            exit 0
            ;;
        * ) 
            echo "Invalid option. Please try again."
            echo ""
            ;;
    esac
done
