# NLP Sentiment Analysis with Flask

This project is an implementation of NLP sentiment analysis using Flask for the API. The model analyzes text input and outputs sentiment scores indicating positive or negative sentiment.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Introduction

This project demonstrates sentiment analysis using Natural Language Processing (NLP). It processes input text and predicts whether the sentiment is positive or negative. The application is built using Flask, and the API can be run locally. The project also includes a user interface for easy interaction.

## Features

- Sentiment analysis of text input
- Simple and intuitive API
- Lightweight Flask application
- JSON-based API responses
- User interface for sentiment prediction using HTML and CSS

## Technologies Used

- Python
- Jupyter Notebook
- Flask
- Natural Language Toolkit (NLTK)
- Scikit-learn
- HTML/CSS

## Dataset

- Download data from [Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    ```
2. **Navigate to the project directory:**
    ```sh
    cd your-repo-name
    ```
3. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask app:**
    ```sh
    python app.py
    ```
2. **Access the API:**
    Open your web browser or API client and navigate to `http://127.0.0.1:5000/`.

3. **User Interface:**
    After running `app.py` and navigating to the provided link, a template file will be executed that takes you to the user interface created using HTML and CSS. Here, you can input your statement, and upon clicking the "Predict" button, you will receive the sentiment analysis output directly on the page.

## API Endpoints

- **`/predict`**: Accepts text input and returns the sentiment score (positive or negative).

