#!/usr/bin/python

import sys
#import GoogleScholar
#import CiteSeerX
from optparse import OptionParser

usage = "usage: %prog [options] arg"
parser = OptionParser(usage)


parser.add_option("--engine", dest="engine",
                  help="Type of searching engine google=GoogleScholar, citeseerx=CiteSeerX",type="string", metavar="ENGINE")

parser.add_option("--type", dest="type",
                  help="Type of search to use, BAS=basic, EXT=EXTENDED",type="string", metavar="BAS/EXT")


parser.add_option("--phrase", dest="phrase",
                  help="Phrase we would like to search",type="string", metavar="PHRASE")


parser.add_option("--output", dest="filename",
                  help="File to write report", metavar="FILE")


parser.add_option("--sort", dest="sort",
                  help="Type of sort for CiteSeeX",type="int", metavar="NUM")


parser.add_option("--citation", dest="citation",
                  help="Include citation for CiteSeeX False=NotInclude True=Include",type="string", metavar="Bool")

parser.add_option("--title", dest="title",
                  help="Title for search for extend search CiteSeerX",type="string", metavar="TITLE")

parser.add_option("--author", dest="author",
                  help="Include autor in extend search CiteSeerX/GoogleScholar",type="string", metavar="Name")

parser.add_option("--authoraffi", dest="authoraffi",
                  help="Include author affiliation in extend search CiteSeerX",type="string", metavar="AFFI")
                  
parser.add_option("--publicvenue", dest="publicvenue",
                  help="Include public venue in extend search CiteSeerX/GoogleScholar",type="string", metavar="VENUE")
                  
parser.add_option("--keywords", dest="keywords",
                  help="Include keywords in extend search CiteSeerX",type="string", metavar="KEYWORDS")

parser.add_option("--abstract", dest="abstract",
                  help="Include name of abstract in extend search CiteSeerX",type="string", metavar="ABST")

parser.add_option("--mincitations", dest="mincitations",
                  help="Include minimal number of citations in extend search CiteSeerX",type="int", metavar="NUM")

parser.add_option("--startyear", dest="startyear",
                  help="Include results from startyear in extend search CiteSeerX/StartYear",type="int", metavar="YEAR")

parser.add_option("--endyear", dest="endyear",
                  help="Include results from endyear in extend search CiteSeerX/GoogleScholar",type="int", metavar="YEAR")

parser.add_option("--withcorrectphrase", dest="withcorrectphrase",
                  help="Include in results withcorrectphrase in extend search GoogleScholar",type="string", metavar="PHRASE")

parser.add_option("--withoutwords", dest="withoutwords",
                  help="DO not include in results withoutwords in extend search GoogleScholar",type="string", metavar="PHRASE")

parser.add_option("--leastoneword", dest="leastoneword",
                  help="Include in results leastoneword in extend search GoogleScholar",type="string", metavar="PHRASE")

parser.add_option("--occurence", dest="occurence",
                  help="Search in occurence=title/article in extend search GoogleScholar",type="string", metavar="PHRASE")

parser.add_option("--format", dest="format",
                  help="format results=NEWLINE/WHITESPACE/JSON",type="string", metavar="FORM")

(options, args) = parser.parse_args()                

if (len(args) <4):
    raise Exception("Little number of parameter")

if (len(options.engine) <1 or len(options.phrase) <1 or len(options.type) <1 or len(options.filename) <1 or len(options.format) <1):
     raise Exception("Little number of parameter")







sys.exit(0)






























