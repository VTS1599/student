from firebase import firebase
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

#firebase = firebase.FirebaseApplication('https://placements-49807.firebaseio.com/', None)

config = {
  "apiKey": "AIzaSyDOcELXS2QwAdcJiftqTB9kYKZEvkjD4q0",
  "authDomain": "placements-49807.firebaseapp.com",
  "databaseURL": "https://placements-49807.firebaseio.com/",
  "storageBucket": "placements-49807.appspot.com",
  "serviceAccount": "placements-49807-firebase-adminsdk.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

#authenticate a user
user = auth.sign_in_with_email_and_password("17jg1a1250.tejaswi@gvpcew.ac.in", "Gvpcew@2017")

# Get a reference to the database service
db = firebase.database()

@app.route('/success/<name>')
def success(name):
   return 'succesfully registered %s ' % name

@app.route('/application',methods = ['POST', 'GET'])
def appli():
   if request.method == 'POST':
      name = request.form['name']
      rollno = request.form['rollno']
      branch = request.form['branch']
      aggregate = request.form['aggregate']
      backlogs = request.form['backlogs']
      yos = request.form['year']
      emailid = request.form['emailid']
      contact = request.form['contactno']
      gender = request.form['gender']

      data =  { 'Name': name,
                #'RollNo': rollno,
		'Percentage': aggregate,
                'Branch': branch,
		'Backlogs': backlogs,
	        'Year of study': yos,
		'Email': emailid,
	        'Contact': contact,
	        'Gender': gender
              }
      #resultPut = firebase.put('/student',rollno,data)
      #print(resultPut)
      result=db.child("student").child(rollno).set(data,user['idToken'])
      print(result)

      return redirect(url_for('success',name = name))
   else:
      name = request.args.get('name')
      return redirect(url_for('success',name = name))
   
if __name__ == '__main__':
   app.run(debug = True)