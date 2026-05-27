from django.db import models


class Course(models.Model):
    YEAR_CHOICES = [('1', 'Year One'), ('2', 'Year Two'), ('3', 'Year Three')]

    name        = models.CharField(max_length=200)
    year        = models.CharField(max_length=1, choices=YEAR_CHOICES)
    description = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['year', 'name']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f"Year {self.year} — {self.name}"


class Application(models.Model):
    PROGRAMME_CHOICES = [
        ('year1', 'Year 1 — Foundation'),
        ('year2', 'Year 2 — Ministry'),
        ('year3', 'Year 3 — Leadership'),
    ]
    STATUS_CHOICES = [
        ('pending',  'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]

    full_name   = models.CharField(max_length=200)
    email       = models.EmailField()
    phone       = models.CharField(max_length=20)
    programme   = models.CharField(max_length=10, choices=PROGRAMME_CHOICES)
    motivation  = models.TextField()
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return f"{self.full_name} — {self.programme} ({self.status})"