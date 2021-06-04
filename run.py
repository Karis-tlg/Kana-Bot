from keep_alive import keep_alive as flask_keep_alive
import main
import click
from replit import db

@click.group()
def cli():
    pass

@cli.command()
@click.option('--keep-alive', is_flag=True, help='Run flask thread to keep Repl alive.')
def run(keep_alive):
    """Run the Discord bot."""
    if keep_alive:
        flask_keep_alive()

    main.main()

@cli.command('cleardb')
def cleardb():
    """Empty replit-db."""
    for k in db.keys():
        del db[k]


if __name__ == '__main__':
    cli()