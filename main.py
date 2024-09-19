import requests
from translate import Translator
import emoji
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
from time import sleep

# objeto Console
console = Console()

def curiosidade():
    url = "https://catfact.ninja/fact"  # Fatos aleatórios sobre gatos
    tradutor = Translator(to_lang="pt-br")  # Biblioteca para traduzir os fatos
    resposta_API = requests.get(url)
    dados = resposta_API.json()
    
    fato = dados['fact']
    fato_traduzido = tradutor.translate(fato)

    return fato_traduzido

def carregando():
    #efeito de carregando
    console.print("\n[bold blue]Carregando novo fato felino...[/bold blue]")
    for _ in track(range(20), description=""):
        sleep(0.05)

def main():
    repitir = 1
    
    while True:
       
        fato = curiosidade()
        carregando()

        fato_txt = Text.from_markup(
            f"{emoji.emojize(':cat_face:')} [bold green]Curiosidade número {repitir}[/bold green] "
            f"{emoji.emojize(':cat_face:')}\n\n[italic green]{fato}[/italic green] "
            f"{emoji.emojize(':cat:')}"
        )

        # título e borda
        painel = Panel(fato_txt, title="Curiosidades Gatísticas", title_align="center", border_style="yellow", padding=(1, 2))

        console.print(painel)

        console.print("[bold cyan]Você quer ouvir outro fato?[/bold cyan] [bold yellow](s/n)[/bold yellow]:", end=" ")

        resposta = input().strip().lower()

        if resposta == 'n':
            console.print(emoji.emojize("\n[bold red]Obrigado por usar o programa! Até a próxima! :wave:[/bold red]"))
            break
        else:
            repitir += 1

if __name__ == "__main__":
    main()
