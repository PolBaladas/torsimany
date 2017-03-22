#-*- coding: utf-8 -*-
import sys
import json

markdown = ""
tab = "  "


def loadJSON(file):
    with open(file, 'r') as f:
        data = f.read().decode('ascii', 'ignore')
    return json.loads(data)


def parseJSON(json_block, depth):
    if isinstance(json_block, dict):
        parseDict(json_block, depth)
    if isinstance(json_block, list):
        parseList(json_block, depth)


def parseDict(d, depth):
    for k in d:
        if isinstance(d[k], (dict, list)):
            addHeader(k, depth)
            parseJSON(d[k], depth + 1)
        else:
            addValue(k, d[k], depth)


def parseList(l, depth):
    for value in l:
        if not isinstance(value, (dict, list)):
            index = l.index(value)
            addValue(index, value, depth)
        else:
            parseDict(value, depth)


def addHeader(value, depth):
    chain = '* ' * (bool(depth)) + '#' * (depth + 1) + \
        ' value ' + ('#' * (depth + 1) + '\n')
    global markdown
    markdown += chain.replace('value', value.title())


def addValue(key, value, depth):
    chain = tab * (bool(depth - 1)) + '* ' + \
        str(key) + ": " + str(value) + "\n"
    global markdown
    markdown += chain


def writeOut(markdown, output_file):
    f = open(output_file, 'w+')
    f.write(markdown)


def justdoit(input_file, output_file):
    json_data = loadJSON(input_file)
    depth = 0
    parseJSON(json_data, depth)
    global markdown
    markdown = markdown.replace('#######', '######')
    writeOut(markdown, output_file)


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = input_file[:-4] + 'markdown'
        if input_file[-4:] == 'json':
            justdoit(input_file, output_file)
        else:
            print('Input must be a .json file')
    else:
        print('\n' + "Sorry, you must specify an input file.")
        print("	usage: python torsimany.py [JSON_FILE].json" + '\n')
