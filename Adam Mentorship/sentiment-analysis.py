from pattern.en import sentiment

f = open('testreviews.txt','r',encoding="utf-8")
reviews = f.read().split("\n")

b = open('review-analysis.txt','w',encoding = "utf-8")


#output (sentiment -1 to 1, subjectivity 0 to 1)

for review in reviews: 
    result = sentiment(review)
    b.write(str(result[1]) + "\n")# + "," + str(result[1]) + "\n")

