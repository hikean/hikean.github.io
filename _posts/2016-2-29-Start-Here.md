---
layout: post
title: Start Here
categories: [Jekyll]
tags: [github, jekyll]
---

<!-- more --> I started Here!<!-- more -->


**Index**


* Contents
{:toc #hello-world}

There are some basic and useful kramdown syntax.

## Code and Highlight


```ruby

def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end

```

## MathJax

$$a^2 = b^2 + c^2$$<br/>
For example this is a Block level $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$ formula, and this is an inline Level 
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$ formula.
\\[ \frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} =1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}{1+\frac{e^{-8\pi}} {1+\ldots} } } } \\]

## Task lists
 - ✘ task one not finish
 - ✓ task two finished 

## Tables

|---
| Default aligned | Left aligned | Center aligned | Right aligned
|-|:-|:-:|-:
| First body part | Second cell | Third cell | fourth cell
| Second line |foo | **strong** | baz
| Third line |quux | baz | bar
|---
| Second body
| 2 line
|===
| Footer row

## Pictures(shown below)
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

## Footnote

This is a footnote[^1] [^foot_note] [^other-note]

[^1]: Some *crazy* footnote definition.

[^foot_note]:
    > Blockquotes can be in a footnote.

        as well as code blocks

    or, naturally, simple paragraphs.

[^other-note]:       no code block here (spaces are stripped away)
