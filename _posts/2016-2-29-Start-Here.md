---
layout: post
title: Start Here
categories: [Jekyll]
tags: [Github, Jekyll,Markdown]
excerpt: "I started Here!There are some basic and useful kramdown syntax."
#MathJax: true
---



* Contents
{:toc #toc_of_keans_blog}


## Code and Highlight

### Code Block

```ruby
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
```

```c
#include <stdio.h>
#include <stdlib.h>

int a, b, c;
int *e, *p = NULL;

int main()
{
	puts("Hello,Kean!");
	return 0;
}
```

### Inline code

I think you should use an
`<addr>` element here instead.


## MathJax

$$a^2 = b^2 + c^2$$<br/>
For example this is a Block level $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$ formula, and this is an inline Level
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$ formula.
\\[ \frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} =1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}{1+\frac{e^{-8\pi}} {1+\ldots} } } } \\]

## Lists
 - ✘ task one not finish
 - ✓ task two finished

-  [x] task three not finish
- [ ] task one not finish `- + SPACE + [ ]`
- [x] task two finished `- + SPACE + [x]`
- [x] This is a complete item

### Unordered List

* Item 1
* Item 2
  * Item 2a
  * Item 2b

### Ordered List

1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b


## Abbreviations (Kramdown)

This is some text not written in HTML but in another language!

*[another language]: It's called Markdown
*[HTML]: HyperTextMarkupLanguage

## Set Classes and IDs

A simple paragraph with an ID attribute.
{: #para-one}

> A blockquote with a title
{:title="The blockquote title"}
{: #myid}

* {:.cls} This item has the class "cls"

{:.ruby}
    Some code here

## Tables

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

|---
| Default aligned | Left aligned | Center aligned | Right aligned
|-|:-|:-:|-:
| First body part | Second cell | Third cell | fourth cell
| Second line |foo | **strong** | baz
| Third line |quux | baz | bar
| Second body
|---
| 2 line
| ok
| sdf
| sdfd
| dfd
|===
| Footer row

## Picture

![_config.yml]({{ site.baseurl }}/images/404.jpg)

## Links

[hikean.github.io repository](https://github.com/hikean/hikean.github.io) on GitHub.

email <example@example.com>

[GitHub](http://github.com)

autolink  <http://www.github.com/>

## Horizontal Rules

***

*****

- - -

## Emphasis

*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

## Footnote

This is a footnote[^1] [^foot_note] [^other-note]

[^1]: Some *crazy* footnote definition.

[^foot_note]:
    > Blockquotes can be in a footnote.

        as well as code blocks

    or, naturally, simple paragraphs.

[^other-note]:       no code block here (spaces are stripped away)
