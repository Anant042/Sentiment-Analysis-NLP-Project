from flask import Flask, request, render_template
import pickle
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')



stop_words = set(stopwords.words('english'))
app = Flask(__name__)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
      
        input_text = request.form['text']
      
        preprocessed_text = preprocess(input_text)
        vector_input = tfidf.transform([preprocessed_text])
        prediction = model.predict(vector_input)[0]
        sentiment = 'positive' if prediction == 1 else 'negative'
        return render_template('result.html', input_text=input_text, sentiment=sentiment)


ps = PorterStemmer()
def preprocess(content):
    text=re.sub('[^a-zA-z]'," ",content)
    text=text.lower()
    text=text.split()
    text=[ps.stem(word) for word in text if not word in stopwords.words('english')]
    text=" ".join(text)
    
    return text


if __name__ == '__main__':
    app.run(debug=True)
