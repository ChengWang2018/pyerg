## ---------------------------------------------------------------------------- ##
#   08/03/2015                                                                   #
#                                                                                #
#   www.henesis.eu                                                               #
#                                                                                #
#   Alessandro Bacchini - alessandro.bacchini@henesis.eu                         #
#                                                                                #
# Copyright (c) 2015, Henesis s.r.l. part of Camlin Group                        #
#                                                                                #
# The MIT License (MIT)                                                          #
#                                                                                #
# Permission is here by granted, free of charge, to any person obtaining a copy  #
# of this software and associated documentation files (the "Software"), to deal  #
# in the Software without restriction, including without limitation the rights   #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      #
# copies of the Software, and to permit persons to whom the Software is          #
# furnished to do so, subject to the following conditions:                       #
#                                                                                #
# The above copyright notice and this permission notice shall be included in all #
# copies or substantial portions of the Software.                                #
#                                                                                #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  #
# SOFTWARE.                                                                      #
## ---------------------------------------------------------------------------- ##

import pyerg


def main():
    doc = 'Module:\n'
    doc += pyerg.__doc__

    for name in pyerg.__dict__:
        if not name.startswith('__'):
            doc += '\n\n' + name + ':\n'
            doc += getattr(pyerg, name).__doc__

    for name in pyerg.Parser.__dict__:
        if not name.startswith('__'):
            doc += '\n\n' + name + ':\n'
            doc += getattr(pyerg.Parser, name).__doc__

    print doc

if __name__ == '__main__':
    main()
