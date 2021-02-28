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
              default="finite-state",
              show_default=True,
              type=click.Choice(['naive', 'finite-state'],
                                case_sensitive=False
                                ),
              help="The matching method.",
              )
def main(case_insensitive, pattern, text_input, method=None):
    """Console tool for pattern matching.

    Print either all positions where the input pattern begins in an input
    string or text document or in all found text documents in an input
    directory by document.

    Args
    ----
    case_insensitive (bool) -- Flag that disables case sensitivity.
    pattern (str) -- Pattern to match to the text input.
    text_input (str) -- The text itself, a txt document containing the text or
    a directory that should be scanned for txt documents.
    method (str) -- One of the implemented matching methods 'naive' or
    'finite-state'. (default is None)

    Return
    ------
    None
    """
    # Don't match if the pattern is empty
    if len(pattern) > 0:
        # If method is defined initilize string matcher with method
        # otherwise use its default
        if method:
            SM = StringMatcher(method=method)
        else:
            SM = StringMatcher()
        # Check wether text input is directory or file
        # If directory scan for text files and match them to pattern
        # If file match it to pattern
        # Otherwise handle text input as matching text
        if os.path.isdir(text_input):
            for file in os.listdir(text_input):
                if file.endswith(".txt"):
                    text_file = open(os.path.join(text_input, file), 'r')
                    pretty_print(SM.match(pattern,
                                          text_file.read(),
                                          case_insensitive=case_insensitive
                                          ),
                                 document=file
                                 )
        elif os.path.isfile(text_input):
            file = open(text_input, 'r')
            pretty_print(SM.match(pattern,
                                  file.read(),
                                  case_insensitive=case_insensitive
                                  )
                         )
        else:
            pretty_print(SM.match(pattern,
                                  text_input,
                                  case_insensitive=case_insensitive
                                  )
                         )
    else:
        print('\nThe pattern is empty. '
              'Please enter a pattern of length > 0.\n')

def pretty_print(start_pos_list, document=None):
    """Pretty print the matched positions.

    Print the list of matched positions as line of comma separated numbers.
    If a document name is given print the document name before the positions.

    Args
    ----
    start_pos_list (list) -- Contains the matched positions.
    document (str) -- Name of the text input document. (default is None)

    Return
    ------
    None
    """
    if len(start_pos_list) > 0:
        out_str = str(start_pos_list[0])
        for pos in start_pos_list[1:]:
            out_str += f', {pos}'
        if document:
            print(f'{document}: {out_str}')
        else:
            print(out_str)
    else:
        if document:
            print(f'{document}: No matches found.')
        else:
            print('No matches found.')


if __name__ == '__main__':
    main()
