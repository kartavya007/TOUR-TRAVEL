from datetime import datetime
from operator import truediv
from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///KARUt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
class todo(db.Model):
    sno= db.Column(db.Integer , primary_key=True)
    name= db.Column(db.String(200) , nullable=False)
    desc= db.Column(db.String(500) , nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/delete/<int:sno>")
def delete(sno):
    akt=todo.query.filter_by(sno=sno).first()
    db.session.delete(akt)
    db.session.commit()
    return redirect('/home') 
@app.route("/update/<int:sno>",methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        tik=todo.query.filter_by(sno=sno).first()
        tik.name=title
        tik.desc=desc
        db.session.add(tik)
        db.session.commit()
        bik=todo.query.filter_by(sno=sno).first()
        print(bik)
        return redirect('/home') 
    bkt=todo.query.filter_by(sno=sno).first()
    return render_template('update.html',all=bkt) 
@app.route("/home",methods=['GET','POST'])
def home():
     if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        tik=todo(name=title, desc=desc)
        db.session.add(tik)
        db.session.commit()
     tt=todo.query.all()
     return render_template('home.html',all=tt)
if __name__=='__main__':
    app.run(debug=True)