# CyberDect - Cyberbullying-tweet-prediction system
It predicts the nature of the tweet into 6 Categories.

* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

## Tools and Technologies  
**Model:** Used linear Support Vector Machine to classify tweets.    

## Methodology
* Downloaded the data from kaggle. [(data)](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
* Performed some Exploratory Data Analysis to get the overview of data. [(initial_modelling.ipynb)](initial_modelling.ipynb)
*  Created a Word Cloud from the data.
*  Performed the necessary steps for textual analysis.
    * Removing Stopwords, puctuations, URLs, etc
    * Performed Stemming and Lemmatization.
* Automated the process of preprocessing by creating functions. Which would be helpful in predicting Custom Outputs.
* https://aryam643.github.io/CyberDect/
   Created a basic website using html, css, javascript in which user enters the tweet and if it will contain cyberbullied data then it will provide you a pop up tha whether
   the enetered text is cyberbullied or not.

## References
* Twitter Sentiment Analysis- A NLP Use-Case for Beginners - [https://www.analyticsvidhya.com/blog/2021/06/twitter-sentiment-analysis-a-nlp-use-case-for-beginners/](https://www.analyticsvidhya.com/blog/2021/06/twitter-sentiment-analysis-a-nlp-use-case-for-beginners/)
