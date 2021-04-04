from django.db import models


# Create your models here.

class Vendas(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    data_venda = models.DateField(auto_now_add=True, blank=True, null=False)
    hora_venda = models.TimeField(auto_now_add=True, blank=True, null=False)
    data_hora_venda = models.DateTimeField(auto_now_add=True, blank=True, null=False)
    numero_venda = models.IntegerField(blank=False, null=False)
    observacao = models.TextField(blank=True, null=True)
    comprovante_venda = models.FileField(upload_to='Comprovante_venda/')
    email_cliente = models.EmailField(blank=True, null=True)
    venda_concluida = models.BooleanField(blank=False, null=False)
    qtd_itens = models.IntegerField(blank=True, null=False, default=0)

    def _str_(self):
        return str(self.pk) + ' - ' + self.nome
