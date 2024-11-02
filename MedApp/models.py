from django.db import models
from dashboard.models import Semestre
# Create your models here.



class Category(models.Model):
    Background_Choices=[
    ('','blue'),
    ('card__orange','orange'),
    ('card__green','green')
    ]
    module = models.CharField(max_length=200)
    semestre = models.ForeignKey(Semestre,models.CASCADE,null=True,blank=True)
    icon = models.CharField(max_length=200)
    background=models.TextField(choices=Background_Choices,max_length=200,null=True,blank=True)
    def __str__(self):
        return self.module
    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
class SubCategory(models.Model):
    sous_module = models.CharField(max_length=200)
    category = models.ForeignKey(Category,models.CASCADE) 
    semestre = models.ForeignKey(Semestre,models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.sous_module
    class Meta:
        verbose_name = 'Sous Module'
        verbose_name_plural = 'Sous Modules'
class cour(models.Model):
    titre = models.CharField(max_length=200)
    semestre = models.ForeignKey(Semestre,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_categorie = models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,null=True)
    file = models.FileField(upload_to='Cour/')
    class Meta:
        verbose_name = 'Cour'
        verbose_name_plural = 'Cours'
class support_cour(models.Model):
    titre = models.CharField(max_length=200)
    categorie = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_categorie = models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,null=True)
    file = models.FileField(upload_to='Support du cour/')
    class Meta:
        verbose_name = 'Support du cour'
        verbose_name_plural = 'Support du cours'
class Resume(models.Model):
    titre = models.CharField(max_length=200)
    categorie = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_categorie = models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,null=True)
    file = models.FileField(upload_to='Résumé/')
    class Meta:
        verbose_name = 'Résumé'
        verbose_name_plural = 'Résumés'
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()    