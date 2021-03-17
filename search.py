#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Sara Derakhshani, 01.02.21
# Programmierung 1: Projekt

"""Console Pattern Matching Tool.

This is a script for searching direct text inputs, single text files or
directories containing multiple text files for a pattern. The tool matches
the pattern to the input and returns all found starting positions of the
search pattern.
"""

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
def search(case_insensitive, pattern, text_input, method=None):
    """Console tool for pattern matching.

    Print all starting positions of the input pattern found in the text input,
    which can be a string, text document or a directory containing multiple
    text documents.
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
            txt_file_exists = False
            for file in os.listdir(text_input):
                if file.endswith(".txt"):
                    txt_file_exists = True
                    text_file = open(os.path.join(text_input, file), 'r')
                    pretty_print(SM.match(pattern,
                                          text_file.read(),
                                          case_insensitive=case_insensitive
                                          ),
                                 document=file
                                 )
            if not txt_file_exists:
                print(f'No .txt files found in {text_input} directory.')
        elif os.path.isfile(text_input):
            if text_input.endswith(".txt"):
                file = open(text_input, 'r')
                pretty_print(SM.match(pattern,
                                      file.read(),
                                      case_insensitive=case_insensitive
                                      ),
                             document=text_input
                             )
            else:
                print(f'{text_input} has unpermitted file format. '
                      'Only .txt files can be searched.')
        else:
            pretty_print(SM.match(pattern,
                                  text_input,
                                  case_insensitive=case_insensitive
                                  )
                         )
    else:
        print('\nThe pattern is empty. '
              'Please enter a pattern containing at least one character.\n')


def pretty_print(start_pos_list, document=None):
    """Pretty print the matched positions.

    Print the number of matched positions and the list of matched positions as
    line of comma separated numbers. If a document name is given print the
    document name with the number of matched positions and the positions.

    Args
    ----
    start_pos_list (list): Contains the matched positions
    document (str): Name of the text input document (default is None)

    Return
    ------
    None
    """
    match_count = len(start_pos_list)
    if match_count > 0:
        # String with comma seperated matched positions for pretty output
        out_str = str(start_pos_list[0])
        for pos in start_pos_list[1:]:
            out_str += f', {pos}'
        # Differentiate between singular and plural in print statement,
        # depending on wether one match or multiple matches were found
        if document:
            if match_count == 1:
                print(f'{match_count} match found in {document}: {out_str}')
            else:
                print(f'{match_count} matches found in {document}: {out_str}')
        else:
            if match_count == 1:
                print(f'{match_count} match found: {out_str}')
            else:
                print(f'{match_count} matches found: {out_str}')
    else:
        if document:
            print(f'No matches found in {document}')
        else:
            print('No matches found in text input. Also no matching file or'
                  ' directory found.')


if __name__ == '__main__':
    search()
