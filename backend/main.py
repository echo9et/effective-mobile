import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Effective Mobile!'

@app.get("/health")
async def liveness():
    return {"status": "ok"}

if __name__ == '__main__':
    port = int(os.environ.get('BACKEND_PORT', 8000))
    app.run(debug=True, host="0.0.0.0", port=port)