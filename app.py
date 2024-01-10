from flask import Flask, render_template, jsonify



app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 1000000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 1500000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'New York, USA',
    'salary': '$120,000'
  },
]




@app.route('/')
def hello_world():
  return render_template('index.html', jobs=JOBS)

@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
