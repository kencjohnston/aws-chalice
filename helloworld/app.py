from chalice import Chalice

app = Chalice(app_name='helloworld')

PARENTS_TO_KIDS = {
   'kenny':'rowan and everett',
   'julie':'benny, liam and freya',
   'marty':'morgan',
   'danny':'',
   'jeff':'',
   'cara':'rowan and everett',
   'thore':'benny, liam and freya',
   'kerry':'morgan',
}
KIDS_TO_PARENTS = {
   'rowan':'kenny and cara',
   'everett':'kenny and cara',
   'morgan':'marty and kerry',
   'benny':'julie and thore',
   'liam':'julie and thore',
   'freya':'julie and thore',
}
@app.route('/')
def index():
    return {'hello': 'world'}
@app.route('/kids/{parent}')
def kids_of_parents(parent):
    return{'kids':PARENTS_TO_KIDS[parent]}
@app.route('/parents/{kid}')
def parents_of_kids(kid):
    return{'parents':KIDS_TO_PARENTS[kid]}

# The view function above will return {"hello": "world"}
# whenver you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users/', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.json_body
#     # Suppose we had some 'db' object that we used to
#     # read/write from our database.
#     # user_id = db.create_user(user_as_json)
#     return {'user_id': user_id}
#
# See the README documentation for more examples.
#
