# Given
text = "X-DSPAM-Confidence:    0.8475"

# Solution
position = text.find("0")
number = float(text[position:])
print(number)
