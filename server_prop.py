__author__ = 'Nicolas'

import re

class ServerProp:

    def __init__(self, fully_qualified_path):
        self.path = fully_qualified_path
        self.lines = list()

    def load(self):
        line_format = re.compile("""
                                ^(?P<property>[\w\-]*)    #property
                                [\s]*=*[\s]?
                                (?P<value>[\w\s]*)        #value
                                ([(#|!)]
                                (?P<comment>[\w\s]*))?$     #comment
                                """, re.VERBOSE)
        with open(self.path, 'r') as configFile:
            for line in configFile:
                content = line_format.match(line)
                if content:
                    self.lines.append([content.group('property'),
                                       content.group('value'),
                                       content.group('comment')])
                    #print line
                    #print '\t var: ' + str(line_format.match(line).group('property'))
                    #print '\t val: ' + str(line_format.match(line).group('value'))
                    #print '\t comment: ' + str(line_format.match(line).group('comment'))

    def get(self, property_name):
        return [val for prop, val, comment in self.lines if prop == property_name][0]

    def set(self, property_name, value):
        index = [index for index, prop in enumerate(self.lines) if prop[0] == property_name][0]
        self.lines[index][1] = value + '\n'

    def save(self):
        with open(self.path+'x', 'w') as configFile:
            for line in self.lines:
                if line[0] and line[1]:
                    configFile.write("{}={}".format(line[0], line[1]))
                    if line[2]:
                        configFile.write(" # {}".format(line[2]))
                    else:
                        pass
                elif line[2]:
                    configFile.write("# {}".format(line[2]))
if __name__ == '__main__':
    test = ServerProp(r'C:\minecraft\server-Copy.properties')
    test.load()
    test.set('network-compression-threshold', '55')
    test.save()
