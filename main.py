from email import message
from flask import Flask, render_template, request

app =  Flask(__name__)

@app.route('/',methods=['GET'])
def login():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    elif request.method=='POST':
        name=request.form['name']
        psw=request.form['psw']
        pswCheck=request.form['pswCheck']
        email=request.form['email']

        if name=='' or psw=='' or pswCheck=='' or email=='':
            return render_template('register.html', err='Se han de rellenar todos los campos')

        if psw!=pswCheck:
            return render_template('register.html', err='Las contraseñas no coinciden')
        
        return render_template('login.html', msg='Revise su correo, se le ha enviado el link de activación')

@app.route('/password_recovery',methods=['GET','POST'])
def fpassword():
    if request.method=='GET':
        return render_template('password_recovery.html')
    elif request.method=='POST':
        email=request.form['email']
        if email=='':
            return render_template('password_recovery.html', err='Es necesario rellenar el campo email')
        return render_template('login.html', msg='Revise su correo, se le ha enviado la contraseña')

@app.route('/inicio')
def index():
    return render_template('index.html')

@app.route('/inicio/perfil')
def perfil():
    return render_template('perfil.html')

# degustaciones
@app.route('/inicio/degustaciones')
def degustaciones():
    return render_template('degustaciones.html')

# galardones
@app.route('/inicio/galardones')
def galardones():
    return render_template('galardones.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000)