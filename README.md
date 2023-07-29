# CompressImage
Compress Any Image To Your Desired Size Without Losing The Image Quality Using Python. Enter the file name, compression percentage and the maximum output file size as input and hit enter. That's Simple 😎.


Make sure to check if PIL is installed if you get any errors by doing

```pip install pillow```

if you want to make it as simple as typing ```imgcom``` follow me:

For Linux/macOS: Open the terminal and type nano ~/.bashrc to open the ```bashrc``` file in a text editor. At the end of the file, add this line: ```alias imgcom='python3 /path/to/your/script/imgcom.py'```. Save and close the file. Now, type source ```~/.bashrc``` to reload the ```bashrc``` file.

For Windows: The process is different as Windows doesn't support aliases in the same way. However, you can add a batch script to the Windows System32 folder, which is part of the system path. This batch script will invoke your Python script. Here's an example of what the batch script could look like:

```
@echo off
python C:\path\to\your\script\imgcom.py %*
```
Save this as imgcom.bat and move it to the ```C:\Windows\System32``` folder. Now, you can invoke your script with ```imgcom``` from any directory in the command prompt.

