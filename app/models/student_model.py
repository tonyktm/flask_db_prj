from app import db
from app import ma
from datetime import datetime


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False, unique=True)
    division = db.Column(db.String())
    status = db.Column(db.String(100),default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id','name', 'division', 'status','updated_at','created_at')


class StudentShortSchema(ma.Schema):
    class Meta:
        fields = ('name', 'division')


student_schema = StudentSchema()
student_short_schema=StudentShortSchema()
all_student_schema = StudentSchema(many=True)
