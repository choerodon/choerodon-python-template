from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "欢迎使用 Choerodon 代码模板"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 80.
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)