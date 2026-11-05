Claude is really good at distilling a site into a style guide and then use it for future designs. 

Really nice 'how to' here: 
https://martinalderson.com/posts/how-to-make-great-looking-consistent-reports-with-claude-code-cowork-code

```
Curl https://www.nasa.gov and extract the brand design tokens — colors,
  typography (font families, sizes, weights), spacing, and any other visual
  patterns you can identify from the page's CSS and inline styles.
  Include the logo (ideally in svg on both dark and white backgrounds).

  Create a design-system.html file that displays all the extracted tokens
  as a visual reference sheet — color swatches with hex values, a type scale
  showing each heading and body style, and spacing examples. It should be
  self-contained (inline CSS, no external dependencies) so I can open it
  in a browser to verify you've captured the brand correctly.

```

```
Using the design system in design-system.html, create two HTML templates:

  1. report-template.html — A4 portrait (210mm x 297mm) document layout with
     print media queries set for clean PDF output. Include a cover page,
     headers/footers with page numbers, a table of contents section, and
     styled sections for headings, body text, code blocks, tables, and callout
     boxes. It should look like a professional NASA-style briefing document.

  2. slides-template.html — 16:9 landscape (254mm x 143mm) slide deck layout.
     Each <section> becomes one slide. Include a title slide, section divider
     slide, content slide with bullets, and a code/diagram slide. Use CSS
     page-break-after to separate slides for PDF rendering.

  Both templates should be self-contained, use the NASA brand tokens, and
  include print media queries that hide browser chrome and set exact page
  sizes. I want to open these in a browser to preview them.
```

Make a markdown to PDF script (I'd uuse a CMS ofc, but this works. Static site generators ftw)
I'd use a CMS probably! But Static Site generators ftw!

```
Create render.js — a Node.js script using Puppeteer that:

  1. Takes a markdown file as input and a flag for format: --format=report
     or --format=slides
  2. Converts the markdown to HTML (use marked or markdown-it — install
     whichever you prefer)
  3. Injects the HTML content into the matching template (report-template.html
     or slides-template.html)
  4. Renders it to PDF with Puppeteer using the correct page size and
     print media settings

  Usage should be: node render.js input.md --format=report -o output.pdf

  Run npm init -y and install the dependencies. Then test it by writing a
  short sample markdown file about a fictional NASA mission status report
  and rendering it as both a report and a slide deck.
```

Thanks https://martinalderson.com ! 
