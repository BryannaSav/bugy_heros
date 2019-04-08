from flask import Flask, render_template, request, session
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def hello_world():
    return render_template('index.html') 

@app.route('/new/hero')         
def new_hero_form():
    return render_template('form_page.html') 

@app.route('/create', methods="POST")         
def create_new_hero():
    session['real_name']=request.form['real_name']
    session['hero_name']=request.form['hero_name']
    session['nemesis_name']=request.form['nemesis_name']
    session['num_of_powers']=request.form['numof_powers']
    return redirect('/show.html')

@app.route('/show')         
    def hello_world():
    return render_template('show.html', realname=session['real_name'], hero_name=session['heroname'], nemesis_name=session['nemesis_name'], num_of_powers=session['num_of_powers']) 

if __name__=="__main__":    
    app.run(debug=True)