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

There are five files:
* __database.py__ 
* __index.py__
* __templates/index.html__
* __templates/details.html__
* __static/style.css__

### static files style.css

files put in the static directory are automatically made available
as stored.

the file __static/style.css__ can be accessed in this application
as __http://localhost:8010/static/style.css__

### template files stored under templates

the directory __templates__ is where template files are expected to be found

there are two in this is a fairly standard style of template using {{field}}
and {% some code %} style of modifying the code.

There are two templates __templates/index.html__ is for the home page and looks
like:
```
<html>
    <head>
        <title>{{ title }}</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <table>
        {% for company in companies: %}
                <tr><td><a href="/detail/{{company}}">{{ company }}</a></td></tr>
        {% endfor %}
        </table>
    </body>
</html>
```
A fairly standard syntax, perhaps a bit old fashined but works well:

__{{ url_for('static', filename='style.css') }}__

specifies the url to style.css in the static directory and is converted to
__/static/style.css__ but may look different if the app had been configured differently.

The other __templates/detail.html__ is similar.
### database.py

This file contains a class that reads the source csv file
__portfolio.csv__ into a list of data and then gives some
access to the data in there. This is currently is read only 
and has no mechanism to write back the data.

It uses a built in csv reader to read the __portfolio.csv__ file.
There is a single class called __Portfolio__ which has a __load()__ method
which loads the contents of the csv file into mewmory

```
import csv
from datetime import datetime

to_num = lambda num: float(num.replace(",", ""))
class Portfolio:
    data = {}

    def load(self):
        """ load the file portfolio.csv into the field data """
        with open('portfolio.csv') as csv_file:
            print("Loading portfolio.csv")
            csv_reader = csv.reader(csv_file, delimiter=',')
            first = True
            for row in csv_reader:
                # skip first line
                if first:
                    first=False
                else:
                    self.data[row[0]]={
                        "name": row[0],
                        "shares": int(to_num(row[1])),
                        "price": round(100*to_num(row[2])/to_num(row[10]))/100,
                        "value": to_num(row[3]),
                        "cost": to_num(row[4]),
                        "profit": to_num(row[5]),

```
The numbers within the csv file contain commas hence the labmda to\_num is used to
convert them to floats. 

This method extracts just some columns and stores them as a list of dictionaries as
the variable  __data__.

There are then two other methods which extract that data.

```
    def names(self):
        """ return a list of share names """
        return [v['name'] for _,v in self.data.items()]
```
This returns a list of names of shares, the reason for the list __"Comprehension"__ is that
if we just returned a list of keys (which is what we would do in Java for instance) we would 
get a list of Keys not strings, which just makes the rest of life confusing, for instance 
the Json serialiser does not understand. I think in the python world it is expected that
most data transfers are native typess; which includes list and dict.

The other method is similar:
```
    def detail(self, key):
        """ return a dictionary of fields pertinent to the specified named share holing"""
        print("detail ", key, "->", self.data[key])
        return self.data[key]
```

This does not need the list __"Comprehension"__ as the value being returned is already a dict.
### index.py

This is the file that is the controler (in mvc style) it contains
4 functions 2 of which produce web pages and two are
API end points producing json.

These are very simple, and what I like is that like Spring in the java world the urls are 
in the same place as the code.

```
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    """ Home page - a list of companies 
        using the templates templates/index.html """
    return render_template('index.html',
        title='Company display',
        companies=pf.names())
```
This function takes the template __templates/index.html__ and populates it with data
two routes are specified / and /index, the render template method is given named parameters
which names are then made available to the template.

Very neat.

Another method returns Json API style:
```
@app.route("/api/shares")
def companies():
    """ A list of companies as json """
    print("List of shares owned in portfolio")
    return {"shares": pf.names()}
```

After these have been created the server is started on port 8010.

__index.py__ can be executed:

```
python index.py
```

This works because there is a line at the end of the file:
```
app.run(host="0.0.0.0", port=8010)
```

which runs the server, this is only intended when developing, as the app can be
run in a slightly different way for production.

