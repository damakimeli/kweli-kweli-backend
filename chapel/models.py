from django.db import models


class ChapelVideo(models.Model):
    title        = models.CharField(max_length=255)
    speaker      = models.CharField(max_length=100)
    date         = models.DateField()
    description  = models.TextField(blank=True)
    fb_url       = models.URLField(max_length=500, blank=True, help_text="Paste the Facebook video URL here")
    youtube_id   = models.CharField(max_length=20, blank=True, help_text="YouTube Video ID only e.g. dQw4w9WgXcQ")
    thumbnail    = models.ImageField(upload_to='chapel/thumbnails/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Chapel Video'
        verbose_name_plural = 'Chapel Videos'

    def __str__(self):
        return f"{self.date} — {self.title}"