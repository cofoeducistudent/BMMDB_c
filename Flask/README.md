# Movie-Review-Database-MS3 #

## Real Movie Review Database ##

## [* Site Link on Heroku Deployment](https://real-movie-reviews-co-h.herokuapp.com)

## [* Git-Hub Documentation](https://github.com/cofoeducistudent/Movie-Review-Database-MS3)

![RMRDB](/support/project-cover-image.png)

With the many film review sites on the internet, I found it frustrating that the reviews frequently had an agenda. Indeed,I have found that I could not trust them. There are reasons for this. Primarily it’s that most reviews come from one source or publisher, and the others from the general public, who mainly are not professional film reviewers, rather individuals voicing an opinion. However, in both situations a bias agenda exits, nonetheless. I wanted to balance this out somewhat. Therefore, I decided to take the best from both sides of reviewer types and see what I could come up with.

I decided to make a film review website, that can be controlled to eliminate the bias as much as possible. Therefore, I set the following brief to attain a site suited to something I would like to see.

>## Project Brief ##

Create a movie review website that will help promote reviews for movies past and present in a professionally critiqued manner.
The site will differ from others by the fact of sourcing reviews from people who are serious film reviewers. We do not wish to have clickbait or slander in respect to our reviews of films, but calm considered critique. We also wish to distance ourselves from the two predominant types of reviewers.

* The first, a homogenous company having the hidden agenda of reviews favouring particular movie production companies via a nepotist back channel.
* The other reviewer class  we wish to distance ourselves from, is the many millennial ‘woke’ childish reviews that target films that do not conform to their partisan view of what a film should be, for slander.

We want a clean looking site, with calm considered reviews, that present reviews within the 'class' a film was intended for. For example,  comparing a low budget film with a tent pole monster $200 million dollar production is simply ridiculous.

* To help solve this issue, each reviewer will come from members of the public, however, they will not be allowed to post reviews without membership and agreeing to our terms and conditions.
* Secondly the reviewers will have segregated topic areas with regards to the film review, and a corresponding section for a citation supporting their review on that section. I feel this will be a good approach because it will cause the poster to validate any assertions made.

|No|Review element|Review Citation|
|--|--------------|---------------|
|.|Synopsis|-|
|.|Script-review|Citation|
|.|Acting-review|Citation|
|.|Technical-review|Citation|
|.|Sound-review|Citation|
|.|Summary|-|

* **Each review should be carried out in-line with a comparison to a film of similar genre and production budget.** Otherwise the reviews are unfair.
* Each review will be supported with one image of the film (usually the production released public poster).
* Particular review attributes must be present. These include Title, sub-title, genre, stars (0-5).
* Each reviewer will have the autonomy to administrate their reviews by update or delete. However, they cannot interfere with other reviewers reviews of course.
* The public will be able to search for a particular title, or browse through existing reviews
----
## Index ##

> [1.UX](#ux)

a. Strategy

b. Scope

c. Structure

d. Skeleton

e. Surface

> 2.FEATURES

a. Existing Features

b. Features Left to Implement

> 3.TECHNOLOGIES USED

> 4.TESTING

> 5.DEPLOYMENT

> 6.CREDITS

> 7.CONTENT

> 8.MEDIA

> 9.ACKNOWLEDGEMENTS

>10.USEAGE INSTRUCTIONS



> ## ---------//--------- ##

># [UX](name="#ux") #

>## [A. Strategy]( ) ##

The website is to be created and hosted on Heroku. **GitHub cannot be used as the site requires technologies that make it dynamic and GitHub does not allow non-static sites.**

I intend to use the following technologies:

* HTML, for the structure
* CSS, for styling
* Google Fonts
* Bootstrap, takes up the heavy lifting of form and formatting
* Mongo database (Atlas) – for a database storage solution
* Flask micro-framework - will be used as the template infrastructure. One that uses the Jinja engine
* Python3 – for program control logic
* Git & GitHub will be used for Version control
* Heroku platform – Will be used for hosting

To clarify the objective for the site, its worth reminding ourselves of the user requirements.

**External User Goal** (Mainly the general public)

* Users will be able to search and browse existing reviews
* Registered users – Will be able receive promotional material via email
* Authorized Users (posters) – Will be able to post movie reviews, having full (CRUD) functionality.

**Site Owner Goal**

* The site owner will be able to publish a “self-user-moderated site”, presenting reviews for movies past and present.
* The site owner will be able to convert registered users to “authorized reviewers”, allowing them to post movie reviews
* Site owners – Will be able post promo material to registered users and communicate.
* Site owners or designated site Admins will be able to delete entire database, promote users to 'posters'



>## [B. Scope]("#scope") ###

There are endless features possible for a site such as this, however we will limit our scope.

**In scope:**

* Database design & connectivity
* Website pages design
* **Although not requested in the MS3 task, a rudimentary authentication process has been implemented to reduce rouge postings and/or abuse of content.** It is not a fully realized login security system and does not employ session variables. Rather, it is a simple authentication against existing database credentials.

In addition there will be :

* Full CRUD ability for ‘authorized-users’ (Create, Read, Update, Delete)
* Partial CRUD for ‘non-authorized / un-registered users’ (Read).
* Affiliate Site link ability for authorized 'posters'

**Outside Scope:**

* **Mass deletion or reviews for admin purposes can be added**, and i have  included a field in the reviews data structure for that purpose(m-process). However as I do not think that is critical for this release it has been de-scoped.


**CRUD features for the un-initiated means:**

* Creation of a movie review (Create).
* Reading of an existing search (Read).
* Modification of an existing review (Update).
* Deletion of an existing review (Delete)

> ## User Stories ##

I have identified 4 main users or stakeholders for this site

1. **Site Owner**
2. **Site Admin**
3. **Registered Users** (Poster)
4. **Anon User**

|Story|User Type|Feature|Reason/Goal|
|-----|---------|-------|-----------|
|1|Site Owner|I want a movie review website|So that I can create a traffic hotspot, that can be used later for marketing purposes|
|2|Site OWner|I want users to be able to post reviews| To reduce the maintenaces and information population burden|
|3|Site Owner|I want some method of rudimentary authentication, incl contact information| So that site has some inherent basic moderation and also I can accquire contact details to reduce SPAM content and ultmately govern uses|
|4|Site Owner|I want a Registration Page|To allow the public to apply for membership|
|5|Site Owner|I want a contact feature| So that the posters and general public an communicate with us|
|6|Site Owner|I want a contribute feature| So that no members can suggest movies for review|
|7|Site Owner|I want a members page| So that member(authorized users) can post film/movie reviews giving them full (CRUD) ability for their posts|
|8|Site Owner|I want a method of affiliation sale-thru| So I can incentivize good reviewers, for more quality posts|  
|-||||
|9|Site Admin|I want a 'PANIC-RESET' ability for reviews on site| If there is corruption I can refresh the site within seconds, before full restore!. To be used mainly on drastic action, or primary install. The PR feature will populate the site with a few model  review examples|
|10|Site Admin|I want a user PROMOTE-TO-POSTER feature|So that I can at will grant a new user 'POSTER' ability on merit"
|11|Site Admin|I want a affiliate-link Activation feature| So that I can target and grant our top reviewers, pass-though-sale ability as a reward for continuous quality postings|
|-||||
|12|Anon User|I wish to see a browse/search feature|So I can read posted reviews about movies|
|-||||
|13|Registered User|I wish for a my movie reviews management page|So that I can (Post/Update/Delete) my reviews|
|14|Registered User| I wish for a browse/review feature|So I can search and view movie reviews on the site|

>## C.Structure ##

The site will be dynamic, involving a few technologies

* HTML
* CSS
* Flask
* Bootstrap
* Google Fonts
* Font-awesome 4.x
* Database (Mongo)

I will implement the site using the following folder/file structure.

![folder structure](support/folder-structure.png)

| Folder   |  Content  |
|----------|-----------|
| static   | This folder contains Images, CSS|
| templates| HTML files, temp files|
| flask | Contains the project files |
| support | files supporting this README.md document |
| vscode| workfolder|
| venv | Virtual environment|

The site will be dynamic. Only features within the defined scope will be implemented. There will be enough functionality to allow the site to be operative.

Incidentally, two pages are hidden from the user interface. To access them (with the right credentials on production), simply append them withit a forward slash.

Note: Ultimately in a fully costed production, these features will and should be implemented in a CMS page of some sort.

<site.domain.com>/.....page

* /resetdata
* /makeadmin

**Warning:These pages should be given security rights equivalent to site admins only!**

The first page **'/resetdata'** - wipes the database and places **5 films reviews** in the site database.
This feature is **destructive!!** and should only be used in a site install or a panic situation, for example if the site has been abused with illicit or pornographic content. As it will take time to restore a full database and also check content.

The second page **'/makeadmin'** - allows the site admin to turn a registered user into a admin-poster. This grants them the rights to Create/Read/Update/Delete reviews that they post( but no one elses). You can at will, once the reviewer/poster has created sufficient reviews conforming to the sites 'terms and condition', run the second page again, entering that users email. The system will allow them to post an AFFILIATE LINK , that can go to a site of their choosing. This is to incentivize reviewers to post many quality  reviews and
benefit by allowing that link to go to a site of their choosing. From here they can have a central affiliate links to many products to make monetary gains.

> ### DATABASE STRUCTURE ###

**MongoDB version Atlas is used.**
I chose to use the atlas version of mongo, because the database is provided as a service online in the cloud. This means
that the provider will maintain the database and fix any failing during run-time. So far as your code is fine , the system should function. Note the project is for the purpose of the course. If this site was to be deployed in a real scenario of course, a discussion would be had with the client as to the database version required, as they may already have a mondo database.

As MongoDB is a document based database, the content will be 'collections' with fields representing each element of data. The site is built on this database structure. The database and collections are represented below.

## **collection:users** ##

When users register on the site and complete the form, this data is created.
Each user is defaulted to 'user' privilege. They are **not allowed** to make any posts.
However the site owner has their emails and can communicate with the user. If they have asked to be a movie reviewer
we will consider it ,and if we agree, will flip their role to 'Admin',allowing them to post.

| database | collection| field | type |purpose|
|----------|-----------|-------|--------|------|
|rmrdb|users|_id|auto|index|
|rmrdb|users|my-info|string|user reason for membership request|
|rmrdb|users|username|string|username|
|rmrdb|users|f-name|string|first name|
|rmrdb|users|l-name|string|last-name|
|rmrdb|users|e-mail|string|users registered email|
|rmrdb|users|password|string|password|
|rmrdb|users|role|string|security privilege -user-Admin|
|rmrdb|users|a-state|string|Affiliation link on poster image active -no-yes|

## **collection:temp** ##

This collection is use dto find and hold the email of the registered poster. We will use this to search for posts, so a user can and only will see his/her post for update or delete actions. This is a safeguard!

| database | collection| field | type |purpose|
|----------|-----------|-------|--------|------|
|rmrdb|temp|_id|auto|index|
|rmrdb|temp|cr|string|user email to be used to track reviews|

## **collection:reviews** ##

This collection holds the reviews created by all the registered/Authorized posters

| database | collection| field | type |purpose|
|----------|-----------|-------|--------|------|
|rmrdb|reviews|_id|auto|index|
|rmrdb|reviews|m-title|string|movie title|
|rmrdb|reviews|m-sub-title|string|movie sub-title |
|rmrdb|reviews|m-genre|text|movie genre classification|
|rmrdb|reviews|m-image-link|string|image hosting address|
|rmrdb|reviews|m-synopsis|string|movie synopsis|
|rmrdb|reviews|m-reviewer-name|string|Name of the reviewer|
|rmrdb|reviews|m-reviewer-date|date|date review was created *|
|rmrdb|reviews|m-stars|string|star quality 0-5|
|rmrdb|reviews|m-sc-review|string|script-review|
|rmrdb|reviews|m-sc-example|string|script-citation|
|rmrdb|reviews|m-ac-review|string|Acting-review|
|rmrdb|reviews|m-ac-example|string|Acting-citation|
|rmrdb|reviews|m-te-review|string|Technical-review|
|rmrdb|reviews|m-te-example|string|Technical-citation|
|rmrdb|reviews|m-so-review|string|Sound-review|
|rmrdb|reviews|m-so-example|string|Sound-citation|
|rmrdb|reviews|m-summary|string|Overall-summary|
|rmrdb|reviews|m-affiliate-link|string|affiliate link only functions if activated for user|
|rmrdb|reviews|m-email|string|email of reviewer who created it|
|rmrdb|reviews|m-process|string|left for future feature of bulk delete etc |

* Note this date is never updated. To generate a new date a complete new review must be created *

## **collections:results** ##

When a search is carried out for a review, this collection holds the results of the search.

| database | collection| field | type |purpose|
|----------|-----------|-------|--------|------|
|rmrdb|results|_id|auto|index|
|rmrdb|results|m-title|string|movie title|
|rmrdb|results|m-sub-title|string|movie sub-title |
|rmrdb|results|m-genre|text|movie genre classification|
|rmrdb|results|m-image-link|string|image hosting address|
|rmrdb|results|m-synopsis|string|movie synopsis|
|rmrdb|results|m-reviewer-name|string|Name of the reviewer|
|rmrdb|results|m-reviewer-date|date|date review was created *|
|rmrdb|results|m-stars|string|star quality 0-5|
|rmrdb|results|m-sc-review|string|script-review|
|rmrdb|results|m-sc-example|string|script-citation|
|rmrdb|results|m-ac-review|string|Acting-review|
|rmrdb|results|m-ac-example|string|Acting-citation|
|rmrdb|results|m-te-review|string|Technical-review|
|rmrdb|results|m-te-example|string|Technical-citation|
|rmrdb|results|m-so-review|string|Sound-review|
|rmrdb|results|m-so-example|string|Sound-citation|
|rmrdb|results|m-summary|string|Overall-summary|
|rmrdb|results|m-affiliate-link|string|affiliate link only functions if activated for user|
|rmrdb|results|m-email|string|email of reviewer who created it|
|rmrdb|results|m-process|string|left for future feature of bulk delete etc |

## **collection:mod** ##

This collection holds the resultant reviews that are about to be updated, as a result of the 'CRUD' update feature. These reviews have the common aspect that they are made by a single reviewer

| database | collection| field | type |purpose|
|----------|-----------|-------|--------|------|
|rmrdb|mod|_id|auto|index|
|rmrdb|mod|m-title|string|movie title|
|rmrdb|mod|m-sub-title|string|movie sub-title |
|rmrdb|mod|m-genre|text|movie genre classification|
|rmrdb|mod|m-image-link|string|image hosting address|
|rmrdb|mod|m-synopsis|string|movie synopsis|
|rmrdb|mod|m-reviewer-name|string|Name of the reviewer|
|rmrdb|mod|m-reviewer-date|date|date review was created *|
|rmrdb|mod|m-stars|string|star quality 0-5|
|rmrdb|mod|m-sc-review|string|script-review|
|rmrdb|mod|m-sc-example|string|script-citation|
|rmrdb|mod|m-ac-review|string|Acting-review|
|rmrdb|mod|m-ac-example|string|Acting-citation|
|rmrdb|mod|m-te-review|string|Technical-review|
|rmrdb|mod|m-te-example|string|Technical-citation|
|rmrdb|mod|m-so-review|string|Sound-review|
|rmrdb|mod|m-so-example|string|Sound-citation|
|rmrdb|mod|m-summary|string|Overall-summary|
|rmrdb|mod|m-affiliate-link|string|affiliate link only functions if activated for user|
|rmrdb|mod|m-email|string|email of reviewer who created it|
|rmrdb|mod|m-process|string|left for future feature of bulk delete etc |


>## SKELETON ##

For design of the site I used Balsamiq 3.x prototype software  to create the mockups
Below are the intended pages

|page|mockup|Created|
|----|------|-------|
|Home page|<img src="support/home-page-mockup.png" width="200">|Yes|
|Menus|<img src="support/menu-bar-mockup.png" width="200">|Yes|
|About|<img src="support/about-us-mockup.png" width="200">|Yes|
|Contribute|<img src="support/contribute-mockup.png" width="200">|Yes|
|Contact|<img src="support/contact-mockup.png" width="200">|Yes|
|Register|<img src="support/register-mockup.png" width="200">|Yes|
|Member Page|<img src="support/member-page-mockup.png" width="200">|Yes|
|Member-Submission-page|<img src="support/member-submission-mockup.png" width="200">|Yes|
|Search page|<img src="support/search-mockup.png" width="200">|Yes|
|Make-Admin Page|<img src="support/make-admin-mockup.png" width="200">|Yes|

>## Surface ##

The design of the site is based on sparse spacing and not clustered. In addition I chose light colours to make it clean looking.

I used the 'Justpick color tool to grab and alter colors"

I used Colormind website to give me colour ideas

|No|Color Pallet variation|
|--|------------|
|1|<img src="support/colormind1.png" width="200">|
|2|<img src="support/colormind2.png" width="200">|
|3|<img src="support/colormind3.png" width="200">|

I did not stick strictly to these options of course,but varied slightly, as I felt a creative flair
The colour was gained by analysis of the curtain image

**Google Fonts CDN**  was used to pull in the font style
**font-family: 'Montserrat', sans-serif;**

**Styling was carried out with CSS** as usual. I decided to add curves to the back panel and the images resulting from the searches.

>## Features ##

Apart from the general page features stipulated in the previous section, lets look at the search page to view the search feature elements.

|Feature|What is it?|state:
|-------|-----------|-----|
|About| Brief highlight of the sites objectives|Yes|
|Contact|Allows public/member to contact site owner|Yes|
|Search|Search the database for reviews|Yes|
|Register|People can request membership|Yes|
|Create Review|Authorized users can post a review|Yes|
|Update Review|Authorized users can update/modify their post|Yes|
|Delete Review|Authorized users can delete their post|Yes|
|Reset Data|Site-Admin can wipe datbase in a **'fire-fight'** situation|Yes|
|Make User an Admin|Site Admin can convert standard users to 'posters'|Yes|
|Enable Affiliate|Site-Admin can enable pass through link for poster for monetary benefit |Yes|
|Social Media|links to social media sites for the owner|Yes|
|Mass Review Deletion/Modification|Allows users to alter review posts en-masse|No|

***Desperate compromised site.**
This allows the site to come back quick. Users can still joined and post. The restore process will merge over existing data (via a yet as unwritten CMS backend tool)

## Search Page ##

**You can search for a movie by any of the criteria below. However the limitation of the free mongo tier seems to only allow partial search on one field.**

*I have opted to place that ability on the (Title) field*

* Title
* Sub-Title
* Reviewer Name
* Genre
* Stars

># TECHNOLOGIES/TOOLS USED #

* **HTML5-**
Html5 will be used for structure
* **CSS3-**
CSS3 will be used for styling
* **Bootstrap 3.x-**
I will use bootstrap for the heavy lifting of alignment for the website components. However, I will be using version 3.x, rather than the current v4. This is to do with flask, which is currently one version behind the current mainstream release.
* **Flask-** mini-framework for templating and page consistency
* **Icons-**
The obligatory font-awesome repository will be utilized for my site icons, for the social media icons etc. Again, I will use the previous release 4.x rather than the current 5.x, as this seems to play nicer with flask.
* **Database-**
As stated, we will employ a database for storage, allowing for rudimentary search and retrieve functionality. I will  use a 'document model', ‘NO-SQL’ database.... **(MongoDB)**. Specifically, I will use the online, cloud-based version, **'Atlas'**.
* **Templates-**
Flask using the Jinja2 engine will be my choice of framework, to speed up design and keep some level of uniformity across the site page content.
* **Python3-**
Although minor elements of jQuery and JavaScript may be be utilized within support modules bootstrap and other elements
Python version 3.x shall be used as the underpinning project logic control within the flask views.
* **E-mail-**
Omitted from the site will be the background extended infrastructure that models the business behavior. I refer to things such as system admin monitoring and email response eco-system. From the front-end perspective, there will be email options, however the forms will remain un-hooked.
* **Testing-**
I will use chrome tools for testing, as that’s proves satisfactory. I will test on the main browsers including, Chrome, Firefox, Opera, Navigator etc. in addition I will use the CSS cross platform tool.
* **Git-** Used for version control
* **Git-Hub-** Repository to store build
* **Heroku-** Used for hosting the site
* **Monosnap-** Used to capture screen Shots
* **Terminal v2.10** used to execute and connect to remote systems
* **Google Fonts** 


># TESTING #

The site features were tested and the results tabled below

| Feature   |  Action  | Screen | Result | Success
|-----------|----------|--------|--------|--------|
| **Launch** site| Browse to Heroku Site|(<https://real-movie-reviews-co-h.herokuapp.com)>|<img src="support/home_page.png" width="200">|Yes|
| **About** the site| click on 'About' |<img src="support/menu.png" width="200">|<img src="support/about-us.png" width="200">|Yes|
| **Contact** us| click on 'Contact' |<img src="support/menu.png" width="200">|<img src="support/contact-us.png" width="200">|Yes|
| **Contribute** a review idea| click on 'Contribute' |<img src="support/menu.png" width="200">|<img src="support/contribute.png" width="200">|Yes|
| **Register** to become a member| click on 'Register' |<img src="support/menu.png" width="200">|<img src="support/register.png" width="200">|Yes|
| **Search** for a movie review| click on 'Search' |<img src="support/menu.png" width="200">|<img src="support/search.png" width="200">|Yes|
| **Member** Submit/update/delete  movie reviews as a member| click on 'Member' |<img src="support/menu.png" width="200">|<img src="support/submission.png" width="200">|Yes|
| Make User into a Poster / Activate Affiliate Link... /makeadmin| click on 'Member' | domain site/makeadmin |<img src="support/make-admin.png" width="200">|Yes|

># DEPLOYMENT #

> **GitHub-Pages**
**N/A - site will not function on the github platform as the site is dynamic in nature.
You can however review the readme (This page).**

> ## **LOCAL:** ##

* **Prereq: Download Git and install on your local computer if you have not already done so.**

* Browse to a location of your choice, on  your local computer, which you have admin access.

1. Goto my github page and press the clone button.

2. Copy the deployment link

<img src="support/github-clonebutton.png" width="200">

3. Open a terminal window. 
* If you are on Mac, you can find it in your applications start-up. 
* If on windows, get to the CMD window (command prompt)

4. Type the following command "git clone **[paste the link]** ; where the link should be on your clipboard from clicking and copying the link in git-hub button in the image

**SETUP ENVIRONMENT VARIABLES:**

* Browse into the Flask directory
* In the directory with the **run.py** command type
You would set in the MONGO_URI environment variable on the local machine, as the python3 code will look for it on execution. It needs this to connect to the database.

**I will not detail the details here as its forbidden and a security breach. However in a real situation this info will be given to the sysadmin.**

The site is already up and running however on Heroku, thereore visit the site. the link is at the top of this page.

[Site Link on Heroku Deployment](https://real-movie-reviews-co-h.herokuapp.com)


> **HEROKU:**

**Connect to Heroku as the site is already up and running.**
*The environment variable is already configured in the Heroku app system setting.*



># CREDITS #

* Code assistance ... Pymongo search - Stack Overflow *
* sr9yar - Stack Overflow *
* user3375448 - Stack Overflow *

># CONTENT #

The coding was entirely mine. No code snippet was used, apart from standard a templates in Bootstrap 3.x 

># MEDIA #

Pictures were taken from pixabay & pexels site.
All images are royalty free and allowed for use. Below are credits for the creators

* Photo by Clem Onojenghuo from pexels *
* Photo free - pixabay *
* Image by Peggy und Marco Lachmann-Anke from Pixabay *
* Photo Raphaelsilva Pixabay License *
* Photo Gordon Johnson Pixabay License *
* Photo Luis Quintero Pexels *

* **Note: movie cover images - remain copyright of that of their respective companies.**

># ACKNOWLEDGEMENTS #

Thanks to Mentor *** for review of site.

># USEAGE INSTRUCTIONS #

The use of the site operationally is pretty simple.

1. Simply browse the site and reviews. If you are unsure of a movie name, then simply click the **blue < Search/browse>** button

2. Register on the site.
If you wish to become a reviewer. If you do not but want registration simply to recieve our promotional material, then indicate this in the box 'why you wish to become a member'

3. ** For the examiner on the address bar append with **'/makeadmin'**
On the resulting page. enter the email address you signed up with, and 'submit'
**Note: This action would normally be carried out by the site administrator.**

4. If you wish to activate affiliate pass thru, you need to exit the screen  once the user is made 'admin-poster', then return
This is because you are not allowed affiliate pass-through benefits, unless you are already an 'admin-poster'. Also
both actions would never happen at once. You need to become a successful poster before you are given affiliate access

## **Posting A Review**

1. As an **'Admin-Poster'**, browse to **'Members Page'**

2. Enter: username/email address/password...

3. scroll down the page , completing the section

4. Press blue <submit> button  to submit your review 

## **Delete A Review** ##

1. As an **'Admin-Poster'**, browse to **'Members Page'**

2. Enter: username/email address/password...

3. Use the drop down and select **'Delete"**

4. Click on red **'<Change/Update Reviews>'**,.. You will be taken to another page, displaying an index of all your reviews

5. Select a review and click on the red  **'<delete selected>'** button

## **Update A Review** ##

1. As an **'Admin-Poster'**, browse to **'Members Page'**

2. Enter: username/email address/password...

3. Use the drop down and select **'Update"**

4. Click on red **'<Change/Update Reviews>'**,.. You will be taken to another page, displaying an index of all your reviews

5. Select the review you wish to update

6. click on the orange **'<Update Selected>'** button. You will be taken to a page where you can update that review



Fin