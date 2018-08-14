#-*- coding: utf-8 -*-
from __future__ import print_function
import sys
import json
import codecs

tab = "  "
list_tag = '* '
htag = '#'

def loadJSON(file):
    with codecs.open(file, 'r', encoding="utf-8", errors="surrogateescape") as f:
        data = f.read().decode('ascii', 'ignore')
    return json.loads(data)

def buildHeaderChain(depth):
    chain = list_tag * (bool(depth)) + htag * (depth + 1) + \
        ' value ' + (htag * (depth + 1) + '\n')
    return chain

def buildValueChain(key, value, depth):
    chain = tab * (bool(depth - 1)) + list_tag + \
        str(key) + ": " + str(value) + "\n"
    return chain

class JsonToMarkdown(object):
    def __init__(self):
        self.markdown = ""             
    
    def parseJSON(self, json_block, depth):
        if isinstance(json_block, dict):
            self.parseDict(json_block, depth)
        if isinstance(json_block, list):
            self.parseList(json_block, depth)

    def parseDict(self, d, depth):
        for k in d:
            if isinstance(d[k], (dict, list)):
                self.addHeader(k, depth)
                self.parseJSON(d[k], depth + 1)
            else:
                self.addValue(k, d[k], depth)

    def parseList(self, l, depth):
        for value in l:
            if not isinstance(value, (dict, list)):
                index = l.index(value)
                self.addValue(index, value, depth)
            else:
                self.parseDict(value, depth)

    def addHeader(self, value, depth):
        chain = buildHeaderChain(depth)
        self.markdown += chain.replace('value', value.title())
     
    def addValue(self, key, value, depth):
        chain = buildValueChain(key, value, depth)
        self.markdown += chain

    def writeOut(self, output_file):
        f = codecs.open(output_file, 'w+', encoding="utf-8", errors="surrogateescape")
        f.write(self.markdown)

    @staticmethod
    def justdoit(input_file, output_file):
        json_data = loadJSON(input_file)
        depth = 0
        converter = JsonToMarkdown()
        converter.parseJSON(json_data, depth)
        converter.markdown = converter.markdown.replace('#######', '######')
        converter.writeOut(output_file)


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = input_file[:-4] + 'markdown'
        if input_file[-4:] == 'json':
            JsonToMarkdown.justdoit(input_file, output_file)
        else:
            print('Input must be a .json file')
    else:
        print('\n' + "Sorry, you must specify an input file.")
        print("	usage: python torsimany.py [JSON_FILE].json" + '\n')
