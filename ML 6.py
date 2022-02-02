#!/usr/bin/env python
# coding: utf-8

# # MACHINE LEARNING 6

# ## 1. In the sense of machine learning, what is a model? What is the best way to train a model?

# In[ ]:


# A model represents what was learned by a machine learning algorithm. The model is the “thing” that is saved after
# running a machine learning algorithm on training data and represents the rules, numbers, and any other algorithm-
# specific data structures required to make predictions


# ## 2. In the sense of machine learning, explain the &quot;No Free Lunch&quot; theorem.

# In[1]:


# The No Free Lunch Theorem (NFLT) is named after the phrase, there ain't no such thing as a free lunch.
# In the “no free lunch” metaphor, each “restaurant” (problem-solving procedure) has a “menu” associating each 
# “lunch plate” (problem) with a “price” (the performance of the procedure in solving the problem).


# ## 3. Describe the K-fold cross-validation mechanism in detail.

# In[2]:


# Cross-validation is a resampling procedure used to evaluate machine learning models on a limited data sample.
# The procedure has a single parameter called k that refers to the number of groups that a given data sample is to
# be split into. Take the group as a hold out or test data set


# ## 4. Describe the bootstrap sampling method. What is the aim of it?

# In[3]:


# Bootstrapping is a statistical procedure that resamples a single dataset to create many simulated samples. 
# This process allows you to calculate standard errors, construct confidence intervals, and perform hypothesis 
# testing for numerous types of sample statistics.


# ## 5. What is the significance of calculating the Kappa value for a classification model? Demonstrate how to measure the Kappa value of a classification model using a sample collection of results.

# In[4]:


# It basically tells you how much better your classifier is performing over the performance of a classifier that 
# simply guesses at random according to the frequency of each class. Cohen's kappa is always less than or equal to 
# 1. Values of 0 or less, indicate that the classifier is useless.


# ## 6. Describe the model ensemble method. In machine learning, what part does it play?

# In[5]:


# Ensemble methods is a machine learning technique that combines several base models in order to produce one
# optimal predictive model . To better understand this definition lets take a step back into ultimate goal of
# machine learning and model building


# ## 7. What is a descriptive model&#39;s main purpose? Give examples of real-world problems that descriptive models were used to solve.

# In[ ]:


# Descriptive modeling is a mathematical process that describes real-world events and the relationships between 
# factors responsible for them. The process is used by consumer-driven organizations to help them target their 
# marketing and advertising efforts.


# ## 8. Describe how to evaluate a linear regression model.

# In[ ]:


# R Square/Adjusted R Square.
# Mean Square Error(MSE)/Root Mean Square Error(RMSE)
# Mean Absolute Error(MAE)


# ## 9. Distinguish :
# ## 1. Descriptive vs. predictive models
# ## 2. Underfitting vs. overfitting the model
# ## 3. Bootstrapping vs. cross-validation

# In[ ]:


# A descriptive model will exploit the past data that are stored in databases and provide you with the accurate 
# report. In a Predictive model, it identifies patterns found in past and transactional data to find risks and 
# future outcomes.

# Your model is underfitting the training data when the model performs poorly on the training data. Your model is 
# overfitting your training data when you see that the model performs well on the training data but does not
# perform well on the evaluation data.

# Cross validation splits the available dataset to create multiple datasets, and Bootstrapping method uses the 
# original dataset to create multiple datasets after resampling with replacement.


# ## 10. Make quick notes on:
# 
# ## 1. LOOCV.
# 
# ## 2. F-measurement
# 
# ## 3. The width of the silhouette

# In[ ]:


# The Leave-One-Out Cross-Validation, or LOOCV, procedure is used to estimate the performance of machine learning 
# algorithms when they are used to make predictions on data not used to train the model.

# Fbeta-measure is a configurable single-score metric for evaluating a binary classification model based on the 
# predictions made for the positive class. The Fbeta-measure is calculated using precision and recall. Precision
# is a metric that calculates the percentage of correct predictions for the positive class

# Silhouette width (SW) of a cell i is the distance of cell i from all of the cells within the same cluster 
# subtracted by the distance of cell i from cells in a nearest but different cluster, normalized by the maximum 
# of these two values

