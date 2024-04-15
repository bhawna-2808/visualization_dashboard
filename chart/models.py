from django.db import models

# Create your models here.
class Insight(models.Model):
    end_year = models.CharField(max_length=100, blank=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100, blank=True)
    impact = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField()

    def __str__(self):
        return self.title