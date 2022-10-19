from django.contrib import admin

# Register your models here.


from blog.models import blog

class blogAdmin(admin.ModelAdmin):
    list_display = ("title","author","published","created_on","last_update",)
    list_editable = ("author","published",)
    
    
admin.site.register(blog,blogAdmin)
