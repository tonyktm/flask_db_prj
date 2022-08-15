from flask import request,render_template
from flask import jsonify
from app import db
from app import app
from app.models import Student,student_schema,student_short_schema,all_student_schema


@app.route('/all')
def index():
    rows = Student.query.all()
    print(rows)
    return render_template('table.html',
                            title='Overview',
                            rows=rows)


@app.route('/table')
def mytable():
    return render_template('table.html')