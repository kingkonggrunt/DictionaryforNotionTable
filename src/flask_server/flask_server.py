from flask import Flask, Response
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    with open(".logs/word.log", 'r') as f:
        content = f.read()
        return Response(content, mimetype='text/plain')
        
    
def run():
    app.run(host='0.0.0.0', port=8080)
    
    
def keep_alive():
    t = Thread(target=run)
    t.start()

    