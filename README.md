# Quotes Recommendation Chatbot using Rasa NLP

## Project Overview
The Quotes Recommendation Chatbot is an AI-powered conversational system that provides motivational, inspirational, humorous, and emotional quotes based on user input. The chatbot understands the user’s intent using Natural Language Processing (NLP) and delivers relevant quotes through an interactive chat interface.

The system helps users improve their mood, gain motivation, and receive emotional encouragement through meaningful quotes.

This chatbot is built using **Rasa NLP**, **Python**, and a **Flask-based web interface**.

---

## Features

- Intent recognition using Natural Language Processing
- Multiple quote categories
- Interactive chatbot conversation
- User feedback handling (Yes / No)
- Unlimited quote recommendations
- Web-based chatbot interface
- Custom action logic using Rasa SDK

---

## Quote Categories Supported

The chatbot supports the following categories:

- Motivation
- Inspiration
- Love
- Success
- Funny
- Life
- Happiness
- Friendship
- Dreams
- Morning
- Attitude
- Spiritual
- Sad / Emotional Support
- Relax / Tired

---

## Technology Stack

- Rasa NLP
- Python
- Flask
- HTML
- CSS
- JavaScript

---

## Project Structure
# Quotes Recommendation Chatbot using Rasa NLP

## Project Overview
The Quotes Recommendation Chatbot is an AI-powered conversational system that provides motivational, inspirational, humorous, and emotional quotes based on user input. The chatbot understands the user’s intent using Natural Language Processing (NLP) and delivers relevant quotes through an interactive chat interface.

The system helps users improve their mood, gain motivation, and receive emotional encouragement through meaningful quotes.

This chatbot is built using **Rasa NLP**, **Python**, and a **Flask-based web interface**.

---

## Features

- Intent recognition using Natural Language Processing
- Multiple quote categories
- Interactive chatbot conversation
- User feedback handling (Yes / No)
- Unlimited quote recommendations
- Web-based chatbot interface
- Custom action logic using Rasa SDK

---

## Quote Categories Supported

The chatbot supports the following categories:

- Motivation
- Inspiration
- Love
- Success
- Funny
- Life
- Happiness
- Friendship
- Dreams
- Morning
- Attitude
- Spiritual
- Sad / Emotional Support
- Relax / Tired

---

## Technology Stack

- Rasa NLP
- Python
- Flask
- HTML
- CSS
- JavaScript

---

## Project Structure
quotes-recommendation-chatbot-nlp
│
├── actions/
│ └── actions.py
│
├── data/
│ ├── nlu.yml
│ ├── stories.yml
│ └── rules.yml
│
├── static/
│ ├── style.css
│ └── script.js
│
├── templates/
│ └── index.html
│
├── models/
│
├── docs/
│ ├── Business_Problem.pdf
│ ├── Business_Requirements.pdf
│ ├── Literature_Review.pdf
│ └── Social_Impact.pdf
│
├── app.py
├── domain.yml
├── endpoints.yml
├── config.yml
└── README.md



---

## How the Chatbot Works

1. User enters a message in the chatbot interface.
2. Rasa NLU analyzes the message and detects the **intent**.
3. The chatbot identifies the **quote category**.
4. A custom action selects a quote from the category.
5. The bot displays the quote and asks for feedback.
6. If the user says **No**, another quote from the same category is provided.

---

## Installation


---

### step 1 : Clone the Repository

```bash
git clone https://github.com/yourusername/quotes-recommendation-chatbot-nlp.git
```

## Running the Project

### Step 2: Navigate to Project Folder
```bash
cd quotes-recommendation-chatbot-nlp
```

### Step 3: Activate Conda Environment
```bash

conda activate chatbot
```

### Step 4: Train the Model
```bash

rasa train
```


## Running the Project

The project requires **three terminals**.

### Terminal 1 – Start Action Server
```bash

rasa run actions
```

### Terminal 2 – Start Rasa Server
```bash

rasa run --enable-api --cors "*"
```

### Terminal 3 – Run Web Interface
```bash

python app.py

```


## Open the Chatbot

Open your browser and go to:

http://127.0.0.1:5000

---
## Example Conversation

User: Hello  
Bot: Hello! I am your Quotes Recommendation Bot.

User: Motivate me  
Bot: Here is your motivation quote:  
"Believe you can and you're halfway there."

Bot: Did you like this quote?

User: No  
Bot: Here is another motivation quote:  
"The secret of getting ahead is getting started."

---
## Research Papers Used

1. Natural Language Processing for Conversational AI: Chatbots and Virtual Assistants  
   IEEE Conference – 2025

2. Designing and Implementing Conversational Intelligent Chat-bot Using NLP  
   International Journal – 2021

3. Quote Recommendation in Dialogue using Deep Neural Network  
   ACM SIGIR Conference – 2016

4. Mood-Based Quote Recommendation Using Deep Learning  
   COMSYS Conference – 2024

5. A Neural Network Approach to Quote Recommendation in Writings  
   ACM CIKM Conference – 2016

---
## Social Impact

The chatbot promotes emotional well-being by providing motivational and uplifting quotes instantly. It helps users cope with stress, improve mood, and maintain positivity through interactive conversations.

---
## Future Improvements

- Sentiment analysis for emotion detection
- Integration with mobile applications
- AI-based personalized quote recommendation
- Integration with voice assistants