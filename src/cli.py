import typer  # kommandolinjer
from pathlib import Path  # filstier
from rich import print  # visuell tekst (farger/format)

app = typer.Typer()  # lag en app for kommandolinjer

@app.command()
def parse_invoices(dir: Path, out: Path = Path("data/out/out.csv")):
    """Teller PDFene i katalogen dir"""  
    files = list(dir.glob("*.pdf"))  # finn alle filer som slutter på .pdf
    print(f"[bold green]Fant {len(files)} PDF-filer i {dir}[/bold green]")  
    # skriver ut antallet i grønt

if __name__ == "__main__":  # sjekker om filen kjøres direkte
    app()  # starter CLI-app'en (typer håndterer argumenter/kommandoer)
