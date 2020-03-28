'''
WARNING : Please delete this file from the directory before making this site public..
or make this file hidden and executable by an site addministrator ONLY!!

This file contains review data. It is installed with the repo
whilst testing and learning the movie-database, you may have placed
some erronues entries
This file is executed at the command line by and administrator
by running the command

' python3 defaultdb.py'

It will 'drop' the current collection and reload with default content!!!
'''


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




movie_database = [      { 
            "m-title": "THE ATTACHMENT",
            "m-sub-title": "-",
            "m-genre": "Mystery",
            "m-image-link": "https://m.media-amazon.com/images/M/MV5BNTM0OTMzNDUwOF5BMl5BanBnXkFtZTgwOTAyMTg5OTE@._V1_SY1000_SX675_AL_.jpg",
            "m-synopsis": "An innocent girl's world is turned upside-down when an ancient evil begins to stalk her family. An attempt by a religious sect to rid the evil from the family results in catastrophic results that will have far-reaching consequences.",
            "m-reviewer-name": "Clement Ofoedu",
            "m-review-date": "09012020",
            "m-stars": "3",
            "m-sc-review": "The script was quite good. Indeed we are sure that with sufficient budget, acting class, and better special effects and a little reworking. It is clear what the director and writer were going for. However, like many low-budget affairs, its budget was miscast for the product. this film should have been executed with 3-4 times the budget to accomplish the objective. We have seen this situation many times, and its of no surprise, as there are a lot of talented writers out there, that need a leg up and funding. But the crazy world of show business and movies, does not allow easy access to higher tiers.",
            "m-sc-example": "The story, if ever published would be worth a read, as the execution in film format,",
            "m-ac-review": "Now here is where we can tell much about the film's budget, as there are no main stars here, and all are unknown. There is the odd cameo by famous musicians, but ultimately this doesn't assist much with movie audiences. The primary actors were ok in the main, some, however, were a bit ropy. Part of that we feel can be attributed to the script, as it can be garnered what's been said. But ultimately it can be viewed as lines that look good on paper but should be reworked for the screen",
            "m-ac-example": "The characters of Callum Bradshaw and Leah Cooper were Good for the budget. Carroll not so much.",
            "m-te-review": "The film employs VFX, but sparingly. This does not surprise us. Most low budget filmmakers have access to VFX tools, as the costs have plummeted for a while now. However, the problem is many filmmakers employ terrible effects. The filmmakers here opted to use the effects sparingly, with only a few money shots",
            "m-te-example": "Regurgitating spider. death scene",
            "m-so-review": "The sound quality was quite good, and it evident that some thought and planning went into the sound element. The tracks were very clean, and void of the usual fizz, crackle and pop that plague independent low budget affairs. As if that was not enough, it was also apparent that the film had a soundtrack composed, and a good one at that. Our thoughts are that this was created by a burgeoning composer willing to work his craft for fame rather than monetary rewards, as the composition of 6 track would easily have taken up half the budget of this movie overall. So well done to the film maker for pulling that out the hat.",
            "m-so-example": "The opening track and the final credit track are very well composed, sounding bombastic and in full flow. We know that many low budget films opt for soundtracks filled with noises or purchased catalogue music. Therefore, to have an original score on a low budget affair like this is indeed unique",
            "m-summary": "The Attachment is a cheaply made mystery/melodrama. The sort that would be shown at teatime. Like a father brown, or Mrs Marple entertainment. It hits the spot for general family viewing. The movie steers clear of excessive gore and sex or nudity. That said it does deal with some heavy topics, but in such a way that it's not too offensive to younger people. For this reason, it can be watched with parental guidance. But to be sure cheaply made does not mean it’s terrible. and our understanding is that the film was made for around 10k, which is a pittance in film budget comparison.",
            "m-affiliate-link": "https://www.imdb.com/title/tt3234668/",
            "m-email": "cofoedu@gmail.com",
            "m-process": "none" 
           },
           {
            "m-title": "BATMAN",
            "m-sub-title": "THE DARK KNIGHT",
            "m-genre": "Action",
            "m-image-link": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
            "m-synopsis": "The Joker wreaks havoc in Gotham City, causing batman to rise to the challenge, resulting in an action-packed, intellectual game of cat and mouse. This cause a critical change in the Dark Knight as he learns that not all people are logical. Indeed for this foe, he comes to the realization that some of me can not be bought or reasoned with. Some men can't be bargained and want to watch the world burn.",
            "m-reviewer-name": "Mark Kermode",
            "m-review-date": "27022020",
            "m-stars": "4",
            "m-sc-review": "Chris Nolan brings to the big screen, and none bigger than IMAX a new interpretation of the caped crusader. The Dark Knight is the second in a trilogy of the re-imagining of the Batman franchise. The costume is the same and so are the characters. However, gone are the comic elements. Mr Nolan has decided to place batman in a real-world of flesh and bones, actions and consequences and man does he score. The script is tight and well crafted. And although the film is lengthy at 2hours and 32 minutes, time flies by when you are having fun.",
            "m-sc-example": "The lines of dialogue suit the characters, and at no time does it feel forced or unreal. The tension is stewed to perfection as from act1, act2 and act3 feel like a three-course meal, leaving you wanting for nothing",
            "m-ac-review": "All the characters are well developed from the library of DC, and Christopher Nolan has aptly portrayed them with competent and experienced A-list actors.",
            "m-ac-example": "The stand out performance must go to Heath Ledger, who unfortunately passed away before the release of the film. Heath takes the villain Joker to another level of insanity. He almost gives a reason , or is it believability to the madness, sucking the viewer in. Soon you find that perhaps he has a point. But isn't that what all great villains should be, sane in their insanity.",
            "m-te-review": "Top-quality laces the production, from shooting sites to sets, stunts and sound. The shooting was done on film and not digital. Indeed not 35mm but the 70mm I-Max I-Max is expensive to shoot and produce. No expense was spared",
            "m-te-example": "The extremes the filmmakers went to can be typified by the design of technologies from the suit to the Tumbler and of course the bike.",
            "m-so-review": "Hans Zimmer continues to impress with is fantastic scoring in Hollywood production and Batman is no exception. The track is brooding, manic at times and bombastic.",
            "m-so-example": "Hans used legendary Japanese KOTO drummers to score the main theme, as well as top musicians. But the genius is Hans, who has almost risen neck and neck with John Wiliams.",
            "m-summary": "The Dark Knight does not disappoint. A film crafted by a professional and expert filmmaker. A film that takes you on all sorts of emotion, yet ultimately leaving you wanting more",
            "m-affiliate-link": "https://www.imdb.com/title/tt0468569/?ref_=fn_al_tt_1",
            "m-email": "m.kermode@gmail.com",
            "m-process": "none"
            },
            {
            "m-title": "STAR WARS",
            "m-sub-title": "A New Hope",
            "m-genre": "SciFi",
            "m-image-link": "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,643,1000_AL_.jpg",
            "m-synopsis": "Luke Skywalker is a young farm boy on a desert planet, who soon becomes swept up in an adventure, that will see him ultimately become part of a rebel alliance, fighting against an almighty domineering empire. The galaxy stands at a knife-edge of total servitude or freedom from oppression.",
            "m-reviewer-name": "Clement Ofoedu",
            "m-review-date": "03022020",
            "m-stars": "4",
            "m-sc-review": "Star war is a rip-roaring adventure brought to the cinema by writer-director George Lucas. A talented young film-maker at the time. Hitting cinema's in 1977, star wars change the world of motion pictures. The script works and the resultant 2hour movie did not seem long at all. For a science fiction-based film, George carefully crafted it also into an adventure like western. Therefore the film wasn't about science, but science just happened to populate the world the characters inhabited. The story followed the Hero's Journey path of storytelling.",
            "m-sc-example": "Some dialogue was difficult to say for some actors. But somehow it worked Han-Solo: 'Travelling through hyperspace ain't like dusting crops boy.'. But as an audience, you go with it.",
            "m-ac-review": "As for the Cast, although many were relatively unknown, they were of good calibre. They also had the quality to believe what they were doing, adding to the overall delivery. George also managed to cast some well-known actors, which helped ultimately propel the film.",
            "m-ac-example": "George cast Sir Alec Guinness and Peter Cushing. Peter was a mainstay in a league of hammer house horror films by then, and Sir Alec had been nominated for many films including the bridge on the river kwai.",
            "m-te-review": "Star Wars surpassed all expectations and is legendary for starting the modern-day visual effects industry and furthering cinematic sound",
            "m-te-example": "George founded two companies to help pioneer the visual effects that they wanted, and also the sound effects.",
            "m-so-review": "John Williams masterfully scored the film, coming off the back of Jaws and it was almost flawless",
            "m-so-example": "The StarWars theme is universally known and acclaimed",
            "m-summary": "Star Wars is a film that brought in a new era of film-making. In doing so it also re-envisaged a genre, creating new ways to achieve films. VFX, SFX, Cinematic, thematic scores. Moviegoers the world over have George Lucas to thank for current films, as without him the industry would look very different",
            "m-affiliate-link": "https://www.imdb.com/title/tt0076759/",
            "m-email": "cofoedu@gmail.com",
            "m-process": "none"
            },
            {
            "m-title": "RAIDERS OF THE LOST ARK",
            "m-sub-title": "-",
            "m-genre": "Action",
            "m-image-link": "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
            "m-synopsis": "Harrison Ford is cast as Indiana Jones an Archeologist professor/Adventurer. Set during WWII, the story follows Indiana as he races to find the long lost Ark of the Covenant, whilst avoiding the Nazi Third Reich, who was also after it. They believed whatever army held the ark, held the ultimate weapon.",
            "m-reviewer-name": "Clement Ofoedu",
            "m-review-date": "02022020",
            "m-stars": "4",
            "m-sc-review": "The story was great and tight. Another production from George Lucas. This time with his friend Steven Speilberg. This proved a great collaboration and Raider of the lost ark surpassed expectations at the box office",
            "m-sc-example": "The film brought many new themes to the cinema, such as a lone explorer searching ancient ruins for treasure, but this time for good rather than riches. The boulder chasing scene has been parodied endlessly",
            "m-ac-review": "The actors in the film were all top calibre, not a dud insight",
            "m-ac-example": "The chemistry between Harrison Ford and Karen Allen worked on screen very well. More so than any of the hookups in the sequels",
            "m-te-review": "The film was, as much of Lucas and Speilberg's offers top-notch. from VFX to stunts",
            "m-te-example": "The truck chase was a well-remembered scene, not only for it was good, but that a stuntman was seriously injured doing it. It was a stunt rarely seen because it was soo dangerous",
            "m-so-review": "Our old friend and maestro John Williams again conducted a memorable bombastic score.",
            "m-so-example": "The main theme is well remembered",
            "m-summary": "Raiders of the Lost Ark is a top tent-pole movie, that made a huge sum at the box office. It also gave Harrison Ford, his second popular character following the Star wars Han-Solo pilot. A film set during WW2 gave the film. ",
            "m-affiliate-link": "https://en.wikipedia.org/wiki/Raiders_of_the_Lost_Ark",
            "m-email": "cofoedu@gmail.com",
            "m-process": "none"
            },
            {
            "m-title": "CLOSE ENCOUNTERS OF THE THIRD KIND",
            "m-sub-title": "-",
            "m-genre": "SciFi",
            "m-image-link": "https://upload.wikimedia.org/wikipedia/en/b/ba/Close_Encounters_of_the_Third_Kind_%281977%29_theatrical_poster.jpg",
            "m-synopsis": "When strange things begin happening in Indianapolis, it soon escalates statewide. From the air force missing planes,  to the small individual family, it soon becomes clear that we are being visited by strangers from another world.",
            "m-reviewer-name": "Mark Kermode",
            "m-review-date": "03/02/2020",
            "m-stars": "3",
            "m-sc-review": "Steven Spielberg stepped up to the platform after jaws and George Lucas's star wars, bringing Close Encounters to the screen. Steven would say its really a collection of hearsay and stories he had heard floating around in the sixties etc with regards to the flying saucer phenomenon.",
            "m-sc-example": "The script is engaging, posing many mysteries from ufo lore, but the driving factor is truly family and relationships. Indeed what happens when a person is witness and experiencer of such phenomenon.",
            "m-ac-review": "Richard Dreyfus is great and engaging as a family man going through an experience that is driving him to insanity",
            "m-ac-example": "Dreyfus and mashed potatoes scene",
            "m-te-review": "ILM brought its A-game as expected",
            "m-te-example": "UFO's,  UFO's, UFO's",
            "m-so-review": "Great sound and the most recognized keynotes in history from John Williams",
            "m-so-example": "5 note arpeggio",
            "m-summary": "A film that fills you with awe and wonder. CE3K is another total masterpiece from Speilberg, which stripping the sci-fi, leaves you with a heartwarming story.",
            "m-affiliate-link": "",
            "m-email": "cofoedu@gmail.com",
            "m-process": "none"
            }
 ]
           
'''
Drop current database collection and upload from file

''' 
coll_reviews.drop()
coll_reviews.insert_many(movie_database)
 
coll_reviews.create_index([("m-title","text"),("m-sub-title","text"),("m-genre","text"),("m-synopsis","text"),("m-reviewer-name","text"),("m-review-date","text"),("m-stars","text"),("m-summary","text")], default_language='english')
 

print("Database Successfully Reloaded!...")