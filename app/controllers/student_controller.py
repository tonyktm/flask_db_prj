from flask import request
from flask import jsonify
from app import db
from app import app
from app.models import Student,student_schema,student_short_schema,all_student_schema
from app.helpers import common_helpers,validation_helper

'''
Routes
students
students?search_name=Tony
students?search_div=11&search_name=Josu
'''

@app.route('/students', methods=["GET"])

def get_students():
    page = request.args.get('page', 1, type=int)
    count = request.args.get('count', 50, type=int)
    name = request.args.get("name", default=None, type=str)
    status = request.args.get("status", default=None, type=str)
    search_name= request.args.get("search_name", default='', type=str)
    search_div= request.args.get("search_div", default='', type=str)

    filters_arr = {}
    if(status is not None):
        filters_arr['status'] = status

    
    record_query = Student.query.filter_by( **filters_arr ).filter(Student.name.contains(search_name)).filter(Student.division.contains(search_div)).order_by(Student.updated_at.desc())
    print(record_query)
    result = all_student_schema.dump(record_query)
    #total = record_query.total
    #record_items = record_query.items
    return jsonify(result=result, total=len(result), success=True)
    #return common_helpers.req_completed_index(result, total, page, count)



@app.route('/students', methods=["POST"])

def post_students():
    required_params = ['name','division']
    validation = validation_helper.validate_presence(request.json, required_params)
    if validation["success"] is False:
        return common_helpers.input_missing(validation["result"])
    name = request.json['name']
    division = request.json['division']
    division = request.json['division']

    student_obj = {'name' : name,'division' : division}
    if 'status' in request.json:
        student_obj['status'] = request.json['status']

    student_rec = Student(**student_obj)

    try:
        db.session.add(student_rec)
        db.session.commit()
        new_student_obj = student_schema.dump(student_rec)
        return common_helpers.req_created(new_student_obj)
    except Exception as e:
        # DB save failed
        return common_helpers.internal_serv_err("Problem inserting into db: " + str(e))


@app.route("/students/<user_name>", methods=["PUT"])
def update_user_active(user_name):
    user_validate = validation_helper.validate_presence_in_db(Student, {'name':user_name})
    if user_validate["success"] is False:
        return common_helpers.input_missing("user " + user_name + " is not present DB")
    else:
        user=user_validate['result']
    
    required_params = ["status"]
    validation = validation_helper.validate_presence(request.json, required_params)
    if validation["success"] is False:
        return common_helpers.input_missing(validation["result"])
    user.status=request.json['status']

    try:
        db.session.commit()
        user_obj = student_schema.dump(user)
        return common_helpers.req_completed(user_obj)
    except Exception as e:
        return common_helpers.internal_serv_err("Problem inserting into db: " + str(e))


@app.route("/students/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user_validate = validation_helper.validate_presence_in_db(Student, {'id':user_id})
    if user_validate["success"] is False:
        return common_helpers.input_missing("user " + user_name + " is not present DB")
    else:
        user=user_validate['result']
    
    db.session.delete(user)
    db.session.commit()
    return common_helpers.req_completed("deleted successfully")




