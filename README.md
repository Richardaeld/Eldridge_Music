
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
## Base - header
+ Logo was given a layered effect that gives it a near shinning look
+ Search bar can be used to search: description, composer, name.
+ A profile icon and button allow users to access log in/out functions, superuser functions, and user profile.
+ A cark icon shows users how much they are spending and will take them to their cart
+ A bar that display's the sites current special.

## Home
+ A hero image was used with a musical theme.
+ A container with a header that displays the site's new or discounted items to help lure in more customers.

## login/logout/etc...
+ Allauth's templates were used with Bootstrap 4's styling.
+ Additional styling was added to give the templates a unique feeling.

## Merchandise
+ A warm and inviting linear gradient was used for the background.
+ Each Merchandise item has its own card that helps it stand out from the background.
+ A used and discount banner are added to merchandise with those tags. This helps users find a cheaper option.
+ Each card has general text and an image of the merchandise to give users all the basic information at a glance.
    + All information has a character max to keep cards brief.
+ Each card is fitted with superuser edit/delete options for easy of inventory management.

## Specials
+ A view that returns only discounted merchandise for the user to see in the same format as the Merchandise view

## Used
+ A view that returns only used merchandise for the user to see in the same format as the Merchandise view

## Merchandise Details
+ A warm and inviting linear gradient was used for the background.
+ A single card is featured here with its full content unabbreviated.

## Cart
+ With nothing in the cart this view asks users to continue shopping.
+ This view allows users to see each item, its quantity, sub-total and more for quickly deciding if they are happy with their order before preceding to the checkout.
+ A convenient remove button is put in the quantity column for users to easilly remove an item.
+ A quantity adjustment input for users to easily adjust the amount of a merchandise item they want.
+ This view features a sub-total per item and a total item subtotal, along with a delivery total and grand total.

## Invoice/Checkout
+ This view give shows a cart summary with grand total to be sure customers know what they are about to order.
+ An invoice a simple form that asks for the users basic shipping and payment information.
+ If the user is signed and has saved their basic informaition the aformentioned form will be prepopulated for the user.
+ This from also allows signed in users to update their information when they submit an invoice.

## Profile
+ This view allows users to see their basic shipping information and all previous invoices.
+ Two buttons located at the top of the form allow users to view their shipping information, previous invoices, or both.
+ User's can update their shipping information from the prefered shipping form on this view.

## Superuser Merchandise CRUD views
+ The add (Merchandise Management) view returns a blank merchandise model so a superuser can create a fully functional new item.
+ The edit view returns a prefilled merchandise model so a superuser can edit any part of the item.
+ The delete view deletes the item without a secondary view.

## Wireframe and Live Applications
### Wire Frame
+ Each wireframe contains curly brackets that give a description of its contents and what the filler (missing database data) content should be.
![Wireframe of the index page](static/readme/wireframe/index-page-large.png "Wireframe of the index page")
+ Balsamiq was used for the planning process and wireframe creation.
+ Wireframes were made for all predetermined size variations of the application.
+ Wireframes were made for the modals to streamline their design. This also allowed for the modals to be shown without over complicating the wireframe design.
+ [Click here to view all wireframes associated to this project.](static/readme/wireframe "Location of wireframes")

### Live App
+ A fully functioning application can be found on [Heroku](https://eldridge-music.herokuapp.com/ "Deplayment location").
![Index page of the Eldridge Music Book Emporium](static/readme/demo/demo-index-large.jpg "Index page of Eldridge Music Book Emporium")
+ GitHub's IDE GitPod was used for the construction process.
+ GitHub houses the [master branch](https://github.com/Richardaeld/Eldridge_Music).

## Scalability
+ Different instrument music books could be added To expand the shop further.
    + These new instrument books could be added to the apps navbar next to piano books or use the categories within piano books to be selectors.
+ The index page could feature a special that is a small contianer with a captioned image to help entice users to make a unexpected purchase.
+ Allow images to show a larger image (in a modal) if clicked.
+ Add a warning modal for superusers when they click the delete merchandise button

# Technology and Languages
+ HTML - Skeleton frame of the application.
+ CSS - Beautifies the skeleton (HTML).
+ JavaScript - Allows for user interaction and limited dynamic function on the application.
+ Python - Allows dynamic function and back end programs to run. These programs (frameworks, libraries, and databases) are:
    + Django - Allows use of templating, security, and other critical functions.
        + Allauth - An app that allows login, log out, password recovery and more.
        + Stripe - An app that allows users to securely use their credit cards.
        + Postgres - The type of SQL server used to store infofrmation.
        + Crispy Forms - Allows for forms to easily, quickly, and neatly be created and configured.
+ AWS - A Server used to store static and media files

# Testing
+ The **Testing** documentation can be found on [TESTING.md](TESTING.md).

# Bugs and Other Problems
## Current Bugs
+ Roman numerals in names for merchandise items display inaccurately.
    + Caused by:
        + The use of Django's tag title `{% | title %}`.
    + Thought(s):
        + If title is removed from the name templating and superusers entered everything in 100% accurate this could be avoided.
        + If a `text-transfrom: uppercase` css command is used it would solve this problem but create an overall poorer user experience.

## Other Problems
+ Bootstrap's toasts wouldn't show up on screen.
    + Caused by:
        + Some error with jQuery.
    + Fix:
        + Wrote custom JS script to reveal any toasts.
+ An active link header was originally used to display the name of the item a user was viewing however, some names proved to be to large.
    + Caused by:
        + Names longer than 15 characters.
    + Fix:
        + Removed the active link that showed users the name of the product they were on.
+ User search bar on the fixed header was evidently askew.
    + Caused by:
        + Responsive design header that used book strap fixed size cols and possibly a myriad of other problems.
    + Fix:
        + A combination of flex, guessed left/right margins, and Bootstrap.

# Deployment
## GitHub - GitPod
+ Go to the location of the original repository in GitHub, [https://github.com/Richardaeld/Eldridge_Music](https://github.com/Richardaeld/Eldridge_Music).
+ Click on the **Code** button to get the drop-down menu.
+ Copy the HTTPS address provided.
+ Create a new GitHub/GitPod project (to house the new clone) and then open this new project.
+ Go to the Bash and type, `git clone <HTTPS>`, paste the HTTPS address found in the GitHub page (don't forget the space after "clone") and press enter.
+ A clone will be created within a new folder called "Eldridge_Music" (name of the original repository).
+ Unpack everything from this new folder to the root of the GitPod project tree and the project will be setup within GitPod (minus the database which we will setup shortly).

### Requirements
### Stripe
+ Go to **Stripe.com** and click **Start now**.
+ Create a new account.
+ Click **Developer** tab
+ Click **API Keys** to find **Publishable Key** and **Secret Key**
+ Click **Webhooks** tab
+ click **Add endpoint** and enter the new apps heroku address with **/invoice/wh/** at the end of the address
+ Stripe will now provide you with a **Signing secret key**

### AWS
+ Go to **aws.amazon.com**
+ Create a new account
+ Log in and click, **My Account** and then **AWS Management Console**
+ Create S3 bucket:
    + Search for and select service **S3**
    + Click **Create bucket**
    + Name the new bucket and uncheck **Block all public access**
    + Click **Create Bucket**
+ Configure bucket:
    + Click on newly created bucket's name.
    + Click on **Properites** tab.
    + Click on **Static website hosting**.
    + Click on **Use this bucket to host a website** and fill out index/error document with default information and save.
    + Click on **Permissions** tab.
    + Click on **CORS configuration** and paste in code [CORES config](AWS.txt).
    + Click on **Bucket Policy** tab and then click **Policy Generator**.
    + For **Type of Policy** select **S3 Bucket Policy**.
    + For **Principal** enter `*`.
    + For **Actions** select **GetObject**.
    + Enter buckets**ARN** into this forms ARN input.
    + Click **Add statement** then **Generate Policy** and copy the policy generated.
    + Paste this copied policy into the **Bucket Policy**
    + add a `/*` onto the end of the value of the key **Resource**
        + Ex. `"Resource": "<bucket ARN>/*"`
    + Click save.
    + Click **Access Control List** tab.
    + Click on **Public access** and set **List objects** and save.

+ Create and configure IAM
    + Go to services menu and select **IAM**.
    + Under **Access Management** click **Groups** and the **create a new group**.
    + Enter a name, select **next step** twice, and then **Create group**.
    + Under **Access Management** click **Policies** and then **Create Policy**.
    + Click **JSON** tab and then click **import managed policy**.
    + Search for **s3**, select **AmazonS3FullAccess**, and click **Import**.
    + Replace the value of **Resource** with [IAM JSON Resource](AWS.txt)
    + Click **Review policy**.
    + Give the policy a name and description.
    + Click **Create policy**.
    + Under **Access Management** click **Groups**.
    + Click recently created group and **Attach Policy**.
    + Search for policy that was just created, select said policy and click **Attach Policy**.
    + Under **Access Management** click **Users** and then **Add User**.
    + Create a name for user (add suffix '-staticfiles-user'), give them **Programmatic access**, and click **Next**.
    + Put newly created user in **IAM Group** and keep clicking **next** until user has been created in **IAM Group**.
    + Download **.csv** and save this file. You will not be able to download it again



### Email
### Heroku
+ Log into Heroku.
+ Create a new app on Heroku by clicking **New** and following the directions.
+ Link Heroku and GitHub:
    + Log into Heroku.
    + From the **Personal apps** page, click on the new app that was just created in Heroku.
    + Click on **Deploy**.
    + Click on **GitHub** from **Deployment method** section.
    + Enter your GitHub information and the name of the cloned repository into the "Connect to GitHub" section.

+ Create a postgres SQL server.
    + From your new apps base page, click on **Resources**.
    + Click on **Find more add-ons**.
    + Select **Postgres**.
    + Finish setup.

<!-- new section just for heroku keys -->
+ Share `env.py` information with Heroku.
    + Click on **Settings**.
    + Click on **Reveal Config Vars** from **Config Vars** section.
    + Add all of the `env.py` key and value pairs without their quotations.
        + (key) == (value)
        + Development == 0
        + USE_AWS == True
        + DATABASE_UTL == (key provided from Postgres server)
        + SECRET_KEY == (any django secret key)
        + STRIPE_PUBLIC_KEY == (provided by **Stripe** as **Publishable key**)
        + STRIPE_SECRET_KEY == (provided by **Stripe** as **Secret Key**)
        + STRIPE_WH_SECRET == (provided by **Stripe** as **Webhook Signing Secret**)
        + AWS_ACCESS_KEY_ID == (provided by **AWS .csv** as **Access Key Id**)
        + AWS_SECRET_ACCESS_KEY == (provided by **AWS .csv** as **Secret Access Key**)
        + EMAIL_HOST_USER == (Gmail address return email will be sent from)
        + EMAIL_HOST_PASS == (provided by **email provider** as **Ass Password**)


+ Enable automatic deployment or manually deploy updates.
    + Automatic Deployment:
        + Click on **Deploy**.
        + Click on **Enable Automatic Deploys** in **automatic deploys** section.
        + Click on **Deploy Branch** in **manual deploy** section to start initial deployment.
    + Manual Deployment:
        + Click on **Deploy Branch** in **manual deploy** section any time there is content you want to update the active app with.

### Django.settings
+ In the Django.settings file:
    + Update **ALLOWED_HOSTS** to the web address of the deployed heroku app.
    + update **STORAGE_BUCKET_NAME** to the name of the bucket created in [AWS](#aws).
    + Update **AWS_S3_REGION_NAME** to the region the becket was created in [AWS](#aws).

### Return Emails with Gmail
+ Log into a Gmail account
+ Go to **settings** and click **Accounts and Import**
+ Under **Change account settings** click on **Other Google Account Settings**.
+ Click on the **security** tab, click on **2-Step Verification**, and then **Get Started**.
+ Verify your setting choice and turn on **2-Step Verification**.
+ Go back to **Other Google Account Settings** and click **Security**.
+ Click on **App passwords**.
+ Select **mail** for the app.
+ Select **Other** for the device and enter **Django**.
+ Gamil will provide you with a email, app password.


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
<!-- + [RandomKeygen](https://randomkeygen.com/)
    + Used to create random secret key for "env.py" -->
<!-- Need key for django  https://miniwebtool.com/django-secret-key-generator/ -->
<!-- Add aws -->
<!-- stripe -->
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
+ [Django](https://docs.djangoproject.com/en/3.2/)
    + A through guide to this massive and intricate frame work.


# Acknowledgements
+ Emily Eldridge for help with revising the grammar and flow of this README document.
+ Felipe Souza Alarcon for his suggestion of a recipe themed project, his help and guidance.