from fastapi import FastAPI, HTTPException
from .schemas import StudentCreate, GradeCreate, GroupCreate, SubjectCreate, TeacherCreate, TimetableCreate
import odoorpc

# Connecting API to Odoo Database
odoo = odoorpc.ODOO('localhost', port=8069)
try:
    odoo.login('odoo', 'panjiyevabdulaziz77@gmail.com', 'admin@odoo')
except odoorpc.error.RPCError as e:
    raise HTTPException(status_code=500, detail="Failed to connect to Odoo: {}".format(e))

app = FastAPI()

# Define a function to handle Odoo errors and exceptions
def handle_odoo_error(e):
    raise HTTPException(status_code=500, detail="Odoo error: {}".format(e))

# Ensure Base64 string is properly padded in order to store image field
def ensure_base64_padding(base64_str):
    missing_padding = len(base64_str) % 4
    if missing_padding:
        base64_str += '=' * (4 - missing_padding)
    return base64_str

# Define CRUD operations for Student Entity
@app.post("/students/")
def create_student(student: StudentCreate):
    try:
        profile_picture = ensure_base64_padding(student.profile_picture)
        student_id = odoo.env['student'].create({
            'name': student.name,
            'email': student.email,
            'phone': student.phone,
            'address': student.address,
            'profile_picture': profile_picture
        })
        return {"id": student_id}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.get("/students/")
def read_students():
    try:
        students = odoo.env['student'].search_read([], ['id', 'name', 'email', 'phone', 'address', 'profile_picture'])
        return students
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    try:
        stud = odoo.env['student'].browse(student_id)
        if not stud.exists():
            raise HTTPException(status_code=404, detail="Student not found")
        profile_picture = ensure_base64_padding(student.profile_picture)
        stud.write({
            'name': student.name,
            'email': student.email,
            'phone': student.phone,
            'address': student.address,
            'profile_picture': profile_picture
        })
        return {"detail": "Student successfully updated"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    try:
        student = odoo.env['student'].browse(student_id)
        if not student.exists():
            raise HTTPException(status_code=404, detail="Student not found")
        student.unlink()
        return {"detail": "Student deleted"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

# Define CRUD operations for Grade Entity
@app.post("/grades/")
def create_grade(grade: GradeCreate):
    try:
        grade_id = odoo.env['grade'].create({
            'student_id': grade.student_id,
            'subject_id': grade.subject_id,
            'grade': grade.grade,
            'semester': grade.semester
        })
        return {"id": grade_id}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.get("/grades/")
def read_grades():
    try:
        grades = odoo.env['grade'].search_read([], ['id', 'student_id', 'subject_id', 'grade', 'semester'])
        return grades
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.put("/grades/{grade_id}")
def update_grade(grade_id: int, grade: GradeCreate):
    try:
        grd = odoo.env['grade'].browse(grade_id)
        if not grd.exists():
            raise HTTPException(status_code=404, detail="Grade not found")
        grd.write({
            'student_id': grade.student_id,
            'subject_id': grade.subject_id,
            'grade': grade.grade,
            'semester': grade.semester
        })
        return {"detail": "Grade successfully updated"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.delete("/grades/{grade_id}")
def delete_grade(grade_id: int):
    try:
        grade = odoo.env['grade'].browse(grade_id)
        if not grade.exists():
            raise HTTPException(status_code=404, detail="Grade not found")
        grade.unlink()
        return {"detail": "Grade deleted"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

# Define CRUD operations for Group
@app.post("/groups/")
def create_group(group: GroupCreate):
    try:
        group_id = odoo.env['group'].create({
            'name': group.name,
            'description': group.description
        })
        return {"id": group_id}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.get("/groups/")
def read_groups():
    try:
        groups = odoo.env['group'].search_read([], ['id', 'name', 'section', 'teacher_id'])
        return groups
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.put("/groups/{group_id}")
def update_group(group_id: int, group: GroupCreate):
    try:
        grp = odoo.env['group'].browse(group_id)
        if not grp.exists():
            raise HTTPException(status_code=404, detail="Group not found")
        grp.write({
            'name': group.name,
            'description': group.description
        })
        return {"detail": "Group successfully updated"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.delete("/groups/{group_id}")
def delete_group(group_id: int):
    try:
        group = odoo.env['group'].browse(group_id)
        if not group.exists():
            raise HTTPException(status_code=404, detail="Group not found")
        group.unlink()
        return {"detail": "Group deleted"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

# Define CRUD operations for Subject Entity
@app.post("/subjects/")
def create_subject(subject: SubjectCreate):
    try:
        subject_id = odoo.env['subject'].create({
            'name': subject.name,
            'description': subject.description
        })
        return {"id": subject_id}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.get("/subjects/")
def read_subjects():
    try:
        subjects = odoo.env['subject'].search_read([], ['id', 'name', 'code'])
        return subjects
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.put("/subjects/{subject_id}")
def update_subject(subject_id: int, subject: SubjectCreate):
    try:
        subj = odoo.env['subject'].browse(subject_id)
        if not subj.exists():
            raise HTTPException(status_code=404, detail="Subject not found")
        subj.write({
            'name': subject.name,
            'description': subject.description
        })
        return {"detail": "Subject successfully updated"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.delete("/subjects/{subject_id}")
def delete_subject(subject_id: int):
    try:
        subject = odoo.env['subject'].browse(subject_id)
        if not subject.exists():
            raise HTTPException(status_code=404, detail="Subject not found")
        subject.unlink()
        return {"detail": "Subject deleted"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

# Define CRUD operations for Teacher Entity
@app.post("/teachers/")
def create_teacher(teacher: TeacherCreate):
    try:
        teacher_id = odoo.env['teacher'].create({
            'name': teacher.name,
            'email': teacher.email,
            'phone': teacher.phone,
            'address': teacher.address
        })
        return {"id": teacher_id}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.get("/teachers/")
def read_teachers():
    try:
        teachers = odoo.env['teacher'].search_read([], ['id', 'name', 'email', 'phone', 'address'])
        return teachers
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.put("/teachers/{teacher_id}")
def update_teacher(teacher_id: int, teacher: TeacherCreate):
    try:
        teach = odoo.env['teacher'].browse(teacher_id)
        if not teach.exists():
            raise HTTPException(status_code=404, detail="Teacher not found")
        teach.write({
            'name': teacher.name,
            'email': teacher.email,
            'phone': teacher.phone,
            'address': teacher.address
        })
        return {"detail": "Teacher successfully updated"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int):
    try:
        teacher = odoo.env['teacher'].browse(teacher_id)
        if not teacher.exists():
            raise HTTPException(status_code=404, detail="Teacher not found")
        teacher.unlink()
        return {"detail": "Teacher deleted"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

# Define CRUD operations for Timetable Entity
@app.post("/timetables/")
def create_timetable(timetable: TimetableCreate):
    try:
        timetable_id = odoo.env['timetable'].create({
            'group_id': timetable.group_id,
            'weekday': timetable.weekday,
            'period': timetable.period,
            'subject_id': timetable.subject_id
        })
        return {"id": timetable_id}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.get("/timetables/")
def read_timetables():
    try:
        timetables = odoo.env['timetable'].search_read([], ['id', 'group_id', 'weekday', 'period', 'subject_id'])
        return timetables
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.put("/timetables/{timetable_id}")
def update_timetable(timetable_id: int, timetable: TimetableCreate):
    try:
        tmtbl = odoo.env['timetable'].browse(timetable_id)
        if not tmtbl.exists():
            raise HTTPException(status_code=404, detail="Timetable not found")
        tmtbl.write({
            'group_id': timetable.group_id,
            'weekday': timetable.weekday,
            'period': timetable.period,
            'subject_id': timetable.subject_id
        })
        return {"detail": "Timetable successfully updated"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)

@app.delete("/timetables/{timetable_id}")
def delete_timetable(timetable_id: int):
    try:
        timetable = odoo.env['timetable'].browse(timetable_id)
        if not timetable.exists():
            raise HTTPException(status_code=404, detail="Timetable not found")
        timetable.unlink()
        return {"detail": "Timetable deleted"}
    except odoorpc.error.RPCError as e:
        handle_odoo_error(e)
