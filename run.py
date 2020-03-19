from journal_app import app
import webbrowser

if __name__ == '__main__':
    port=5000
    #url = 'localhost:{}'.format(port)
    #webbrowser.open(url)
    app.run(debug=False, port=port)
