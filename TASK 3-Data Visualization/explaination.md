# Task 3: Data Visualization

## Dataset
E-commerce customer reviews — 2500 rows, 12 columns covering products, brands, prices, ratings, and purchase behavior across 7 categories.

---

## Libraries Used
- **Pandas** — data loading and manipulation
- **Matplotlib** — base plotting
- **Seaborn** — statistical visualizations

---

## What I Analyzed

### 1. Rating Analysis
Looked at how ratings are spread across the dataset and whether they changed over time.

- **Overall Distribution** — Most reviews lean positive (4 and 5 stars dominate). Very few 1-star reviews, which is typical in e-commerce datasets.
- **Rating Trend Over Time** — Plotted monthly average rating to check if product quality or customer satisfaction shifted across 18 months.

---

### 2. Brand Insights
Compared all 10 brands across three metrics — popularity, quality, and pricing.

- **Most Popular Brands** — Measured by total review count. Some brands generate significantly more reviews than others.
- **5-Star Reviews by Brand** — Filtered only 5-star ratings to see which brand gets the most top ratings, not just the most reviews.
- **Brand-wise Average Rating** — Calculated mean rating per brand to find the most consistently well-rated one.
- **Brand-wise Average Price** — Compared pricing across brands to see if premium brands actually charge more.

---

### 3. Category Insights
Explored which product categories are most active and which offer the best deals.

- **Reviews by Category** — Electronics and Smartphones had the most reviews overall.
- **Category-wise Average Rating** — Some categories like Gaming had slightly higher average ratings than others.
- **Average Discount by Category** — Checked if certain categories run more aggressive discounts than others.

---

### 4. Price Analysis
Checked price distribution and whether higher-priced products earn better ratings.

- **Price Distribution** — Prices are fairly spread between ₹500 and ₹50,000 with no major skew.
- **Price vs Rating (Box Plot)** — No strong relationship found. Customers rate cheap and expensive products similarly, meaning price alone doesn't drive satisfaction.

---

### 5. Time-based Analysis
Looked at seasonal patterns in review volume across all 12 months.

- **Seasonal Pattern** — Some months had noticeably higher review counts, possibly tied to sales events or product launches.

---

### 6. Review Behavior
Focused on whether verified buyers behave differently from unverified ones.

- **Verified vs Non-Verified Count** — Around 85% of reviews came from verified purchases, which is realistic.
- **Verified Purchase vs Rating** — Verified buyers tend to give slightly more balanced ratings compared to non-verified reviewers.
- **Helpful Votes Distribution** — Most reviews have low helpful vote counts. A small number of reviews get a very high number of votes, showing a long-tail distribution.

---

## Key Takeaways

1. Ratings are heavily skewed toward 4 and 5 stars — common in real e-commerce data.
2. Brand popularity and rating quality don't always align — a brand can be popular but not highest rated.
3. Price doesn't guarantee satisfaction — expensive products aren't rated higher.
4. Verified buyers are more reliable reviewers and make up the majority of the dataset.
5. Review volume varies by month, hinting at seasonal buying behavior.

---

## Files
```
TASK 3-Data Visualization/
├── python.ipynb     ← main analysis notebook
├── ecommerce_reviews.csv
└── README.md
```