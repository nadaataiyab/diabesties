# Diabesties
## Predicting User Churn for a Digital Health App
### The Quick Summary
Diabesties is a mobile health app designed to help college students with Type 1 diabetes better manage their condition by tracking their blood glucose, insulin, and carbs and sharing their data with a friend or 'diabestie'. This project uses machine learning algorithms to predict user churn, which is defined as users that log their data less than ten times after the first week of use. 

### The Data
The exploratory data analysis yielded some interesting and sometimes suprising results:
* 70% of users were not college age. The median age was 37 
* 42% of users had Type II and not Type I diabetes
* The app was primarily used as a glucose tracker
* Having a diabestie did not seem to make a difference to churn (although it is possible that it did improve user outcomes)

### The Modeling and Results
I used a combination of demographic data (eg. age, ethnicity, diabetes type, etc.) and behavioral data (number of log entries, page views in app, etc.)

I ran 4 classifier models:
* Logistic Regression
* Random Forest
* Gradient Boosted Trees
* AdaBoost

Gradient Boosted Trees slightly outperformed the other models. 

![Model Scores](https://github.com/nadaataiyab/diabesties/blob/master/images/Galvanize_Capstone_Nadaa.025.jpeg)

Gradient Boosted Trees Model Scores:




### Conclusion
The model seemed to do a good job of predicting churn, but model performance was inflated by a heavy class imabalance. More work could be done in terms of feature engineering and tweaking the hyper-parameters to improve the ability to predict non-churn. 

### Technologies Used
* Python, Pandas, Numpy, MySQL, scikit-learn, matplotlib, seaborn, Jupyter Notebook

### View the slides and Live Presentation
[View the slide presentation of the analysis.](https://www.slideshare.net/secret/7XXDeLkAWWXyWC)

View the narrated slide presentation - COMING SOON!

[View the live presentation at Galvanize in Phoenix, AZ, on October 5th, 2017.](https://youtu.be/6jJtakvCEqA)

### About Diabesties
Diabesties was built by Ayogo, a Canadian digital health app developer, in partnership with the College Diabetes Network. The app was available in the iPhone app store from 2012-2015. This project was completed as a capstone project for the Galvanize Data Science Immersive program in Phoenix, AZ. 
