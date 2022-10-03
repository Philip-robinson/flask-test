# Flask test

This is a very simple application, it produces a web interface
and API on data read from a CSV file
no __"proper"__ database.

It relates to displaying information about a portfolio of shares
presented in a CSV file

you need to have python3 python3-venv and flask installed

python3 and python3-venv are both os level installations
flask can be installed with pip

On ubuntu:
```
sudo apt-get install python3
sudo apt-get install python3-venv
```

Standard process is to create a virtual invironment, this is I think not 
necessary but allows an application to be run in isolation from other
applications 

You create the the virtual environment inside the directory
in which youy are to create the code.

```
python3 -m venv venv
```

And actrivate it with
```
source venv/bin/activate
```
microsoft equivalent

```
venv\\Scripts\\activate
```

You can now install flask into this virtual environment (venv)

```
pip install flask
```

## The application

There are two files __database.py__ and __index.py__

### database.py

This file contains a class that reads the source csv file
__portfolio.csv__ into a list of data and then gives some
access to the data in there. This is currently is read only 
and has no mechanism to write back the data.

### index.py

This is the file that is the controler (in mvc style) it contains
4 functions 2 of which produce web pages and two are
API end points producing json.

After these have been created the server is started on port 8010.

__index.py__ can be executed:

```
python index.py
```

