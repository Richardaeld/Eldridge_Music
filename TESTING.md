[Testing](#testing)
+ [Developer Testing Specifications](#developer-testing-specifications)
    + [Developer Testing Systems](#developer-testing-systems)
    + [Developer Testing Methods](#developer-testing-methods)
+ [Developer Tests](#developer-tests)


+ [Program Tests](#program-tests)
    + [BrowserStack](#browserstack)
    + [Lighthouse](#lighthouse)
    + [JigSaw]
    + [W3C Validator](#w3c-validator)
    + [JSHint](#jshint)
    + [PEP8 Online](#pep8-online)
+ [Return to README](#return-to-readme)
---------------------------------------------------


# Testing
## Developer Testing Specifications
### Developer Tested Systems
+ Windows 10 (Chrome 87**, Edge 87**, Firefox 84**)
    + Chrome
        + Developed in Chrome.
        + Initially tested in every bootstrap breakpoint during development.
        + Tested in landscape, which is desktop responsiveness level.
        + Tested in portrait, which is tablet responsiveness level.
    + Edge
        + Tested in landscape, which is desktop responsiveness level.
        + Tested in portrait, which is tablet responsiveness level.
    + Firefox
        + Tested in landscape, which is desktop responsiveness level.
        + Tested in portrait, which is tablet responsiveness level.
+ G8 ThinQ (Chrome 87**)
    + Chrome
        + Tested in landscape, which is tablet responsiveness level.
        + Tested in portrait, which is Mobile responsiveness level.
+ iPad, 5th gen 13.3(Safari 13**)
    + Safari
        + Tested in landscape, which is tablet responsiveness level.
        + Tested in portrait, which is tablet responsiveness level.

### Developer Testing Methods
+ Every test of **Developer Tests** was performed on the above listed systems and the specified screen orientation.
+ The tester will perform each test of **Developer Tests** three times:
    + Once in landscape.
    + Once in portrait.
    + Once with random moments of spam clicking and switching between landscape/portrait. This final test is critical to ensure tablet and mobile users have an enjoyable experience.

## Developer Testing Specifications
### Developer Testing Systems
### Developer Testing Methods
## Developer Tests


## Program Tests
### BrowserStack
### Lighthouse
+ Identifies problems with performance, accessibility, best practices, and SEO.
![Light house results](static/readme/testing/lighthouse-fat-raccoon.jpg "Light house results")

### JigSaw
+ Identifies errors in CSS
![Jigsaw results](static/readme/testing/w3c-jigsaw.jpg "Jigsaw results")
<!-- + Errors are present for some of the CSS art but MDN shows they are not a problem. -->
<!-- + Warnings are present for some of the vendor extensions, but those extensions are necessary and the errors can be ignored. -->

### W3C Validator
+ Identifies errors in HTML.
+ Helpful for proper semantic HTML and ARIA standard practices.
![W3C validator results](static/readme/testing/w3c.jpg "W3c validator results")

### JSHint
+ Identifies errors in JS.
![JSHint results](static/readme/testing/jshint.jpg)

### PEP8 online
+ Identifies errors in Python.
![PEP8 results](static/readme/testing/pep8.jpg)

# Return to README
+ [Return to the README.md](README.md)