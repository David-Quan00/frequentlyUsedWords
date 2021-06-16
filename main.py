'''
Author: David Q
Date: June 16, 2021
Project Description: Taking a book (Arsène Lupin by Maurice Leblanc), and
extracting the top 10 most popular words that start or end with the letter s.
The book can be found at: https://www.gutenberg.org/files/6133/6133-0.txt
'''
import matplotlib.pyplot as plt

# Open the file.  Note: Need the encoding to avoid a UniDecodeError
input_file = open("arsene_lupin.txt", "r", encoding="utf -8")

# Stop Words that we will want to ignore
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
              'you', "you're", "you've", "you'll", "you'd", 'your', 'yours',
              'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
              "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
              'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
              'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
              'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
              'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the',
              'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
              'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
              'into', 'through', 'during', 'before', 'after', 'above', 'below',
              'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
              'under', 'again', 'further', 'then', 'once', 'here', 'there',
              'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
              'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
              'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's',
              't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",
              'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',
              "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn',
              "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't",
              'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't",
              'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
              'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn',
              "wouldn't"]

# Create a list that will hold all our uncleansed words
raw_words_lst = []

# List of punctuation we don't want in our word
punctuation_lst = ['.', ',', '\"', "?", "!", ";", ":", "\'", "‘", "’", "“", "”"]

# Create a new list that will hold our cleansed words
clean_words_lst = []

# Create a dict containing the count of each word
words_and_count_dict = {}

# Create a dict that will be sorted.
sorted_words_and_count_dict = {}

# Iterate through the input_file, line by line
for line in input_file:
    # Split will parse our words and help create the individual raw_words
    words = line.split()
    # Add the words to the list called raw_words
    for element in words:
        # There was a weird edge case in which “ != "
        # So I removed these words manually.
        if element != '“I':
            raw_words_lst.append(element)

# Cleaning the data
for raw_word in raw_words_lst:
    # The word has a punctuation attached to the end, ie. period, question mark
    # Remove the punctuation from the word
    # We will only add it to the list of clean_words if it's not an unwanted
    # stop word, and we will want to ignore the capitalization.
    is_clean = False
    if is_clean == False:
        if raw_word[len(raw_word) - 1] in punctuation_lst:
            raw_word = raw_word[:-1]
            if raw_word.lower() not in stop_words:
                clean_words_lst.append(raw_word)
        elif raw_word[len(raw_word) - 1].isalpha():
            # Only add the raw_word if it's not a stop word.
            if raw_word.lower() not in stop_words:
                clean_words_lst.append(raw_word)
                is_clean = True

# Count/establish the number of occurrences of each word.
for word in clean_words_lst:
    # If the word is not yet in the dictionary, we add it and set the value to 1
    if word not in words_and_count_dict:
        words_and_count_dict[word] = 1
    # If the word is already in the dict, we just add 1 to the current value.
    elif word in words_and_count_dict:
        words_and_count_dict[word] += 1

# Sort the dict in descending order, namely in most to least occurrences
sorted_words_and_count_dict = dict(sorted(words_and_count_dict.items(), key = lambda item: item[1], reverse = True))

# Remove the dictionary entries that are stop words.
for key in sorted_words_and_count_dict:
    if key in stop_words:
        sorted_words_and_count_dict.pop(key)

# Return the top 10 words
sorted_words_and_count_dict_items = sorted_words_and_count_dict.items()
top_ten = list(sorted_words_and_count_dict_items)[:10]
print("The Top 10 Words are: ", top_ten)

# Arrange our data in a list for our x and y axes
words = []
occurrences = []
for element in top_ten:
    words.append(element[0])
    occurrences.append(element[1])

#Plot our Data:
#Draw the size of our canvas/figure.
plt.figure(figsize=(9, 6))

# Create labels for our graph.
plt.title("Top 10 Most Frequently Used Words in the book, 'Arsène Lupin' by Maurice Leblanc", fontsize=11)
plt.ylabel("Number of Occurrences")
plt.xlabel("Word")

# Create a bar graph with words on x-axis and
# its respective occurrences on the y-axis.
plt.bar(words, occurrences)

# Output the graph.
plt.show()

# Close our file
input_file.close()
