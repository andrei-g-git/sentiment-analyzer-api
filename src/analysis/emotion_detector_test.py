from transformers import pipeline, RobertaTokenizerFast, TFRobertaForSequenceClassification

class Emotion_detector_test:
    def __init__(self):

        self.tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
        self.model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

        self.emotion = pipeline("text-classification", model="arpanghoshal/EmoRoBERTa", return_all_scores=True)

    def test_emotions(self, corpus):
        emotion_labels = self.emotion(corpus)
        return emotion_labels
