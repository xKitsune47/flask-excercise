from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def weeklyTodo():
    monday = [
        'go to school',
        'clean the house'
    ]
    tuesday = [
        'go to school',
        'wash the dishes'
    ]
    wednesday = [
        'go to school',
        'wash clothes'
    ]
    thursday = [
        'go to school',
        'make dinner',
        'wash the dishes'
    ]
    friday = [
        'go to school',
        'go to the doctor'
    ]
    saturday = [
        'wash the dishes',
        'wash clothes',
        'clean the house'
    ]
    sunday = [
        'you are free to do anything today'
    ]

    choresDict = {
        'Monday': monday,
        'Tuesday': tuesday,
        'Wednesday': wednesday,
        'Thursday': thursday,
        'Friday': friday,
        'Saturday': saturday,
        'Sunday': sunday
    }
    if request.method == "POST":
        dayOfWeek = request.form.get('dayOfWeek')
        print(dayOfWeek)
        return render_template('index.html', choresDict=choresDict, submittedDay=dayOfWeek,
                               today=datetime.now().strftime('%A'))
    else:
        return render_template('index.html', choresDict=choresDict)


if __name__ == '__main__':
    app.run()
