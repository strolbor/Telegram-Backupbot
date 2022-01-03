import subprocess
import time
import request as r

process = subprocess.Popen(["echo", "hi"])
time.sleep(1)
def backup():
    global process
    if process.poll() == 0: 
      cmd = ["/media/HDD/Backup-New/intern.sh"]
      f = open("log.txt","w")
      process = subprocess.Popen(cmd,stdout=f)
      r.sendmsg(receiver="python3 /media/HDD/Backup-New/cronjob.py",text="Backup wurde automatisch gestartet.")

if __name__ == '__main__':
    backup()
