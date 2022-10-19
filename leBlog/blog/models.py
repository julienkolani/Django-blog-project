from django.urls                    import reverse
from django.db                      import models
from django.template.defaultfilters import slugify
from django.contrib.auth            import get_user_model

# Create your models here.

User = get_user_model()

class blog(models.Model):
    title        = models.CharField     (max_length=225,unique=True,verbose_name="Titre")
    slug         = models.SlugField     (max_length=225,unique=True,blank=True)
    author       = models.ForeignKey    (User, on_delete=models.SET_NULL,null=True,blank=True)
    last_update  = models.DateTimeField (auto_now=True)
    created_on   = models.DateField     (blank=True,null=True)
    published    = models.BooleanField  (default=False , verbose_name="Publié")
    content      = models.TextField     (blank=True,verbose_name="Contenu")
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"
        
    def __str__(self) :
        return  self.title
    
    def save(self ,*args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    @property
    def author_or_default(self):
        return self.author.username if  self.author else " Un auteur inconnu. "
    
    
    def get_absolute_url(self):
        return reverse("blog:home")
    