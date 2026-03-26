"""
    GERA O PDF DE EXEMPLO PARA O CODIGO
    a finalidade desse script é apenas criar o PDF para ser processado pelo código principal.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
import os

CAMINHO_SAIDA = os.path.join("relatorios", "relatorio_q1_2024.pdf")
CAMINHO_TEXTO = os.path.join("relatorios", "relatorio_q1_2024.txt")

COR_TITULO = HexColor("#1A3A5C")
COR_SECAO  = HexColor("#2E86AB")

def construir_estilos() -> dict:
    """
    Função para criar estilos personalizados para:
        - Titulo
        - Corpo
        - Seção
    Esses estilos serão utilizados posteriormente com o objeto Paragraph,
    para transformar uma string em um elemento visual estilizado.
    """
    base = getSampleStyleSheet()
    estilos = {}

    estilos["titulo"] = ParagraphStyle(
        name = "title_style",
        fontSize= 16,
        textColor= COR_TITULO,
        alignment= TA_CENTER,
        fontName= "Helvetica-Bold" 
    )
    
    estilos["secao"] = ParagraphStyle(
        name = "section_style",
        fontSize= 11,
        textColor= COR_SECAO,
        fontName= "Helvetica-Bold" 
    )
    
    estilos["corpo"] = ParagraphStyle(
        name = "body_style",
        fontSize= 9.5,
        leading = 14,
        alignment= TA_JUSTIFY 
    )

    return estilos

def gerar_pdf():
    os.makedirs("relatorios", exist_ok=True)

    with open(CAMINHO_TEXTO, "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()

    doc = SimpleDocTemplate(
        CAMINHO_SAIDA,
        pagesize=A4, 
        leftMargin = 2.5 * cm,
        rightMargin = 2.5 * cm,
        topMargin = 2.5 * cm,
        bottomMargin = 2.5 * cm)
    
    estilos = construir_estilos()
    elementos = []
    primeira = True

    for linha in linhas:
        linha = linha.strip()

        if not linha:
            elementos.append(Spacer(1, 0.3 * cm))
            continue

        if linha.isupper() and len(linha) > 8:
            elementos.append(HRFlowable(color=COR_SECAO, width="100%"))
            elementos.append(Paragraph(linha, estilos["secao"]))
        elif linha and primeira:
            elementos.append(Paragraph(linha, estilos["titulo"]))
            primeira = False
        else:
            elementos.append(Paragraph(linha, estilos["corpo"]))

    doc.build(elementos)
    print(f"PDF gerado em: {CAMINHO_SAIDA}")

if __name__ == "__main__":
    gerar_pdf()