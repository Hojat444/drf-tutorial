from django.db import models

class Concept(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Relationship(models.Model):
    origin = models.ForeignKey(Concept, related_name='origin_relationships', on_delete=models.CASCADE)
    destination = models.ForeignKey(Concept, related_name='destination_relationships', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.origin} -> {self.destination}"
