from forms import LoginForm
from flask import Flask, url_for, render_template
from Jobs import Jobs
from User import User
from db_session import create_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/jobs-table')
def job_monitor():
    session = create_session()
    with session.begin():
        job = Jobs()
        job.job = 'Работа'
        job.work_size = 20
        job.collaborators = '4, 5'
        job.is_finished = True
        user = User()
        user.name = 'Egor'
        user.surname = 'Martynenko'
        session.add(user)
        job.team_leader = user
        session.add(job)
        jobs = session.query(Jobs).all()
    return render_template('jobs_monitor.html', jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
