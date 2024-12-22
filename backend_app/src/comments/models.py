from django.db import models

class Comment(models.Model):
    text = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author_name}'

    class Meta:
        ordering = ['created_dt']
