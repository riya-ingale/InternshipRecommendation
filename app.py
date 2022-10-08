from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from MLStudioModels.data_clean import dataclean
from MLStudioModels.similaritymatrix import similarity_matrix
from MLStudioModels.makereco import make_recs
import pandas as pd

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class ScrappedInternships(db.Model):
    iid = db.Column(db.Integer, primary_key = True)
    id = db.Column(db.Integer)
    title = db.Column(db.Text)
    company = db.Column(db.Text)
    location = db.Column(db.Text)
    duration = db.Column(db.Text)
    stipend = db.Column(db.Text)
    perks = db.Column(db.Text)
    numberofopenings= db.Column(db.Integer)
    link = db.Column(db.Text)
    skills = db.Column(db.Text)
    apply_by = db.Column(db.Text)
    applicants = db.Column(db.Text)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/internships', methods=['GET','POST'])
def internships():
    if request.method =="POST":
        search = request.form.get('search')
        result = search.title()
        cards = ScrappedInternships.query.filter_by(title = search ).all()
        if cards:    
            return render_template('internships.html',result = result,records = cards )
        else:
            return render_template('internships.html',result = result, records = None)

    records = ScrappedInternships.query.all()
    return render_template('internships.html', records = records, result = None)


@app.route('/internshipdetails/<int:internship_id>', methods = ['GET','POST'])
def internshipdetails(internship_id):
    internship = ScrappedInternships.query.filter_by(id = internship_id).first()
    df = pd.read_csv('MLStudioModels/internshala_dataset.csv')
    df=dataclean(df)
    
    sim = similarity_matrix(df)
    sim.rename_axis("", axis="columns")
    sim.rename_axis("", axis="columns")
    sim = sim.rename_axis("", axis="columns")
    simrenamed= sim.rename_axis("", axis="index")
    simrenamed.insert(0, 'id', range(0, 0 + len(simrenamed)))
    newsim=simrenamed.set_index('id')
    
    df[df.id == internship_id]
    records = make_recs(newsim, df, internship_id, 3)
    records = records.to_dict('records')
    return render_template('internshipdetails.html', internship = internship, records = records)

@app.route('/addcsvtodb', methods = ['GET'])
def addcsvtodb():
    df = pd.read_csv('MLStudioModels/internshala_dataset.csv')
    df=dataclean(df)
    records = df.to_dict('records')
    for r in records:
        newrecord = ScrappedInternships(id = r['id'], title = r['Title'], company = r['Company'], location = r['Location'], duration= r['Duration'], stipend = r['Stipend'], perks = r['Perks'],numberofopenings = r['Number of Openings'], link = r['Link'], skills = r['Skills Required'] ,apply_by = r['Apply By'], applicants = r['Applicants'])
        db.session.add(newrecord)
    db.session.commit()
    return "Done"

# main driver function
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)