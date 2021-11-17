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
### Developer Testing Systems
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

## Developer Tests

---

### Testing All Merchandise View

---

#### User Story
+ As a shopper I want to view all merchandise.

#### Expectation(s):
+ All the items in the merchandise model will be displayed.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester knows how many merchandise items are in the database.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Click on **Piano Books**.
1. Click on **All Music Books**.
1. Count number of merchandise items displayed in this view

#### Documented Result(s):
1. If there is an incorrect number of displayed merchandise items, record:
    + The test name, number of displayed merchandise items, and a description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Merchandise Detailed Information View

---

#### User Story
+ As a shopper I want to view a specific merchandise's detailed information.

#### Expectation(s):
+ The tester will check five different detail views.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester knows the content that should display for each product they look at.
+ The tester knows multiple ways to get to a details view

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. The tester will navigate to the details view of a merchandise item.
1. The tester will check all the information of this merchandise item for correctness.
1. The tester will repeat steps steps 1 - 3 choosing a different path to the details view each time.

#### Documented Result(s):
1. If any information of the merchandise item is incorrect, record:
    + The test name, merchandise item name, a brief description of the incorrect material.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Discounted Merchandise View

---

#### User Story
+ As a shopper I want to see all discounted merchandise.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 4

---

#### User Story
+ As a shopper I want to view all items in my cart.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 5

---

#### User Story
+ As a shopper I want to be able to sort the available products by their category.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 6

---

#### User Story
+ As a shopper I want to be able to search for an item by name, description, or composer.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 7

---

#### User Story
+ As a shopper I want to be sent a confirmation email after I checkout.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 8

---

#### User Story
+ As a returning user I would like a create an account.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 9

---

#### User Story
+ As a returning user I would like a confirmation email after registering.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 10

---

#### User Story
+ As a returning user I would like to easily login or logout.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 11

---

#### User Story
+ As a returning user I would like to recover my forgotten passord.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 12

---

#### User Story
+ As a returning user I would like to have a personalized profile that has all my previous order information.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 13

---

#### User Story
+ As a returning user I would like to update my shipping information.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 14

---

#### User Story
+ As a store manager I want to be able to add merchandise.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 15

---

#### User Story
+ As a store manager I want to be able to edit merchandise.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### test - 16

---

#### User Story
+ As a store manager I want to be able to delete merchandise.

#### Expectation(s):
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
#### Testing Step(s):
#### Documented Result(s):
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.




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