import intentDetector as id

#Testing
text = "Can you help me?"
pred = id.predictions(text)
print("Intent Detected: "+ id.get_final_output(pred, id.unique_intent))
