# Importa as classes necessárias do Django para criação de modelos e autenticação de usuários.
from django.db import models
from django.contrib.auth.models import User

# Define as opções de status possíveis para um post.
STATUS = (
    (0, 'Draft'), #Rascunho
    (1, 'Publish') #Publicado
)

# Define o modelo de Post.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # Campo para armazenar o título do post.
    slug = models.SlugField(max_length=200, unique=True) # Campo para armazenar o slug (URL amigável) do post.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post') # Campo de chave estrangeira que relaciona o autor do post a um usuário do Django.
    updated_on = models.DateTimeField(auto_now=True) # Campo para armazenar a data e hora da última atualização do post.
    content = models.TextField() # Campo para armazenar o conteúdo do post em formato de texto longo.
    created_on = models.DateTimeField(auto_now_add =True) # Campo para armazenar a data e hora de criação do post.
    status = models.IntegerField(choices=STATUS, default=0) # Armazenar o status do post, usando as opções em STATUS.

    class Meta: # Metaclasse que especifica metadados do modelo, como a ordenação padrão.
        ordering = ['-created_on'] # Ordena os posts pela data de criação em ordem decrescente.

    def __str__(self): # Método que retorna uma representação em string do objeto (post).
        return self.title # Retorna o título como representação do objeto.