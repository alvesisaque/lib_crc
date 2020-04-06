from peewee import *


class Operacao(Model):
	nu_opercao = 
	modality = 
	va_operacao = FloatField(max_length=126)
	pe_tx_efet_juros = FloatField(max_length=126)
	indexador = ?? #
	pe_custo_efetivo_total = FloatField(max_length=126)
	nu_prazo_meses_operacao = IntegerField()
	regime_amortizacao = ??
	data_contratacao = ?? 
	# origem_recursos = "0208" # campo fixo
	tipo_operacao = ?? # tem que verificar o camopo CO_TIPO_OPERACAO e ligar com o layout
	grau_garantia = ??

	DT_AVALIACAO_IMOVEL = DateField()
	VA_IMOVEL_MERCADO = FloatField(max_length=126)
	
	class Meta:
        database = database
        db_table = "operacao_credito"
