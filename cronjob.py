import write
import subprocess
import time

process = subprocess.Popen(["echo", "hi"])
time.sleep(1)
def backup():
    global process
    if process.poll() == 0: 
      cmd = ["/media/HDD/Backup-New/intern.sh"]
      f = open("log.txt","w")
      process = subprocess.Popen(cmd,stdout=f)

if __name__ == '__main__':
    backup()
