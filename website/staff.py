from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from website.datab import *

staff = Blueprint('staff', __name__)

# Staff records functions


@staff.route('/staff-records', methods=['GET', 'POST'])
@login_required
def staffRec():
    staffRecords = getStaffRecords()
    return render_template("staffRecords.html", StaffRecords=staffRecords, user=current_user)

@staff.route("/add-staff", methods=['POST'])
def add():
    sName = request.form['StaffName']
    sRec = request.form['StaffRec']
    addStaff(sName, sRec)
    return redirect(url_for('staff.staffRec'))

@staff.route("/update-staff", methods=['POST'])
def update():
    updated_Name = request.form['updateStaffName']
    updated_Record = request.form['updateStaffRecord']
    updated_id = request.form['id']
    button = request.form['saveOrDelete']
    if button == "Save":
        updateStaffRecords(updated_Name, updated_Record, updated_id)
    elif button == "X":
        deleteStaffRecords(updated_id)
    return redirect(url_for('staff.staffRec'))

