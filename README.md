# name_classifier
For a given name, predict the expected gender of the person (using nltk)

# Background
Originated from assignment from NLP class - to build the best name gender classifier possible. First, I did some research on how this problem would typically be approached from a non-programming perspective. Most of the top results returned on Google were of other aspiring data scientists working through the same exercise. After some further digging, here's what I found:

* 
https://www.scientificamerican.com/article/the-inherent-gender-of-names/
* background on naming practices in other cultures and regions, with examples
https://www.fbiic.gov/public/2008/nov/Naming_practice_guide_UK_2006.pdf
* provides more background knowledge on naming patterns based on sound, endings, etc.
https://debuk.wordpress.com/2015/08/22/girls-called-jack-and-boys-named-sue/
* https://www.quora.com/What-is-the-secret-to-distinguish-whether-any-name-is-masculine-or-feminine?no_redirect=1
* https://gender-gap-in-science.org/2018/07/16/telling-the-gender-from-a-name/
# Examining the Dataset
* contains many unique entries, variations of the same name in terms of spelling and syllables (short vs long versions) 
* developed in 1990s, no description of methodology on how/where names were obtained from

* SSA Baby Names Dataset - contains name, frequency, gender for each year since 1880.
 https://www.ssa.gov/oact/babynames/limits.html
 
 # Requirements
 * use Naive Bayes Classifier
 * use Names Corpus from nltk 
 * test set of 500 names
 * dev-test set of 500 names
 * training set of remainder (6900 names)
 * check final performance on test set
 
 # Design Considerations
 * determine what features to use
 * use stemming on the names to get name prefix/suffixes and map that to frequency
 * using Naive Bayes classifier to determine/count syllables
 http://www.sociology-hacks.org/?p=128
 
 # Code Flow
 * create dev-test and test sets by setting aside 500 names each at random, from combined list of names
 
* https://tekeli.li/onomastikon/England-Firstnames/Coinages/Suffix.html
