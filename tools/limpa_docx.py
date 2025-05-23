import importlib.util
import os
from docx import Document

# ======== CONFIGURAÇÃO DO USUÁRIO ========
# Caminho para o .docx a ser tratado
docx_path = "F:\OneDrive\Documentos\Calibre\Roman Brocki\Supreme Harem God System 1601 - 1700.docx"

# Caminho para o arquivo pattern.py (opcional)
pattern_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pattern.py")
# =========================================

def replace_or_remove_terms(pattern_path, docx_path, replace_with=None):
    # Importar a lista "pattern" de pattern.py
    spec = importlib.util.spec_from_file_location("pattern_module", pattern_path)
    pattern_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pattern_module)

    terms_to_find = pattern_module.pattern  # usa a variável chamada 'pattern'

    # Abrir o documento Word
    doc = Document(docx_path)

    # Substituição ou remoção dos termos
    for paragraph in doc.paragraphs:
        for term in terms_to_find:
            if term in paragraph.text:
                paragraph.text = paragraph.text.replace(term, "" if replace_with is None else replace_with)

    # Salvar o documento sobrescrevendo o original
    doc.save(docx_path)

# ============ EXECUTAR ============
replace_or_remove_terms(pattern_path, docx_path)

