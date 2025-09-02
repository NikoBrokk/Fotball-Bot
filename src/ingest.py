from pathlib import Path 
import pdfplumber 

def extract_text_from_pdf(pdf_path: Path) -> str:  # lager kun hele string-tekster av PDF, ikke OCR
    text_chunks = []  # gi plass til string chunks per side
    with pdfplumber.open(pdf_path) as pdf:  # åpne PDF og hent info
        for page in pdf.pages:  # for hver PDF-side
            txt = page.extract_text() or ""  # hent teksten fra siden, eller tom streng hvis ingen
            text_chunks.append(txt)  # legg denne chunken inn i lista
    full_text = "\n".join(text_chunks).strip()  # lag en samlet tekst, fjern unødvendige whitespace
    return full_text  # gi tilbake teksten

def has_useful_text(text: str, min_len: int = 30) -> bool:  # test om teksten faktisk har noe innhold
    return len(text) >= min_len
