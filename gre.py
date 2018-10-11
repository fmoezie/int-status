#!/usr/bin/python3
'''
Check for active connections on our netscalers
'''
def double_quote(word):
    # return f'"{word}"' 
    return '"{}"'.format(word)

def main():

    '''
    Main fuction
    Get username
    Get password
    then call ssh_connect.py to test regex.
    print returned answer
    '''
    import re 
    import sys
    import ssh_connect as s
    import getpass



    username = "username"
    password = "password"
    try:
        username = input('username ')
        password = getpass.getpass("password ")
    except Exception as error:
        print("error", error)

    if len(sys.argv) != 2:
        print ('connection-check.py <username> <password> <ip address>')
        sys.exit(1)


    hostname = open("gre-routers.txt")


    port = 22

# Show IP route get network
    command = ('show route' + double_quote("SOURCEIP = " +sys.argv
[1]))
    regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9](.*)"
    for netscreen in hostname:
        try:
            returned_ans = s.sshconnect(netscreen, port, username, password, com
mand, regex)
            print (netscreen, ' Known by ', returned_ans)
        except ValueError:
            print('duh')


main()

