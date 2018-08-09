from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))
    
@app.route('/add', methods=['GET' , 'POST'])
def add_student_route():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        print('recieved post request')
        print(request.form['student_name'])
        print(request.form['student_name'])

        add_student(
            request.form['student_name'],
            request.form['student_year'],False)
            
        
        return  render_template('add.html')
@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_student_id(student_id):
    session.query(Student).filter_by(student_id=student_id).delete()
    return redirect(url_for('home'))
    

app.run(debug=True)
