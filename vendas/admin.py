from django.contrib import admin

from .models import Vendas, Produto

# Register your models here.

admin.site.register(Vendas)
admin.site.register(Produto)
