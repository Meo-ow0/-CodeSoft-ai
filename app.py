import webbrowser
from threading import Timer
from flask import Flask, request, jsonify, render_template
from tictactoe import get_best_move

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ai_move', methods=['POST'])
def ai_move():
    data = request.json
    board = data['board']
    move = get_best_move(board)
    return jsonify({'move': move})

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000'
    Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(debug=True, host='0.0.0.0', port=5000)
