# Launch EC2 using script

1. If you are not a linux machine, please create an EC2 Ubuntu 16.04 machine for yourself.
2. Login to the Ubuntu machine. Then run the following:
   
   sudo apt-get update
   
   sudo apt-get install git python-pip
   
   sudo pip install boto
   
   cd ~
   
   git clone https://github.com/vvash94/MangersSession.git
   
   cd ManagersSession
   
   cp .boto ~
   
   cd ~
   
   vi .boto
   
3. Fill the access id and secret key obtained from IAM without quotes or spaces.

4. Run the following:
   
   cd ManagersSession
   
   python launch_ec2.py
   
