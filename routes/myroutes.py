from config import app

@app.get('/message')
def greetnow():
    return "Hi, How are you?"

@app.get('/number')
def fun():
    return " 8121234223"