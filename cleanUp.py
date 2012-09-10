from send2trash import send2trash
import os
import gntp.notifier
import sys
import urllib

def download(url):
    """Copy the contents of a file from a given URL
    to a local file.
    """
    home = os.getenv("HOME")
    folder = home + "/Library/Application Support/NH_CleanUp/"
    if not os.path.exists(folder):
        os.makedirs(folder)
    if not os.path.exists(folder + url.split('/')[-1]):
        webFile = urllib.urlopen(url)
        localFile = open(folder + url.split('/')[-1], 'w')
        localFile.write(webFile.read())
        webFile.close()
        localFile.close()
    return (folder + url.split('/')[-1])
    
if __name__ == '__main__':
    folder = ""
    exception = "empty"
    num = 0
    message =""
    image = ""
    
    ### image runterladen
    try:
        image = open(download("http://niklas-heer.de/pics/trash.png")).read()
    except IOError:
        print 'Filename not found.'
    
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