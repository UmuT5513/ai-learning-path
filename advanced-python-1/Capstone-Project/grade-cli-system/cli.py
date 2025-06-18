from program import Student, Course, OnlineCourse, LabCourse
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(prog="program.py", description="Öğrenci Yönetim Sistemi")
    subparsers = parser.add_subparsers(dest="command")

    add_student_parser = subparsers.add_parser("add-student", help="Yeni Öğrenci Ekle")
    add_student_parser.add_argument("--name", required=True)
    add_student_parser.add_argument("--id", type=int, required=True)
    add_student_parser.set_defaults(func=handle_add_student)

    add_course_parser = subparsers.add_parser("add-course", help="Kurs Ekle")
    add_course_parser.add_argument("--type", required=True)
    add_course_parser.add_argument("--name_katilim_note", required=True)
    add_course_parser.set_defaults(func=handle_add_course)

    assign_course_parser = subparsers.add_parser("assign-course", help="Ders Ata")
    assign_course_parser.add_argument("--id", type=int, required=True)
    assign_course_parser.add_argument("--courses", required=True)
    assign_course_parser.set_defaults(func=handle_assign_course)

    add_grade_parser = subparsers.add_parser("add-grade", help="Not Ekle")
    add_grade_parser.add_argument("--id", type=int, required=True)
    add_grade_parser.add_argument("--course", required=True)
    add_grade_parser.add_argument("--katilim", type=int, required=True)
    add_grade_parser.add_argument("--note", type=int, required=True)
    add_grade_parser.set_defaults(func=handle_add_grade)

    list_students_parser = subparsers.add_parser("list-students", help="Öğrencileri Listele")
    list_students_parser.set_defaults(func=handle_list_students)

    list_courses_parser = subparsers.add_parser("list-courses", help="Dersleri Listele")
    list_courses_parser.set_defaults(func=handle_list_courses)

    list_grades_parser = subparsers.add_parser("list-grades", help="Notları Listele")
    list_grades_parser.add_argument("--id", type=int, required=True)
    list_grades_parser.set_defaults(func=handle_list_grades)

    args = parser.parse_args()
    if hasattr(args, "func"):
        try:
            args.func(args)
        except Exception as e:
            print(f"Hata: {e}")
            sys.exit(1)
    else:
            parser.print_help()

def handle_add_student(args):
    # 1. args.name ve args.id al
    name = args.name
    id = args.id
    # 2. Student.add_student(f"{name} {id}") çağır
    Student.add_student(f"{name} {id}")
    # 3. Başarı mesajını yaz
    print("Öğrenci Sisteme Eklendi")
    # 4. Hata varsa except bloğunda ekrana bas

def handle_add_course(args):
    """
    Komut satırından --type, --name, --katilim ve --note parametreleri alınır.
    Alınan parametreler ile ya OnlineCourse ya da LabCourse oluşturulur.
    Oluşturulan kurs sisteme eklenir ve basarili bir sekilde eklendigini gosteren bir mesaj yazdirilir.
    """
    
    type = args.type
    name_katilim_note = args.name_katilim_note

    if type == "Online":
        OnlineCourse.create_course(name_katilim_note) #not burada sinav_notu
        print("Sisteme bir Çevrimiçi Kurs Eklendi")
    if type == "Lab":
        LabCourse.create_course(name_katilim_note) #note burada lab_notu
        print("Sisteme bir Laboratuvar Kursu Eklendi")

def handle_assign_course(args):
    """
    Komut satırından --id ve --courses parametreleri alınır.
    Alınan parametreler ile ilgili öğrencinin kursları güncellenir.
    Güncelleme işlemi başarılıysa "Kurs Atama İşlemi Başarılı" mesajı yazdırılır.
    """
    ogr_id = args.id
    courses = args.courses

    student = next((s for s in Student.student_list if s.id == ogr_id), None) # studen list içinde generator ile gezinme
    if student:
        student.add_course(courses)
    print("Kurs Atama İşlemi Başarılı")


def handle_add_grade(args):
    """
    Komut satırından --id, --course, --katilim, --note parametreleri alınır.
    Alınan parametreler ile ilgili öğrencinin notu güncellenir.
    Güncelleme işlemi başarılıysa "Not Ekleme Başarılı" mesajı yazdırılır.
    """
    
    ogr_id = args.id
    course_name = args.course
    katilim = args.katilim # burada not eklerken int türünde 0-100 arası not
    note = args.note # int türünde 0-100 arası not

    student = next((s for s in Student.student_list if s.id == ogr_id), None)
    course = next((c for c in Course.course_list if c.name == course_name), None)

    student.add_grade(course, katilim, note)
    print("Not Ekleme Başarılı")


def handle_list_students(args):
    for std in Student.display_saved_students():
        print(std.name, " ")

def handle_list_courses(args):
    courses = (c for c in Course.course_list)
    for c in courses:
        print(c,"\n")

def handle_list_grades(args):
    ogr_id = args.id
    student = next((s for s in Student.student_list if s.id == ogr_id), None)
    print("Öğrencini Puanları aşağıdaki gibidir:\n")
    student.display_grades()

if __name__ == "__main__":
    main()






    