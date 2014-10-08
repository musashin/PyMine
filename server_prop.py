__author__ = 'Nicolas'

import re

class ServerProp:

    def __init__(self, fully_qualified_path):
        self.path = fully_qualified_path

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
                pass
                #print line
                #print '\t var: ' + str(lineFormat.match(line).group('property'))
                #print '\t val: ' + str(lineFormat.match(line).group('value'))
                #print '\t comment: ' + str(lineFormat.match(line).group('comment'))



if __name__ == '__main__':
    test = ServerProp(r'C:\minecraft\server-Copy.properties')
    test.load()
