from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/', methods=["GET"])
def index():
        return render_template("index.html")

@app.route('/calendar', methods=["GET"])
def calendar():
        return render_template("calendar.html")

@app.route('/hallHire', methods=["GET"])
def hallHire():
        return render_template("hallHire.html")

@app.route('/supportUs', methods=["GET"])
def supportUs():
        return render_template("supportUs.html")

@app.route('/supportUsDonate', methods=["GET"])
def supportUsDonate():
        return render_template("supportUsDonate.html")

@app.route('/supportUsJoin', methods=["GET"])
def supportUsJoin():
        return render_template("supportUsJoin.html")

@app.route('/supportUsVolunteer', methods=["GET"])
def supportUsVolunteer():
        return render_template("supportUsVolunteer.html")

@app.route('/whatWeAreAbout', methods=["GET"])
def whatWeAreAbout():
        return render_template("whatWeAreAbout.html")

@app.route('/news', methods=["GET"])
def news():
        return render_template("news.html")

@app.route('/history', methods=["GET"])
def history():
        return render_template("history.html")