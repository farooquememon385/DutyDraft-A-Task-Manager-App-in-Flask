from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), nullable = False)
    dueDate = db.Column(db.Date, nullable = False)

    def __repr__(self):
        return f'{self.title} is due on {self.dueDate}'
    

    # from app import app, db
    # with app.app_context():
    #   db.create_all()

    # add data to database
    # t = Task(title = "title", dueDate = datetime.utcnow())
    # db.session.add(t)
    # db.session.commit()

    # see tasks
    # tasks = Task.query_all()