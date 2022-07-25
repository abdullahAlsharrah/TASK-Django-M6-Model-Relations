from django.contrib import admin

from classes import models

to_register = [
    models.Lecture,
    models.Slide,
    models.Course,
    models.Tag,
]

admin.site.register(to_register)
