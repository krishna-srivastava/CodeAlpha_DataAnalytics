# Task 4: Sentiment Analysis

## Dataset
Same e-commerce reviews dataset — 2500 rows. Used the `Review_Text` column to classify customer sentiment using NLP.

---

## Libraries Used
- **TextBlob** — NLP library for polarity-based sentiment detection
- **Pandas** — data manipulation
- **Matplotlib & Seaborn** — visualization

---

## How It Works

TextBlob reads each review and returns a **polarity score** between -1 and +1:

```
Polarity > 0  →  Positive
Polarity < 0  →  Negative
Polarity = 0  →  Neutral
```

Applied this logic to every row using a custom function:

```python
def get_sentiment(review):
    polarity = TextBlob(review).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review_Text"].apply(get_sentiment)
```

---

## Results

| Sentiment | Count | Percentage |
|-----------|-------|------------|
| Positive  | ~2161 | 86.44% |
| Negative  | ~284  | 11.36% |
| Neutral   | ~55   | 2.20%  |

---

## Sample Predictions

**Positive Reviews detected correctly:**
```
"Amazing product! Exceeded my expectations."       → Positive ✅
"Outstanding quality! Will definitely buy again."  → Positive ✅
"Great quality and fast delivery. Very satisfied." → Positive ✅
```

**Negative Reviews detected correctly:**
```
"Broken on arrival. Very upset."        → Negative ✅
"Disappointing. Not as described."      → Negative ✅
"Poor quality. Waste of money."         → Negative ✅
```

**Neutral Reviews:**
```
"Satisfactory. Met my expectations."              → Neutral ✅
"It's decent. Nothing special but works fine."    → Neutral ✅
```

---

## Visualization

Plotted a bar chart showing **Sentiment Distribution** across all 2500 reviews. Positive reviews dominate, which aligns with typical e-commerce behavior where satisfied customers leave more reviews.

---

## Key Observations

1. **86% reviews are Positive** — customers are largely satisfied with products.
2. **Only 11% Negative** — complaints exist but are a minority.
3. **TextBlob vs Star Rating** — TextBlob marked 86% positive while actual 4-5 star ratings were 70%. This is a known TextBlob behavior where neutral-toned reviews get a slight positive polarity.
4. **Most negative reviews** mention words like "broken", "waste of money", "terrible", "disappointed" — strong negative language that TextBlob correctly identifies.
5. **Accessories and Gaming** categories had the most extreme sentiments — either very happy or very frustrated customers.

---

## Limitation

TextBlob is a **lexicon-based** model — it doesn't understand sarcasm or context. For example, "not bad" might get classified differently. For better accuracy, a trained ML model like VADER or BERT would work better, but for this internship task TextBlob gives solid results.

---