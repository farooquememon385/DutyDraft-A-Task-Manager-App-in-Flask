from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
import forms

@app.route('/')
@app.route('/index')

@app.route('/tasks')
def getTask():
    form = forms.AddTaskForm()
    get_flashed_messages()
    tasks = Task.query.all()
    return render_template('addtask.html', form=form, tasks=tasks, 
    Action = 'Add Task', action='/addtask')

@app.route('/addtask', methods = ['POST'])
def addTask():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print(form.title.data,'added successfully')
        t = Task(title=form.title.data, dueDate=form.dueDate.data)
        db.session.add(t)
        db.session.commit()
        flash('Task Added successfully')
        return redirect(url_for('getTask'))
    return "Form not validated"

@app.route('/edit/<int:task_id>', methods =['GET', 'POST'] )
def editTask(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.dueDate = form.dueDate.data
            db.session.commit()
            flash(task.title+' has been updated')
            return redirect('/tasks')
        form.title.data = task.title
        form.dueDate.data = task.dueDate
        tasks = Task.query.all()
        return render_template('addtask.html', 
        form=form, tasks=tasks, Action='Update Task',
        action = f'/edit/{task_id}')
    return redirect(url_for('getTask'))