from docx import Document
import re
import os

def desfazer_censura(texto):
    """
    Remove pontos entre letras (ex: s.e.x → sex), somente se for uma palavra inteira.
    """
    return re.sub(r'\b(?:[a-zA-Z]\.){2,}[a-zA-Z]\b', lambda m: m.group(0).replace('.', ''), texto)

def limpar_censura_docx(caminho_docx):
    """
    Lê um .docx, remove censura por pontos, e salva como arquivo novo com sufixo '-uncens'.

    Parâmetro:
    - caminho_docx (str): caminho para o arquivo .docx original

    Retorna:
    - caminho_saida (str): caminho do novo arquivo salvo
    """
    doc = Document(caminho_docx)
    novo_doc = Document()

    for par in doc.paragraphs:
        texto_corrigido = desfazer_censura(par.text)
        novo_par = novo_doc.add_paragraph(texto_corrigido)
        novo_par.style = par.style

    nome_base, ext = os.path.splitext(caminho_docx)
    caminho_saida = f"{nome_base}_uncens{ext}"
    novo_doc.save(caminho_saida)

    return caminho_saida

limpar_censura_docx(r"F:\OneDrive\Documentos\Calibre\Roman Brocki\Divine Emperor of Death 2201-2500.docx")
