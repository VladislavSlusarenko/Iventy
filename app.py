from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    schedules = {
        'Каріна': [
            {'event_id': 'Подія 1', 'start': '10:00', 'location': 'Місце 1'},
            {'event_id': 'Подія 2', 'start': '12:00', 'location': 'Місце 2'}
        ]
    }
    return render_template('index.html', schedules=schedules)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

