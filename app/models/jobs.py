from django.db import models
import uuid

class Job(models.Model):

    SITE_CHOICES = [
        ("onsite", "Onsite"),
        ("remote", "Remote"),
        ("hybrid", "Hybrid"),
    ]

    TYPE_CHOICES = [
        ("full-time", "Full-Time"),
        ("part-time", "Part-Time"),
        ("contract", "Contract"),
        ("internship", "Internship"),
    ]   

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    company = models.CharField(max_length=200, null=True, blank=True)
    site = models.CharField(max_length=50, choices=SITE_CHOICES, default="onsite")
    job_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    experience = models.CharField(max_length=100)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Responsibility(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    job = models.ForeignKey(Job, related_name='responsibilities', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"Responsibility for {self.job.title}"

class Requirement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    job = models.ForeignKey(Job, related_name='requirements', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"Requirement for {self.job.title}"

class Benefit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    job = models.ForeignKey(Job, related_name='benefits', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"Benefit for {self.job.title}"


class SalaryRange(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    job = models.OneToOneField(Job, related_name='salary_range', on_delete=models.CASCADE)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Salary Range for {self.job.title}: {self.min_salary} - {self.max_salary}"