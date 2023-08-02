## **Install Python Ubuntu 22.04**

By default Python were installed on Ubuntu 22.04 with version 3.10. So, first thing to begin the python journey is by installing `pip` (python package manager) and virtualenv (manage python package inside an environment).

Check the python version to make sure the python is already installed:

```bash
$ python3 -V
```

Install `pip`:

```bash
$ sudo apt install pip
```

Install `virtualenv`:

```bash
$ pip install virtualenv
```

## **Working with Python Virtual Environment**

Then create virtual environment with specific python version:

```bash
$ virtualenv venv -p /usr/bin/python3.10
```

Activate the virtual environment:
	
On Linux/Mac:

```bash
$ source venv/bin/activate
```

Then you can working with `pip` inside the virtual environment and install the packages that you wanna use. Then use this command to backup all the packages that you've install:

```bash
$ pip freeze > <file name>.txt
```
	
For example:

```bash
$ pip freeze > requirements.txt
```
	
Use this command to install the all backup packages:

```bash
$ pip install -r <file name>.txt
```

For example:

```bash
$ pip install -r requirements.txt
```

Use this command to exit or deactivate the virtual environment:

```bash
$ deactivate
```

## **Install New Python Version**

Install python 3.11 or latest:

```bash
$ sudo apt install python3.11
```

Install python 3.9 or oldest (e.g. 3.8, 3.7, and etc):

```bash
$ sudo apt install python3.9 python3.9-distutils
```

## **Change Python Version for Development**

Create new virtual environment, usually in the specific project directory that used for development (e.g. `my-python-app`).

```bash
$ mkdir my-python-app
$ cd my-python-app
$ virtualenv venv -p /usr/bin/python3.10
```

Activate the virtual environment:
	
On Linux/Mac:

```bash
$ source venv/bin/activate
```

Create your own code (e.g. `main.py`) and runs with this command:

```bash
$ python main.py
```

## **Handle Multiple Python Version by Changing with Update Alternative**

**This step is not recommended to do**, it will change the entire OS python system since Ubuntu were build and runs python too. 

Set the ID of each python version in Update Alternative. 

```bash
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 2
$ sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.9 3
$ sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.8 4
```

List or look at the list of update alternative:

```bash
$ update-alternatives --list python
/usr/bin/python3.10
/usr/bin/python3.11
/usr/local/bin/python3.9
/usr/local/bin/python3.8
```

Change or update the default pyhton version who run in operating system (Ubuntu):

```bash
$ sudo update-alternatives --config python
```

Select the pyhton version by enter it's ID:

```bash
There are 2 choices for the alternative python (providing /usr/bin/python).

Selection    Path                      Priority   Status
------------------------------------------------------------
* 0            /usr/local/bin/python3.8   2         auto mode
	1            /usr/bin/python3.6         1         manual mode
	2            /usr/local/bin/python3.8   2         manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

