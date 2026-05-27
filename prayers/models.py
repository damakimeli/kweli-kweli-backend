from django.db import models


class PrayerRequest(models.Model):
    name         = models.CharField(max_length=150)
    email        = models.EmailField(blank=True)
    request      = models.TextField()
    is_prayed_for = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Prayer Request'
        verbose_name_plural = 'Prayer Requests'

    def __str__(self):
        return f"{self.name} — {self.submitted_at.strftime('%d %b %Y')}"