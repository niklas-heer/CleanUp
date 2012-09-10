from send2trash import send2trash
import os
import gntp.notifier
import sys

folder = "/Users/nh/REPOS/git/sellaround"
exception = "empty"
num = 0
message =""
for f in sys.argv[1:]:
    folder = f

for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if not (os.path.isfile(file_path)):
            if (os.path.basename(file_path) == "mariaTmp"):
                subfolder1 = folder + "/" + os.path.basename(file_path)
                for the_file in os.listdir(subfolder1):
                    file_path = os.path.join(subfolder1, the_file)
                    if not (os.path.basename(file_path) == exception):
                        send2trash(file_path)
                        num += 1
            if (os.path.basename(file_path) == "www"):
                subfolder2 = folder + "/" + os.path.basename(file_path) + "/" + "mariaTmp"
                for the_file in os.listdir(subfolder2):
                    file_path = os.path.join(subfolder2, the_file)
                    if not (os.path.basename(file_path) == exception):
                        send2trash(file_path)
                        num += 1
    except Exception, e:
        print e


message = str(num) + ' files deleted!'
image = open('/Users/nh/Pictures/trash.png').read()
growl = gntp.notifier.GrowlNotifier(
    applicationName = "My Application Name",
    notifications = ["New Updates","New Messages"],
    defaultNotifications = ["New Messages"],
)
growl.register()

growl.notify(
    noteType = "New Messages",
    title = "mariaTmp cleaned!",
    description = message,
	icon = image,
    sticky = False,
    priority = 1,
)