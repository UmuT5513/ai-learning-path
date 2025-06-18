from abc import ABC, abstractmethod

class Student:
    student_list = [] # öğrencileri nesne olarak tutar
    student_count = 0
    def __init__(self, name, id):
        '''
        parametres:
            courses (list): aldığı derslerin listesi.'''
        self._id = id
        self._student_name = name
        self._courses= []
        self._grades = {} # key: Course objesi, value: int türünde puan
        self._iter_index = 0

    def __str__(self):
        return f"İsim:{self._student_name} ID:{self._id}"
    
    def __iter__(self):
        self._iter_index = 0
        return self
    
    def __next__(self):
        if self._iter_index < len(self._courses):
            course = self._courses[self._iter_index]
            self._iter_index += 1
            return course.course_name
        else:
            raise StopIteration
        
    
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._student_name
    @property
    def grades(self):
        '''
        dict türünde key: Course objesi, value: int türünde puan içeren _grades sözlüğü
        '''
        return self._grades
    @property
    def courses(self):
        return [c.course_name for c in self._courses]
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._student_name = value
        else:
            raise TypeError
        
    @classmethod
    def add_student(cls, data_str):
        '''
        parameters:
            
            data_str (string) : öğrenci ismini ve id sini arada bir boşluk olacak şekilde girin. 
            ÖRN: "jason 1001" 
        
        '''
        name, id = data_str.split(" ")
        std = cls(name, int(id))
        cls.student_list.append(std)
        cls.student_count += 1
        return std
        
    def display_courses(self):
        for course in self:
            yield course

    def add_course(self, value):
        '''value (Course) : Course tipinde nesneleri liste olarak alır.'''
        self._courses = value
        print(f"course ekleme işlemi başarılı!")

    def validate_grade(func):
        def wrapper(self, course_obj, derse_katilim, note):
            if not isinstance(derse_katilim, int) and not isinstance(note, int):
                raise TypeError("Not sadece tam sayi olabilir!")
            if not (100 >= derse_katilim >= 0): 
                raise ValueError("Derse Katilim notu 0-100 arasında olmalı!")
            elif not (100 >= note >= 0):
                raise ValueError("Sinav notu 0-100 arasında olmalı!")
            return func(self, course_obj, derse_katilim, note)
        return wrapper
    
    @validate_grade
    def add_grade(self, course_obj, derse_katilim=0, note=0):
        '''
        Aynı derse iki kez not eklenirse sonuncusu güncellenmiş olur.

        Not eklerken Course nesnesini kullanmalısın (sadece string değil, nesne!).

        note: online dersler için sinavı notu, lab dersleri için lab notu.
        '''
        total_grade = course_obj.hesapla_not(derse_katilim, note)
        self._grades[course_obj] = total_grade

    def display_grades(self):
        for course, grade in self._grades.items():
            print(f"Öğrenci:{self._student_name}\nDers:{course.course_name}\nAldığı Not:{grade}")

    @classmethod
    def display_saved_students(cls):
        return cls.student_list
        

class Course(ABC):
    course_count = 0
    course_list = [] # açık kurslar nesne olarak tutulur
    def __init__(self, course_name, katilim_agirlik):
        self.course_name = course_name
        self.agirlik = katilim_agirlik

    
    def __str__(self):
        return f"kurs adı: {self.course_name}"
    
    @property
    def name(self):
        return self.course_name


    @abstractmethod
    def hesapla_not(self):
        pass

    @classmethod
    @abstractmethod
    def create_course(cls, data_str):
        pass
        



class LabCourse(Course):
    kurs = "Laboratuvar"
    def __init__(self, course_name, katilim_agirlik, lab_agirlik):
        '''Course objesi oluşturulurken ilgili dersin derse katilim notu ağırlığı ve lab/sinav notu ağırlığı parametre olarak girilir.'''
        super().__init__(course_name, katilim_agirlik)
        self.lab_agirlik = lab_agirlik
        

    def __str__(self):
        return f"{super().__str__()}, kurs türü: {LabCourse.kurs}"

    def hesapla_not(self, derse_katilim, lab_notu):
        return derse_katilim*self.agirlik + lab_notu*self.lab_agirlik

    @classmethod
    def create_course(cls, data_str):
        course_name, katilim_agirlik, lab_agirlik = data_str.split("-")
        Course.course_count += 1
        kurs = cls(course_name, float(katilim_agirlik), float(lab_agirlik))
        Course.course_list.append(kurs)
        return kurs

class OnlineCourse(Course):
    kurs = "Çevrimiçi"
    def __init__(self, course_name, katilim_agirlik, sinav_agirlik):
        super().__init__(course_name, katilim_agirlik)
        self.sinav_agirlik = sinav_agirlik
        

    def __str__(self):
        return f"{super().__str__()}, kurs türü: {OnlineCourse.kurs}"
    
    def hesapla_not(self, derse_katilim, sinav_notu):
        return derse_katilim*self.agirlik + sinav_notu*self.sinav_agirlik
    
    @classmethod
    def create_course(cls, data_str):
        course_name, katilim_agirlik, sinav_agirlik = data_str.split("-")
        Course.course_count += 1
        kurs = cls(course_name, float(katilim_agirlik), float(sinav_agirlik))
        Course.course_list.append(kurs)
        return kurs
    

