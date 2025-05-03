# Spam Detector Project
This is a Python-based spam detection system that uses machine learning to classify messages as spam or not spam (ham). 
The system connects to a MySQL database for training data, uses TF-IDF vectorization for text processing, and employs logistic regression for classification.

![Spam Detector Image](https://www.marcbrain.com/images/detector.jpg)



# Table of Contents
    Features

    Requirements

    Installation

    Database Setup

    Usage

    API Documentation

    Training Data

    Testing

    Contributing

    License

# Features

    MySQL database integration for storing and retrieving training data

    TF-IDF vectorization for text feature extraction

    Logistic Regression classifier for spam detection

    Simple prediction function for classifying new messages

    Example test cases included

# Requirements

    Python 3.6+

    MySQL Server

    Python packages:

        mysql-connector-python

        pandas

        scikit-learn
  # Installation
1. Clone the repository:

git clone https://github.com/marcellinus123/spam-detector.git
cd spam-detector

2. Install the required Python packages:

pip install mysql-connector-python pandas scikit-learn

3. Set up your MySQL database ( Link: [see Database Setup](https://dev.mysql.com/doc/mysql-getting-started/en/) )

# Database Setup
1. Create a MySQL database named spam_detector:
   CREATE DATABASE spam_detector;
   
2. Create a table for training data:
   USE spam_detector;

CREATE TABLE spam_training_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    label INT NOT NULL COMMENT '0 for ham, 1 for spam'
);

3. Insert some sample training data:
   INSERT INTO spam_training_data (message, label) VALUES
('Free vacation to Bahamas! Click here to book.', 1),
('Hi there, I''m following up on our last conversation.', 0),
('Win cash instantly, limited time!', 1),
('Meeting reminder: Tomorrow at 2pm in conference room', 0),
('You''ve won a free iPhone! Claim now!', 1),
('Hi John, just checking in about the project', 0);

# Usage
1. Configure the database connection in the script by modifying these lines:
conn = mysql.connector.connect(
    host='localhost',
    user='root',         # your MySQL username
    password='',         # your MySQL password
    database='spam_detector'
)

2. Run the script:
   python spam_detector.py

3. The script will:

    Connect to the MySQL database

    Fetch training data

    Train the model

    Run test predictions on sample messages



# API Documentation

predict_message(msg)

Classifies a given message as spam or not spam.

**Parameters:**

    msg (str): The message to classify

**Returns:**

    str: 'Spam' or 'Not Spam'

**Example:**

prediction = predict_message("Free vacation offer!")
print(prediction)  # Output: 'Spam'


# Training Data
Training Data

The model expects training data in the following format stored in a MySQL table called spam_training_data:

| Column | Type | Description |
|--------|------|-------------|
| message | TEXT | The text message to learn |
| label   | INT  | 0 for ham, 1 for spam |

To improve accuracy, add more diverse examples of both spam and ham messages to your training data.


# Testing

The script includes some test cases that run when executed directly:

    test_messages = [ "Free vacation to Bahamas! Click here to book.",
    "Hi there, I'm following up on our last conversation.",
    "Win cash instantly, limited time!" 
    ]

**To add your own tests, modify this section or create a separate test file.
Contributing** 

**Contributions are welcome! Here's how:**

    Fork the project

    Create your feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some amazing feature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

# License
**Distributed under the MIT License. See LICENSE for more information.**






















The model expects training data in the following format stored in a MySQL table called spam_training_data:




  
