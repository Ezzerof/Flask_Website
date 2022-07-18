from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from website.datab import *

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/students-records', methods=['GET', 'POST'])
@login_required
def sRec():
    studentRecords = getStudentsRecords()
    return render_template("studentRecords.html", StudentRecords=studentRecords, user=current_user)

@views.route("/add", methods=['POST'])
def add():
    sName = request.form['StudentName']
    sRec = request.form['StudentRec']
    addStudent(sName, sRec)
    return redirect(url_for('views.sRec'))

@views.route("/update", methods=['POST'])
def update():
    updated_Name = request.form['updateName']
    updated_Record = request.form['updateRecord']
    updated_id = request.form['id']
    button = request.form['saveOrDelete']
    if button == "Save":
        updateStudentRecords(updated_Name, updated_Record, updated_id)
    elif button == "X":
        deleteStudentRecords(updated_id)
    return redirect(url_for('views.sRec'))



