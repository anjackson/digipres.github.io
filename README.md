digipres.org
============

This repository holds the source files that are used to generate <http://www.digipres.org>.

How it works
------------

The site is generated using [GitHub Pages](https://pages.github.com/), which uses the [Jekyll](http://jekyllrb.com/) site generator to create static sites from a set of source files and templates. This repository holds the source material (including various data files in _data as well as HTML or MD files) along with templates used to present the content (in _layouts and _includes).

However, note that some of these source files, particularly the _data files, are not intended to be edited manually. They are generated from various other sources of information via a periodic automated process. The information on formats is drawn from many different sources (e.g. PRONOM and the Archive Team File Formats Wiki).

The code that performs these updates is called [Sentinel](https://github.com/digipres/sentinel).

Contributing to this site
-------------------------

* Fork it.
* Install Jekyll and required dependencies: `bundle init`
* Run Jekyll in development mode: `bundle exec jekyll serve --incremental --watch --livereload`
* Commit changes to your fork.
* Submit a pull request, describing the change.

