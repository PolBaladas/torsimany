#-*- coding: utf-8 -*-
import sys,json,requests,random
# Set default encoding to utf-8 to avoid problems with the json reading
reload(sys)
sys.setdefaultencoding('utf-8')
markdown = ""
tab = "  "
list_tag = ""
htag = '#'


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

def buildHeaderChain(depth):
    chain = list_tag * (bool(depth)) + htag * (depth + 1) + \
        ' value ' + (htag * (depth + 1) + '\n')
    return chain

def buildValueChain(key, value, depth):
    chain = tab * (bool(depth - 1)) + list_tag + \
        str(key) + ": " + str(value) + "\n"
    return chain

def addHeader(value, depth):
    chain = buildHeaderChain(depth)
    global markdown
    markdown += chain.replace('value', value.title())

def addValue(key, value, depth):
    chain = buildValueChain(key, value, depth)
    global markdown
    markdown += chain

def justdoit(json_data, output_file):
    depth = 0
    parseJSON(json_data, depth)
    global markdown
    markdown = markdown.replace('#######', '######')
    with open(output_file, "w+") as f:
        f.write(markdown)
        print(output_file)
        print(markdown)

def main():
    if len(sys.argv) > 1:
        input_file = str(sys.argv[1])
        if input_file[:7] == "http://" or input_file[:8] == "https://":
            output_file = "url_"+str(random.randint(0,1000))+".markdown" # Gives the output file a random name (ie. url_714.markdown)
            json_data = requests.get(input_file).json()
            justdoit(json_data, output_file)
        elif input_file[-5:] == '.json':
            output_file = input_file[:-4] + 'markdown'
            justdoit(loadJSON(input_file), output_file)
        else:
            print('Input must be a .json file or an URL of a .json file')
    else:
        print('\n' + "Sorry, you must specify an input file.")
        print("	usage: python torsimany.py [JSON_FILE].json" + '\n')
