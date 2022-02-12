
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import gi
import time
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MetaMyDBUSService(type(Gtk.Window), type(dbus.service.Object)):
    pass


class MyDBUSService(Gtk.Window,dbus.service.Object,metaclass=MetaMyDBUSService):
    def __init__(self):
        super().__init__(title="Demo")
        self.working = Gtk.Label(label="Çalışıyor...")
        bus_name = dbus.service.BusName('org.app.backup', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/app/backup')
        self.add(self.working)
        self.show_all()



    @dbus.service.method('org.app.backup')
    def backup(self,wait_second=None):
            
            if wait_second is not None:
                eta=str(wait_second)+" saniye kaldı"
                time.sleep(1)
                self.working.set_text(eta)
                print(eta)
                if wait_second == 0:
                    self.working.set_text("Çalışıyor...")
                return True
            self.working.set_text("Yedekleme Başladı")
            return True
  

    
DBusGMainLoop(set_as_default=True)
window = MyDBUSService()
window.set_size_request(300, 300)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
