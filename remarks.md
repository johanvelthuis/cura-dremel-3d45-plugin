My instructions are for a MacOS system.
I'm not shure how it differs from a window system, but if anyone gets it to work, please contact me so we can post the windows instructions here too.

Open Cura 4.8, Click Help in the Menubar, then 'Show Configuration Folder'

It should show you a 4.8 folder.

Compare it's content with the content from this github projects 4.8 folder.
Just to be shure, copy the 4.8 folder to a save backup location so it can be stored if your cura setup gets messed up.

Copy any 3d45 related files to your own 4.8 folder so that the  relative paths are correct.

In the cura.cfg file, there is a section about 3d45 network printer.
For now the dialog_save_path needs to be set to a similar file path that is valid on your system.
I used a path in my download folder, since that is probably not heavily secured for read/write by the Cura system user.

there is a test.py file outside of the cura folder. This contains a rough copy of the heart of the plugin, the actual sending to the printer.
for it to work it needs a correct python version (2 or 3, not sure, but your OS will complain if it's the wrong one.
Before executing, open the file and change the variables
ip_address = "10.0.0.114" to match your printers IP
file = "/path/to/filename/in/downloadsfolder" to match a file that you would like to print.

then save and execute the file:
./test.py

For the actual plugin, there are some hardcoded settings right. I aim to make there variable and accessible from a settings or preferences menu, or when starting the first print.

open the file: 4.8/plugins/Dremel3D45OutputDevice/Dremel3D45OutputDevice.py

at about line 25, change variable to correct ip address.

When you restart cura, you should see a downward triangle (see screenshot.png)
choose 'Print over Network' and click it again.
It should say that it is saving the file. Then the messaging stops in Cura, but the print should start shortly after that.

For troubleshooting, in the 4.8 folder, there is also a cura.log file, which contains info and errors from cura including problems in the plugin.
If there is a fatal error in the plugin, cura will crash. 


