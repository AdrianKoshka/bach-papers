# Quotes

A decent bare-bones crash course to `bach` syntax can be found
[here](https://github.com/tawesoft/bach).

## Context

Perhaps you had something that you wanted organized into a structured document.
For examples sake, we'll use a list of quotes, with an author, and date. You
want the contents of this document to both show up as an `MOTD` (Message of the
day), but also generate a nice HTML page for the corporate intranet, let's say
you've already written said parser in `python`, but need to show a co-worker
how to parse and write additions to the document.

## Creating the document

Your document could end up looking something like this.

```
list

(quote "Only Thing We Have to Fear Is Fear Itself."
  (author "Franklin Delano Roosevelt")
  (date "1933-03-04")
)

(quote "I believe that freedom is the deepest need of every human soul."
  (author "George W. Bush")
  (date "2004-04-13")
)

(quote "We don't wage war, but we are called upon to impose a peaceful solution."
  (author "Gerhard Schröder")
  (date 1999-03-24"")
)
```

Let's break this document down, the first line contains the word `list`, this is
simply to signal to the parser, what type of document/SCHEMA you're using. Then
comes:

```
(quote "Only Thing We Have to Fear Is Fear Itself"
  (author "Franklin Delano Roosevelt")
  (date "1933-03-04")
)
```

the first tag `(quote)` tells the parser that you're going to start a quote,
then in quotation marks, the quote itself is entered, which is an `attribute`.
Nested within `(quote)` are `children` like `(author)`, and `(date)`, which
contain their own `attributes`. The tag `(author)` contains the string-literal `"Franklin Delano Roosevelt"`, and the `(date)` tag contains an ISO 8601
formatted date. After the `(date)` tag, the `(quote)` tag is closed.

## Usage

You now have the document `quotes.bach`, and have written a parser in `python`
which you need to show your co-worker how to use. You also have a validator,
though it expects `XML`, as does the program which creates the `MOTD` and
generates the HTML. The parsing could be done something like:

``bach2xml quotes.bach | validator yourschema.rng | foobar-program``

We'll just assume upon successful validation, your validator passes the XML onto
the next program, this is just a super rough example. Realistically programs
might not pipe together so cleanly.

## Why did we write the document in bach then!?

So, why did we write the document in `bach`, something you probably had to write
your own parser for your schema for? Simply put, it's quite a bit nicer and
easier to read and write then XML is.
