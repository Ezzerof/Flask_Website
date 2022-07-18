from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from website.datab import *

library = Blueprint('library', __name__)

# Lib records functions

@library.route('/lib-records', methods=['GET', 'POST'])
@login_required
def libRec():
    libRecords = getLibRecords()
    return render_template("libraryRecords.html", LibraryRecords=libRecords, user=current_user)

@library.route("/add-lib", methods=['POST'])
def add():
    bType = request.form['BookType']
    bAuthor = request.form['Author']
    bName = request.form['BookName']
    bYear = request.form['Year']
    addLib(bType, bAuthor, bName, bYear)
    return redirect(url_for('library.libRec'))

@library.route("/update-lib", methods=['POST'])
def updateLib():
    updated_Type = request.form['updateType']
    updated_Author = request.form['updateAuthor']
    updated_Name = request.form['updateBookName']
    updated_Year = request.form['updateYear']
    updated_id = request.form['id']
    button = request.form['saveOrDelete']
    if button == "Save":
        updateLibRecords(updated_Type, updated_Author, updated_Name, updated_Year, updated_id)
    elif button == "X":
        deleteLibRecords(updated_id)
    return redirect(url_for('library.libRec'))

