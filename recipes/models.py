from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    
    name = models.CharField(max_length = 50)
    
    # metodo para ver o nome do atributo na tabela como string
    def __str__(self):
        return self.name


class Recipe(models.Model):

    title = models.CharField(max_length = 65)  # título  
    description = models.CharField(max_length = 150)  # descrição  
    slug = models.SlugField()  # identificador (URL amigável)  
    preparation_time = models.IntegerField()  # tempo de preparo  
    preparation_time_unit = models.CharField(max_length = 65)  # unidade do tempo de preparo (ex: minutos, horas)  
    servings = models.IntegerField()  # porções  
    servings_unit = models.CharField(max_length = 65)  # unidade das porções (ex: pessoas, fatias)  
    preparation_steps = models.TextField()  # etapas do preparo  
    preparation_steps_is_html = models.BooleanField(default = False)  # etapas em formato HTML?  
    created_at = models.DateTimeField(auto_now_add = True) # criado em
    updated_at = models.DateTimeField(auto_now = True) # atualizdo em
    is_published = models.BooleanField(default = False) # foi publicado?
    cover = models.ImageField(upload_to = 'recipes/covers/%Y/%m/%d/') # imagem da capa, cria uma pasta 'covers' com a data de criacao
    category = models.ForeignKey(
        Category, on_delete = models.SET_NULL, null = True
        )
    author = models.ForeignKey(
        User, on_delete = models.SET_NULL, null = True
    )

    def __str__(self):
        return self.title

