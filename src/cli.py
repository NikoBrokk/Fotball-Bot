import typer  
from pathlib import Path  
from rich import print 

from .ingest import extract_text_from_pdf, has_useful_text

app = typer.Typer()  # lag en app for kommandolinjer

@app.command()
def parse_invoices(dir: Path, out: Path = Path("data/out/out.csv")):
    """Teller PDFene i katalogen dir"""  
    files = list(dir.glob("*.pdf"))  # finn alle filer som slutter på .pdf
    print(f"[bold green]Fant {len(files)} PDF-filer i {dir}[/bold green]")  
    # skriver ut antallet i grønt

    needs_ocr = 0  # teller hvor mange som trenger OCR
    for f in files:  # gå gjennom alle filene
        text = extract_text_from_pdf(f)  # hent tekst via ingest.py
        if has_useful_text(text):  # om PDFen kan leses, gi navnet og antall tegn
            print(f" - {f.name}: {len(text)} tegn")
        else:
            print(f"[yellow] - {f.name}: lite/ingen tekst - trenger OCR [/yellow]")  
            needs_ocr += 1
    
    print(f"\n[bold]Oppsummering: [/bold] {len(files) - needs_ocr} med tekst, {needs_ocr} trolig skannet.")  
    # summerer resultatene

if __name__ == "__main__":  # sjekker om filen kjøres direkte
    app()  # starter CLI-app'en (typer håndterer argumenter/kommandoer)
