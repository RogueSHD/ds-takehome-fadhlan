# ds-assessment - 1 answer

1. **SQL Task:**
   You have a table `events` with:

   * `user_id` (STRING)
   * `event_type` (STRING)
   * `event_timestamp` (TIMESTAMP)

   **Write a query to find the number of unique users who triggered both a `signup` and a `purchase` event within 7 days.**

   **Answer:** 

    WITH signups AS (
    SELECT user_id, event_timestamp AS signup_time
    FROM events
    WHERE event_type = 'signup'
),
    purchases AS (
    SELECT user_id, event_timestamp AS purchase_time
    FROM events
    WHERE event_type = 'purchase'
)
    SELECT COUNT(DISTINCT s.user_id) AS num_users
    FROM signups s
    JOIN purchases p
    ON s.user_id = p.user_id
    AND p.purchase_time BETWEEN s.signup_time AND DATEADD(day, 7, s.signup_time)

    Step 1: The query defines a signups temporary table (CTE) that selects all user sign-up events, recording their sign-up time.

    Step 2: It defines a purchases temporary table (CTE) that selects all user purchase events, recording their purchase time.

    Step 3: It joins these two tables on user_id, and further filters for purchase events that occurred between the user’s sign-up time and 7 days after sign-up.

    Step 4: It counts the distinct number of users who meet these criteria.

2. **Exploratory Analysis:**
   **Given a dataset with customer transactions, how would you identify:**

   *High-value customers?
   *Seasonality trends?

    **Answer 1: High value customers, based on the dataset given high value customers is customers who spend more, below is how to derive high value customers using sql**

       SELECT 
           member_id, 
           SUM(spend_amount) AS total_spend,
           COUNT(*) AS num_transactions,
           MAX(timestamp) AS last_purchase
       FROM 
           transactions
       GROUP BY 
           member_id
       ORDER BY 
           total_spend DESC


    **Answer 2: Seasonality trend is where we notice that certain events or data points increase or decrease during certain times: below is how i query the table to find seasonality trends**

       SELECT 
           DATEPART(year, timestamp) AS year,
           DATEPART(month, timestamp) AS month,
           SUM(spend_amount) AS total_monthly_spend,
           COUNT(*) AS transaction_count
       FROM 
           transactions
       GROUP BY 
           DATEPART(year, timestamp), DATEPART(month, timestamp)
       ORDER BY 
           year, month


3. **Python Task:**
   You're given a dataset with features: `user_id`, `last_login_days_ago`, `num_purchases`, `avg_purchase_value`, and a binary target `churned`.

   * Write Python code to prepare this data for a logistic regression model.
   * Briefly explain how you'd evaluate the model performance.

         **For this part i created a sample data for the above features about 2000 rows for testing called "churn_dataset.csv"**

         **Answer can be found in ds-assessment-1.py file that i have created along the explaination as well :)**

4. **Machine Learning:**
   You are asked to build a customer segmentation model.

   * Which algorithm(s) would you use and why?
   * What preprocessing would you do before modeling?

   Answer 1:

         1. Algorithms to Use

             For customer segmentation (where the goal is to group customers by similar behaviors or characteristics, and you usually do not have a target label), you use unsupervised learning algorithms, most commonly:

             a. K-Means Clustering
             Why: Simple, scalable, and works well when you expect well-separated groups.

             How: Assigns each customer to a cluster so that customers in the same cluster are similar.

             b. Hierarchical Clustering
             Why: Good for smaller datasets and to visualize nested groupings (dendrograms).

             How: Builds a tree of clusters based on distance metrics.

             c. DBSCAN
             Why: Useful if clusters are of uneven shape/density and to detect outliers.

             How: Groups points that are closely packed together, marking outliers as noise.
   

    Answer 2:

    2. Preprocessing Steps

        a. Data Cleaning

            -Handle missing values (impute or drop).

            -Remove duplicate records.

            -Ensure relevant columns (drop irrelevant ones like user IDs).

        b. Feature Engineering

            -Aggregate transactional data (e.g., total spend, purchase frequency).

            -Create RFM features: Recency, Frequency, etc

        c. Encoding Categorical Variables

            -Convert categorical features (e.g., tier, region) to numerical using one-hot encoding or label encoding.

        d. Feature Scaling

            -Scale features (standardization or normalization). K-Means and most clustering algorithms are sensitive to scale.

        e. Outlier Detection and Removal

            -Outliers can skew clusters; consider removing them

5. **Business Case:**
   A product team wants to understand what factors lead to user conversion (first purchase).

   * What approach would you take to analyze this?
   * How would you explain your findings to a non-technical stakeholder?

   Answer 1:

          Step 1: Define “Conversion”
          Conversion = User makes their first purchase.

          Step 2: Prepare the Dataset
          Target variable: Binary (converted=1 if user made a purchase, otherwise 0).

          Features: User demographics, engagement data, signup channel, app usage, etc.

          Step 3: Exploratory Data Analysis
          Compare features between converted and non-converted users (e.g., average age, app opens, sign-up source).

          Visualize: Bar charts, distributions, etc.

          Step 4: Statistical Analysis or Predictive Modeling
          Use Logistic Regression (or other classification models) to model the probability of conversion.

          Look for significant predictors (e.g., age, location, number of app opens, etc.).

          Check feature importance (how much each feature influences this conversion).

          Step 5: Validate Findings
          Test the model on holdout data.

          Use metrics like AUC, accuracy, or lift.

    Answer 2:

          1- Use plain language, not technical terms.

          2- Explain in analogical terms : for example EDA, what is EDA? It is more like getting to know more about your     data and discover any insights or etc same goes to people if we want to know more about the person we need to know his/her background to truly                understands them

          3- Show visuals: e.g., “Users with more logins have a higher conversion rate” (show a bar chart).

          4- Highlight actionable insights:

             - “Encouraging new users to open the app more frequently may increase conversion.”

             - “Referral programs are effective at driving conversions.”

# ds-case-study - 2 answer

# Answer can be founf in ds-case-study-2.ipynb inside notebook folder

