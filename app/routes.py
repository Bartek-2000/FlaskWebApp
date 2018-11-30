from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    obrazki = ["https://vignette.wikia.nocookie.net/youtubepoop/images/6/6e/Qwertyuiopasdfghjklzxcvbnm.jpg/revision/latest?cb=20180812190747", "https://i.stack.imgur.com/WOlr3.png", "https://demotywatory.pl/uploads/201704/1492981008_lfhb2h_fb_plus.jpg"]
    return render_template('galeria.html', obrazki=obrazki)

@app.route('/user/<name>')
def getUser(name):
    
    return render_template('user.html', name=name)

