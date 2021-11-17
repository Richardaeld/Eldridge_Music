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
1. Click on **Piano Books** on the navigation bar.
1. Click on **All Music Books** from the **Piano Books** drop-down menu.
1. Count number of merchandise items displayed in this view.

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
+ All the items with the boolean tag **special** will be displayed as discounted merchandise with a discount value.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester knows how many merchandise items are on discount.
+ The tester knows where the discount tag is displayed on the details view.
+ The tester knows the correct selling value for each item.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Click on **speials** on the navigation bar.
1. Count the discounted merchandise displayed.
1. Check each item for both the discount tag and the updated price value.

#### Documented Result(s):
1. If there is an incorrect number of displayed discount merchandise items, record:
    + The test name, number of displayed merchandise items, and a description of the problem.
1. If a discounted merchandise item is displayed without a discount value, recored:
    + The test name, merchandise item name, and a description of the problem.
1. If a discounted merchandise item is displayed with an incorrect new price, recored:
    + The test name, merchandise item name, anticipated price, and a description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Shopping Cart

---

#### User Story
+ As a shopper I want to view all items in my cart.

#### Expectation(s):
+ All items chosen for purchase will be displayed in cart view with the proper amounts.
+ The no delivery fee function operates correctly.
+ Sub-total and grand total calculate properly in the **cart** and **cart icon**
+ Success toasts show up for each item added to the cart and the toast contains all the correct information.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester will write down all merchandise they have chosen to purchase and their amounts.
+ The tester knows there is an empty cart page and what it's supposed to look like.
+ The tester will watch the **cart total** and be sure it updates as they add merchandise to their cart.
+ The tester will start the test with an empty cart.
+ The tester knows that with a purchase of more then $50 there is no delivery fee.
+ The tester is watch the success toasts and checking for their accuracy.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Click on the **cart** icon at the top right corner of the view.
1. Check for the correct empty cart page.
1. Click on **Piano Books** on the navigation bar.
1. Click on **All Music Books** from the **Piano Books** drop-down menu.
1. Choose a random merchandise item with a random quantity amount and add that to the cart.
1. Repeat step 4 - 6, four to nine times more.
1. Click on the **cart** icon at the top right corner of the view.
1. Check for a correct grand total, delivery total, and sub-total.
1. Empty cart.
1. Repeat steps 4 - 7. This time ending with a grand total under $50
1. Check for a correct grand total, delivery total, and sub-total.


#### Documented Result(s):
1. If the empty cart view does not display with an empty cart, record:
    + The test name, and a brief description of the problem.
1. If the delivery cost doesn't update correctly according to the free delivery threshold, record:
    + The test name, all items with their quantities in the cart, and a brief description of the problem.
1. If the success toast doesn't work or displays incorrect information, record:
    + The test name, all items with their quantities in the cart, the last item and amount choosen, and a brief description of the problem.
1. If the sub-total, delivery total, grand total do not appropriately sum up, record:
    + The test name, all items with their quantities in the cart, and a brief description of the problem
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Piano Book Categories

---

#### User Story
+ As a shopper I want to be able to sort the available products by their category.

#### Expectation(s):
+ Each Category will display all the correct merchandise.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester knows all merchandise items that should appear in each category.
+ The tester knows the total of merchandise items that should appear in each category.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Click on **Piano Books** on the navigation bar.
1. Click on **Seasonal** from the **Piano Books** drop-down menu.
1. Check the view for the correct number of merchandise items.
1. Check each additional category under **Piano Books** until all categories have been checked.

#### Documented Result(s):
1. If a category doesn't have the correct number of merchandise items, record:
    + The test name, the category, the total amount of merchandise items present, a brief description of the problem, and the incorrect merchandise item present or item missing.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing User Search Bar

---

#### User Story
+ As a shopper I want to be able to search for an item by name, description, or composer.

#### Expectation(s):
+ User search bar returns correct information when a user submits a item name or its composer(s).
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester knows all the books two composers have in database.
+ The tester know the names of four different books in database.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Enter a composers name into the user search bar.
1. Check returns for correct information.
1. Repeat step 2 - 3.
1. Enter a merchandise item's name into the user search bar.
1. Check returns for correct information.
1. Repeat step 5 - 6, three more times.

#### Documented Result(s):
1. If any user search returns are incorrect, record:
    + The test name, if a composer or item name was being searched for, and a brief description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Confirmation Email for Purchase

---

#### User Story
+ As a shopper I want to be sent a confirmation email after I checkout.

#### Expectation(s):
+ A confirmation email will be sent out after a purchse.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester knows the dummy codes for Stripe
+ The tester has access to an email account.
+ The tester will create an account for this test, and will keep a record of the account.
+ The tester know the content of a confirmation email.
+ The tester will have their invoice #, date, sub-total, delivery-total, grand total, and contact information written down.
+ The tester knows how to use an e-commerce store.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Be sure there is no current session or log out of current session.
1. Put multiple merchandise items into the cart with different quantity amounts.
1. Proceed to checkout and finalize checkout.
1. Check over content of confirmation email.
1. Load the **Index View** of Eldridge Music.
1. Log into an account.
1. Repeat steps 3 - 5.

#### Documented Result(s):
1. If the success toast does not display or displays incorrect information, record:
    + The test name, if the tester was logged in, anticipated toast information, actual toast information, and a bried description of the problem.
1. If the confirmation email is not received, record:
    + The test name, if the tester was logged in, the email name, the invoice #, and a bried description of the problem
1. If any of the email content is incorrect, record:
    + The test name, if the tester was logged in, the content expected, and actual content, and a bried description of the problem.
1. A user account was created to fulfill the test's requirements, record:
    + The username, email address of the account, and that this is a test account.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Account Confirmation Email

---

#### User Story
+ As a returning user I would like a confirmation email after registering.

#### Expectation(s):
+ A confirmation email will be sent out at the end of the account creation process.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester has access to an email account.
+ The tester will create an account for this test, and will keep a record of the account.
+ The tester knows the content of both the confirmation email and the confirmation page.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Click on the **Profile** icon.
1. Click on **Create Account**.
1. Fill out information and submit.
1. Open the email account the confirmation email was sent to and open the confirmation email.
1. Select the confirmation string.
1. Check the information provided here is correct and then confirm.

#### Documented Result(s):
1. A user account was created to fulfill the test's requirements, record:
    + The username, email address of the account, and that this is a test account.
1. If the information provided on the confirmation email or the confirmation page is incorrect, record:
    + The test name, the incorrect information, the anticipated information, and a brief description of the problem
1. If no confirmation email is received, record:
    + The test name, the email used, the account name used, and a bried description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Account Creation

---

#### User Story
+ As a returning user I would like a create an account.

#### Expectation(s):
+ An account can be created, accessed, and updated.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester has access to an email account.
+ The tester will create an account for this test, and will keep a record of the account.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Click on the **Profile** icon.
1. Click on **Create Account**.
1. Fill out information and submit.
1. Open the email account the confirmation email was sent to and open the confirmation email.
1. Select the confirmation string.
1. Confirm for a new account.
1. Log in with new account.
1. Click on the **Profile** icon.
1. Click on the **Profile** button.
1. Update **Shipping Info** and submit.
1. Check for correctness.

#### Documented Result(s):
1. A user account was created to fulfill the test's requirements, record:
    + The username, email address of the account, and that this is a test account.
1. If the new account does not accept the login information, record:
    + The test name, the email name, the user name, and a bried description of the problem.
1. If the new account information does not update, record:
    + The test name, the email name, the username, the anticipated information updated, and a brief description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.



---

### Testing Login and Logout

---

#### User Story
+ As a returning user I would like to easily login or logout.

#### Expectation(s):
+ The tester can login and logout.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester will create an account for this test or use a pre-existing account. The tester will keep a record of the account.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Click on the **Profile** icon.
1. Click on the **Login** button.
1. Log into Eldridge Music Book Emporium.
1. Click on the **Profile** icon.
1. Click on the **Profile** button.
1. Check for correct profile page.
1. Click on the **Profile** icon.
1. Click on the **Logout** button.
1. Click on the **Profile** icon.
1. Check for correct content of drop-down.

#### Documented Result(s):
1. A user account was created to fulfill the test's requirements or a pre-existing account was used, record:
    + The username, email address of the account, and that this is a test account.
1. If the login information was not accepted, record:
    + The test name, the email name, the username, and a brief description of the problem.
1. If the logout was not accepted , record:
    + The test name, the username, the email name, and a brief description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Password Recovery

---

#### User Story
+ As a returning user I would like to recover my forgotten passord.

#### Expectation(s):
+ A user can recover/change their current password.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester will create an account for this test or use a pre-existing account. The tester will keep a record of the account.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Click on the **Profile** icon.
1. Click on the **Login** button.
1. Click on **Forgot Password?**.
1. Enter email for account and submit.
1. Open the email account the change password email was sent to and open the change password email.
1. Click on the change password string.
1. Create a new passwrod and submit.
1. Login with the new password.


#### Documented Result(s):
1. A user account was created to fulfill the test's requirements or a pre-existing account was used, record:
    + The username, email address of the account, and that this is a test account.
1. If no change password email is received, record:
    + The test name, the email used, the account name used, and a bried description of the problem.
1. If the new password does not work, record:
    + The test name, the username, the email name, and a brief description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Invoice Remember Information

---

#### User Story
+ As a returning user I would like to have a personalized profile that has all my previous order information.

#### Expectation(s):
+ When **Remember My Information** box is checked it will update users **Shipping Information**.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester will create an account for this test or use a pre-existing account. The tester will keep a record of the account.
+ Tester knows Striped dummy codes.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Proceed through to checkout with any combination of items in the cart.
1. Fill out shipping information and check **Remember My Information**.
1. Submit order with Stripe's dummy information.
1. Open **Profile view** and check to see if **Shipping Information** has been updated.

#### Documented Result(s):
1. A user account was created to fulfill the test's requirements or a pre-existing account was used, record:
    + The username, email address of the account, and that this is a test account.
1. If the **Shipping Information** is not updated, record:
    + The test name, the email name, the username, the information anticipated, the actual information, and a brief description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Updating Shipping Information from Profile View

---

#### User Story
+ As a returning user I would like to update my shipping information.

#### Expectation(s):
+ The **Shipping Information** is updatable from **Profile View**.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester will create an account for this test or use a pre-existing account. The tester will keep a record of the account.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Proceed to **Profile View**.
1. Change all the information found within **Shipping Information** and update.
1. Check for correctness.

#### Documented Result(s):
1. A user account was created to fulfill the test's requirements or a pre-existing account was used, record:
    + The username, email address of the account, and that this is a test account.
1. If the **Shipping Information** does not update, record:
    + The test name, the email name, the username, the information anticipated, the actual information, and a brief description of the problem.
1. If any links or images are broken, record:
    + The test name, image or link name, and a brief description of the problem.
1. If any content has bad UX, record:
    + The test name, screen resolution, browser/device, view (page), and a brief description of the bad UX.

---

### Testing Superuser Add Merchandise

---

#### User Story
+ As a store manager I want to be able to add merchandise.

#### Expectation(s):
+ Any superuser can add merchandise.
+ The page content fills appropriately and doesn't spill out beyond obvious borders.
+ The page content doesn't overlap and is easy to read.

#### Assumptions(s):
+ The tester will have a pre-existing superuser account. The tester will keep a record of the account.
+ The tester will keep a record of any and all created merchandise. Including the merchandise name, and sku
+ The tester will create a test specific sku with each merchandise item.
+ The tester will add an image to the merchandise item and keep a record of the image name.
+ The tester will have an image to upload as a merchandise image.

#### Testing Step(s):
1. Load the **Index View** of Eldridge Music.
1. Log into account.
1. Click on the **Profile** icon.
1. Click on the **Merchandise Management** button
1. Create a new merchandise item.
1. Find the new item and check for accuracy.
1. Create a new merchandise item with an image.
1. Find the new item and check for accuracy.

#### Documented Result(s):
1. A user account was created to fulfill the test's requirements or a pre-existing account was used, record:
    + The username, email address of the account, and that this is a test account.
1. A merchandise item was created to fullfill the test's requirements, record:
    + The test name, the merchandise name, sku, and that these are test merchandise.
1. A image was used to fullfill the test's requirements, record:
    + The test name, the image name, and that these are test image(s).
1. If the merchandise item is incorrect, record:
    + The test name, the merchandise name, merchandise sku, anticipated information, actual information, and a brief description of the problem.
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