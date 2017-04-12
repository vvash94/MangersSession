# MangersSession

1. If you are not a linux machine, please create an EC2 Ubuntu 16.04 machine for yourself.
2. Login to the Ubuntu machine. Then run the following:
   sudo apt-get update
   sudo apt-get install git python-pip
   sudo pip install boto
   cd ~
   git clone https://github.com/vvash94/MangersSession.git
   cd ManagersSession
3. Open the file "account-create.py" in the vi editor
4. Enter the email from which mails have to be sent in place of \<\<ENTER EMAIL ID HERE>>
5. Open the file "emails" in the vi editor
6. Enter the email ids of the participants. Each on a single line.
7. Open the file "password" in the vi editor
8. Please make sure your screen is not shared before you do this step. Enter your password in the file.
9. Run: python account-create.py
