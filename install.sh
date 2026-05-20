# Logo
cat << "EOF" 

▗▄▄▖ ▗▄▄▖  ▗▄▖ ▗▄▄▖  ▗▄▄▖▗▄▄▄▖▗▄▖▗▄▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌     █ ▐▌ ▐▌ █  
▐▛▀▘ ▐▛▀▚▖▐▌ ▐▌▐▛▀▘  ▝▀▚▖  █ ▐▛▀▜▌ █  
▐▌   ▐▌ ▐▌▝▚▄▞▘▐▌   ▗▄▄▞▘  █ ▐▌ ▐▌ █  
                                      
Welcome to the Propstat (c) SSL Deploy Installer. 
All rights to the Propstat Logo and Name reserved.
This tool is provided with an open source or source accessible license depending on your use case.
Please verify which license applies on our Github Repository:
https://github.com/propstat/ssldeploy
EOF

# Dependencies
echo "Do you wish to proceed installing this software?"
select strictreply in "Yes" "No"; do
    relaxedreply=${strictreply:-$REPLY}
    case $relaxedreply in
        Yes | yes | y ) exit; break;;
        No  | no  | n ) exit;;
    esac
done
