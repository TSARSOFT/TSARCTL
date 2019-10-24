import os
import tkinter
import subprocess
import re
import psutil
import threading
import time
import socket

usr=subprocess.check_output('whoami')
user=usr.decode('ascii')
list1 = re.sub("[^\w]", " ",  user).split()
user1=list1[0]

def check_connection(host="64.233.160.0", port=53, timeout=5):
  try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    return True
  except socket.error as ex:
    print(ex)
    return False

def tprint(text):
        debug.config(state='normal')
        debug.insert(tkinter.END, text+'\n')
        debug.config(state='disabled')
        
def update():
        net0=subprocess.Popen(['rfkill', 'list', '0'], stdout=subprocess.PIPE)
        net1=net0.communicate()[0].decode('ascii')
        net=net1.splitlines()[1].split('Soft blocked: ')[1]
        levelout=subprocess.Popen(['brightnessctl', 'g'], stdout=subprocess.PIPE)
        level1=levelout.communicate()[0].decode('ascii')
        level=(int(level1)/09.37)
        screen=str(level)[0:5]
        batdev=psutil.sensors_battery()
        bat1=str(batdev.percent)
        bat=bat1[0:5]
        batmon.delete(0, tkinter.END)
        batmon.insert(tkinter.END, bat+'%')
        scrmon.delete(0, tkinter.END)
        scrmon.insert(tkinter.END, screen+'%')
        usrmon.delete(0, tkinter.END)
        usrmon.insert(tkinter.END, user1)
        killnetmon.delete(0, tkinter.END)
        killnetmon.insert(tkinter.END, net)

def netloop():
        netmon.delete(0, tkinter.END)
        netmon.insert(tkinter.END, str(check_connection()))
        time.sleep(5)

if user1 == 'root':
        print('running as root, using all privalages')
        runningroot=True
else:
        print('running as non root user \''+user1+'\', you can still use, but with lesser privalages')
        runningroot=False

ctlroot=tkinter.Tk()
ctlroot.title('TSARCTL')
ctlroot.geometry('500x250')
ctlroot.resizable(False, False)

menubar=tkinter.Menu()
File=tkinter.Menu()

menubar.add_cascade(menu=File, label='File')

ctlroot.config(menu=menubar)

File.add_command(label='Close', command=lambda:ctlroot.destroy())

scroller=tkinter.Scrollbar()
scroller.place(x=146, height=250)

debug=tkinter.Text(ctlroot, width=20, yscrollcommand=scroller.set)
debug.pack(side='left')
debug.config(state='disabled')

scroller.config(command=debug.yview)

stats=tkinter.LabelFrame(ctlroot, pady=0, padx=0, text='stats', relief='ridge')
stats.pack(side='right', fill='both')

config=tkinter.LabelFrame(ctlroot, padx=0, pady=0, text='sysconf', relief='ridge')
config.pack(side='right', fill='both')

tkinter.Label(stats, text='battery:').grid(row=0, column=0)

batmon=tkinter.Entry(stats, width=6)
batmon.grid(row=0, column=1)

tkinter.Label(stats, text='backlight:').grid(row=1, column=0)

scrmon=tkinter.Entry(stats, width=6)
scrmon.grid(row=1, column=1)

tkinter.Label(stats, text='user:').grid(row=2, column=0)

usrmon=tkinter.Entry(stats, width=6)
usrmon.grid(row=2, column=1)

tkinter.Label(stats, text='net connected:').grid(row=3, column=0)

netmon=tkinter.Entry(stats, width=5)
netmon.grid(row=3, column=1)

tkinter.Label(stats, text='net disabled:').grid(row=4, column=0)

killnetmon=tkinter.Entry(stats, width=5)
killnetmon.grid(row=4, column=1)

tprint('UI set up')
tprint('will now update\nstats every half-second')

tkinter.Label(config, text='brightness', heigh=2).grid(row=0, column=0)

lightslider=tkinter.Scale(config, from_=0, to=100, orient=tkinter.HORIZONTAL)
lightslider.grid(row=0, column=1)
lightslider.set(50)

def loop():
        while True:
                update()
                time.sleep(0.5)

def brightloop():
        while True:
                light1=lightslider.get()
                light=light1*9.371
                os.system('brightnessctl s '+str(light))
                time.sleep(0.1)

p1=threading.Thread(target=loop)
p2=threading.Thread(target=brightloop)
p3=threading.Thread(target=netloop)
p1.start()
p2.start()
p3.start()

ctlroot.mainloop()
