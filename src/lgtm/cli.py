import click
import os
from PIL import Image


@click.command()
@click.option('--words', default='Hello')
@click.argument('name')
def greet(name, words):
    click.echo(f'{words}, {name}')


def thumbnail(infile, size=(128, 128)):
    outfile = os.path.splitext(
        infile)[0] + ".thumbnail"
    try:
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(outfile, "JPEG")
    except:
        print("cannot create", infile)


if __name__ == '__main__':
    # greet()
    thumbnail('sample.jpg')
