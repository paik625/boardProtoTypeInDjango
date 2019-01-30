
from django.db import models
from django.urls import reverse_lazy
from django.utils.timezone import now
from datetime import datetime
# Create your models here.
#BMI_


# Create your models here.


class BOARD(models.Model):
    author = models.TextField(null=False, max_length=20)
    title = models.TextField(null=False)
    content = models.TextField(null=False)
    create_at = models.DateTimeField(default=now, editable=False)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return self.author + "님의 게시글"

    def get_absolute_url(self):
        return reverse_lazy('board_detail', args=[self.id])

    @property
    def hit_count(self):
        self.hit = self.hit + 1
        self.save()
        return""

    class Meta:
        ordering = ['-create_at']
