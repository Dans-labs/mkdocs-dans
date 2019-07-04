# Customization

## A great starting point

Project documentation is as diverse as the projects themselves and the DANS
theme is a good starting point for making it look great. However, as you write
your documentation, you may reach a point where some small adjustments are
necessary to preserve the desired style.

## Adding assets

[MkDocs][1] provides several ways to interfere with themes. In order to make a
few tweaks to an existing theme, you can just add your stylesheets and
JavaScript files to the `docs` directory.

  [1]: https://www.mkdocs.org

### Additional stylesheets

If you want to tweak some colors or change the spacing of certain elements,
you can do this in a separate stylesheet. The easiest way is by creating a
new stylesheet file in your `docs` directory:

``` sh
mkdir docs/stylesheets
touch docs/stylesheets/extra.css
```

Then, add the following line to your `mkdocs.yml`:

``` yaml
extra_css:
  - 'stylesheets/extra.css'
```

Spin up the development server with `mkdocs serve` and start typing your
changes in your additional stylesheet file – you can see them instantly after
saving, as the MkDocs development server implements live reloading.

### Additional JavaScript

The same is true for additional JavaScript. If you want to integrate another
syntax highlighter or add some custom logic to your theme, create a new
JavaScript file in your `docs` directory:

``` sh
mkdir docs/javascripts
touch docs/javascripts/extra.js
```

Then, add the following line to your `mkdocs.yml`:

``` yaml
extra_javascript:
  - 'javascripts/extra.js'
```

Further assistance can be found in the [MkDocs documentation][2].

  [2]: https://www.mkdocs.org/user-guide/styling-your-docs/#customizing-a-theme

## Theme development

The Material theme, on which the DANS theme is based,
uses [Webpack][3] as a build tool to leverage modern web
technologies like [Babel][4] and [SASS][5]. If you want to make more fundamental
changes, it may be necessary to make the adjustments directly in the source of
the Material theme and recompile it. This is fairly easy.

  [3]: https://webpack.js.org/
  [4]: https://babeljs.io
  [5]: http://sass-lang.com

In fact, this is exactly the way how the DANS theme has been derived
from the Material theme.

If you want to go this road, make a new clone of the original
[mkdocs-material](https://github.com/squidfunk/mkdocs-material)
repository, consult the 
[docs](https://squidfunk.github.io/mkdocs-material/customization/#theme-development)
over there, and go ahead.
