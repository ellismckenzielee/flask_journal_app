from journal_app import app

@app.route('/')
def home():
    return 'Hello App'
    