# Diabesties
## Predicting User Churn for a Digital Health App
#### The Quick Summary
Diabesties is a mobile health app designed to help college students with Type 1 diabetes better manage their condition by tracking their blood glucose, insulin, and carbs and sharing their data with a friend or 'diabestie'. I ran machine learning algorithms on data representing user demographics and their usage patterns within the app, to predict user churn. ('Churned' users are those that stop engaging with the app after a defined period of time.) This work was completed as my capstone project for the [Galvanize Data Science bootcamp](https://www.galvanize.com/phoenix/data-science) in Phoenix, AZ. 

* [Slides](https://www.slideshare.net/secret/7XXDeLkAWWXyWC)  
* [Live Presentation](https://youtu.be/6jJtakvCEqA)  
* Narrated Slides - COMING SOON!

#### The Data
The data included ~3,000 users who had made a total of ~50,000 log entries and ~400,000 clicks in the app over a three year period (2012-2015). The exploratory data analysis yielded some surprising results:
* 70% of users were not college age. The median age was 37. 
* 42% of users had Type II and not Type I diabetes. 
* The app was primarily used as a glucose tracker.
* Having a diabestie did not seem to make a difference to churn (although it is possible that it did improve user outcomes).

#### The Modeling and Results
I used 23 features to run my models, including demographic data (eg. age, ethnicity, diabetes type, etc.) and behavioral data (number of log entries, page views in app, etc.)

I ran 4 classifier models and plotted their [ROC curves](https://github.com/nadaataiyab/diabesties/blob/master/images/Galvanize_Capstone_Nadaa.024.jpeg). Their respective AUC (Area Under the Curve) measures are listed below:
* Logistic Regression              0.89
* Random Forest                    0.88
* Gradient Boosted Trees           0.91
* AdaBoost                         0.89

Gradient Boosted Trees had a slightly higher AUC versus the other models and produced the following scores:
* Accuracy:       94%
* Precision:      95%
* Recall:         98%

*Accuracy: total number of correctly labeled samples; Precision: 95% of the samples labeled as churn really did churn; Recall: 98% of samples that churned were labeled as churn - only 2% 'got away' and were labeled as 'not churn.'

The model did well at predicting churn, but it performed poorly at predicting non-churn. In the test data, the non-churn class was only 10% of the total observations. Only about 50% of the non-churn class was correctly labeled.  

According to the feature importance analysis produced by the Random Forest algorithm, the following features had the highest predictive power:
1. Number of page views in the first week
2. Number foo
3. Age
4. ...
5. ....

### Conclusion
The model seemed to do a good job of predicting churn, but model performance was inflated by a heavy class imabalance. More work could be done in terms of feature engineering and tweaking the hyper-parameters to improve the ability to predict non-churn. Behavioral data appears to have more predictive power than demographic data. 

### Technologies Used
* Python, Pandas, Numpy, MySQL, scikit-learn, matplotlib, seaborn, Jupyter Notebook

### About Diabesties
Diabesties was built by (Ayogo)[http://ayogo.com/], a Canadian digital health app developer, in partnership with the (College Diabetes Network)[https://collegediabetesnetwork.org/content/diabesties-iphone-application-release]. The app was available in the iPhone app store from 2012-2015. 
