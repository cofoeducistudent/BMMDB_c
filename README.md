# Real Movie-Review-Database (MS3) #

>## **Blockbusters, McGuffins & Moes** ##

**WARNING: THIS SITE REQUIRES USER ACCOUNTS WITH THE CORRECT CREDENTIALS, BEFORE POSTING REVIEWS ARE POSSIBLE. THEREFORE PLEASE READ THE USAGE INSTRUCTIONS AT THE BOTTOM...BEFORE USE!**

I have provided a sample 'poster-user' having CRUD capability & affiliate authority  for use:

* Username:fc
* First name: Full
* Last Name :Crud
* Email address:f.crud@gmail.com
* password:1

> Note:!! You may experience a delay when you launch the site. This is not a site coding issue per-sae, rather Heroku and is a universal experience.  Heroku seems to store, then spin up your site after some time of non-use. Also it may need to reload your app if cleared in the cloud CDN.

[BMMDB Live Site](https://bmmdb.herokuapp.com)

[BMMDB - Github - Site](https://github.com/cofoeducistudent/BMMDB_c)

![Blockbusters - Mcguffins & Moes](/support/‎1-home-page.png)

## Index ##

[Overview](#overview)

[Project Brief](#projectbrief)

>[1 UX](#ux)

[a. Strategy](#strategy)

* [External Goals](#externalusergoals)
* [Internal Goals](#siteownergoals)

[b. Scope](#scope)

* [In Scope](#inscope)

* [Outside scope](#outsidescope)

* [CRUD features](#crudfeatures)

* [User Stories](#userstories)

[c. Structure](#structure)

* [Folder/Directory Structures](#folderstructures)

* [Database Structure](#databasestructure)

[d. Skeleton](#skeleton)

[e. Surface](#surface)

* [Color scheme](#colorscheme)

* [Font Family](#fontfamily)

>[2.FEATURES](#features)

>[3.TECHNOLOGIES USED](#technologiesused)

>[4.TESTING](#testing])

>[5.DEPLOYMENT](#deployment)

* [MongoDb Atlas](#mongoatlasconfiguration)

* [Local Deployment](#localdeployment)

* [Setup Environment Variables](#setupenvironmentvariables)

* [Heroku Deployment](#herokudeployment)

* [Heroku Environment Configuration](#herokuenvironmentconfiguration)

>[6.CREDITS](#credits)

>[7.CONTENT](#content)

>[8.MEDIA](#media)

>[9.ACKNOWLEDGEMENTS](#acknowledgements)

>[10.USEAGE INSTRUCTIONS](#useageinstructions)

* [For Examiner](#forexaminer)

* [Post a Review](#postareview)

* [Delete a Review](#deleteareview)

* [Update a Review](#updateareview)

* [Important - post install action](#important)

>
<a id="overview"></a>

> ## Overview ##

> With the many film review sites on the internet, I found it frustrating that the reviews frequently had an agenda. Indeed, I have found that I could not trust them. There are reasons for this. Primarily it’s that most reviews come from one source or publisher, and the others from the general public, who mainly are not professional film reviewers, rather individuals voicing an opinion. However, in both situations a bias agenda exits, nonetheless. I wanted to balance this out somewhat. Therefore, I decided to take the best from both sides of the reviewer types and see what I could come up with. I decided to make a film review website, that can be controlled to eliminate the bias as much as possible. Therefore, I set the following brief to attain a site suited to something I would like to see.

<a id="projectbrief"></a>

> ## Project Brief ##

* My scenario was to create a **MOVIE REVIEW WEBSITE** to promote movies past and present, in a professionally critiqued manner. The sites 'usp' will be the sourcing of reviews from curated public film reviewers. I don't wish to have clickbait/slanderous soundbite reviews, concerning our reviews, but calmly considered critique. In effect, I wish to distance the site from the predominant types of reviewers on the web. The first, a homogenous company having the hidden agenda of reviews favouring particular movie production companies via a nepotist backchannel. The other is the many millennial ‘woke’ childish reviews targeting films that do not conform to their partisan view of what a film should be, simply for slander for gaining self-promotion.

* I want a clean looking site, with calmly considered reviews, that present reviews within the 'class' a film was intended for. The site will aim to have more serious content and attract true film officiators. Comparing a low budget film with a tent pole $200 million movie production is simply ridiculous.

* To help solve the above issues, each reviewer is being sourced from the public, however, they will not be allowed to post reviews without membership and agreeing to our terms and conditions. Or they will be struck off, with all their reviews removed.

* Secondly, the reviewers will cover specific topic areas, thus keeping a strict format. Each section will have a corresponding one,  for a citation supporting the review

* This will cause the poster to think and validate any assertions made. Rather than writing flippant soundbites!

|No|Review Area|Supporting Citation|
|--|--------------|---------------|
|1|Synopsis|N/A|
|2|Script-review|Citation|
|3|Acting-review|Citation|
|4|Technical-review|Citation|
|5|Sound-review|Citation|
|6|Summary|N/A|

A guiding principle will be that each review should be carried out in comparison to a film of similar genre and production budget, else the reviews will be unfair.

Each review will be supported with:

* A single image of the film (usually the production released public poster).

* review attributes. These include:

* Title, sub-title, genre, stars (0-5).

* Each reviewer will have the autonomy to administrate their reviews by an update or delete. However, they cannot interfere with other reviewers reviews of course.

* The public will be able to search for a particular title, or browse through existing reviews

<a id="ux"></a>

## UX ##

<a id="strategy"></a>

## STRATEGY ##

The website is to be created and hosted on Heroku. **GitHub cannot be used in this instance as the site requires technologies that make it dynamic. GitHub does not allow non-static sites.**

I intend to use the following technologies:

* HTML, for the structure
* CSS, for styling
* Google Fonts
* Fontawesome - for icons
* Bootstrap, takes up the heavy lifting of form and formatting
* Mongo database (Atlas) – for a database storage solution
* Flask micro-framework - will be used as the template infrastructure. One that uses the Jinja engine
* Python3 – for program control logic
* Git & GitHub will be used for Version control
* Heroku platform – Will be used for hosting

To clarify the objective for the site, it's worth reminding ourselves of the user requirements.

<a id="externalusergoals"></a>

> **External User Goal** (Mainly the general public)

* Users will be able to search and browse existing reviews
* Registered users – Will be able to receive promotional material via email
* Authorized Users (posters) – Will be able to post movie reviews, having full (CRUD) functionality.
* Authorized valued users will in addition to posting privileges, have the ability to create an affiliate link to an ec-commerce site of their choosing within the sites terms & rules

<a id="siteownergoals"></a>

> **Site Owner Goal**

* The site owner will be able to publish a “self-user-moderated site”, presenting reviews for movies past and present.
* The site owner will be able to convert registered users to “authorized reviewers”, allowing them to post movie reviews
* Site owners – Will be able to post promo material to registered users and communicate.
* Site owners or designated site Admins will be able to delete the entire database, promote users to 'posters'

<a id="scope"></a>

## SCOPE ##

Endless features are possible for a site such as this, however, we will limit our scope.

<a id="inscope"></a>

**In scope:**

* Database design & connectivity
* Website pages design
* **Although not requested in the MS3 task, a rudimentary authentication process has been implemented to reduce rouge postings and/or abuse of content.** It is not a fully realized login security system and does not employ sessions. Rather, it is a simple authentication against existing database credentials.

In addition there will be :

* Full CRUD ability for ‘authorized-users’..... (Create, Read, Update, Delete)
* Partial CRUD for ‘non-authorized / un-registered users’.....(Read).
* Affiliate site link ability for authorized 'posters' ( Allows them to link to a e-commerce site)

<a id="outsidescope"></a>

**Outside Scope:**

* **Mass deletion or reviews for admin purposes can be added**, and I have included a field in the reviews data structure for that purpose(m-process). However, as I do not think that is critical for this release it has been de-scoped.

<a id="crudfeatures"></a>

**CRUD features for clarity mean:**

* Creation of a movie review (Create).
* Reading of an existing search (Read).
* Modification of an existing review (Update).
* Deletion of an existing review (Delete)

<a id="userstories"></a>

> ## User Stories ##

I have identified 4 main users or stakeholders for this site

1. **Site Owner**
2. **Site Admin**
3. **Registered Users** (Poster)
4. **Anon User**

|Story|User Type|Feature|Reason/Goal|
|-----|---------|-------|-----------|
|1|Site Owner|I want a movie review website|So that I can create a traffic hotspot, that can be used later for marketing purposes|
|2|Site OWner|I want users to be able to post reviews| To reduce the maintenance and information population burden|
|3|Site Owner|I want some method of rudimentary authentication, incl contact information| So that site has some inherent basic moderation and also I can acquire contact details to reduce SPAM content and ultimately govern uses|
|4|Site Owner|I want a Registration Page|To allow the public to apply for membership|
|5|Site Owner|I want a contact feature| So that the posters and general public an communicate with us|
|6|Site Owner|I want a contribute feature| So that no members can suggest movies for review|
|7|Site Owner|I want a members page| So that member(authorized users) can amend/delete their reviews giving them fully (CRUD) ability for their posts|
|8|Site Owner|I want a method of affiliation sale-thru| So I can incentivize good reviewers, for more quality posts|  
|-||||
|9|Site Admin|I want a 'Database Initialize' ability | I can restore (after initialization & test of new site install ) The site can be cleared within seconds.
|10|Site Admin|I want a user 'PROMOTE-USER' feature|So that I can at will grant a new (Registered) member 'POST' ability on merit"
|11|Site Admin|I want an affiliate-link Activation feature| So that I can target and grant our top reviewers, pass-though-sale ability as a reward for continuous quality postings|
|-||||
|12|Anon User|I wish to see a browse/search feature|So I can read posted reviews about movies|
|-||||
|13|Registered User|I wish for my movie reviews management page|So that I can (Post/Update/Delete) my reviews|

<a id="structure"></a>

>## Structure ##

The site will be dynamic, involving a few technologies

* HTML
* CSS
* Flask
* Bootstrap
* Google Fonts
* Font-awesome
* Database (Mongo)

I will implement the site using the following folder/file structure.

<a id="folderstructures"></a>

>##Folder/Directory Structures

![folder structure](/support/2-folder-structure1.png)

| Folder   |  Content  |
|----------|-----------|
| static   | This folder contains Images, CSS|
| templates| HTML files, temp files|
| flask | Contains the project files |
| support | files supporting this README.md document |
| vscode| workfolder|
| venv | Virtual environment|

![Folder](/support/3-folder-structure2.png)

![Folder](/support/4-folder-structure3.png)

![Folder](/support/5-folder-structure4.png)

The site is classed as dynamic, moving data back and forth from a separate database. Only features within the defined scope will be implemented. There will be enough functionality to allow the site to be visibly operative. However, the greater infrastructure support such as email - communications to the members and mailshot facility will not be operational.

Note:
Two features are placed within the repo by default. These need to be removed when the site is put in a production scenario.

* **defaultdb-py**

* **promoteuser.html**... link, Currently only found on the homepage, lower left of screen

Ultimately in a fully costed production, these features will and should be implemented in a CMS page of some sort, accessed by users with the appropriate rights.

>**Warning:The following features should be removed or accessed with security rights equivalent to 'site admins only!'**

* The first feature **'defaultdb-py'** - wipes the database and places **5 films reviews** in the site database. This feature is and should only be used in an initial site install.

* The second feature **'promoteuser'** - allows the site admin to turn a registered user into a **'poster'**. This grants the user rights to Create/Read/Update/Delete reviews that they post( but no one else).

* once the reviewer/poster has created sufficient reviews conforming to the sites 'terms and condition', re-run the second page again, entering that users email.

* The system will allow them to post an AFFILIATE LINK, that can go to a site of their choosing. This is to incentivize reviewers to post many quality reviews and benefit by allowing that link to go to a site of their choosing. From here they can have a central affiliate link to many products to make monetary gains.

<a id="databasestructure"></a>

> ### DATABASE STRUCTURE ###

**MongoDB version Atlas is used.**
I chose to use the atlas version of mongo because the database is provided as a service online in the cloud. This means
that the provider will maintain the database and fix any failings during run-time. So far as your code is fine, the system should function. Note the project is for the purpose of the course. If this site was to be deployed in a real scenario, of course, a discussion would be had with the client as to the database version required, as they may already have a mondo database.

As MongoDB is a document-based database, the content will be 'collections' with fields representing each element of data. The site is built on this database structure. The database and collections are represented below.

## **collection:users** ##

When users register on the site and complete the form, this data is created.
Each user defaults to 'user' privilege. They are **not allowed** to make any posts.
However, the site owner has their emails and can communicate with the user. If they have asked to be a movie reviewer
we will consider it, and if we agree, will flip their role to 'Admin', allowing them to post.

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

This collection is used to find and hold the email of the registered poster. We will use this to search for posts, so a user can and only will see his/her post for the update or delete actions. This is a safeguard!

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
|rmrdb|reviews|(**m-sub-title**)|string|movie sub-title **|
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

* *  Note this date is never updated. To generate a new date a completely new review must be created *
* ** This data field was later converted to **release date**, without index text search  attached. I felt it was more beneficial. I left it here as-is, rather than change it, to show the changes I made in my strategy.

<a id="skeleton"></a>

>## SKELETON ##

For design of the site I used Balsamiq 3.x prototype software  to create the mockups
Below are the intended pages

|page|mockup|Created|
|----|------|-------|
|Home page|<img src="support/mock-1.png" width="200">|Yes|
|Menus|<img src="support/mock-2.png" width="200">|Yes|
|About|<img src="support/mock-3.png" width="200">|Yes|
|Contribute|<img src="support/mock-5.png" width="200">|Yes|
|Contact|<img src="support/mock-6.png" width="200">|Yes|
|Register|<img src="support/mock-7.png" width="200">|Yes|
|Member Page|<img src="support/mock-8.png" width="200">|Yes|
|Member-Submission-page|<img src="support/mock-9.png" width="200">|Yes|
|Search page|<img src="support/mock-4.png" width="200">|Yes|
|Make-Admin Page|<img src="support/mock-10.png" width="200">|Yes|

<a id="surface"></a>

>## Surface ##

The design of the site is sparse and not clustered. This was intentional as my site is trying to attract serious film reviewers and fans. No javascript pop-ups in the site. I wish more written content than images, as this is the only way I can consider a film justifiably reviewed. With the same mind, I chose light colours to make it look clean.

<a id="colorscheme"></a>

> ## Colour Scheme ##

I used the **'Just pick'** colour tool to grab and alter colours

Additionally, I used **'Colormind website'** to give me colour ideas

|No|Color Pallet variation|
|--|------------|
|1|<img src="support/colormind1.png" width="200">|
|2|<img src="support/colormind2.png" width="200">|
|3|<img src="support/colormind3.png" width="200">|

I did not stick strictly to these options of course, but varied slightly and felt a necessity for some creative flair.

The colour was gained by analysis of the curtain image

<a id="fontfamily"></a>

> ## Font Family ##

**Google Fonts CDN**  was used to pull in the font style
**font-family: 'Montserrat', sans-serif;**
**Styling was carried out with CSS** as usual. I decided to add curves to the back panel and the images resulting from the searches.

<a id="features"></a>

>## Features ##

Apart from the general page features stipulated in the previous section, let's look at the search page to view the search feature elements.

Feature|What is it?|Employed?|
|-------|-----------|-----|
|About| Brief highlight of the sites objectives|Yes|
|Contact|Allows public/member to contact site owner|Yes|
|Search|Search the database for reviews|Yes|
|Register|People can request membership|Yes|
|Create Review|Authorized users can post a review|Yes|
|Update Review|Authorized users can update/modify their post|Yes|
|Delete Review|Authorized users can delete their post|Yes|
|defaultdb-py|Site-Admin can wipe datbase after install & initial tests, restoring to a default selection of films|Yes|
|Promote User|Site Admin can convert 'standard users' to a 'posters' In addition allow pass through link to e-commerce site for reviewer|Yes|
|Social Media|links to social media sites for the owner|Yes|
|Mass Review Deletion/Modification|Allows users to alter review posts en-masse|No|

## Search page content ##

<a id="searchpage"></a>

* **Title**
* **Sub-Title**
* **Reviewer Name**
* **Genre**
* **Stars**
* **Synopsis**

>** Note: The way MongoSearch works is that its search for a term across all field's with an index applied. Therefore it is possible to enter a search term in one field and have the result found in another field. The solution can be to just have one 'general search' field available, however, I have opted to have each defined for clarity and speed response.

* Note:**I added a **'search quantity'** button feature, during coding as I found that that would be useful if the database grows.**

<a id="technologiesused"></a>

>## TECHNOLOGIES/TOOLS USED ##

* **HTML5-**
Html5  is used for structure
* **CSS3-**
CSS3 is used for styling
* **Bootstrap 3.x-**
I used bootstrap for the heavy lifting of alignment for the website components. However, I used version 3.x, rather than the current v4. This is to do with flask, which is currently one version behind the current mainstream release. It is not advised to mesh v5 with it as it's untested at the time of build.
* **Flask-** mini-framework for templating and page consistency
* **Icons-**
The obligatory font-awesome repository will be utilized for my site icons, for the social media icons etc. Again, I will use the previous release 4.x rather than the current 5.x, as this seems to play nicer with flask version.
* **Database-**
As stated, I employed a database for storage, allowing for rudimentary search and retrieval functionality. I will use a 'document model', ‘NO-SQL’ database.... **(MongoDB)**. Specifically, I will use the online, cloud-based version, **'Atlas'**.
* **Templates-**
Flask using the Jinja2 engine will be my choice of framework, to speed up design and keep some level of uniformity across the site page content.
* **Python3-**
Although minor elements of jQuery and JavaScript maybe be utilized within support modules bootstrap and other elements
Python version 3.x shall be used as the underpinning project logic control within the flask views.
* **E-mail-**
Omitted from the site will be the background extended infrastructure that models the business behavior. I refer to things such as system admin monitoring and email response eco-system. From the front-end perspective, there will be email options, however, the forms will remain un-hooked.
* **Testing-**
I used chrome tools for testing, as that has proved satisfactory historically for me. I will test on the main browsers including, Chrome, Firefox, Opera, Navigator etc. also I will use the CSS cross-platform tool.
* **Git-** I used for version control
* **Git-Hub-** I used GitHub Repository to store the build
* **Heroku-** I used for hosting the site
* **Monosnap-** I used to capture screenshots
* **Terminal v2.10** I used Apples Terminal client to execute and connect to remote systems
* **Google Fonts** I used google fonts for the page font work

<a id="testing"></a>

>## TESTING ##

The site features were tested and the results tabled below

| Feature   |  Action  | Screen | Result | Success|
|-----------|----------|--------|--------|--------|
| **Launch site**| Browse to Heroku Site|<img src="support/sc_menu.PNG" width="200">|<img src="support/sc_homepage.PNG" width="200">|Yes|
| **About the site**| Click on 'About' |<img src="support/sc_menu.PNG" width="200">|<img src="support/sc_about.PNG" width="200">|Yes|
| **Contact us**| Click on 'Contact' |<img src="support/sc_menu.PNG" width="200">|<img src="support/sc_contact.PNG" width="200">|Yes|
| **Contribute a review idea**| Click on 'Contribute' |<img src="support/sc_menu.PNG" width="200">|<img src="support/sc_contribute.PNG" width="200">|Yes|
| **Register to become a member**| Click on 'Register' |<img src="support/sc_menu.PNG" width="200">|<img src="support/sc_register.PNG" width="200">|Yes|
| **Search for a movie review**| Click on 'Search' |<img src="support/sc_menu.PNG" width="200">|<img src="support/sc_search.PNG" width="200">|Yes|
| **Member Submit/update/delete  movie reviews as a member**| Click on 'Member' |<img src="support/sc_menu.PNG" width="200">|<img src="support/sc_maintenance.PNG" width="200">|Yes|
| **Make a user into a 'Poster' / Activate Affiliate Link...**| Click on 'delete this link' @ bottom left of screen' |<img src="support/sc_homepage.PNG" width="200"> |<img src="support/sc_grantprivilage.PNG" width="200">|Yes|

>**Tested Browsers**

|Browser|Result|
|-------|------|
|Firefox|Ok|
|Safari|Ok|
|Opera|Ok|
|IExplorer|OK|

>## DEPLOYMENT ##

<a id="mongoatlasconfiguration"></a>

>## **MONGO ATLAS DATABASE CONFIGURATION:** ##

**I have already carried out the Mongo Atlas Database setup as part of the task of this project.** However, if you wish to create/use your own Mongo DB Atlas instance, you need to set up and configure it

1 . Sign up to mongo atlas if you have not. The [Mongo Site](https://www.mongodb.com/cloud/atlas/register)

* Keep your Atlas Login, **This is the master account password and not the one for the database connectivity**.

2 . Follow instructions and carry out the basic set up account credentials (note the username & password)

* **Create a Cluster**

* **Create a 'database' in that cluster 'xxxx'**

* **Create 3 'collections' (reviews, temp, users ) in that cluster**

* **In Security - Database Access .. Add New Database User ( Keep these credentials as they will be used to connect to the database)**
* **In Security - Network Access ... Add IP address 0.0.0.0/0.. This ensures anyone can connect to the database because you cannot predict where the users of your website will be.**

**N/A - The site will not function on a published Github platform as the site is dynamic. You can, however, review the readme (This page).**

<a id="localdeployment"></a>

> ## **LOCAL DEPLOYMENT:** ##

* Prereq: [**Download Git**](https://git-scm.com/) and install on your local computer if you have not already done so.

* Browse to a **location of your choice, on your local computer**, which you have admin access.

1. Goto [BMMDB_c GithubRepo](https://github.com/cofoeducistudent/BMMDB_c) and press the clone button.

2. Copy the deployment link by clicking on the 'grab Url' icon

<img src="support/sshot-clone-link.png" width="200">

3. Open a terminal window.

* If you are on Mac, you can find it in your applications start-up.

* If on windows, get to the CMD window (command prompt)

4. Type the following command "git clone **[paste the link]**; where the link should be on your clipboard from clicking and copying the link in git-hub button in the image

<a id="setupenvironmentvariables"></a>

**SETUP ENVIRONMENT VARIABLES:**

during development on the local machine and operations, an environment variable is required to allow the database to connect
when python3 is run and attempts to connect to the mongo database ( in our case its mongo Atlas). Therefore on the local machine type.

>## export  MONGO_URI=  mongodb+srv://**username**: **password**@cluster0-ored3.mongodb.net/**xxxx**   where xxxx = database ##

This command will create an environment variable on the local system named **'MONGO_URI'**
When the site is launched flask/mongo will look for it during initialization
The site was created inside a virtual environment.
The file **requirements.txt** details the modules installed to allow the install of the website.

**I will not lay out the access credentials here,  as it is forbidden by task requirements and a security breach. However, in a real situation this info will be given to the sysadmin.** The site is already up and running however on the Heroku platform, therefore visit the site. the link is at the top of this page.

[Heroku Deployment](https://bmmdb.herokuapp.com/)
**Connect to Heroku as the site is already up and running.**
*The environment variable is already configured in the Heroku app system setting.*

<a id="herokudeployment"></a>

>## **HEROKU DEPLOYMENT:** ##

If you wish to deploy to the Heroku Platform:

* Ensure you have cloned the repo from the **BMMDB_c GitHub Site** to a local drive location, you have admin access.

* Ensure these two files are within the same directory as the python executable..

* **(run.py)**

* **requirements.txt**  

This can be generated (inside the folder with python executable.. **(run.py)**) with the command python3 freeze -local > requirements.txt

* **Procfile** --- This can be generated (inside the folder with python executable.. **(run.py)**) with the command
* **echo "web: python run.py" > Procfile**  ... ensure it is a capital 'P'

* Sign Up to the **Heroku Platform** Follow their instructions:

* Install the Heroku CLI
* Download and install the Heroku CLI.
* If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
* $ heroku login
* **$ heroku git:clone -a bmmdb**
* $ cd bmmdb

* Create a **Heroku - APP** and note the name [ app-name ]. This will be used to hold the local **BMMDB** repo you have cloned

* In the **local terminal window*, within the flask folder( holding the two files requirements.txt and Procfile)**.

type **Heroku login**

* A webpage will launch inviting you to **enter login credentials.** You will now be connected to the Heroku Site

*  Now you must upload the repo using the **Git** tool.

1. type git add .
2. git commit -am "..message..."
3. git push heroku master

    **Git will upload the repo**

<a id="herokuenvironmentconfiguration"></a>

## **Setup Environment Variables for the Heroku App** ##

The 'Heroku-App' will not operate unless its environmental settings are completed

1. Click on settings
2. Click on **Reveal Configs**
3. Add a key **'IP'**  with a value **'0.0.0.0'**   ; This will allow the website-app to run on any computer
4. Add a key **'MONGO_URI'**  with the  Value of the MONGO_URI environment var create earlier, following the = sign.

>## export  MONGO_URI=  mongodb+srv://**username**: **password**@cluster0-ored3.mongodb.net/**xxxx**   where xxxx = database ##

    **Note substitute the credentials accordingly with those created when you configured the MONGO ATLAS DB previously**

5. Add a key **PORT** & a value **'8000'**

    Finally at the bottom you will find the heroku site launch address of your **Heroku-App**.

    **https://appname.herokuapp.com/**

<a id="credits"></a>

>## CREDITS ##

Inspiration was provided on the StackOverflow website. Below are some
key coders that provided solutions to some of my trickier issues.

* Code from Stackoverflow - Philip Feldmann... Keep text from overspilling out of columns */ 'keep-insideBSol' .. CSS
* Code assistance ... Pymongo search - Stack Overflow *
* sr9yar - Stack Overflow *
* user3375448 - Stack Overflow *

<a href="content"></a>

>## CONTENT ##

The coding was entirely mine. No code snippet was directly used, apart from standard templates code in Bootstrap 3.x and w3schools.

<a id="media"></a>

>## MEDIA ##

Pictures were taken from pixabay & pexels site.
All images are royalty-free and allowed for use. Below are the credits for the creators

* Photo by Clem Onojenghuo from pexels *
* Photo free - pixabay *
* Image by Peggy und Marco Lachmann-Anke from Pixabay *
* Photo Raphaelsilva Pixabay License *
* Photo Gordon Johnson Pixabay License *
* Photo Luis Quintero Pexels **

**Note: movie cover images - remain the copyright of that of their respective companies.**

<a id="acknowledgements"></a>

>## ACKNOWLEDGEMENTS ##

Thanks to Mentor **Precious Ijedge**, **Aaron Sinnott** I for review of the site.

<a id="useageinstructions"></a>

>## USEAGE INSTRUCTIONS ##

The site operation is simple.

1. Browse the site and reviews. If you wish to browse, then simply click the **blue < Search/browse>** button

2. Register on the site.

* If you wish to become a reviewer.

* If you want registration simply to receive our promotional material
<a id="forexaminer"></a>

> **NOTES FOR THE EXAMINER:**

**The following feature will be removed or made available for site administrators only via a CMS page of sorts.**

3. On the home page (bottom left). The **"delete this link"**, allows access to the promote user tool

4. On the resulting page. enter the email address you signed up with, and 'submit' to promote a new user to a ' review poster'

5. If you wish to activate affiliate pass thru, you need to exit the screen  once the user is made 'review-poster', then **re-run**
the promote user tool but selecting the affiliate link.

**This is because you are not allowed affiliate pass-through benefits unless you are already a 'review-poster'. Also,
both actions would never normally happen at once. You need to become a successful poster before you are given affiliate access**

<a id="postareview"></a>

## **Post: A Review** ##

1. As a **'Review-Poster'**, browse to **'Members - Add Review Page'**

2. Enter: username/email address/password...

3. scroll down the page, completing the section.

* Warning: The **"image-link"** field is expected to hold a link of an image that is hosted on another site. There are free hosting sites all over the internet.
However I have used a lot of wikipedia just to show the example.**

* The **"Affiliate-Link"** holds a link to the reviewers e-commerce ideals. THis is only activated amd viable when the site owner promotes the reviewer as detailed already.

4. Press blue <Submit Review> button.

<a id="deleteareview"></a>

## **Delete: A Review** ##

1. As a **'Review-Poster'**, browse to **'Members Maintenance Page'**

2. Select Radio Button Option **Get My Review(s)**

2. Enter: username/email address/password

3. Press the blue <'Process Button'>

    **This will provide a selection of all your reviews**

3. Use the drop-down and select a review to delete

4. Select Radio Button Option **Delete Review**

5. Enter: username/email address/password

5. Click on orange **'<Action Selected Process>'**

<a id="updateareview"></a>

## **Update: A Review** ##

1. As a **'Review-Poster'**, browse to **'Members Page'**

2. Select Radio Button Option **Get Review(s)**

3. Enter: username/email address/password...

4. Press the blue <'Process'> button

    **This will provide a selection of all your reviews**

5. Select Radio Button Option **Update Review(s)**

6. Re-enter: username/email address/password...

7. Use the **drop-down** and **select a review** to update

8. click on the orange **'<Update Selected>'** button.

    **The Member Update Sheet page will open, allowing you can complete your review update/changes**

    To do this...

10. Re-enter: username/email address/password... on the update-sheet

11. Complete the Sheet

12. Tick the **'Confirm Changes'** checkbox

13. press the orange **Submit Review** button.

<a id="important"></a>

**Note: The reason for multiple entries of email cred is to make it harder for an unauthorized user to access the member's page and carry out updates. This is not a full authentication site, so sessions are not active.**

> ## *FINALLY!!** The file **'defaultdb.py'** is a tool to allow the site administrator to reset the database quickly after site installation and testing of review submissions##

* It is NOT intended to remain and is a one-shot tool for this purpose. Therefore it is to be deleted once all is working satisfactorily.  It can be executed with running "python3 defaultdb.py"

End
