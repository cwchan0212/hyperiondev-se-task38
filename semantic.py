# Task 38 - Semantic Similarity (NLP)
# Compulsory Task 1
# semantic.py

# Import spaCy liabrary
import spacy

# Set an object "nlp" to store the load the model "en_core_web_md" 
nlp = spacy.load("en_core_web_md")
# Set the "word1" object to to store the "nlp" object by processing a string "cat"
word1 = nlp("cat")
# Set the "word2" object to to store the "nlp" object by processing a string "monkey"
word2 = nlp("monkey")
# Set the "word3" object to to store the "nlp" object by processing a string "banana"
word3 = nlp("banana")
# compare the "word1" object and the "word2" object and predict similarity, 
# return a similarity score and print it
print(f"The similarity score bewteen {word1.text} and {word2.text}:\t{word1.similarity(word2)}")
# compare the "word3" object and the "word2" object and predict similarity, 
# return a similarity score and print it
print(f"The similarity score bewteen {word3.text} and {word2.text}:\t{word3.similarity(word2)}")
# compare the "word3" object and the "word1" object and predict similarity, 
# return a similarity score and print it
print(f"The similarity score bewteen {word3.text} and {word1.text}:\t{word3.similarity(word1)}\n")

#######################################################################################################################
# Note: 
# The similarity scores are under "en_core_web_md" 
# The similarity score bewteen cat and monkey:    0.5929929675536907
# The similarity score bewteen banana and monkey: 0.4041501317354622
# The similarity score bewteen banana and cat:    0.22358825939615987
#

# The pair of the "word1" (cat) object and the "word2" (monkey) object gets the highest simiarity score,
# where the pair of "word3" (banana) object the "word1" (cat") objects get the lowest score.
# Spacy may classify "cat" and "monkey" are animals and "monkey" has preference on "banans", 
# therefore "cat" and "monkey" get the highest similarity score.

 # Under the model "en_core_web_sm"
# The results are as follow:
# c:\Task_project38\semantic.py:18: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
# print(word1.similarity(word2))
# 0.7371059361772669
# c:\Task_project38\semantic.py:21: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   print(word3.similarity(word2))
# 0.7291608292298537
# c:\Task_project38\semantic.py:24: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
#   print(word3.similarity(word1))
# 0.6775488293064781
#
# In order to use similarity, We need a larger spaCy pipeline that has word vectors included. 
# # For example, the medium or large English pipeline – but not the small one. 
# So if we need to use vectors, always go with a pipeline that ends in "md" or "lg". 
#
#######################################################################################################################

items = ["bear", "bee", "honey"]

for index_one in range(len(items)-1):
    for index_two in range(index_one, len(items)):
        if index_one != index_two:
            # print(items[index_one], items[index_two])
            nlp_one = nlp(items[index_one])
            nlp_two = nlp(items[index_two])
            similarity_score = nlp_one.similarity(nlp_two)
            print(f"The similarity score between {nlp_one.text} and {nlp_two.text}:\t{similarity_score}")

#
# The similarity scores are under "en_core_web_md" 
# The similarity score between bear and bee:      0.19568899976696913
# The similarity score between bear and honey:    0.20337587003330035
# The similarity score between bee and honey:     0.5371793725217946
#
# The pair of the "nlp" (bee) object and the "nlp" (honey) object gets the highest simiarity score,
# where the pair of "nlp" (bear) object the "word1" (bee") objects get the lowest score.
# I think the similarity is based on the cohesion of the two items, that may depeond on the same classification,
# or the favourite of the item. For example, bear is an animal but bee is an insect whereas bear like drinking honey.
# 
#######################################################################################################################