from datetime import datetime

from flask import request, make_response, render_template

from project import app, db
from project.models import Ids


@app.route('/')
def main():
    """
    Gets a GET request with ID to check
    check if ID exists in a database and 
    recieve response
    """
    id = request.args.get('id')
    current_timestamp = datetime.now().timestamp()
    my_id = Ids.query.filter_by(id=id).first()
    if id is not None and my_id:
        response = make_response(
            render_template('id_exists.html', 
                timestamp = current_timestamp, 
                id=my_id.id
            ), 
            200
        )
        response.headers['timestamp']  = current_timestamp
        return response
    elif id is not None and my_id is None:
        response = make_response(
            render_template('404_error.html', 
                timestamp = current_timestamp
            ), 
            404
        )
        response.headers['timestamp']  = current_timestamp
        return response
    return render_template('index.html')

@app.route('/add_id')
def add_id():
    """
    Render add_id page
    """
    return render_template('add_id.html')

@app.route('/add', methods=['POST'])
def add():
    """
    Send POST request with ID to add to the database
    """
    new_id = request.form['new_id']
    if Ids.query.filter_by(id=new_id).first() is None:
        message = 'a new ID {} is will be added'.format(new_id)
        id_to_add = Ids(id=new_id)
        db.session.add(id_to_add)
        db.session.commit()
        return render_template('add_id.html', message=message)
    else:
        message = 'the added ID already exists'
        return render_template('add_id.html', message=message)
