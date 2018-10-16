#!/usr/bin/env python
"""Translate all of Aseprite's --sheet --data output into an .aseprite-data file with a slice for each image added.

Converts the JSON frame output from Aseprite CLI to an XML file with slice info that Aseprite auto imports.
"""

__author__ = "Carl Baumann"
__copyright__ = "Copyright 2018"

__license__ = "MIT"

import argparse
import json
import os.path


def aseprite_data():
    # Set up Command line argument detection
    parser = argparse.ArgumentParser(description="Translate Aseprite's JSON data export from --sheet to XML Slices")
    parser.add_argument('data', help='the json data file from aseprite')
    parser.add_argument('output', help='the corresponding image file name')
    parser.add_argument('-f', '--force', action='store_true', help='Ignore existing files and overwrite without prompt')
    json_format = parser.add_mutually_exclusive_group()
    json_format.add_argument('-jh', '--hash', action='store_true',
                             help='Force reading JSON file as a Hash format (default)')
    json_format.add_argument('-ja', '--array', action='store_true', help='Force reading JSON file as an Array format')

    args = parser.parse_args()

    if args.array is False and args.hash is False:
        args.hash = True

    # Verify output target is .aseprite-data
    if '.' not in args.output:
        args.output += '.aseprite-data'
    else:
        out_file_suffix = args.output.split('.')
        if len(out_file_suffix) > 1:
            if out_file_suffix[-1] is not 'aseprite-data':
                out_file_suffix[-1] = 'aseprite-data'
                args.output = '.'.join(out_file_suffix)

    if args.force is False and os.path.isfile(args.output):
        resp = input('\n\nThe file output target already exists, would you like to Overwrite it? (Y/n)')
        if resp is '' or resp is 'y' or resp is 'Y':
            print('Continuing with data translation.')
        else:
            print('\n\nThe file has not been modified.')
            print('Exiting...')
            exit(0)

    with open(args.data, 'r') as infile, open(args.output, 'w+') as outfile:
        j = json.load(infile)

        # Write initial XML tags
        outfile.write('<?xml version="1.0" encoding="utf-8" ?>\n')
        outfile.write('<sprite>\n')
        outfile.write('\t<slices>\n')

        if args.array is True:
            for id in j['frames']:
                outfile.write(
                    new_slice(id['filename'], id['frame']['x'], id['frame']['y'], id['frame']['w'], id['frame']['h']))

        else:
            for id, value in j['frames'].items():
                outfile.write(
                    new_slice(id, value['frame']['x'], value['frame']['y'], value['frame']['w'], value['frame']['h']))

        # Write closing XML tags
        outfile.write('\t</slices>\n')
        outfile.write('</sprite>')

    print('\nFile ' + args.output + ' successfully created from ' + args.data + '.')


def new_slice(id, x, y, w, h, color='#0000ff'):
    id_split = id.split('.')
    if len(id_split) > 1:
        id = id_split[0].rstrip()
    temp_slice = '\t\t<slice id="' + id + '" color="' + color + '">\n'
    temp_key = '\t\t\t<key frame="0" x="' + str(x) + '" y="' + str(y) + '" w="' + str(w) + '" h="' + str(h) + '" />\n'
    return temp_slice + temp_key + '\t\t</slice>\n'


if __name__ == "__main__":
    try:
        aseprite_data()
    except AttributeError:
        print("\nERROR: <class 'AttributeError'>",
              "\nIt could be a wrong file format, try using -ja to force reading as an array")
    except TypeError:
        print("\nERROR: <class 'TypeError'>",
              "\nIt could be a wrong file format, try using -jh to force reading as a hash")
