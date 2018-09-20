#cerner_2^5_2018
#Coding for clear cache files older than 10 minutes in current working directory.
import os
import time
outer = os.getcwd() #/ method for current working directory of a process/#
cache = os.path.join(outer, 'cache')
filecount = 0
for f in os.listdir(cache):
        f = os.path.join(cache, f)
        used_by = time.time() - 10 * 60
        if os.path.getatime(f) < used_by:
                os.remove(f)
                filecount += 1
print("Removed {} files.".format(filecount))
