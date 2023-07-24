from django.db import models

class Message(models.Model):
    YES = 'yes'
    NO = 'no'
    CHOSEN_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    source_message = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    chosen = models.CharField(max_length=3, choices=CHOSEN_CHOICES, default=NO)
    class Meta:
        db_table = 'messages'