# collection Model
<<<<<<< HEAD
##########################################
=======
################################################################################
>>>>>>> refs/remotes/origin/Chris-new-stuff
# "_id": i[0],
# 'title': i[1],
# 'content': i[2],
# 'content_lenght': i[3],
# 'city': i[4],
# 'hotel_name': i[5],
# 'review_stars': i[6],
# 'helpful_reader': i[7],
# 'title_score': i[8],
# 'title_eval': i[9],
# 'content_score': i[10],
# 'content_eval' : i[11],
# 'review_score': i[12],
# 'review_eval' : i[13],
# 'stars_eval' : i[14]
<<<<<<< HEAD
##########################################
def sentieval (collection):
=======
################################################################################
from mongodb_connect import db
import math
def sentieval (db, col, collection, time):
>>>>>>> refs/remotes/origin/Chris-new-stuff
    all_cases = len(collection)
    false_positiv = []
    false_negativ = []
    false_neutral = []
    true_positiv_count = 0
    true_neutral_count = 0
    true_negativ_count = 0
    false_positiv_count = 0
    false_neutral_count = 0
    false_negativ_count = 0
<<<<<<< HEAD
=======
    _id = 0
>>>>>>> refs/remotes/origin/Chris-new-stuff
    for n in range(len(collection)):
        review_score = collection[n][12]
        review_eval = collection[n][13]
        stars_eval = collection[n][14]
<<<<<<< HEAD

=======
        # Dictionary for all false cases
        my_dict = {
        "review_id": collection[n][0],
        "title" :collection[n][1],
        "content": collection[n][2],
        "title_eval": collection[n][11],
        "content_eval": collection[n][13],
        "stars_eval": collection[n][14]
        }
        #Checking the cases
>>>>>>> refs/remotes/origin/Chris-new-stuff
        if review_eval == stars_eval and review_score > 0 :
            #True positiv
            true_positiv_count += 1
        elif review_eval == stars_eval and review_score == 0 :
            #True neutral
            true_neutral_count += 1
        elif review_eval == stars_eval and review_score < 0 :
            #True negativ
            true_negativ_count += 1
        elif review_eval != stars_eval and review_score > 0 :
            #False positiv
            false_positiv_count += 1
<<<<<<< HEAD
        elif review_eval != stars_eval and review_score == 0 :
            #False neutral
            false_neutral_count += 1
        elif review_eval != stars_eval and review_score < 0 :
            #False negativ
            false_negativ_count += 1
        else:
            print "something is wrong"
    #Total
    true_cases = true_positiv_count + true_neutral_count + true_negativ_count
    total_accuracy = float(true_cases) / all_cases * 100
    total_accuracy = round(total_accuracy, 2)
    # #Positiv
    true_false_positiv = true_positiv_count + false_positiv_count
    positiv_accuracy = float(true_positiv_count) / true_false_positiv * 100
    # #Neutral
    true_false_neutral = true_neutral_count + false_neutral_count
    neutral_accuracy = float(true_neutral_count) / true_false_neutral * 100
    # #Negativ
    true_false_negativ = true_negativ_count + false_negativ_count
    negativ_accuracy = float(true_negativ_count) / true_false_negativ * 100
    #results
    print "Results of the Evaluation\n"
    print "True positiv", true_positiv_count
    print "True neutral", true_neutral_count
    print "True negativ", true_negativ_count
    print "False positiv", false_positiv_count
    print "False neutral", false_neutral_count
    print "False negativ", false_negativ_count, "\n\n"
    print "The total_accuracy is", total_accuracy, "%"
    print "The positiv_accuracy is", positiv_accuracy, "%"
    print "The neutral_accuracy is", neutral_accuracy, "%"
    print "The negativ_accuracy is", negativ_accuracy, "%"
=======
            false_positiv.append(my_dict)
        elif review_eval != stars_eval and review_score == 0 :
            #False neutral
            false_neutral_count += 1
            false_neutral.append(my_dict)
        elif review_eval != stars_eval and review_score < 0 :
            #False negativ
            false_negativ_count += 1
            false_negativ.append(my_dict)
        else:
            print "something is wrong"
    #Accuracy
    ############################################################################
    #All cases
    true_cases = true_positiv_count + true_neutral_count + true_negativ_count
    total_accuracy = float(true_cases) / all_cases * 100
    total_accuracy = round(total_accuracy, 2)
    #Positiv
    true_false_positiv = true_positiv_count + false_positiv_count
    positiv_accuracy = float(true_positiv_count) / true_false_positiv * 100
    positiv_accuracy = round(positiv_accuracy, 2)
    #Neutral
    true_false_neutral = true_neutral_count + false_neutral_count
    neutral_accuracy = float(true_neutral_count) / true_false_neutral * 100
    neutral_accuracy = round(neutral_accuracy, 2)
    #Negativ
    true_false_negativ = true_negativ_count + false_negativ_count
    negativ_accuracy = float(true_negativ_count) / true_false_negativ * 100
    negativ_accuracy = round(negativ_accuracy, 2)
    #Insert the results to MongoDB
    ############################################################################
    db[col].insert_one(
        {
            "true positiv count": true_positiv_count,
            "true neutral count": true_neutral_count,
            "true negativ count": true_negativ_count,
            "false positiv count": false_positiv_count,
            "false neutral count": false_neutral_count,
            "false negativ count": false_negativ_count,
            "the total accuracy": total_accuracy,
            "the positiv accuracy": positiv_accuracy,
            "the neutral accuracy": neutral_accuracy,
            "the negativ accuracy": negativ_accuracy,
            "true false": false_positiv,
            "neutral false": false_neutral,
            "negativ false": false_negativ,
            "timestamp" : time
        }
    )
    ############################################################################
    #results
    print "Results of the Evaluation\n"
    print "Count: True positiv", true_positiv_count
    print "Count: True neutral", true_neutral_count
    print "Count: True negativ", true_negativ_count
    print "Count: False positiv", false_positiv_count
    print "Count: False neutral", false_neutral_count
    print "Count: False negativ", false_negativ_count, "\n\n"
    print "The total_accuracy is", total_accuracy, "%"
    print "The positiv_accuracy is", positiv_accuracy, "%"
    print "The neutral_accuracy is", neutral_accuracy, "%"
    print "The negativ_accuracy is", negativ_accuracy, "%\n\n"
>>>>>>> refs/remotes/origin/Chris-new-stuff
    return;
