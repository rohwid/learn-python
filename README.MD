## **Install Python Dependencies**

If you're install the python for the first time, update first:

	$ sudo apt update && apt sudo upgrade -y

Install the dependencies:

	$ sudo apt-get install build-essential checkinstall
	$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    	libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

## **Install Python (Include Updating the Python Version)**

You need to remove the previous python which installed in `/usr/local/bin/` before update.

Remove the previous installed python version. For example in python3.8 (skip this step if you're first time to install python):

	$ sudo rm /usr/local/bin/*3.8*

Download the latest python version (for example):

	$ cd /opt
	$ sudo wget https://www.python.org/ftp/python/3.8.0/Python-3.8.11.tgz
	$ sudo tar xzf Python-3.8.11.tgz

Install the python:

	$ sudo apt install liblzma-dev -y
	$ sudo apt install lzma -y
	$ cd Python-3.8.11
	$ sudo ./configure --enable-optimizations
	$ sudo make altinstall

**Current Conclusion:**

The default or installed python by linux system will be saved in `/usr/bin/*3.6*` for **Python3.6**. For the **Python3.8**, it will be saved `/usr/bin/*3.8*`. But, for the manually installed version it will be saved in `/usr/local/bin/*3.6*` for the **Python3.6** and `/usr/local/bin/*3.8*` for the **Python3.8**.

## **Handle Multiple Python Version by Changing with Update Alternative**

Set the ID of each python version in Update Alternative

	$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
	$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
	$ sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.6 3
	$ sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.8 4

List or look at the list of update alternative:

	$ update-alternatives --list python
	/usr/bin/python3.6
	/usr/bin/python3.8
	/usr/local/bin/python3.6
	/usr/local/bin/python3.8

Change or update the default pyhton version who run in operating system (Ubuntu):

	$ sudo update-alternatives --config python

Select the pyhton version by enter it's ID:

	There are 2 choices for the alternative python (providing /usr/bin/python).

	Selection    Path                      Priority   Status
	------------------------------------------------------------
	* 0            /usr/local/bin/python3.8   2         auto mode
	  1            /usr/bin/python3.6         1         manual mode
	  2            /usr/local/bin/python3.8   2         manual mode

	Press <enter> to keep the current choice[*], or type selection number:

## **Working with Python Virtual Environment**

Here's the command that i usually use. Start with create environment:

	$ pip install virtualenv

Then create virtual environment with specific python version:

	$ virtualenv <environment naame> -p <specific python version location file>
	
On Windows:
  
	> virtualenv venv -p C:\Python\Python36\python.exe

Or

	> virtualenv venv -p C:\Python\Python38\python.exe
	
On Linux:

	$ virtualenv venv -p /usr/bin/python3.6
	
Or

	$ virtualenv venv -p /usr/local/bin/python3.8

Activate the virtual environment:

On Windows:

	> .\venv\Scripts\activate
	
On Linux/Mac:

	$ source venv/bin/activate

Then you can working with `pip` and install the packages that you wanna working with. Use this command to backup all the packages that you've install:

	$ pip freeze > <file name>.txt
	
For example:

	$ pip freeze > requirement.txt
	
Use this command to install the all backup packages:

	$ pip install -r <file name>.txt
	
For example:

    $ pip install -r requirement.txt

Use this command to exit or deactivate the virtual environment:

    $ deactivate

## **Static Virtual Environment in VSCode (Optional)**

First, Install `pylint` in your virtual environment:

	$ pip install pylint

Set VSCode to load the virtual environment in `File > Preferences > Settings` and search `Python`. Bellow the `Python: Default Interpreter Path` set the value to your python executable from the virtual envoronment. For example:

	/home/rohwid/PyEnvironment/work-3.8.11-all-packages/bin/python

And bellow the `Python > Linting: Pylint Path` set the value to your python executable from the virtual envoronment. For example:

	/home/rohwid/PyEnvironment/work-3.8.11-all-packages/bin/pylint

