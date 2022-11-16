from transformers import pipeline, RobertaTokenizerFast, TFRobertaForSequenceClassification

class Emotion_detector:
    def __init__(self):
        self.tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
        self.model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

        self.emotion_model = pipeline("text-classification", model="arpanghoshal/EmoRoBERTa", return_all_scores=True)

    def assess_emotions(self, corpus):
        rawResults = self.emotion_model(corpus)
        #return {k: v for dict in rawResults[0] for k, v in dict.items()} #{label: score for label, score in rawResults[0]}
        resutlsList = rawResults[0]
        emotionsDict = {}
        for dict in resutlsList:
            emotionsDict[dict["label"]] = dict["score"]

        return emotionsDict