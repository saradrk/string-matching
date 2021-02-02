# Sara Derakhshani, 01.02.21
# Programmierung 1: Projekt
# Test: String-Matching-Tool

import click
from string_matcher import StringMatcher


@click.command()
@click.option('-p',
              '--pattern',
              help='The pattern you want to match.',
              required=True
              )
@click.option('-t',
              '--text',
              help='The text you want to search the pattern for.',
              required=True
              )
@click.option('-m',
              '--method',
              default="naive",
              show_default=True,
              type=click.Choice(['naive', 'finite-state'],
                                case_sensitive=False
                                ),
              help="The matching method.",
              )
def main(pattern, text, method=None):
    """Pattern matcher"""
    if method:
        SM = StringMatcher(method=method)
    else:
        SM = StringMatcher()
    print(SM.match(pattern, text))


if __name__ == '__main__':
    main()
