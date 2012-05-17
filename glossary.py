#!/usr/bin/python
#
# Boston Scientific Confidential
# Copyright (C) Boston Scientific Corporation 2012, All Rights Reserved
#

"""
Example:
    python glossary.py --merge 1.csv 2.csv

"""

import argparse

from core.data import Data

__version__ = '0.1'

def main():
    """
    glossary app parses the arguements from command lines, do the
    corresponding operations.
    """
    data = Data()
    args = get_args()

    if args.merge_files:
        data.merge(args.merge_files, args.data_format)
    else:
        data.export(args.export_file, args.data_format)

def get_args():
    """get the arguements by argparse module"""

    parser = argparse.ArgumentParser(
        description='Manage the glossary in a convenient way',
        epilog=__doc__,
        version=__version__)

    parser.add_argument(
        '--format', action='store', dest='data_format', default='yaml',
        choices=('csv', 'json', 'yaml', 'md', 'rst'),
        help='choose the data exchange format, by default yaml')

    group = parser.add_mutually_exclusive_group()

    #merge - shall have at least one input file
    group.add_argument(
        '--merge', action='append', dest='merge_files', nargs='+',
        help='merge the files with the current glossary data')

    group.add_argument(
        '--export', action='store', dest='export_file',
        help='export the data with specified format type')

    return parser.parse_args()

if __name__ == '__main__':
    main()
