# Instructions for creating a PyQt5 Custom GUI

## Average Calculator Example

### Initial Project Creation and Setup

1. Install Python 3.6 at https://www.python.org/downloads/release/python-360/
    1. If you are a Windows 10 user, download and run the **Windows x86 executable installer**
    2. Select *Install Now*
    3. Keep track of what the installation path is
    4. The default is %HOME%\AppData\Local\Programs\Python\Python36-32
1. Download PyCharm community edition and install with default settings
2. Open this project within PyCharm
    1. Open the root directory (PythonGUIs)
    2. **Cancel or skip anything that shows up immediately upon opening**
3. Reopen this *README.md* file in PyCharm
    1. This allows you to use the .md previewer
    2. It will render this file into more readable text
    3. Click the *Show Preview Only* in the top right corner of the editor will 
       allow you to view this rendered file without the text editor open next to it
3. Once the project loads, do the following setup:
      1. Go to *File->Settings->Project: PythonGUIs->Python Interpreter*
      2. Click the cogwheel near the upper right-hand corner and click *Add...*
         1. Select *Virtualenv Environment* in the left pane
         2. Select *New environment* in the right pane
         3. Hit *OK*
         4. **The above setttings will likely be the default options**
      3. Let PyCharm do the work to create a new virtual environment
      4. Exit the settings menu by hitting *OK*
4. Open the *Terminal* on the lower left of the PyCharm window
   1. To install the prerequisite packages to run and compile your application,
      run the following commnand:
        - `pip install -r requirements.txt`
    2. This command will output a bunch of progress details and other information
        1. Ignore warnings (in yellow)
        2. Let me know if there are any errors (in red)
      
### How to use your custom PyQt5 GUI Application

Navigate to the *src/main/python* directory in the Project pane. Run `average_calculator.py` 
by right-clicking the file in the Project pane and hitting *Run 'average_calculator'*.

Alternatively you can run it from the Terminal by executing the following command 
in the root directory:

`python src/main/python/average_calculator.py`

### Compile your application to an executable (AvgCalc.exe)

In the root directory of the project, run the following command:

`fbs freeze`

This command can take a few minutes to complete execution.

This will create a folder within the `target` directory called `AvgCalc`. Within that directory
there will be an executable `AvgCalc.exe` that will run the custom GUI. This *folder* can be
moved to any location on your PC or another PC with the same operating system and run.

### More information

I created this project in part by following this tutorial: \
https://build-system.fman.io/pyqt5-tutorial