

<!-- README.md is generated from README.qmd. Please edit that file -->

# JOAS

This Quarto format will help you create articles for the Journal of Open
Aviation Science (JOAS).

## Creating a new article

You can use this as a template to create an article. To do this, use the
following command:

``` bash
# eventually to be moved to quarto-journals
quarto use template espinielli/quarto-joas
```

This will install the extension and create an example qmd file that you
can use as a starting place for your article.

**NOTE**: please soon after the creation of your article remember to
render the qmd twice for the first time. This will copy the needed
files.

## Installation for existing document

You may also use this format with an existing Quarto project or
document. From the quarto project or document directory, run the
following command to install this format:

``` bash
# eventually to be moved to quarto-journals
quarto install extension espinielli/quarto-joas
```

## Example

[![](examples/template.png)](examples/template.pdf)

# Options

## Document class

- `manuscript=`
  - `manuscript=article` (default)
  - `manuscript=rescience`
  - `manuscript=data`
  - `manuscript=software`
  - `manuscript=proceedings`
  - `manuscript=poster`
- `layout=`
  - `preprint` for submission
  - `publish` for publisher only. This prepared the paper for
    publication with all the *blees & whistles* required. See also
    <a href="#sec-publisher-options" class="quarto-xref">Section 2.2</a>
    and <a href="#fig-metadata" class="quarto-xref">Figure 1 (a)</a>.
- `volume=` used by publisher, see
  <a href="#fig-metadata" class="quarto-xref">Figure 1 (a)</a>.
- `year=` used by publisher, see
  <a href="#fig-metadata" class="quarto-xref">Figure 1 (a)</a>.

For example the following YML snippet (and the ones in
<a href="#sec-publisher-options" class="quarto-xref">Section 2.2</a>)

``` yml
format:
  joas-pdf:
    classoption:
      - "manuscript=proceedings"
      - "layout=publish"
      - "volume=x"
      - "year=20xx"
```

will render metadata as per
<a href="#fig-metadata" class="quarto-xref">Figure 1 (a)</a>. The
published paper will as well mention the open license JOAS promotes, see
<a href="#fig-license" class="quarto-xref">Figure 1 (b)</a>.

<div id="fig-published">

<div id="fig-metadata">

<img src="examples/final-metadata-joas.png"
data-ref-parent="fig-published" />

(a) publishing touches

</div>

<div id="fig-license">

<img src="examples/license-joas.png" data-ref-parent="fig-published" />

(b) License at the bottom of the title page.

</div>

Figure 1: Final touches for publication.

</div>

## Publisher options

- `layout=publish`, see
  <a href="#sec-doc-class" class="quarto-xref">Section 2.1</a>
- `joas-doi`: the DOI of the paper
- `joas-editor`: the name of the editor
- `joas-reviewer`: the list of reviewers
- `joas-dates`: the review dates

The following settings will render as per
<a href="#fig-published" class="quarto-xref">Figure 1</a>.

``` yml
joas-doi: "xx.xxxxx/joas.x.xxxx"
joas-editor: Editor Name
joas-reviewer:
  - First Reviewer
  - Second Reviewer
  - Third Reviewer
joas-dates:
  received: "1 April 2024"
  revised: "1 May 2024"
  accepted: "10 May 2024"
  published: "20 May 2024"
```

## Other options

``` yml
joas-abbreviations:
  - "JOAS: Journal of Open Aviation Science"
  - "ATM: Air Traffic Managment"
```

# Deficiencies

1.  On macOS I do not get the same font as per orignal JOAS. I think it
    is due to some other packages or options selected there.
2.  The plain `joas.cls` needs to be edited: the line \> does not work,
    `eulergreek` needs to be removed.

# How to upgrade to a new `joas.cls`

Other than what mentioned above about `eulergreek`, I changed the
original class to read

``` tex
\ProvidesClass{joas}
```

instead of

``` tex
\ProvidesClass{extra/joas}
```
