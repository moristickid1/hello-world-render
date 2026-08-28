from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '''
    <html>
      <head>
        <title>Hello World</title>
        <style>
          body {
            height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: -apple-system, Segoe UI, Roboto, sans-serif;
            background: #0d1219;
            color: #e9edf3;
          }
          h1 {
            font-size: 48px;
            font-weight: 700;
            letter-spacing: -0.02em;
          }
        </style>
      </head>
      <body>
        <h1>Hello, World!</h1>
      </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
