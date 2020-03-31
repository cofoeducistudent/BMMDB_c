# Real Movie-Review-Database (MS3) #

## Blockbusters, McGuffins & Moes 

[BMMDB Live Site](https://bmmdb.herokuapp.com)

[BMMDB - Github - Site](https://github.com/cofoeducistudent/BMMDB_c)

![Blockbusters - Mcguffins & Moes](/support/‎1-home-page.png)

>With the many film review sites on the internet, I found it frustrating that the reviews frequently had an agenda. Indeed,I have found that I could not trust them. There are reasons for this. Primarily it’s that most reviews come from one source or publisher, and the others from the general public, who mainly are not professional film reviewers, rather individuals voicing an opinion. However, in both situations a bias agenda exits, nonetheless. I wanted to balance this out somewhat. Therefore, I decided to take the best from both sides of reviewer types and see what I could come up with.I decided to make a film review website, that can be controlled to eliminate the bias as much as possible. Therefore, I set the following brief to attain a site suited to something I would like to see.

>## Project Brief ##

* My scenario was to create a MOVIE REVIEW WEBSITE to promote movies past and present, in a professionally critiqued manner. The sites 'ssp' will be the sourcing of reviews from curated public film reviewers. I don't wish to have clickbait/slanderous soundbite reviews, in respect to our reviews, but calm considered critique. In effect I wish to distance the site from the predominant types of reviewers on the web.The first, a homogenous company having the hidden agenda of reviews favouring particular movie production companies via a nepotist back channel.
The other is the many millennial ‘woke’ childish reviews targeting films that do not conform to their partisan view of what a film should be, simply for slander for gaining self promotion.

* I want a clean looking site, with calm considered reviews, that present reviews within the 'class' a film was intended for. The site will aim to have more serious content and attract true film officiators.Comparing a low budget film with a tent pole $200 million dollar production is simply ridiculous.

* To help solve the above issues, each reviewer is be sourced from the public, however, they will not be allowed to post reviews without membership and agreeing to our terms and conditions. Or they will be struck off, with all their reviews removed.

* Secondly the reviewers will cover specific topic areas, thus keeping a strict format. Each section section will have a corresponding one,  for a citation supporting the review

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

* Each reviewer will have the autonomy to administrate their reviews by update or delete.However, they cannot interfere with other reviewers reviews of course.

* The public will be able to search for a particular title, or browse through existing reviews

# Index

>1 UX

a. Strategy

b. Scope

c. Structure

d. Skeleton

e. Surface

>2.FEATURES

a. Existing Features

b. Features Left to Implement

>3.TECHNOLOGIES USED

>4.TESTING

>5.DEPLOYMENT

>6.CREDITS

>7.CONTENT

>8.MEDIA

>9.ACKNOWLEDGEMENTS

>10.USEAGE INSTRUCTIONS

# UX

## STRATEGY

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

To clarify the objective for the site, its worth reminding ourselves of the user requirements.

> External User Goal** (Mainly the general public)

* Users will be able to search and browse existing reviews
* Registered users – Will be able receive promotional material via email
* Authorized Users (posters) – Will be able to post movie reviews, having full (CRUD) functionality.

> Site Owner Goal

* The site owner will be able to publish a “self-user-moderated site”, presenting reviews for movies past and present.
* The site owner will be able to convert registered users to “authorized reviewers”, allowing them to post movie reviews
* Site owners – Will be able post promo material to registered users and communicate.
* Site owners or designated site Admins will be able to delete entire database, promote users to 'posters'

## SCOPE

There are endless features possible for a site such as this, however we will limit our scope.

**In scope:**

* Database design & connectivity
* Website pages design
* **Although not requested in the MS3 task, a rudimentary authentication process has been implemented to reduce rouge postings and/or abuse of content.** It is not a fully realized login security system and does not employ sessions. Rather, it is a simple authentication against existing database credentials.

In addition there will be :

* Full CRUD ability for ‘authorized-users’..... (Create, Read, Update, Delete)
* Partial CRUD for ‘non-authorized / un-registered users’.....(Read).
* Affiliate Site link ability for authorized 'posters' ( Allows them to lik to a ecommerce site)

**Outside Scope:**

* **Mass deletion or reviews for admin purposes can be added**, and i have  included a field in the reviews data structure for that purpose(m-process). However as I do not think that is critical for this release it has been de-scoped.

**CRUD features for clarity mean:**

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
|7|Site Owner|I want a members page| So that member(authorized users) can amend/delete their reviews  giving them full (CRUD) ability for their posts|
|8|Site Owner|I want a method of affiliation sale-thru| So I can incentivize good reviewers, for more quality posts|  
|-||||
|9|Site Admin|I want a 'Database Initialize' ability | I can restore (after initialization & test of new site install ) The site can be cleared within seconds.
|10|Site Admin|I want a user 'PROMOTE-USER' feature|So that I can at will grant a new (Registered) member 'POST' ability on merit"
|11|Site Admin|I want a affiliate-link Activation feature| So that I can target and grant our top reviewers, pass-though-sale ability as a reward for continuous quality postings|
|-||||
|12|Anon User|I wish to see a browse/search feature|So I can read posted reviews about movies|
|-||||
|13|Registered User|I wish for a my movie reviews management page|So that I can (Post/Update/Delete) my reviews|

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

The site is classed as dynamic, moving data back and forth from a separate database. Only features within the defined scope will be implemented. There will be enough functionality to allow the site to be visibly operative. However the greater infrastructure support such as email - communications to the members and mailshot facility will not be operational.

Note:
Two features are placed within the repo by default. These need to be removed when the site is put in a production scenarion.

* defaultdb.py

* promoteuser html... link

Ultimately in a fully costed production, these features will and should be implemented in a CMS page of some sort, accessed by users with the correct rights.
 
**Warning:These features should be removed or accessed with security rights equivalent to 'site admins only!'**

The first feature **'defaultdb.py'** - wipes the database and places **5 films reviews** in the site database.
This feature is and should only be used in an initial site install.

* The second feature **'promoteuser'** - allows the site admin to turn a registered user into a **'poster'**. This grants the user rights to Create/Read/Update/Delete reviews that they post( but no one elses).

* once the reviewer/poster has created sufficient reviews conforming to the sites 'terms and condition', re-run the second page again, entering that users email.

* The system will allow them to post an AFFILIATE LINK , that can go to a site of their choosing. This is to incentivize reviewers to post many quality  reviews and benefit by allowing that link to go to a site of their choosing. From here they can have a central affiliate links to many products to make monetary gains.
