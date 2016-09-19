from chalice import Chalice

app = Chalice(app_name='johnstonkids')

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

@app.route('/kids')
def index():
    return {'kids':'%s' % (', '.join(KIDS_TO_PARENTS.keys()))}
    
@app.route('/kids/{parent}')
def kids_of_parents(parent):
    return{'kids':PARENTS_TO_KIDS[parent]}

@app.route('/parents/{kid}')
def parents_of_kids(kid):
    return{'parents':KIDS_TO_PARENTS[kid]}
