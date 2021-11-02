import wmi
import subprocess

c = wmi.WMI()

info = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
a = str(info)

try:
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[i])
except IndexError as e:
    print("All Done")

print()

for s in c.Win32_StartupCommand():
    print("%s <%s>" % (s.Caption, s.Command))

print()

for u in c.Win32_UserAccount():
    print("%s <%s>" % (u.name, u.Status))
