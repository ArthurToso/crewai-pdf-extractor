# O Pydantic é usado para garantir a validação do tipo do dado de uma classe
# Ao herdar a  classe BaseModel, a classe vira um modelo validado do pydantic
# por exemplo, se o atributo for idade: int e tentar passar idade = "vinte", vai retornar erro usando o pydantic
# Por python base não ocorreria erro 
from pydantic import BaseModel, Field
from typing import List

class InformacoesExtraidas(BaseModel):
    """
    Contrato de dados que o agente extrator deve preencher.
    """
    datas: List[str] = Field(
        description=( 
            "Lista de todas as datas encontradas no documento, "
            "preservando o formato exato como aparecem no texto (ex: '31 de março de 2024', '07/03/2024', 'Q1 2024')"
            "Seja exaustivo: Não omita nenhuma ocorrência"
        )
    )

    valores_monetarios: List[str] = Field(
        description=("Lista de todos os Valores monetarios encontrados no texto, "
        "inlcuindo a moeda e preservando o formato exato como aparecem no texto (ex:  'R$ 214.750.320,00', 'USD 12.500.000', 'R$ 1,58 por ação')"
        "Seja exaustivo: Não omita nenhuma ocorrência"
        )
    )

    entidades: List[str] = Field(
        description=(
            "Lista de todas as Pessoas fisicas com cargo quando disponivel encontradas no texto,"
            " e tambem empresas/organizacoes (ex.: 'Dr. Renato Cavalcante Drummond (CEO)', 'Tecnoverde Sistemas Ltda.')"
            "Seja exaustivo: Não omita nenhuma ocorrência"
        )
    )