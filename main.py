#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sara Derakhshani, 01.02.21
# Programmierung 1: Projekt
# Test: String-Matching-Tool

import os
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
              '--text-input',
              help='The text input you want to search for the pattern.',
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
def main(case_insensitive, pattern, text_input, method=None):
    """Pattern matcher"""
    if method:
        SM = StringMatcher(method=method)
    else:
        SM = StringMatcher()
    if os.path.isdir(text_input):
        for file in os.listdir(text_input):
            if file.endswith(".txt"):
                text_file = open(os.path.join(text_input, file), 'r')
                print('{}: {}'.format(file,
                                      SM.match(pattern,
                                               text_file.read(),
                                               case_insensitive=case_insensitive
                                               )
                                      )
                      )
    elif os.path.isfile(text_input):
        text_file = open(text_input, 'r')
        print(SM.match(pattern,
                       text_file.read(),
                       case_insensitive=case_insensitive
                       )
              )
    else:
        print(SM.match(pattern,
                       text_input,
                       case_insensitive=case_insensitive
                       )
              )



if __name__ == '__main__':
    main()
