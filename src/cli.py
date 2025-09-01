import typer #kommandolinjer
from pathlib import Path #filstier
from rich import print #visuell tekst

app = typer.Typer() #lag en app for kommandolinjer

@app.command() 
def parse_invoices(dir: Path, out: Path = Path("data/out/out.csv")): #teller PDFene i katalogen dir
  files = list(dir.glob("*pdf")) 
  print(f"[bold grenn]Fant {len(files)} PDF-filer i {dir}[/bold green]")

if __name__ == "__main__": #en test, spesifikk for cli.py
  app() #kjør CLI appen


if __name__ == "__main__":  # sjekker om filen kjøres direkte
    app()  # starter CLI-app'en (typer håndterer argumenter/kommandoer)
