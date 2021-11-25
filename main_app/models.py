from django.conf import settings
from django.db import models
from django.utils import timezone




class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    EAN = models.CharField(max_length=16, blank=True, default='')
    IMD = models.CharField(max_length=200)
    QTY = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    MOA = models.CharField(max_length=20, blank=True, default='')
    PRI = models.CharField(max_length=20)
    TAX = models.CharField(max_length=20)
    create_date = models.DateTimeField(default=timezone.now())

    def publish(self):
        self.create_date = timezone.now()
        self.save()

    def __str__(self):
            return self.IMD










        # class Post_old(models.Model):
        #     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        #     title = models.CharField(max_length=200)
        #     text = models.TextField()
        #     created_date = models.DateTimeField(default=timezone.now)
        #     published_date = models.DateTimeField(blank=True, null=True)
        #
        #     def publish(self):
        #         self.published_date = timezone.now()
        #         self.save()
        #
        #     def __str__(self):
        #         return self.title










