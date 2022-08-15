
from flask import jsonify
from flask import request

def req_completed_index(data, total_count, page, count):
    message = {
            'success': True,
            'result': data,
            'total_results': total_count,
            'page': page,
            'count': count
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp

# success handing
def req_completed(data):
    message = {
            'success': True,
            'result': data
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp


def input_missing(message):
    message = {
            'success': False,
            'message': message,
            'request_url': request.url
    }
    resp = jsonify(message)
    resp.status_code = 400
    return resp

# success handing
def req_created(data):
    message = {
            'success': True,
            'result': data
    }
    resp = jsonify(message)
    resp.status_code = 201
    return resp

# Internal server error
def internal_serv_err(error):
    message = {
            'success': False,
            'message': 'Internal server error : ' + str(error) + ' on:' + str(request.url),
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp
