from django.db import models
from django.urls import reverse
from django.conf import settings


class Company(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique='created')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='Images/%Y/%m/%d', null=True)
    file = models.FileField(upload_to='CSV/%Y/%m/%d')

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stock:detail', args=[self.id, self.slug])


class Investors(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='companies', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return 'Investor {}'.format(self.user)



