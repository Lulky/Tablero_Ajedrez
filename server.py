from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_ajedrez():
    return render_template('ajedrez.html', num1=8, num2=8, color1='red', color2='black')


@app.route('/<int:num1>')
def ejercicio(num1):
    return render_template('ajedrez.html', num1=num1, num2=8, color1='red', color2='black')

@app.route('/<int:num1>/<int:num2>')
def Bonus_ninja(num1,num2):
    return render_template('ajedrez.html', num1=num1, num2=num2, color1='red', color2='black')

@app.route('/<int:num1>/<int:num2>/<string:color1>')
def Sensei_ninja(num1,num2,color1):
    return render_template('ajedrez.html', num1=num1, num2=num2, color1=color1, color2='black')

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def Sensei_ninja1(num1,num2,color1,color2):
    return render_template('ajedrez.html', num1=num1, num2=num2, color1=color1, color2=color2)



if __name__ == "__main__":
    app.run(debug=True)