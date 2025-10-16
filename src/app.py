from flask import Flask

app = Flask(__name__)
app = Flask(__name__)

@app.route('/')

def home():
    return "¡Hola desde DevOps y Git!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# Ejemplo en Node.js:

# const express = require('express');
# const app = express();
# app.get('/', (req, res) => res.send('¡Hola desde DevOps y Git!'));
# app.listen(3000, () => console.log('App corriendo en puerto 3000'));
