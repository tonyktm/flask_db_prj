def register_routes(app):
     from app.controllers.student_controller import StudentController
     resources(app, 'students', StudentController)

def test():
    print("This is a test function")

def add_route(app, route_name, pattern, controller, action, *args, **kwargs):
    app.add_url_rule(pattern, view_func=controller.as_view(route_name, action), *args, **kwargs)


def resources(app, name, controller):
    add_route(app, 'create_%s' % name, '/%s' % name, controller, 'create', methods=['POST'])
    add_route(app, 'read_%s' % name, '/%s' % name, controller, 'read', methods=['GET'])
    add_route(app, 'read_%s_with_id' % name, '/%s/<id>' % name, controller, 'read', methods=['GET'])
    add_route(app, 'update_%s' % name, '/%s/<id>' % name, controller, 'update', methods=['PUT'])
    add_route(app, 'delete_%s' % name, '/%s/<id>' % name, controller, 'delete', methods=['DELETE'])
