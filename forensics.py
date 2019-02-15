import subprocess
import re
from time import strftime
timestamp=strftime("%Y-%m-%d %H-%M-%S")
print(timestamp)
usr=input("Enter the system type:\n 1.Redhat \n 2.Debian \n")
if usr=="1":
    op=subprocess.check_output(["cat","/mnt/etc/redhat-release"],stderr=subprocess.STDOUT,universal_newlines=True)
    dns=subprocess.check_output(["cat","/mnt/etc/resolv.conf"],stderr=subprocess.STDOUT,universal_newlines=True)
    md5=subprocess.check_output(["sudo","md5sum","/dev/mapper/ddimage-root"],stderr=subprocess.STDOUT,universal_newlines=True)
    print("Operating System:\n",op)
    print("DNS Servers:\n",dns)
    print("MD5 of Disc: \n",md5)

elif usr=="2":
    os=subprocess.check_output(["cat", "/mnt/etc/os-release"], stderr=subprocess.STDOUT,universal_newlines=True)
    x=re.search(r'PRETTY_NAME=(.*)', str(os))

    dns=subprocess.check_output(["cat", "/mnt/run/resolvconf/interface/original.resolvconf"], stderr=subprocess.STDOUT,universal_newlines=True)

    md5=subprocess.check_output(["sudo", "md5sum", "/dev/mapper/loop0p1"], stderr=subprocess.STDOUT,universal_newlines=True)

    print("Operating System: \n",x.group(0))
    print("DNS Servers:\n",dns)
    print("MD5 of Disc:\n",md5)
else:
    print("Invalid Input")
    


op1=subprocess.check_output(["ls","/mnt/lib/modules"],stderr=subprocess.STDOUT,universal_newlines=True)
op2=subprocess.Popen(["cat","/mnt/etc/passwd"],stdout=subprocess.PIPE,shell=False)
op3=subprocess.Popen(["wc","-l"],stdin=op2.stdout,stdout=subprocess.PIPE,shell=False)
op2.stdout.close()
log=subprocess.Popen(["cat","/mnt/etc/passwd"],stdout=subprocess.PIPE,shell=False)
login=subprocess.Popen(["grep","/bin/bash"],stdin=log.stdout,stdout=subprocess.PIPE,shell=False)
log.stdout.close()
login1=subprocess.Popen(["wc","-l"],stdin=login.stdout,stdout=subprocess.PIPE,shell=False)
login.stdout.close()
fstab=subprocess.check_output(["cat","/mnt/etc/fstab"],stderr=subprocess.STDOUT,universal_newlines=True)
host=subprocess.check_output(["cat","/mnt/etc/hostname"],stderr=subprocess.STDOUT,universal_newlines=True)

print("Hostname:\n",host)
print("Contents of fstab:\n",fstab)
print("Logged-in users on the system:\n",login1.communicate()[0].decode())
print("Total users in the system:\n",op3.communicate()[0].decode())
print("Kernel Level:\n",op1)






