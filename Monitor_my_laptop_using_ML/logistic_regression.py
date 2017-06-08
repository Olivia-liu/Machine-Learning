import numpy as np  
import pandas as pd  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.linear_model.logistic import LogisticRegression  
from sklearn.cross_validation import train_test_split, cross_val_score  
  
df = pd.read_csv(r'C:\Users\Olivia\Desktop\Machine Learning\Machine-Learning\Monitor_my_laptop_using_ML\smsspamcollection\SMSSpamCollection', delimiter='\t', header=None)  
  
print (df.head())  
print ('spam text number:',df[df[0]== 'spam'][0].count())  
print ('ham text number:',df[df[0]== 'ham'][0].count())  

X_train_raw,X_test_raw,y_train,y_test = train_test_split(df[1],df[0])  
  
#用TF-IDF算法来抽取短信的特征向量  
vectorizer = TfidfVectorizer()  
X_train = vectorizer.fit_transform(X_train_raw)  
X_test = vectorizer.transform(X_test_raw)  

classifier = LogisticRegression()  
classifier.fit(X_train,y_train)  
predictions = classifier.predict(X_test)  

for i,predictions in enumerate(predictions[-5:]):  
    print ('Prediction type:%s. Information: %s' %(predictions,X_test_raw.iloc[i]))  
	
scores = cross_val_score(classifier, X_train, y_train, cv=5)  
print('Score:',np.mean(scores), scores)  