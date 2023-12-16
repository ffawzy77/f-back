from django.db import models

class Event(models.Model):
    event_type = models.CharField(max_length=100)
    event_id = models.TextField(unique=True)
    check_in = models.DateTimeField(help_text="YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]")

    def __str__(self):  #__str__. This method is used to represent the object as a string when it's printed or displayed.
        return f"{self.event_type} - {self.event_id}"
# 21211