import io
import sys
import random
from lxml import etree

fp = io.TextIOWrapper(sys.stdin.buffer, encoding=sys.stdin.encoding)
doc = etree.parse(fp)
author = doc.xpath('/list/quote/author')
date = doc.xpath('/list/quote/date')
text = doc.xpath('/list/quote/text')
ranquote = random.randrange(0,len(text))
print("%s\n%s,\n%s" % (text[ranquote].text, author[ranquote].text, date[ranquote].text))
