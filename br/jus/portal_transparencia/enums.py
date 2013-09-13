#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
Item = namedtuple('Item', 'value label')

def Enum(**enums):
    return type("Enum", (), enums)

elementos = Enum(
    APOSENTADORIAS_E_REFORMAS = Item(value="01", label= u"Aposentadorias e Reformas"),
    AQUISICAO_DE_IMOVEIS = Item(value="61", label= u"Aquisição de Imóveis"),
    AQUISICAO_DE_PRODUTOS_PARA_REVENDA = Item(value="62", label= u"Aquisição de Produtos para Revenda"),
    AQUISICAO_DE_TITULOS_DE_CREDITO = Item(value="63", label= u"Aquisição de Títulos de Crédito"),
    AQUISICAO_DE_TITULOS_REPRESENTATIVOS_DE_CAPITAL_JA_INTEGRALIZADO = Item(value="64", label= u"Aquisição de Títulos Representativos de Capital já Integralizado"),
    ARRENDAMENTO_MERCANTIL = Item(value="38", label= u"Arrendamento Mercantil"),
    AUXILIO_FINANCEIRO_A_ESTUDANTES = Item(value="18", label= u"Auxílio Financeiro a Estudantes"),
    AUXILIO_FINANCEIRO_A_PESQUISADORES = Item(value="20", label= u"Auxílio Financeiro a Pesquisadores"),

    AUXILIO_ALIMENTACAO = Item(value="46", label= u"AUXILIO-ALIMENTACAO"),

    AUXILIO_FARDAMENTO = Item(value="19", label= u"Auxílio-Fardamento"),
    AUXILIOS = Item(value="42", label= u"Auxílios"),

    AUXILIO_TRANSPORTE = Item(value="49", label= u"AUXILIO-TRANSPORTE"),

    BENEFICIO_MENSAL_AO_DEFICIENTE_E_AO_IDOSO = Item(value="06", label= u"Benefício Mensal ao Deficiente e ao Idoso"),
    CONCESSAO_DE_EMPRESTIMOS_E_FINANCIAMENTOS = Item(value="66", label= u"Concessão de Empréstimos e Financiamentos"),
    CONSTITUICAO_OU_AUMENTO_DE_CAPITAL_DE_EMPRESAS = Item(value="65", label= u"Constituição ou Aumento de Capital de Empresas"),
    CONTRATACAO_POR_TEMPO_DETERMINADO = Item(value="04", label= u"Contratação por Tempo Determinado"),
    CONTRIBUICAO_A_ENTIDADES_FECHADAS_DE_PREVIDENCIA = Item(value="07", label= u"Contribuição a Entidades Fechadas de Previdência"),
    CONTRIBUICOES = Item(value="41", label= u"Contribuições"),
    CORRECAO_MONETARIA_DA_DIVIDA_DE_OPERACOES_DE_CREDITO_POR_ANTECIPACAO_DE_RECEITA = Item(value="75", label= u"Correção Monetária da Dívida de Operações de Crédito por Antecipação de Receita"),
    CORRECAO_MONETARIA_OU_CAMBIAL_DA_DIVIDA_CONTRATUAL_RESGATADA = Item(value="73", label= u"Correção Monetária ou Cambial da Dívida Contratual Resgatada"),
    CORRECAO_MONETARIA_OU_CAMBIAL_DA_DIVIDA_MOBILIARIA_RESGATADA = Item(value="74", label= u"Correção Monetária ou Cambial da Dívida Mobiliária Resgatada"),
    DEPOSITOS_COMPULSORIOS = Item(value="67", label= u"Depósitos Compulsórios"),

    DESPESAS_DE_EXERCICIOS_ANTERIORES = Item(value="92", label= u"DESPESAS DE EXERCICIOS ANTERIORES"),
    DIARIAS_CIVIL = Item(value="14", label= u"DIARIAS - PESSOAL CIVIL"),

    DIARIAS_MILITAR = Item(value="15", label= u"Diárias - Militar"),
    DISTRIBUICAO_CONSTITUCIONAL_OU_LEGAL_DE_RECEITAS = Item(value="81", label= u"Distribuição Constitucional ou Legal de Receitas"),
    ENCARGOS_PELA_HONRA_DE_AVAIS_GARANTIAS_SEGUROS_E_SIMILARES = Item(value="27", label= u"Encargos pela Honra de Avais, Garantias, Seguros e Similares"),
    ENCARGOS_SOBRE_OPERACOES_DE_CREDITO_POR_ANTECIPACAO_DA_RECEITA = Item(value="25", label= u"Encargos sobre Operações de Crédito por Antecipação da Receita"),
    EQUALIZACAO_DE_PRECOS_E_TAXAS = Item(value="45", label= u"Equalização de Preços e Taxas"),
    EQUIPAMENTOS_E_MATERIAL_PERMANENTE = Item(value="52", label= u"Equipamentos e Material Permanente"),
    INDENIZACAO_PELA_EXECUCAO_DE_TRABALHOS_DE_CAMPO = Item(value="95", label= u"Indenização pela Execução de Trabalhos de Campo"),

    INDENIZACOES_E_RESTITUICOES = Item(value="93", label= u"INDENIZACOES E RESTITUICOES"),

    INDENIZACOES_E_RESTITUICOES_TRABALHISTAS = Item(value="94", label= u"Indenizações e Restituições Trabalhistas"),
    JUROS_SOBRE_A_DIVIDA_POR_CONTRATO = Item(value="21", label= u"Juros sobre a Dívida por Contrato"),
    JUROS_DESAGIOS_E_DESCONTOS_DA_DIVIDA_MOBILIARIA = Item(value="23", label= u"Juros, Deságios e Descontos da Dívida Mobiliária"),

    LOCACAO_DE_MAO_DE_OBRA = Item(value="37", label= u"LOCACAO DE MAO-DE-OBRA"),
    MATERIAL_DE_CONSUMO = Item(value="30", label= u"MATERIAL DE CONSUMO"),

    MATERIAL_DE_DISTRIBUICAO_GRATUITA = Item(value="32", label= u"Material de Distribuição Gratuita"),

    OBRAS_E_INSTALACOES = Item(value="51", label= u"OBRAS E INSTALACOES"),

    OBRIGACOES_DECORRENTES_DE_POLITICA_MONETARIA = Item(value="26", label= u"Obrigações decorrentes de Política Monetária"),

    OBRIGACOES_PATRONAIS = Item(value="13", label= u"OBRIGACOES PATRONAIS - OP.INTRA-ORCAMENTARIAS"),
    OBRIGACOES_TRIBUTARIAS_E_CONTRIBUTIVAS = Item(value="47", label= u"OBRIG.TRIBUT.E CONTRIB-OP.INTRA-ORCAMENTARIAS"),

    OUTRAS_DESPESAS_DE_PESSOAL_DECORRENTES_DE_CONTRATOS_DE_TERCEIRIZACAO = Item(value="34", label= u"Outras Despesas de Pessoal decorrentes de Contratos de Terceirização"),

    OUTRAS_DESPESAS_VARIAVEIS_PESSOAL_CIVIL = Item(value="16", label= u"OUTRAS DESPESAS VARIAVEIS - PESSOAL CIVIL"),
    OUTRAS_DESPESAS_VARIAVEIS_PESSOAL_MILITAR = Item(value="17", label= u"Outras Despesas Variáveis - Pessoal Militar"),
    OUTROS_AUXILIOS_FINANCEIROS_A_PESSOAS_FISICAS = Item(value="48", label= u"Outros Auxílios Financeiros a Pessoas Físicas"),
    OUTROS_BENEFICIOS_ASSISTENCIAIS = Item(value="08", label= u"OUTROS BENEF.ASSIST. DO SERVIDOR E DO MILITAR"),
    OUTROS_BENEFICIOS_DE_NATUREZA_SOCIAL = Item(value="10", label= u"Outros Benefícios de Natureza Social"),
    OUTROS_BENEFICIOS_PREVIDENCIARIOS = Item(value="05", label= u"Outros Benefícios Previdenciários"),
    OUTROS_ENCARGOS_SOBRE_A_DIVIDA_MOBILIARIA = Item(value="24", label= u"Outros Encargos sobre a Dívida Mobiliária"),
    OUTROS_ENCARGOS_SOBRE_A_DIVIDA_POR_CONTRATO = Item(value="22", label= u"Outros Encargos sobre a Dívida por Contrato"),

    OUTROS_SERVICOS_DE_TERCEIROS_PESSOA_FISICA = Item(value="36", label= u"OUTROS SERVICOS DE TERCEIROS - PESSOA FISICA"),
    OUTROS_SERVICOS_DE_TERCEIROS_PESSOA_JURIDICA = Item(value="39", label= u"OUTROS SERVICOS DE TERCEIROS-PESSOA JURIDICA"),
    PASSAGENS_E_DESPESAS_COM_LOCOMOCAO = Item(value="33", label= u"PASSAGENS E DESPESAS COM LOCOMOCAO"),
    PENSOES = Item(value="03", label= u"PENSOES DO RPPS E DO MILITAR"),

    PREMIACOES_CULTURAIS_ARTISTICAS_CIENTIFICAS_DESPORTIVAS_E_OUTRAS = Item(value="31", label= u"Premiações Culturais, Artísticas, Científicas, Desportivas e Outras"),
    PRINCIPAL_CORRIGIDO_DA_DIVIDA_CONTRATUAL_REFINANCIADO = Item(value="77", label= u"Principal Corrigido da Dívida Contratual Refinanciado"),
    PRINCIPAL_CORRIGIDO_DA_DIVIDA_MOBILIARIA_REFINANCIADO = Item(value="76", label= u"Principal Corrigido da Dívida Mobiliária Refinanciado"),
    PRINCIPAL_DA_DIVIDA_CONTRATUAL_RESGATADO = Item(value="71", label= u"Principal da Dívida Contratual Resgatado"),
    PRINCIPAL_DA_DIVIDA_MOBILIARIA_RESGATADO = Item(value="72", label= u"Principal da Dívida Mobiliária Resgatado"),
    REMUNERACAO_DE_COTAS_DE_FUNDOS_AUTARQUICOS = Item(value="28", label= u"Remuneração de Cotas de Fundos Autárquicos"),

    RESSARCIMENTO_DE_DESPESAS_DE_PESSOAL_REQUISITADO = Item(value="96", label= u"RESSARCIMENTO DE DESP. DE PESSOAL REQUISITADO"),

    SALARIO_FAMILIA = Item(value="09", label= u"Salário-Família"),

    SENTENCAS_JUDICIAIS = Item(value="91", label= u"SENTENCAS JUDICIAIS"),
    SERVICOS_DE_CONSULTORIA = Item(value="35", label= u"SERVICOS DE CONSULTORIA"),

    SUBVENCOES_SOCIAIS = Item(value="43", label= u"Subvenções Sociais"),

    VENCIMENTOS_E_VANTAGENS_FIXAS_PESSOAL_CIVIL = Item(value="11", label= u"VENCIMENTOS E VANTAGENS FIXAS - PESSOAL CIVIL"),

    VENCIMENTOS_E_VANTAGENS_FIXAS_PESSOAL_MILITAR = Item(value="12", label= u"Vencimentos e Vantagens Fixas - Pessoal Militar"),
)