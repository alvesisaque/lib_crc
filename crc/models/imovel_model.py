from peewee import *


class imovelOperacao(Model):
	nu_operacao = ForeignKeyField() 	# chave extrangeira
	municipio = ?? # 
	co_uf = CharField(max_length=2) 
	nu_cep = CharField(max_length=9)
	tipo_imovel = ??
	dt_compra_venda = DateField()
	va_preco_imovel = FloatField(max_length=126)
	nu_laudo_avaliacao = CharField(max_length=15)

	class Meta:
        database = database
        db_table = "imovel_operacao"