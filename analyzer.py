import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = positives
        self.negatives = negatives        
        self.positive_list =[]
        self.negative_list =[]

        with open(self.positives, 'r') as lines:
            for line in lines:
                if not line.startswith(';'):
                    self.positive_list.append(line.strip('\n'))
        self.positive_list.pop(0)
                
        with open(self.negatives, 'r') as lines:
            for line in lines:
                if not line.startswith(';'):
                    self.negative_list.append(line.strip('\n'))
        self.negative_list.pop(0)

    def analyze(self, text):
        self.text = text
        self.score = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(self.text)
        
        for word in tokens:
            if word.lower() in self.positive_list:
                self.score += 1
            elif word.lower() in self.negative_list:
                self.score  += -1
            else:
                self.score += 0
            
        return self.score
