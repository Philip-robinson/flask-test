from flask import Flask, render_template
import database


pf = database.Portfolio()
pf.load()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    """ Home page - a list of companies 
        using the templates templates/index.html """
    return render_template('index.html',
        title='Company display',
        companies=pf.names())
                             
@app.route('/detail/<name>')
def detail(name):
    """ Details page - a list of information about 1 company 
        using the templates templates/detail.html """
    print("Got name "+name) 
    print("Deatil is ", pf.detail(name))
    ret = pf.detail(name)
    ret['timestamp'] = ret['timestamp'].strftime("%d/%m/%Y %H:%M")
    return render_template('detail.html',
        title='Company display for '+name,
        detail=ret)

@app.route("/api/shares")
def companies():
    """ A list of companies as json """
    print("List of shares owned in portfolio")
    return {"shares": pf.names()}

@app.route("/api/share/detail/<name>")
def company(name):
    """ The details of one company (as specified by name)
        as json """
    print("detail of shares owned for ", name)
    ret = pf.detail(name)
    # convert timestamp to iso standard string
    ret['timestamp'] = ret['timestamp'].isoformat()
    return ret

# start the application on port 8010
app.run(port=8010)
