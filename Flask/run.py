# Imports
import os
import pymongo
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_bootstrap import Bootstrap
from os import path
from bson.objectid import ObjectId


# Load Environment Variables
if path.exists("env.py"):
    import env


MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "rmrdb"
COLLECTION_USER_NAME = "users"
COLLECTION_REVIEWS = "reviews"

# Database Connection


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)  # Connect database with environment string
coll_users = conn[DBS_NAME][COLLECTION_USER_NAME]
coll_reviews = conn[DBS_NAME][COLLECTION_REVIEWS]

app = Flask(__name__)
Bootstrap(app)


# //###############################################//==================
##     G L O B A L - V A R S - S E C T I O N                          ##
# //###############################################//==================
total_allowed = 0
total_found = 0
users = {}


# Footer Message
siteText = {
    "footer-message": " ~ Copyright 2020, Code-Institute Milestone Project-3 - Clement Ofoedu ~ ",
}

rev_result = {}
rev_bag = []
my_revs = {}
crv_em = ""  # current reviewer email
select = ""

 

mt=""


 

# //###############################################//==================
##     M A I N  - C O D E - S E C T I O N                             #
# //###############################################//==================

'''
CHECK FOR DUPLICATE OBJECT ID
'''


def checkDup(id):
    matchid = 0
    store = coll_reviews.find()
    for stuff in store:
        if id == stuff['_id']:
            matchid = 1
            return matchid


# //###############################################//==================
##     M A I N  - VIEWS - S E C T I O N                              ##
# //###############################################//==================







@app.route('/')
def index():

    return render_template('index.html', page='Blockbusters, McGuffins & Moes', fm=siteText["footer-message"])
# =====================================//=============================

# About
@app.route('/about')
def about():
    '''
    #ABOUT PAGE VIEW
    '''

    return render_template('about.html', page='About Us', fm=siteText["footer-message"])
# =====================================//=============================









@app.route('/contact', methods=["GET", "POST"])
def contact():
    '''
    CONTACT PAGE VIEW
    '''
    if request.method == "POST":
        return redirect(url_for('contactSuccessOk'))
    return render_template('contact.html', page='Contact us', fm=siteText["footer-message"])
# =====================================//=============================
# Contact Success
@app.route('/contact-success', methods=["GET", "POST"])
def contactSuccessOk():
    '''
    VIEW SHOWN ON COMPLETION & POST OF CONTACT FORM
    '''
    return render_template('contact-success.html', page='Thank You for contacting us!', fm=siteText["footer-message"])
# =====================================//=============================










@app.route('/contribute', methods=["GET", "POST"])
def contribute():

    if request.method == "POST":
        return redirect(url_for('contributeS'))
    return render_template('contribute.html', page='Contribute Movie Suggestions For Review', fm=siteText["footer-message"])
# =====================================//=============================
# Contribute Success
@app.route('/contribute-success', methods=["GET", "POST"])
def contributeS():

    return render_template('contribute-success.html', page='Contribution success!', fm=siteText["footer-message"])
# =====================================//=============================













@app.route('/search', methods=["GET", "POST"])
def search():

    total_found = 0
    total_allowed = 0

    # Start search when
    if request.method == "POST":

        rev_results = []

        # Search criteria
        search_tit = request.form["s-title"]
        search_sub = request.form["s-sub-title"]
        search_rev = request.form["s-reviewer-name"]
        search_syn = request.form["s-synopsis"]
        search_gen = request.form["s-genre"]
        search_stars = request.form["s-stars"]

       ##########################//###############################

        if search_tit != "":
            print(search_tit)
            rev_results = coll_reviews.find(
                {"$text": {"$search": search_tit}}).limit(10)

        if search_sub != "":
            print(search_sub)
            rev_results = coll_reviews.find(
                {"$text": {"$search": search_sub}}).limit(10)

        if search_rev != "":
            print(search_rev)
            rev_results = coll_reviews.find(
                {"$text": {"$search": search_rev}}).limit(10)

        if search_syn != "":
            print(search_syn)
            rev_results = coll_reviews.find(
                {"$text": {"$search": search_syn}}).limit(10)

        if search_gen != "":
            print(search_gen)
            rev_results = coll_reviews.find(
                {"$text": {"$search": search_gen}}).limit(10)

        if search_stars != "":
            print(search_stars)
            rev_results = coll_reviews.find(
                {"$text": {"$search": search_stars}}).limit(10)

        if search_tit == "" and search_sub == "" and search_gen == "" and search_rev == "" and search_syn == "" and search_stars == "":
            search_tit = "The Attachment"

            rev_results = coll_reviews.find(
                {"$text": {"$search": search_tit}}).limit(10)

        return render_template('search-results.html', rev_results=rev_results, fm=siteText["footer-message"], page='Search Result Page..')

    return render_template('search.html', page='Search', fm=siteText["footer-message"], total_found=total_found, total_allowed=total_allowed)
# =====================================//=============================

# Search Result
@app.route('/search-results', methods=["GET", "POST"])
def searchResults():
    '''
    #SEARCH RESULTS PAGE!
    '''

    return render_template('search-results.html', page='Search Result(s) Page..', fm=siteText["footer-message"],  total_found=total_found, total_allowed=total_allowed)
# =====================================//=============================













@app.route('/register', methods=["GET", "POST"])
def register():
    '''
    # Register Users .... Change the role default to Member if you wish everyone to be able to submit a review

    '''

    if request.method == "POST":
        post = {
            "my-info": request.form["info"],
            "username": request.form["username"],
            "f-name": request.form['f-name'],
            "l-name": request.form['l-name'],
            "e-mail": request.form['e-mail'],
            "password": request.form['password'],
            "role": "user",
            "a-state": "no"
        }

        found = False
        unlock = False

        documents = coll_users.find()
        found = 0
        for entry in documents:
            if entry["e-mail"] == request.form["e-mail"]:
                found = 1
                print("Email Already Exists")
                return redirect(url_for('dupEmail'))

        for entry in documents:
            if entry['e-mail'] == request.form['e-mail'] and entry['password'] == request.form['password']:
                unlock = True
            if entry['e-mail'] == request.form['e-mail']:
                found = True

            # Login success
        if unlock == True:
            return redirect(url_for('loginSuccess'))
        elif found == True:
            return redirect(url_for('errorem'))
        elif entry['e-mail'] != request.form['e-mail']:
            coll_users.insert_one(post)
            return redirect(url_for('index'))

    return render_template('register.html', page='Member Registration Request', fm=siteText["footer-message"], users=users)
# =====================================//=============================

@app.route('/dup-email')
def dupEmail():
    '''
    # Duplicate Email Address Found
    Email address has already been used in the database record
    '''
    return render_template('dup-email.html', page='Error - Duplicate Email!', methods=["GET", "POST"], fm=siteText["footer-message"])
# =====================================//=============================




























@app.route('/promoteuser', methods=["GET", "POST"])
def promoteUser():
    '''
    PROMOTE USER VIEW
    '''
    if request.method == "POST":
        users = coll_users.find()
        fem = request.form['e-mail']
        for user in users:
            uUsername = user['username']
            uFname = user['f-name']
            uLname = user['l-name']
            uEmail = user['e-mail']
            uPassword = user['password']
            uRole = user['role']
            aff_state = request.form['a-state']

            if fem.upper() == uEmail.upper() and aff_state.upper() == "-" and uRole == "user":
                print("<<>>"+fem.upper())
                nw = {
                    "$set": {
                        "username": uUsername,
                        "f-name": uFname,
                        "l-name": uLname,
                        "e-mail": uEmail,
                        "password": uPassword,
                        "role": 'Admin',
                        "a-state": "no"
                    }
                }
                coll_users.update_one(user, nw)
                print("DONE")
                return redirect(url_for('promoteUserS'))

            if fem.upper() == uEmail.upper() and uRole == "Admin" and aff_state.upper() == "YES":
                print("+//+"+aff_state)
                nw = {
                    "$set": {
                        "username": uUsername,
                        "f-name": uFname,
                        "l-name": uLname,
                        "e-mail": uEmail,
                        "password": uPassword,
                        "role": 'Admin',
                        "a-state": "Yes"
                    }
                }
                coll_users.update_one(user, nw)

                return redirect(url_for('promoteUserS'))
    return render_template('promoteuser.html', page="Grant - Poster Privilege", Methods=["GET", "POST"], fm=siteText["footer-message"])
# #####################################################################


@app.route('/makeadmin-success', methods=["GET", "POST"])
def promoteUserS():
    '''
    # PROMOTE USER SUCCESS OK!
    Successfully converted standard user to an Admin, or added Affiliate pass-thru link ability
    '''
    return render_template('promoteuser-success.html', page="Promote User - Success", Methods=["GET", "POST"], fm=siteText["footer-message"])
# #####################################################################






















































 
@app.route('/member', methods=["GET", "POST"])
def member():
    '''
    INSERTION OF NEW MOVIE REVIEW
    VIEW PAGE!
    '''

    unlock = False
    if request.method == "POST":
        documents = coll_users.find()
        for u_cred in documents:
 
            crv_em = u_cred["e-mail"]

            for entry in documents:
                reviews = {
                    "m-title": request.form["m-title"].upper(),
                    "m-sub-title": request.form["m-sub-title"].upper(),
                    "m-genre": request.form["m-genre"],
                    "m-image-link": request.form["m-image-link"],
                    "m-synopsis": request.form["m-synopsis"],
                    "m-reviewer-name": request.form["r-name"].upper(),
                    "m-review-date": request.form["r-date"].upper(),
                    "m-stars": request.form["m-stars"].upper(),
                    "m-sc-review": request.form["sc-review"],
                    "m-sc-example": request.form["sc-example"],
                    "m-ac-review": request.form["ac-review"],
                    "m-ac-example": request.form["ac-example"],
                    "m-te-review": request.form["te-review"],
                    "m-te-example": request.form["te-example"],
                    "m-so-review": request.form["so-review"],
                    "m-so-example": request.form["so-example"],
                    "m-summary": request.form["su-review"],
                    "m-affiliate-link": request.form["m-af-link"],
                    "m-email": request.form["e-mail"],
                    "m-process": "none",
                }

                if entry['e-mail'] == request.form['e-mail'] and entry['password'] == request.form['password'] and entry['role'] == 'Admin':
                    unlock = True

                    if unlock == True:
                        '''
                            # ADD TO DATABASE NEW REVIEW #
                        '''
                        tuser = coll_users.find()
                        for auser in tuser:

                            # Add to Database if Title entry has been made!!
                            if auser['e-mail'] == crv_em and auser['a-state'] == "Yes":
                                # Insert A Review!!!!!!
                                reviews["m-affiliate-link"] = request.form["m-af-link"]
                                coll_reviews.insert_one(reviews)
                                return render_template(url_for('memberSubmitOk'), page='Member Review Submission OK!', fm=siteText["footer-message"])

                            # REMOVE AF-LINK IF MEMBER AF STATUS FALSE
                            if auser['e-mail'] == crv_em and auser['a-state'] == "no":
                                reviews["m-affiliate-link"] = "#"
                                coll_reviews.insert_one(reviews)
                                return render_template(url_for('memberSubmitOk'), page='Member Review Submission OK!', fm=siteText["footer-message"])

    return render_template('member.html', page='Member Add Review - Page', methods=["GET", "POST"], fm=siteText["footer-message"])
# =====================================//=============================







































@app.route('/member_d', methods=["GET", "POST"])
def member_d():
    '''
    ** MEMBER REVIEW DELETE VIEW **

    '''
    rev_bag=[]
    if request.method == "POST":


        unlock = False
        movies = coll_reviews.find()
        rev_bag = []
        documents = coll_users.find()

        for u_cred in documents:
            users = {
                "u_my_info": u_cred["my-info"],
                "u_username": u_cred['username'],
                "u_f_name": u_cred['f-name'],
                "u_l_name": u_cred['l-name'],
                "u_email": u_cred['e-mail'],
                "u_password": u_cred['password'],
                "u_role": u_cred['role'],
                "u_state": u_cred['a-state'],
            }







            crv_em = request.form['e-mail']
            if users['u_email'] == request.form['e-mail'] and users['u_password'] == request.form['password'] and users['u_role'] == 'Admin':
                unlock = True
                crv_em = u_cred["e-mail"]

                if unlock == True :#DELETE!!!
                    coll_reviews.find()
                    for mr in movies:
                        if mr['m-email'] == crv_em:
                            rev_bag.append(mr)
 
                    return redirect(url_for('deleteSelected'))
                 
                    select = request.form.get('revoption')

                    coll_reviews.delete_one({"_id": ObjectId(select)})

                    
                    # return render_template('assemble-for-deletion.html', fm=siteText["footer-message"], crv_em=crv_em, rev_bag=rev_bag)


                # return render_template('member.html', fm=siteText["footer-message"], crv_em=crv_em, rev_bag=rev_bag)

    return render_template('member_d.html', page='Member - Delete Page', methods=["GET", "POST"], fm=siteText["footer-message"],rev_bag=rev_bag )
# =====================================//=============================












# @app.route('/delete-process', methods=["GET", "POST"])
# def deleteProcess():
#     '''
#      #DELETE PAGE 
#     '''

#     return render_template('delete-process.html', page="Delete Review(s)", Methods=["GET", "POST"], fm=siteText["footer-message"])
# # #####################################################################

@app.route('/delete-selected', methods=["GET", "POST"])
def deleteSelected():





    return render_template('delete-selected.html', page='Member - Delete Page', methods=["GET", "POST"], fm=siteText["footer-message"],rev_bag=rev_bag )
# =====================================//=============================

























@app.route('/member_u', methods=["GET", "POST"])
def member_u():
    '''
    ** MEMBER REVIEW UPDATE  VIEW **

    '''
    if request.method == "POST":
        unlock = False
        movies = coll_reviews.find()
        rev_bag = []
        documents = coll_users.find()

        for u_cred in documents:
            users = {
                "u_my_info": u_cred["my-info"],
                "u_username": u_cred['username'],
                "u_f_name": u_cred['f-name'],
                "u_l_name": u_cred['l-name'],
                "u_email": u_cred['e-mail'],
                "u_password": u_cred['password'],
                "u_role": u_cred['role'],
                "u_state": u_cred['a-state'],
            }

            crv_em = request.form['e-mail']
            if users['u_email'] == request.form['e-mail'] and users['u_password'] == request.form['password'] and users['u_role'] == 'Admin':
                unlock = True
                crv_em = u_cred["e-mail"]

                if unlock == True and request.form['admin-action'] == "d":#DELETE!!!
                    coll_reviews.find()
                    for mr in movies:
                        if mr['m-email'] == crv_em:
                            rev_bag.append(mr)

                    select = request.form.get('revoption')
                    # coll_reviews.delete_one({"_id": ObjectId(select)})

                    
                    return render_template('assemble-for-deletion.html', fm=siteText["footer-message"], crv_em=crv_em, rev_bag=rev_bag)


                # return render_template('member.html', fm=siteText["footer-message"], crv_em=crv_em, rev_bag=rev_bag)

    return render_template('member_u.html', page='Member - Update / Delete Page', methods=["GET", "POST"], fm=siteText["footer-message"])
# =====================================//=============================























#//
            
            # crv_em = request.form['e-mail']
            # if users['u_email'] == request.form['e-mail'] and users['u_password'] == request.form['password'] and users['u_role'] == 'Admin':
            #     unlock = True
            #     crv_em = u_cred["e-mail"]
                 
            #     if unlock == True and request.form['admin-action'] == "u": #UPDATE!!!!!
                    
            #         coll_reviews.find()
            #         for mr in movies:
            #             if mr['m-email'] == crv_em: # CORRECT REVIEWER EMAIL
            #                 rev_bag.append(mr) # Add Review to bag

            #             select = request.form.get('revoption') # get selected review ID...
            #             if select == mr['_id']:

            #                 # mt=mr['m-title']
            #                 # print(mt)    
            #                 # rev_results = coll_reviews.find({"$text": {"$search": search_tit}}).limit(10)
                            
            #                 crv={

            #                     "m_title":mr['m-title'].upper(),
            #                     "m_sub_title":mr['m-sub-title'],
            #                     "m_genre":mr['m-genre'],
            #                     "m_image_link":mr['m-image-link'],
            #                     "m_synopsis":mr['m-synopsis'],
            #                     "m_reviewer_name":mr['m-reviewer-name'],
            #                     "m_review_date":mr['m-review-date'],
            #                     "m_stars":mr['m-stars'],

            #                     "m_sc_review": mr['m-sc-review'],
            #                     "m_sc_example": mr['m-sc-example'],

            #                     "m_ac_review": mr['m-ac-review'],
            #                     "m_ac_example": mr['m-ac-example'],
                                
            #                     "m_te_review": mr['m-te-review'],
            #                     "m_te_example": mr['m-te-example'],
                                
            #                     "m_so_review": mr['m-so-review'],
            #                     "m_so_example": mr['m-so-example'],

            #                     "m_summary": mr['m-summary'],
            #                     "m_affiliate_link": mr['m-affiliate-link'],
            #                     "m_email": mr['m-email'],
            #                     "m_process":'none'

            #                 }
                     

            #                 return render_template('update-sheet.html', crv=crv,  page='** Update Sheet! **', select=select, fm=siteText["footer-message"], crv_em=crv_em, rev_bag=rev_bag )
                


            #         return render_template('update-my-reviews.html', fm=siteText["footer-message"], crv_em=crv_em, rev_bag=rev_bag )



#     return render_template('member_ad.html', page='Member - Update / Delete Page', methods=["GET", "POST"], fm=siteText["footer-message"])
# # =====================================//=============================





















@app.route('/member-options', methods=["GET", "POST"])
def memberOptions():
    rev_bag=[]
    if request.method == "POST":
       
        movies = coll_reviews.find() # get movie collection
        documents = coll_users.find() # get users collection
        for u_cred in documents:
            users = {
                "u_my_info": u_cred["my-info"],
                "u_username": u_cred['username'],
                "u_f_name": u_cred['f-name'],
                "u_l_name": u_cred['l-name'],
                "u_email": u_cred['e-mail'],
                "u_password": u_cred['password'],
                "u_role": u_cred['role'],
                "u_state": u_cred['a-state'],
            }

            unlock = False
            crv_em = request.form['e-mail']
         
            if users['u_email'] == request.form['e-mail'] and users['u_password'] == request.form['password']  and request.form['user-options'] !='Delete'  and users['u_role'] == 'Admin':
                unlock = True

                for mr in movies:
                    if mr['m-email'] == crv_em and unlock == True:
                        rev_bag.append(mr)
       
                return render_template('member-options-gr.html', page='Member Options Page!', fm=siteText["footer-message"], rev_bag=rev_bag, unlock=unlock )

            elif users['u_email'] == request.form['e-mail'] and users['u_password'] == request.form['password'] and request.form['user-options']=='Delete'  and users['u_role'] == 'Admin':
                unlock = True
                coll_reviews.find()
                deleterev = request.form['movie-list']
 
                coll_reviews.delete_one({'_id':ObjectId(deleterev)})

                print("DELETED REVIEW!!")
                print(deleterev)

                return render_template('member-options-gr.html', page='Member Options Page!', fm=siteText["footer-message"], rev_bag=rev_bag)

    return render_template('member-options.html', page='Member Options Page!', fm=siteText["footer-message"],rev_bag=rev_bag)
# =====================================//=============================

 





@app.route('/member-options-gr', methods=["GET", "POST"])
def memberOptionsGr():

     
    return render_template('member-options-gr.html', page=' Page!', fm=siteText["footer-message"],rev_bag=rev_bag)
# =====================================//=============================





@app.route('/delete-success.html', methods=["GET", "POST"])
def deleteSuccessOk():
   
    # print("DELETE SUCCESS!")

    return render_template('delete-success.html', page='Delete Success OK!', fm=siteText["footer-message"])
# =====================================//=============================



























@app.route('/member-submission-ok.html', methods=["GET", "POST"])
def memberSubmitOk():
    '''
    # MEMBER REVIEW SUBMISSION OK 
    '''
    return render_template('member-submission-ok.html', page='Member Review Submission OK!', fm=siteText["footer-message"])
# =====================================//=============================














@app.route('/update-sheet.html', methods=["GET", "POST"])
def updateMyReviews():

    # if request.method == "POST":

    #     movies = coll_reviews.find()
    #     for each_movie in movies:
    #         # if each_movie['_id'] == request.form['rev_option']:
    #         if each_movie['_id'] == select:

    #             print("---")

    #         # coll_reviews.delete_one({"_id":request.form['rev_option']})

    #     return render_template('update-ok.html', page='Update Review Success', fm=siteText["footer-message"])

    return render_template('update-sheet.html', page='Update Reviews', fm=siteText["footer-message"])
# =====================================//=============================


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "127.0.0.1"), port=int(
        os.environ.get("PORT", 8000)), debug=True)



