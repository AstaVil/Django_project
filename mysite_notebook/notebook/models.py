from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_name = models.CharField('Kategorija', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('cat', args=[str(self.id)])


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Pavadinimas', max_length=200, null=True, blank=True)
    text = models.TextField('Tekstas', null=True, blank=True)
    picture = models.ImageField('Paveiksliukas', max_length=50, upload_to='notes/img/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='note_cat_name')

    def __str__(self):
        return f' {self.category} / {self.title} / {self.text} / {self.picture}'

    # jei žinutė bus ištrinta, ištrina ir ikelta failą iš db
    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('note', args=[str(self.id)])

