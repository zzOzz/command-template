import typer
from dotenv import load_dotenv

app = typer.Typer()
load_dotenv()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye(name: str):
    print(f"Goodbye {name}")

def getApp():
    return app