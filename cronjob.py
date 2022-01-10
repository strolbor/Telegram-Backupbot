import subprocess
import time
import telegramsendapi as r
import write

process = subprocess.Popen(["echo", "hi"])
time.sleep(1)
def backup():
    global process
    if process.poll() == 0: 
      cmd = ["/media/HDD/Backup-New/intern.sh"]
      f = open(write.path+"backup.txt","w")
      process = subprocess.Popen(cmd,stdout=f)
      r.sendmsg(receiver="978618750",text="Backup wurde automatisch gestartet.")

if __name__ == '__main__':
    backup()
