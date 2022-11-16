from transformers import pipeline, RobertaTokenizerFast, TFRobertaForSequenceClassification

class Emotion_detector:
    def __init__(self):
        self.tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
        self.model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

        self.emotion_model = pipeline("text-classification", model="arpanghoshal/EmoRoBERTa", return_all_scores=True)

    def assess_emotions(self, corpus):
        return self.emotion_model(corpus)