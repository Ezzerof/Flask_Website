import psycopg2

db_name = "studentsRecords"
db_user = "staff_user"
db_password = "197874"
db_host = "localhost"

def getStudentsRecords():
    connect = psycopg2.connect(dbname = db_name, user = db_user, password = db_password, host = db_host)
    cursor = connect.cursor()
    cursor.execute('SELECT id, "Name", "Records" FROM public."Students_records"')
    studentrec = cursor.fetchall()
    cursor.close()
    connect.close()
    return studentrec

def executeQuery(querry):
    connect = psycopg2.connect(dbname=db_name, user=db_user, password = db_password, host = db_host)
    cursor = connect.cursor()
    cursor.execute(querry)
    connect.commit()
    cursor.close()
    connect.close()

def executeStaffQuery(querry):
    connect = psycopg2.connect(dbname=db_name, user=db_user, password = db_password, host = db_host)
    cursor = connect.cursor()
    cursor.execute(querry)
    connect.commit()
    cursor.close()
    connect.close()


def addStudent(name, record):
    executeQuery('INSERT INTO public."Students_records"("Name", "Records") values(\'%s\', \'%s\');commit;' % (name, record))

def updateStudentRecords(name, record, id):
    executeQuery('UPDATE public."Students_records" SET "Name"=\'%s\', "Records"=\'%s\' WHERE id=%s;' % (name, record, id))

def deleteStudentRecords(id):
    executeQuery('DELETE FROM public."Students_records" WHERE id=%s;' % (id))

# Staff zone

def getStaffRecords():
    connect = psycopg2.connect(dbname = db_name, user = db_user, password = db_password, host = db_host)
    cursor = connect.cursor()
    cursor.execute('SELECT id, "Name", "Records" FROM public."Staff_records"')
    staffRec = cursor.fetchall()
    cursor.close()
    connect.close()
    return staffRec

def addStaff(name, record):
    executeStaffQuery('INSERT INTO public."Staff_records"("Name", "Records") values(\'%s\', \'%s\');commit;' % (name, record))

def updateStaffRecords(name, record, id):
    executeStaffQuery('UPDATE public."Staff_records" SET "Name"=\'%s\', "Records"=\'%s\' WHERE id=%s;' % (name, record, id))

def deleteStaffRecords(id):
    executeStaffQuery('DELETE FROM public."Staff_records" WHERE id=%s;' % (id))

# Library zone

def executeLibQuery(querry):
    connect = psycopg2.connect(dbname=db_name, user=db_user, password = db_password, host = db_host)
    cursor = connect.cursor()
    cursor.execute(querry)
    connect.commit()
    cursor.close()
    connect.close()

def getLibRecords():
    connect = psycopg2.connect(dbname = db_name, user = db_user, password = db_password, host = db_host)
    cursor = connect.cursor()
    cursor.execute('SELECT id, "Type", "Author", "Name", "Year" FROM public."Library_records"')
    libRec = cursor.fetchall()
    cursor.close()
    connect.close()
    return libRec

def addLib(type, author, name, year):
    executeStaffQuery('INSERT INTO public."Library_records"("Type", "Author", "Name", "Year") values(\'%s\', \'%s\', \'%s\', \'%s\');commit;' % (type, author, name, year))

def updateLibRecords(type, author, name, year, id):
    executeStaffQuery('UPDATE public."Library_records" SET "Type"=\'%s\', "Author"=\'%s\', "Name"=\'%s\', "Year"=\'%s\' WHERE id=%s;' % (type, author, name, year, id))

def deleteLibRecords(id):
    executeStaffQuery('DELETE FROM public."Library_records" WHERE id=%s;' % (id))

