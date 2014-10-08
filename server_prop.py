__author__ = 'Nicolas'

import re

class ServerProp:

    def __init__(self, fully_qualified_path):
        self.path = fully_qualified_path
        self.lines = list()

    def load(self):
        lineFormat = re.compile("""
                                (?P<property>[\w\-]*)    #property
                                [\s]*[=]*[\s]*
                                (?P<value>[\w]+)*        #value
                                [\s]*
                                [(#|!)]*
                                (?P<comment>[\w\s]*)     #comment
                                """, re.VERBOSE)
        with open(self.path, 'r') as configFile:
            for line in configFile:
                content = lineFormat.match(line)
                self.lines.append([content.group('property'),
                                   content.group('value'),
                                   content.group('comment')])
                #print line
                #print '\t var: ' + str(lineFormat.match(line).group('property'))
                #print '\t val: ' + str(lineFormat.match(line).group('value'))
                #print '\t comment: ' + str(lineFormat.match(line).group('comment'))

    def get(self, property_name):
        return [val for prop, val, comment in self.lines if prop == property_name][0]

    def set(self, property_name, value):
        index = [index for index, prop in enumerate(self.lines) if prop[0] == property_name][0]
        self.lines[index][1] = value


if __name__ == '__main__':
    test = ServerProp(r'C:\minecraft\server-Copy.properties')
    test.load()
    print test.get('network-compression-threshold')
    test.set('network-compression-threshold', '55')
    print test.lines
