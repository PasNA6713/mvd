from django.db import models


class SessionModel(models.Model):
    token = models.TextField(primary_key=True)
    session = models.TextField()

    def __repr__(self):
        return f'{self.token} - {self.session}'
    
    def __str__(self):
        return f'{self.token} - {self.session}'