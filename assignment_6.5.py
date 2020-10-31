text = "X-DSPAM-Confidence:    0.8475"
k = text[text.find('0'):text.find('5')+1]
print(float(k))
