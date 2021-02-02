# Sara Derakhshani, 01.02.21
# Programmierung 1: Projekt
# Test: String-Matching-Tool

import click
from string_matcher import StringMatcher


@click.command()
@click.option('-i',
              '--case-insensitive',
              is_flag=True,
              help='Disables case sensitivity.'
              )
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
def main(case_insensitive, pattern, text, method=None):
    """Pattern matcher"""
    if method:
        SM = StringMatcher(method=method)
    else:
        SM = StringMatcher()
    # If case_insensitivity is True: case_sensitive = False, else True
    print(SM.match(pattern, text, case_sensitive=(not case_insensitive)))


if __name__ == '__main__':
    main()
