# Processing

Picking up where we [left off](intro.md), this section will aim to show how you
can manipulate a bach document. Unlike the introduction, where manipulating
documents was just glanced over, there will be practical examples you can try.

## Context

You've authored the bach document, a list of quotes with an author, and date.
Now you need to write a program that takes one of these quotes randomly
generates a nice HTML page for the corporate intranet, and secondly appends
said quote to the `MOTD`.

## Converting bach to XML

First off, clone the bach repo from tawesoft on github.

```shell
$ git clone git@github.com:tawesoft/bach.git
# alternatively
$ git clone https://github.com/tawesoft/bach.git
```

in `bach/python/` there's `bach2xml.py`, which can be used as follows:

```shell
$ python3 ~/bach/python/bach2xml.py < quotes.bach
# alternatively
$ cat quotes.bach | python3 ~/bach/python/bach2xml.py
```

doing this will print the XML to `stdout`, you can save the document by altering
the command slightly.

```shell
$ python3 ~/bach/python/bach2xml.py < quotes.bach > quotes.xml
# alternatively
$ cat quotes.bach | python3 ~/bach/python/bach2xml.py > quotes.xml
```


## Writing a simple "shim" program

Previously It was assumed you already had some solution to parsing the XML.
In case you don't, one has been written for example purposes and will be broken
down line by line.

```python
import io
import sys
import random
from lxml import etree

fp = io.TextIOWrapper(sys.stdin.buffer, encoding=sys.stdin.encoding)
doc = etree.parse(fp)
author = doc.xpath('/list/quote/author')
date = doc.xpath('/list/quote/date')
text = doc.xpath('/list/quote/text')
ranquote = random.randrange(0,3)
print("%s\n%s,\n%s" % (text[ranquote].text, author[ranquote].text, date[ranquote].text))
```

Let's break down the import statements.

```python
import io
import sys
import random
from lxml import etree
```

the import function allows for use to take advantage of other modules that have
already been written. Sometimes modules can be large, so we only want to use a
certain part of them, which is why the last line is `from lxml import etree`, as
we're only importing the `etree` specific section of the `lxml` module.

Now to break down the variables, and what they do.

```python
fp = io.TextIOWrapper(sys.stdin.buffer, encoding=sys.stdin.encoding)
doc = etree.parse(fp)
author = doc.xpath('/list/quote/author')
date = doc.xpath('/list/quote/date')
text = doc.xpath('/list/quote/text')
ranquote = random.randrange(0,3)
```

- `fp`  is what handles the input, allowing the xml document to be fed into the
program.
- `doc` takes the input from `fp` and using `etree` parses the XML.
- `author`, `date`, and `text` use `xpath` from etree to find the tags within the XML
- `ranquote` uses `random` to generate a random number between 0 and 3.

Now all of this code comes together into the final line, the `print()` function.

```python
print("%s\n%s,\n%s" % (text[ranquote].text, author[ranquote].text, date[ranquote].text))
```

Each `%s` corresponds to a variable in the next part of the print function, with
newlines (`\n`) separating each variable to be printed. In parenthesis are the
variables `text`, `author`, and `date`, though they have `[ranquote].text`
appended to them. This is because each variable is really an array, and we use
`ranquote` to randomly pick something out of that array, `.text` specifying
the text contained within the element, and not the element tag itself.

## Using the "shim" program

Now that we've written a shim program that can parse the XML we've generated,
let's use it!

```shell
$ python3 ~/bach/python/bach2xml.py < quotes.bach | python3 shim.py
# alternatively
$ cat quotes.bach | python3 bach2xml.py | python3 shim.py
# and if you had the XML saved already
$ python3 shim.py < quotes.xml
I believe that freedom is the deepest need of every human soul.
George W. Bush,
2004-04-13
```

Any of the 3 ways shown will get the same result.

## Using processed results

In the [next]() section, I'll detail how to take the results we obtained from
processing the bach document, and integrate them into something like HTML, or
an MOTD.
