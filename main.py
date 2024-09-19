import requests
from translate import Translator
import emoji
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Cria um objeto Console
console = Console()

def curiosidade():
    url = "https://catfact.ninja/fact"  # Fatos aleatórios sobre gatos
    tradutor = Translator(to_lang="pt-br")  # Biblioteca para traduzir os fatos
    response = requests.get(url)
    dados = response.json()
    
    fato = dados['fact']
    fato_traduzido = tradutor.translate(fato)

    return fato_traduzido

repitir = 1
    
while True:
    fato = curiosidade()

    fato_txt = Text.from_markup(f"{emoji.emojize(':cat_face:')} [bold green]Curiosidade número {repitir}[/bold green] {emoji.emojize(':cat_face:')}\n{emoji.emojize(':cat:')} [italic] {fato} [/italic] {emoji.emojize(':cat:')}")
    painel = Panel(fato_txt, title="Curiosidades Gatísticas", title_align="left", border_style="yellow", padding=(1, 2))

    console.print(painel)

    resposta = input("Você quer ouvir outro fato? (s/n): ").strip().lower()
        
    if resposta == 'n':
        console.print(emoji.emojize("Obrigado por usar o programa! Até a próxima! :wave:"), style="bold red")
        break
    else:
        repitir += 1
