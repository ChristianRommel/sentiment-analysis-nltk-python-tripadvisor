# collection Model
##########################################
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
##########################################
def sentieval (collection):
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
    for n in range(len(collection)):
        review_score = collection[n][12]
        review_eval = collection[n][13]
        stars_eval = collection[n][14]

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
    return;
