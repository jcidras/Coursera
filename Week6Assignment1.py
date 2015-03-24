# Week 6 Assignment 1
sText = "X-DSPAM-Confidence:    0.8475";
sSlicedText = sText[sText.find("0"):len(sText)]
fNum = float(sSlicedText)
print fNum