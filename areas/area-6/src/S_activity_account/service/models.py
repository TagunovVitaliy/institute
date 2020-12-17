from django.db import models

class ScientificActivity(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} {self.description}'

class Teacher(models.Model):
    PART_TIME_TEACHER = 'PART_TIME_TEACHER'
    FULL_TIME_TEACHER = 'FULL_TIME_TEACHER'
    ROLES = [
        (PART_TIME_TEACHER, 'Part-time teacher'),
        (FULL_TIME_TEACHER, 'Full-time teacher'),
    ]
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLES)
    s_activity = models.ForeignKey(ScientificActivity, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.surname} {self.role} {self.s_activity}'

class User(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.teacher}'

class IndividualPlan(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.user}'

class ScientificWork(models.Model):
    SEMINAR = 'SEMINAR'
    PUBLICATION = 'PUBLICATION'
    TYPES = [
        (SEMINAR, 'Seminar'),
        (PUBLICATION, 'Publication'),
    ]
    name = models.CharField(max_length=50)
    point = models.IntegerField(default=0)
    term_date = models.DateField(default=0)
    actual_date = models.DateField(default=0)
    type = models.CharField(max_length=50, choices=TYPES)
    description = models.CharField(max_length=250)
    i_plan = models.ForeignKey(IndividualPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.point} {self.term_date} {self.actual_date} {self.type} {self.description} {self.i_plan}'




