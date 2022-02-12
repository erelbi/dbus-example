import dbus
import time

try:
    bus = dbus.SessionBus()
    backupservice = bus.get_object('org.app.backup', '/org/app/backup')
    backup = backupservice.get_dbus_method('backup', 'org.app.backup')
except Exception as e:
    print("Hata: {}".format(e))



try:
    if backup():
        i = 0
        while   i < 11:
            backup(10-i)
            print(i)
            time.sleep(1)
            i += 1
except Exception as e:
    print("Hata: {}".format(e))



