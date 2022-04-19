from forms.login import LoginForm
from forms.register import RegisterForm
from forms.add_job import JobForm
from flask import Flask, redirect, render_template
from Jobs import Jobs
from User import User
from db_session import create_session
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    with session.begin():
        user = session.query(User).get(user_id)
        session.expunge(user)
    return user


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add-job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    session = create_session()
    with session.begin():
        users = session.query(User).all()
        choices = [(str(user.id), f'{user.name} {user.surname}') for user in users]
        form.team_leader_id.choices = choices
        form.collaborators.choices = choices

    if form.validate_on_submit():
        collaborators = ', '.join(form.collaborators.data)
        session = create_session()
        with session.begin():
            job = Jobs(
                job=form.job.data,
                team_leader_id=form.team_leader_id.data,
                collaborators=collaborators,
                work_size=form.work_size.data,
                is_finished=form.is_finished.data
            )
            session.add(job)
        return redirect('/')
    return render_template('add_job.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        session = create_session()
        with session.begin():
            user = session.query(User).filter(User.email == form.email.data).first()

            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect('/')

            return render_template('login.html',
                                   message='Неправильный логин или пароль',
                                   form=form, title='Авторизация')

    return render_template('login.html', form=form, title='Авторизация')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if form.password != form.password_again:
            render_template('register.html', message='Пароли не совпадают',
                            title='Регистрация', form=form)

        session = create_session()

        with session.begin():
            if session.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html',
                                       message='Такой пользователь уже зарегистрирован',
                                       title='Регистрация', form=form)

            user = User(
                name=form.name.data,
                surname=form.surname.data,
                email=form.email.data,
                position=form.position.data,
                speciality=form.speciality.data,
                address=form.address.data,
                age=form.age.data
            )
            user.set_password(form.password.data)
            session.add(user)
            return redirect('/login')

    return render_template('register.html', form=form)


@app.route('/')
def job_monitor():
    session = create_session()
    with session.begin():
        jobs = session.query(Jobs).all()
    return render_template('jobs_monitor.html', jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
