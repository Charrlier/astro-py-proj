import click
import matplotlib.pyplot as plt

@click.command()
@click.option('--name', prompt='Your name', help='The user\'s name.')
def greet(name):
    """Simple program that greets NAME."""
    click.echo(f"Hello, {name}!")

def display_chart():
    """Displays a simple chart."""
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("Sample Chart")
    plt.show()

if __name__ == "__main__":
    greet()
    display_chart()
