## Trio: Structured Concurrency for Python

This is the source for my
[PyConZA 2020 talk](https://2020.za.pycon.org/talks/23-trio-structured-concurrency-for-python/) of the same name.

### Usage

This repo uses https://gitlab.com/oer/emacs-reveal to turn org-mode inputs into
reveal.js outputs.

To generate the presentation, install emacs-reveal as per its documentation and
then run the following command:

```
emacs --batch --load elisp/publish.el
```

#### Generate PDF

To generate a PDF, run the publish command above and then edit the `public/main.html` as follows:
- Globally replace `./img` with `./reveal.js/dist/img`
- Add `pdfMaxPagesPerSlide: 1` to the `Reveal.initialize` call

Start the server:
```
(cd public/reveal.js/; npm start)
```

Follow the print-to-pdf instructions at https://revealjs.com/pdf-export/ to get
a PDF.

### Licenses

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
