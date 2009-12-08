#! /usr/bin/env python

import os
import sys

reader = open("./quran-simple.txt",'r')

OUTPUT_FILE_PREFIX = "QuranVerses."
aya_count = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]
lines = reader.readlines()
text_expander_dict = '''\t\t<dict>
\t\t\t<key>abbreviation</key>
\t\t\t<string>%s</string>
\t\t\t<key>abbreviationMode</key>
\t\t\t<integer>0</integer>
\t\t\t<key>creationDate</key>
\t\t\t<date>2009-11-12T13:27:11Z</date>
\t\t\t<key>flags</key>
\t\t\t<integer>0</integer>
\t\t\t<key>label</key>
\t\t\t<string></string>
\t\t\t<key>lastUsed</key>
\t\t\t<date>2009-11-12T13:28:33Z</date>
\t\t\t<key>modificationDate</key>
\t\t\t<date>2009-11-12T13:27:27Z</date>
\t\t\t<key>plainText</key>
\t\t\t<string>%s</string>
\t\t\t<key>snippetType</key>
\t\t\t<integer>0</integer>
\t\t\t<key>useCount</key>
\t\t\t<integer>1</integer>
\t\t</dict>\n'''

def file_handler(output_file):
    if os.path.exists(output_file):
        os.remove(output_file)
    return open(output_file,'w')
    
    
def create_typinator_bundle(output_file):
    surah=1
    writer = file_handler(output_file)
    i=0;    
    for a in aya_count:
        print surah
        for verse in range(a):
            final_line = "q%s:%s\t%s" %(surah,verse+1,lines[i])
            writer.write(final_line)
            i=i+1
        surah=surah+1    
    writer.close()
    
def create_text_expander_bundle(output_file):
    writer = file_handler(output_file)
    i=0;    
    surah=1
    header = open("text_expander_header.txt",'r').read()
    writer.write(header)
    for a in aya_count:
        for verse in range(a):
            abbr = "q%s:%s" %(surah, verse+1)
            line = text_expander_dict % (abbr,lines[i])
            writer.write(line)
            i=i+1
        surah=surah+1    
    footer = open("text_expander_footer.txt",'r').read()
    writer.write(footer)
    writer.close()

usage = '''
./bundle-creator.py --te
./bundle-creator.py --ty '''

if __name__=='__main__':
    from optparse import OptionParser
    p = OptionParser(usage)

    general_group = p.add_option_group("General Options")

    general_group.add_option("--ty", default=False, action="store_true", help="Create Typinator bundle")
    general_group.add_option("--te", default=False, action="store_true", help="Create TextExpander bundle")

    (opts, args) = p.parse_args()

    if len(args) != 0:
        print "Invalid arguments"
        sys.exit(126)
    elif opts.ty:
        file = OUTPUT_FILE_PREFIX + "txt"
        create_typinator_bundle(file)
    elif opts.te:
        file = OUTPUT_FILE_PREFIX + "textexpander"
        create_text_expander_bundle(file)