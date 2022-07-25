from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)
    


class Lecture(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name


class Slide(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    lecture = models.OneToOneField(
        Lecture,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return self.name
    class Meta:
        abstract = True


class Assignment(Slide):
    pass
    # name = models.CharField(max_length=30)
    # link = models.URLField()
    # lecture = models.OneToOneField(
    #     Lecture,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    # def __str__(self):
    #     return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(
        Course, related_name="tags"
    )
    def __str__(self):
        return self.name
