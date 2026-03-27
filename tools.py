from crewai.tools import BaseTool
from pydantic import Field
import pdfplumber

class LerPDFTool(BaseTool):
    name: str = "read_pdf_tool"
    # Para escrever uma boa description:
    # o que a Tool faz ? 
    # quando usar a Tool ?
    # o que a Tool retorna ? 
    description: str = ("Lê o conteúdo completo de um arquivo PDF e retorna o texto extraído "
        "página por página. Use esta ferramenta quando precisar acessar o "
        "conteúdo do documento para análise ou extração de informações.")
    caminho_pdf: str = Field(default="", description="Caminho do arquivo PDF")

    def _run(self, consulta: str = "") -> str:
        """
        Lê todas as paginas do PDF e retorna o texto completo
        O parametro consulta existe por compatibilidade com a interface BaseTool, mas não é utilizada
        """
        texto_completo = []
        
        with pdfplumber.open(self.caminho_pdf) as pdf:
            # o parametro start=1 no enumerate faz com que o idx começe em 1 ao inves de 0
            for idx, pagina in enumerate(pdf.pages, start=1):
                num_pag = idx
                cabecalho = f"----Página {num_pag}/{len(pdf.pages)} ----"
                texto = pagina.extract_text()
                if texto:
                    texto_completo.append(cabecalho)
                    texto_completo.append(texto)
        
        if len(texto_completo) == 0:
            return "Nenhum texto extraivel encontrado no PDF."
        
        return "\n\n".join(texto_completo)