#Remote-Execution

A simple tool using dropbox as a bridge for user to execute python codes on a target device

It's a by-product in the process of developing a Hong Kong Stock Market Anaylsis tool

**You will need a Dropbox account shared on both remote-controlling and target device**

##How to use

1)  Tune the settings for your environment

Provide local path for your dropbox account, the location where your will keep your **command.txt**

**Listener.py** line 12

    dbPath = 'C:\Dropbox\Remote'

**You may also want to set a different listening time interval**

**Listener.py** line 13

    checkInterval = 30

2)  Define a command and a python program full path inside **list.csv**

    hkex    D:/Works/Programs/Python/HKEx/hkex.py

3)  Run Listener.py in cmd, the command.txt will be created at the dropbox path defined (i.e. dbPath)

    python listener.py

4)  Edit the 'command.txt' with a pre-defined command, on a dropbox connected device (e.g. iPhone)

    hkex

##How it works

<br>
<img src="/workflow.jpg">
<br>

