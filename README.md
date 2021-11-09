
# Contents
[Eldridge Music Book Emporium - Introduction](#eldridge-music-book-emporium---introduction)

[UX](#ux)
+ [Goals](#goals)
    + [User Stories](#user-stories)
    + [Developer Goals](#developer-goals)
+ [Client Stories](#client-stories)

[Design Choices](#design-choices)
+ [Home](#home)
+ [Login-Logout-Etc...](#login-logout-etc...)
+ [Merchandise](#merchandise)
+ [Specials](#specials)
+ [Merchandise Details](#merchandise-details)
+ [Invoice - Checkout](#invoice---checkout)
+ [Cart](#cart)
+ [Profile](#profile)
+ [Return Emails](#return-emails)
+ [Superuser Merchandise CRUD views](#superuser-merchandise-crud-views)
+ [Wireframe and Live Applications](#wireframe-and-live-applications)
    + [Wire Frame](#wire-frame)
    + [Live App](#live-app)
+ [Scalability](#scalability)

[Technology and Languages](#technology-and-languages)

[Testing](#testing)

[Bugs and Other Problems](#bugs-and-other-problems)
+ [Currnet Bugs](#currnet-bugs)
+ [Other Problems](#other-problems)

[Deployment](#deployment)
+ [GitHub - GitPod](#github---gitpod)
+ [Requirements](#requirements)
+ [Heroku](#heroku)
+ [AWS](#aws)

[Tools and Credits](#tools-and-credits)
+ [Tools](#tools)
+ [Credits](#credits)
    + [Code Citations](#code-citations)
    + [References and Ideas](#references-and-ideas)
[Acknowledgements](#acknowledgements)

--------------------------------------------------------------------------------------

# Introduction
Eldridge Music Book Emporium is dedicated to spreading the love and appreciation of music through the exchange of used and new music books. 
We are a small mom and pop shop that is entering the 21st century with our first e-commerce store! Currently we have plans to expand our 
music selection to include other books than Piano, however it might be some time until we make it that far. Until then please spend a moment 
to peruse our selection and hopfully give some lightly used music books a second chance!

# UX
## Goals
### User Stories
+ As a shopper I want to view all merchandise.
    + I opened the home page of Eldridge Music Book Emporium. I clicked on, 'Music Books' on the header and I saw a drop down menu. I then 
    clicked on, 'All Music Books' and saw a list of all the music books of the site.
+ As a shopper I want to view a specific merchandise's detailed information.
    + I opened the home page of Eldridge Music Book Emporium. I clicked on, 'Music Books' on the header and I saw a drop down menu. I then 
    clicked on, 'All Music Books' and saw a list of all the music books of the site. I found a book I liked and clicked on the merchandise 
    card and found all the detailed information I needed.
+ As a shopper I want to see all discounted merchandise.
    + I opened the home page of Eldridge Music Book Emporium. I clicked on, 'Specials' on the header and was taken to a page containing 
    all the discounted music books.
+ As a shopper I want to view all items in my cart.
    + As I am shopping I'm curious how much money I am spending on my selected merchandise. I click on a cart icon in the top right corner 
    of the page and I'm taken to a page where I can see all the items I have in my cart and the total amount of money it will cost me.
+ As a shopper I want to be able to sort the available products by their category.
    + I opened the home page of Eldridge Music Book Emporium. I clicked on, 'Music Books' on the header and I saw a drop down menu. I then 
    am able to select which category of music books I would like to view.
+ As a shopper I want to be able to search for an item by name, description, or composer.
    + I opened the home page of Eldridge Music Book Emporium. I see a user input search bar and input the composer I am looking for. I am 
    taken to a page containing all the books composed by the composer I input.
+ As a shopper I want to be sent a confirmation email after I checkout.
    + As I am finishing shopping I click the, 'Go to secure checkout' button and I am taken to a from I must fill to check out. I finish 
    form and after I submit it I am sent an email with detailed information about my order.

+ As a returning user I would like a create an account.
    + I opened the home page of Eldridge Music Book Emporium. I click on the profile button on the top right corner of the page and I am 
    able to click, 'Create Account'. I am taken to a page where I can start the process to create an acoount.
+ As a returning user I would like a confirmation email after registering.
    + I opened the home page of Eldridge Music Book Emporium. I click on the profile button on the top right corner of the page and I am 
    able to click, 'Create Account'. I am taken to a page where I can start the process to create an acoount and when I finish I am sent 
    a confirmation email.
+ As a returning user I would like to easily login or logout.
    + I opened the home page of Eldridge Music Book Emporium. I click on the profile button on the top right corner of the page and I am 
    able to click, 'Login'. I am taken to a page and asked to login.
+ As a returning user I would like to recover my forgotten passord.
    + I opened the home page of Eldridge Music Book Emporium. I click on the profile button on the top right corner of the page and I am 
    able to click, 'Login'. I click a button 'Forgot Password?' and I am taken to a password reset page.
+ As a returning user I would like to have a personalized profile that has all my previous order information.
    + I opened the home page of Eldridge Music Book Emporium. I click on the profile button on the top right corner of the page and I am 
    able to click, 'Login'. I am taken to a page where I login. After I login I can clearly see all of my previous orders.
+ As a returning user I would like to update my shipping information.
    + I opened the home page of Eldridge Music Book Emporium. I click on the profile button on the top right corner of the page and I am 
    able to click, 'Login'. I am taken to a page where I login. After I login I can clearly see all of my shipping information. I update 
    my shipping information and submit the changes.

+ As a store manager I want to be able to add merchandise.
    + I login with my store manager account. I click on the profile button and select, 'Merchandise Management'. I am taken to a page 
    where I can add a merchandise item.
+ As a store manager I want to be able to edit merchandise.
    + I login with my store manager account. I search for and find the item that needs editing. On the top right corner of the merchandise 
    card I see a button that says, 'edit'. I click this button and I am able to edit all the fields of the merchandise item
+ As a store manager I want to be able to delete merchandise.
    + I login with my store manager account. I search for and find the item that needs to be removed from the store. On the top right 
    corner of the merchandise card I see a button that says, 'delete'. I click the delete button and the item is removed from the store.

# Design Choices
## Home

## login/logout/etc...
## Merchandise
# Specials
## Merchandise Details
## Invoice/Checkout
## Cart
## Profile
## Superuser Merchandise CRUD views
## Wireframe and Live Applications
### Wire Frame
### Live App
## Scalability
+ add different music book types, guitar, etc...
+ create a column for each guitar, etc...
+ add a 'special' to the index page as a way to tempt users to make an additional purchase

# Technology and Languages
# Testing
# Bugs and Other Problems

## Currnet Bugs
+ displaying roman numerals accurately -- django title tag -- no solution

## Other Problems
+ bootstraps toasts wouldnt function proper -- wrote own JS vanilla
+ Had to remove header that showed the page user was on because names were to big and caused a poor user experience

# Deployment
## GitHub - GitPod
### Requirements
### Heroku
### AWS
### Return Emails

# Tools and Credits
## Tools
+ [Balsamiq](https://balsamiq.com/)
    + Used to produce the wireframes.
+ [Bootstrap](https://getbootstrap.com/)
    + Used as framework.
+ [BrowserStack](https://www.browserstack.com/)
    + Used to check for compatibility errors.
+ [GitHub](https://github.com/)
    + Used for version control and deploys application information to Heroku.
+ [GitPod](https://www.gitpod.io/)
    + Integrated development environment used.
+ [Google Fonts](https://fonts.google.com/)
    + Imported font families from here.
+ [Heroku](https://www.heroku.com/)
    + Site where application is deployed.
+ [Jigsaw (Validation Service)](https://jigsaw.w3.org/css-validator/)
    + Used to identify errors in CSS.
+ [JSHint](https://jshint.com/)
    + Used to identify errors in JavaScript.
+ [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    + Used to check for performance, accessibility, best practices, and SEO.
+ [Pingdom](https://tools.pingdom.com/)
    + Used to check load time.
+ [Techsini](https://techsini.com/multi-mockup/)
    + Used for their viewable responsiveness PNG.
+ [TinyPNG](https://tinypng.com/)
    + Used to Minimize KB load per image.
+ [W3C Validator](https://validator.w3.org/)
    + Used to identify errors in markup.
+ [JSFiddle](https://jsfiddle.net/)
    + Used for tinkering and creating CSS art.
+ [Inkscape](https://inkscape.org/)
    + Used to create scalable vector graphics (SVG).
+ [RandomKeygen](https://randomkeygen.com/)
    + Used to create random secret key for "env.py"
+ [PEP8 online](http://pep8online.com/)
    + Used to identify errors in Python.

## Credits
### Code Citations
### References and Ideas
+ [Bootstrap](https://getbootstrap.com/)
    + A framework used to help speed up development and provide a better overall UX.
+ [MDN Web Docs](https://developer.mozilla.org/en-US/)
    + Invaluable source of information about JavaScript, HTML, and CSS.
+ [Stack Overflow](https://stackoverflow.com/)
    + A great source of information for finding a starting place for research.
+ [TestLodge](https://blog.testlodge.com/how-to-write-test-cases-for-software-with-sample/)
    + Used to help formulate the test syntax structure.
+ [W3Schools](https://www.w3schools.com/)
    + Extremely helpful for explaining base HTML, CSS, and JavaScript principles.
+ [World Wide Web Consortium (W3C)](https://www.w3.org/)
    + Used to understand basic standardization practices for web-based apps.
+[Django](https://docs.djangoproject.com/en/3.2/)
    + A through guide to this massive and intricate frame work.


# Acknowledgements
+ Emily Eldridge for help with revising the grammar and flow of this README document.
+ Felipe Souza Alarcon for his suggestion of a recipe themed project, his help and guidance.