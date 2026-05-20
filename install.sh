# Logo
cat << "EOF" 

                         ggggg,                 vggggg                       
                      ,@ `@@@@@L              /L t@@@@@                      
                     _@@@  @@@@@p            g@@a \@@@@@,                    
                    /@@@@@  0@@@@@          @@@@@r '@@@@@L                   
                   g@@@@@    T@@@@@       ,@@@@@F    @@@@@a                  
                  @@@@@P      \@@@@@,    _@@@@@'      Q@@@@g                 
                .@@@@@F        '@@@@@_  /@@@@@         f@@@@@                
               ,@@@@@/           @@@@@L \@@@@           \@@@@@,              
              /@@@@@              Q@@@@g '@8             '@@@@@,             
             J@@@@@                %@@@@@                 `@@@@@L            
            g@@@@@@@@@@@@@@@@@@@@@L \@@@@@@@@@@@@@@@@@@@@@@@@@@@@b           
           @@@@@@@@@@@@@@@@@@@@@@@@g '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
         .BBBBBBBBBBBBBBBBBBBBBBBBBBB `BBBBBBBBBBBBBBBBBBBBBBBBBBBBB         
                                                                             
         !@@@g_  @@@@g   _g@@@_   @@@@_  _g@@g, @@@@@@   A@   @@@@@@!        
         [@  [@  @|  [@ !@    0@  @|  @| @@__     @@    /@T@    [@           
         [@BB=   @P4@[  (@    [@  @@BD"    "<@L   @@   ,@L_@p   [@           
         [@      @| `@L  "@@@@P   @]     4@gg@"   @@   @'   @\  [@   


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
