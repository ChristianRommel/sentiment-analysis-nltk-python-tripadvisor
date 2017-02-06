# collection Model
################################################################################
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
################################################################################
from mongodb_connect import db
import math
def sentieval (db, col, collection, time):
    all_cases = len(collection)
    false_positiv = []
    false_negativ = []
    false_neutral = []
    #Reviews
    true_positiv_count = 0
    true_neutral_count = 0
    true_negativ_count = 0
    false_positiv_count = 0
    false_neutral_count = 0
    false_negativ_count = 0
    #Only Title
    title_true_positiv_count = 0
    title_true_neutral_count = 0
    title_true_negativ_count = 0
    title_false_positiv_count = 0
    title_false_neutral_count = 0
    title_false_negativ_count = 0
    #Only Content
    content_true_positiv_count = 0
    content_true_neutral_count = 0
    content_true_negativ_count = 0
    content_false_positiv_count = 0
    content_false_neutral_count = 0
    content_false_negativ_count = 0

    _id = 0
    for n in range(len(collection)):
        review_score = collection[n][12]
        review_eval = collection[n][13]
        stars_eval = collection[n][14]
        title_eval = collection[n][9]
        content_eval = collection[n][11]
        title_score = collection[n][8]
        content_score = collection[n][10]
        #Dictionary for all false cases
        my_dict = {
        "review_id": collection[n][0],
        "title" :collection[n][1],
        "content": collection[n][2],
        "title_eval": title_eval,
        "content_eval": content_eval,
        "stars_eval": stars_eval,
        "review_eval" : review_eval,
        }
        #Checking the cases for Reviews
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
        #Title cases
        ########################################################################
        if title_eval == stars_eval and title_score > 0 :
            #True positiv
            title_true_positiv_count += 1
        elif title_eval == stars_eval and title_score == 0 :
            #True neutral
            title_true_neutral_count += 1
        elif title_eval == stars_eval and title_score < 0 :
            #True negativ
            title_true_negativ_count += 1
        elif title_eval != stars_eval and title_score > 0 :
            #False positiv
            title_false_positiv_count += 1
        elif title_eval != stars_eval and title_score == 0 :
            #False neutral
            title_false_neutral_count += 1

        elif title_eval != stars_eval and title_score < 0 :
            #False negativ
            title_false_negativ_count += 1
        else:
            print "something is wrong"
        #Content cases
        ########################################################################
        if content_eval == stars_eval and content_score > 0 :
            #True positiv
            content_true_positiv_count += 1
        elif content_eval == stars_eval and content_score == 0 :
            #True neutral
            content_true_neutral_count += 1
        elif content_eval == stars_eval and content_score < 0 :
            #True negativ
            content_true_negativ_count += 1
        elif content_eval != stars_eval and content_score > 0 :
            #False positiv
            content_false_positiv_count += 1
        elif content_eval != stars_eval and content_score == 0 :
            #False neutral
            content_false_neutral_count += 1
        elif content_eval != stars_eval and content_score < 0 :
            #False negativ
            content_false_negativ_count += 1
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
    ############################################################################
    #Only Title
    title_true_cases = title_true_positiv_count + title_true_neutral_count + title_true_negativ_count
    title_total_accuracy = float(title_true_cases) / all_cases * 100
    title_total_accuracy = round(title_total_accuracy, 2)
    #Positiv
    title_true_false_positiv = title_true_positiv_count + title_false_positiv_count
    title_positiv_accuracy = float(title_true_positiv_count) / title_true_false_positiv * 100
    title_positiv_accuracy = round(title_positiv_accuracy, 2)
    #Neutral
    title_true_false_neutral = title_true_neutral_count + title_false_neutral_count
    title_neutral_accuracy = float(title_true_neutral_count) / title_true_false_neutral * 100
    title_neutral_accuracy = round(title_neutral_accuracy, 2)
    #Negativ
    title_true_false_negativ = title_true_negativ_count + title_false_negativ_count
    title_negativ_accuracy = float(title_true_negativ_count) / title_true_false_negativ * 100
    title_negativ_accuracy = round(title_negativ_accuracy, 2)
    ############################################################################
    #Only Content
    content_true_cases = content_true_positiv_count + content_true_neutral_count + content_true_negativ_count
    content_total_accuracy = float(content_true_cases) / all_cases * 100
    content_total_accuracy = round(content_total_accuracy, 2)
    #Positiv
    content_true_false_positiv = content_true_positiv_count + content_false_positiv_count
    content_positiv_accuracy = float(content_true_positiv_count) / content_true_false_positiv * 100
    content_positiv_accuracy = round(content_positiv_accuracy, 2)
    #Neutral
    content_true_false_neutral = content_true_neutral_count + content_false_neutral_count
    content_neutral_accuracy = float(content_true_neutral_count) / content_true_false_neutral * 100
    content_neutral_accuracy = round(content_neutral_accuracy, 2)
    #Negativ
    content_true_false_negativ = content_true_negativ_count + content_false_negativ_count
    content_negativ_accuracy = float(content_true_negativ_count) / content_true_false_negativ * 100
    content_negativ_accuracy = round(content_negativ_accuracy, 2)
    ############################################################################
    #Insert the results to MongoDB
    db[col].insert_one(
        {
            "true_positiv_count": true_positiv_count,
            "true_neutral_count": true_neutral_count,
            "true_negativ_count": true_negativ_count,
            "false_positiv_count": false_positiv_count,
            "false_neutral_count": false_neutral_count,
            "false_negativ_count": false_negativ_count,
            "the_total_accuracy": total_accuracy,
            "the_positiv_accuracy": positiv_accuracy,
            "the_neutral_accuracy": neutral_accuracy,
            "the_negativ_accuracy": negativ_accuracy,
            "positiv_false": false_positiv,
            "neutral_false": false_neutral,
            "negativ_false": false_negativ,
            "timestamp" : time,
            "review_count" : all_cases,
            #Title only
            "title_true_positiv_count": title_true_positiv_count,
            "title_true_neutral_count": title_true_neutral_count,
            "title_true_negativ_count": title_true_negativ_count,
            "title_false_positiv_count": title_false_positiv_count,
            "title_false_neutral_count": title_false_neutral_count,
            "title_false_negativ_count": title_false_negativ_count,
            "title_the_total_accuracy": title_total_accuracy,
            "title_the_positiv_accuracy": title_positiv_accuracy,
            "title_the_neutral_accuracy": title_neutral_accuracy,
            "title_the_negativ_accuracy": title_negativ_accuracy,
            #Content only
            "content_true_positiv_count": content_true_positiv_count,
            "content_true_neutral_count": content_true_neutral_count,
            "content_true_negativ_count": content_true_negativ_count,
            "content_false_positiv_count": content_false_positiv_count,
            "content_false_neutral_count": content_false_neutral_count,
            "content_false_negativ_count": content_false_negativ_count,
            "content_the_total_accuracy": content_total_accuracy,
            "content_the_positiv_accuracy": content_positiv_accuracy,
            "content_the_neutral_accuracy": content_neutral_accuracy,
            "content_the_negativ_accuracy": content_negativ_accuracy,

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
    return;
