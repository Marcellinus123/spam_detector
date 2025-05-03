import mysql.connector
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class SpamDetector:
    """
    A spam detection system that connects to MySQL for training data
    and uses logistic regression for classification.
    """
    
    def __init__(self, host='localhost', user='root', password='', database='spam_detector'):
        """
        Initialize the spam detector with database connection parameters.
        
        Args:
            host (str): MySQL host
            user (str): MySQL username
            password (str): MySQL password
            database (str): Database name
        """
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = LogisticRegression()
        
    def load_data(self):
        """Load training data from MySQL database."""
        self.cursor.execute("SELECT message, label FROM spam_training_data")
        data = self.cursor.fetchall()
        return pd.DataFrame(data, columns=['message', 'label'])
    
    def train(self):
        """Train the spam detection model."""
        df = self.load_data()
        X = self.vectorizer.fit_transform(df['message'])
        y = df['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        
    def predict(self, msg):
        """
        Predict whether a message is spam or not.
        
        Args:
            msg (str): Message to classify
            
        Returns:
            str: 'Spam' or 'Not Spam'
        """
        vec = self.vectorizer.transform([msg])
        pred = self.model.predict(vec)
        return 'Spam' if pred[0] == 1 else 'Not Spam'
    
    def close(self):
        """Close database connection."""
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    # Example usage
    detector = SpamDetector()
    detector.train()
    
    test_messages = [
        "Free vacation to Bahamas! Click here to book.",
        "Hi there, I'm following up on our last conversation.",
        "Win cash instantly, limited time!"
    ]
    
    for msg in test_messages:
        print(f"> {msg}")
        print(f"Prediction: {detector.predict(msg)}\n")
    
    detector.close()
  
