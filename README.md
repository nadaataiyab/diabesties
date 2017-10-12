# Diabesties
## Predicting User Churn for a Digital Health App
### Quick Summary
Diabesties is a mobile health app designed to help college students with Type 1 diabetes manage their condition by tracking their blood glucose, insulin, and carbs and sharing that data with a friend or 'diabestie'.  In this project, I used machine learning algorithms to predict user churn. 'Churned' users are those that stop engaging with the app after a defined period of time. This work was completed as my capstone project for the [Galvanize Data Science bootcamp](https://www.galvanize.com/phoenix/data-science) in Phoenix, AZ. 

* [Slides](https://www.slideshare.net/secret/7XXDeLkAWWXyWC)  
* [Live Presentation](https://youtu.be/6jJtakvCEqA)  
* Narrated Slides - COMING SOON!

### Data
The data included ~3,000 users who had made a total of ~50,000 log entries and ~400,000 clicks in the app over a three year period (2012-2015). The exploratory data analysis yielded surprising results:
* 70% of users were not college age. The median age was 37. 
* 42% of users had Type II and not Type I diabetes. 
* The app was primarily used as a glucose tracker.
* Having a diabestie did not appear to impact churn rates (although it is possible that it did improve user outcomes).

### Churn Definition
I defined churn as a user who logged less than ten additional times after the first week of use, because I was interested in identifying the users that were truly engaged and committed to tracking their data. 

### Modeling and Results
I used 23 features to run my models, including demographic data (eg. age, ethnicity, diabetes type, etc.) and behavioral data (number of log entries, page views, etc.). 

I ran 4 classifier models and plotted their [ROC curves](https://github.com/nadaataiyab/diabesties/blob/master/images/Galvanize_Capstone_Nadaa.024.jpeg). Their respective AUC (Area Under the Curve) measures are listed below:
* Logistic Regression              0.89
* Random Forest                    0.88
* Gradient Boosted Trees           0.91
* AdaBoost                         0.89

Gradient Boosted Trees produced the highest AUC and the following scores:
* Accuracy:       94% labeled correctly
* Precision:      95% labeled as churn actually churned (5% were wrongly labeled as churn)
* Recall:         98% that actually churned were labeled as churn (2% of churn users were labeled as non-churn)

The non-churn class comprised only 10% of the total observations and was only correctly labeled as non-churn ~50% of the time.  

### Feature Importance
According to the feature importance analysis produced by the Random Forest algorithm, the following features had the highest predictive power. All behavioral data was based on the first week of use:
1. num page views (behavioral)
2. num log entries (behavioral)
3. age (demographic)
4. num notes entered (behavioral)
5. num moods entered (behavioral)

### Conclusion
The model did a good job of predicting churn, but model performance was inflated by a heavy class imabalance. More work could be done in terms of feature engineering and tweaking the hyper-parameters to improve the ability to predict non-churn. Behavioral data appears to have more predictive power than demographic data. Many of the app's users were different from the intended target market. 

### Technologies Used
* Python, Pandas, Numpy, MySQL, scikit-learn, matplotlib, seaborn

### Code and Notebook
* [Python scripts](https://github.com/nadaataiyab/diabesties/tree/master/src)
* [Jupyter notebook](https://github.com/nadaataiyab/diabesties/blob/master/diabesties_analysis.ipynb)

### About Diabesties
Diabesties was built by [Ayogo](http://ayogo.com/), a Canadian digital health app developer, in partnership with the [College Diabetes Network](https://collegediabetesnetwork.org/content/diabesties-iphone-application-release). The app was available in the iPhone app store from 2012-2015. 
