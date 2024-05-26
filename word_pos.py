import spacy

nlp = spacy.load("en_core_web_sm")
text = "SpaCy একটি জনপ্রিয় প্রাকৃতিক ভাষা প্রক্রিয়াকরণ লাইব্রেরি।"
doc = nlp(text)

print("Original Text: ", text)
print("PoS Tagging Result:")
for token in doc:
	print(f"{token.text}: {token.pos_}")
