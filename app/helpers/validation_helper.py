from datetime import datetime

def validate_presence(req_json,item_list):
    if not req_json:
        return {'success': False, 'result': ("Required parameters missing. Required parameters are : '%s'" % (", ".join(item_list))) }
    message = {'success': True, 'result': "validation passed"}
    for x in item_list:
        if not x in req_json:
            message = {'success': False, 'result': ("Required parameters missing. '%s' is a required parameter." % (x)) }
            break
    return message


def validate_presence_in_db(klass, kwargs):
    g = klass.query.filter_by(**kwargs).first()
    if g is not None:
        message = {'success': True, 'result': g}
    else:
        message = {'success': False, 'result': "Could not find %s : %s in %s" %(kwargs.keys(),kwargs.values(), klass.__table__.name)}
    return message

    
