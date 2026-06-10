'''
3. Movie Review Sentiment Analyzer 
Problem Statement 
Movie reviews are stored as follows: 
reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
] 
Requirements 
Create the following functions: 
1. count_sentiments(reviews) 
Counts: 
• Excellent  
• Good  
• Average  
• Poor reviews  
2. most_common_word(reviews) 
Returns the most frequently occurring word. 
3. longest_review(reviews) 
Returns the review containing the maximum number of characters. 
4. reviews_with_keyword(reviews, keyword) 
Displays all reviews containing a given keyword. 
Sample Output 
Excellent Reviews: 4 
Good Reviews: 2 
Average Reviews: 2 
Poor Reviews: 2 
 
Most Common Word: 
excellent 
 
Longest Review: 
good cinematography 
 
Reviews containing 'excellent': 
excellent movie 
excellent acting 
excellent visuals 
excellent climax
'''
# =====================================
# Movie Review Sentiment Analyzer
# =====================================

# List of movie reviews
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# -------------------------------------
# Function to count sentiments
# -------------------------------------
def count_sentiments(reviews):

    # Variables to store counts
    excellent = 0
    good = 0
    average = 0
    poor = 0

    # Check each review
    for review in reviews:

        if "excellent" in review:
            excellent += 1

        elif "good" in review:
            good += 1

        elif "average" in review:
            average += 1

        elif "poor" in review:
            poor += 1

    # Return all counts
    return excellent, good, average, poor


# -------------------------------------
# Function to find most common word
# -------------------------------------
def most_common_word(reviews):

    # Empty dictionary
    word_count = {}

    # Check each review
    for review in reviews:

        # Split review into words
        words = review.split()

        # Check each word
        for word in words:

            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Find word with maximum frequency
    most_word = max(word_count, key=word_count.get)

    return most_word


# -------------------------------------
# Function to find longest review
# -------------------------------------
def longest_review(reviews):

    # Return review with maximum characters
    return max(reviews, key=len)


# -------------------------------------
# Function to display reviews
# containing a keyword
# -------------------------------------
def reviews_with_keyword(reviews, keyword):

    print("Reviews containing", keyword)

    # Check each review
    for review in reviews:

        if keyword in review:
            print(review)


# =====================================
# Main Program
# =====================================

# Get sentiment counts
excellent, good, average, poor = count_sentiments(reviews)

print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

# Most common word
print("\nMost Common Word:")
print(most_common_word(reviews))

# Longest review
print("\nLongest Review:")
print(longest_review(reviews))

print()

# Reviews containing keyword
reviews_with_keyword(reviews, "excellent")