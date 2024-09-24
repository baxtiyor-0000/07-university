from django.db import models


class Faculty(models.Model):
     name = models.CharField(max_length=100)

     def __str__(self):
         return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Kafedra(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
