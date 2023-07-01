import click


@click.command()
@click.option('--message', '-m', default='LGTM',
              show_default=True, help='画像に乗せる文字列')
@click.argument('keyword')
def cli(kyeword, message):
    """LGTM画像生成ツール"""
    lgtm(kyeword, message)
    click.echo('lgtm')


def lgtm():
    pass
