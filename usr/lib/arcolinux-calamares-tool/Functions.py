# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import os
import threading  # noqa
import subprocess
from pathlib import Path

base_dir = os.path.dirname(os.path.realpath(__file__))
working_dir = ''.join([str(Path(__file__).parents[2]),
                       "/share/hefftor-welcome-app/"])
proc = subprocess.Popen(["who"], stdout=subprocess.PIPE, shell=True, executable='/bin/bash') # noqa
users = proc.stdout.readlines()[0].decode().strip().split(" ")[0]
print(users)
DEBUG = False

if DEBUG:
    config = "/home/bheffernan/Repos/GITS/HLWM/hefftor-calamares-config-herbstluftwm/calamares-basic/modules/partition.conf"  # noqa
    liveuser = users
else:
    config = "/etc/calamares/modules/partition.conf"
    awa = "/usr/share/arcolinux-welcome-app/arcolinux-welcome-app.py"
    liveuser = "erik"
    #liveuser = "liveuser"
fs = [
    'btrfs',
    'xfs',
    'jfs',
    'reiser',
    'ext4',
]

liveusermessage = "The ArcoLinux Calamares tool is only for the live ISO"  # noqa
calamaresdebugmessage = "Calamares is in debugging modus."
calamaresnodebugmessage = "Calamares is not in debugging modus."

def __get_position(lists, string):
    data = [x for x in lists if string in x]
    pos = lists.index(data[0])
    return pos


def set_config(string):
    with open(config, "r") as f:
        lines = f.readlines()
        f.close()

    pos = __get_position(lines, "defaultFileSystemType:")

    lines[pos] = "defaultFileSystemType:  \"" + string + "\"\n"

    with open(config, "w") as f:
        f.writelines(lines)
        f.close()

def set_awa(string):
    with open(awa, "r") as f:
        lines = f.readlines()
        f.close()

    pos = __get_position(lines, '    	subprocess.Popen(["/usr/bin/calamares_polkit"')

    lines[pos] = '    	subprocess.Popen(["/usr/bin/calamares_polkit"' + string + "\n"

    with open(awa, "w") as f:
        f.writelines(lines)
        f.close()      

def on_debugswitch_toggled(self, switch):
    if self.get_active():
        print("Switch toggled to on")
        #show_in_app_notification(self,
        #                            "Calamares debugging is on")
        d = threading.Thread(target=set_awa,
                                args=(', "-d" ], shell=False)',))
        d.daemon = True
        d.start()
    else:
        print("Switch toggled to off")
        #show_in_app_notification(self,
        #                            "Calamares debugging is off")
        d = threading.Thread(target=set_awa,
                                args=('], shell=False)',))
        d.daemon = True
        d.start()

# =====================================================
#               NOTIFICATIONS
# =====================================================


def show_in_app_notification(self, message):
    if self.timeout_id is not None:
        GLib.source_remove(self.timeout_id)
        self.timeout_id = None

    self.notification_label.set_markup("<span foreground=\"white\">" +
                                       message + "</span>")
    self.notification_revealer.set_reveal_child(True)
    self.timeout_id = GLib.timeout_add(3000, timeOut, self)


def timeOut(self):
    close_in_app_notification(self)


def close_in_app_notification(self):
    self.notification_revealer.set_reveal_child(False)
    GLib.source_remove(self.timeout_id)
    self.timeout_id = None