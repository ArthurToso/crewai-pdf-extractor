from pydantic import BaseModel, Field
from typing import List

class InformacoesExtraidas(BaseModel):
    """
    Contrato de dados que o agente extrator deve preencher.
    """
    datas: List[str] = Field(
        description= "Datas, preservando o formato exato como aparecem no texto (ex: '31 de março de 2024', '07/03/2024', 'Q1 2024')"
    )

    valores_monetarios: List[str] = Field(
        description="Valores monetarios, inlcuindo a moeda e preservando o formato exato como aparecem no texto (ex:  'R$ 214.750.320,00', 'USD 12.500.000', 'R$ 1,58 por ação')"
    )

    entidades: List[str] = Field(
        description="Pessoas fisicas com cargo quando disponivel, e tambem empresas/organizacoes (ex.: 'Dr. Renato Cavalcante Drummond (CEO)', 'Tecnoverde Sistemas Ltda.')"
    )