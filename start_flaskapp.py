from app import create_app

app = create_app()
app.run(host='0.0.0.0', debug=True) # 127.0.0.1 == localhost