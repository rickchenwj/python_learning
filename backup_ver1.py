import os
import time

#1. The files and directories to be backed up are specified in a list
source = ['/home/swaroop/byte','/home/swaroop/bin']
#If you are using Windows, use source =[r'C:\Documents'.r'C:\Work'] or something like that

#2. THe backup must be stored in a main backup directory
target_dir ='/mnt/e/backup'#Remember to chage this to what you wil be using

#3. THe files are backed up into a zip file.
#4. The name of the zip archive is the current date and item
target = target_dir + time.strftime('%Y%M%D%H%M%S') + '.zip'

#5. We use the zip command (in Unix/LInux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

#Run the backup
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
