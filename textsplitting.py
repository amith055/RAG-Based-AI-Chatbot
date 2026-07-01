text = """Data Science & AI Mastery Syllabus 
Phase 1: The Foundations (Weeks 1–6) 
Module 1: Python Programming Fundamentals and Flow Control (Weeks 1-3) 
• Core Syntax & Variables: Variable assignment, naming conventions, and basic math 
operators. 
• Primitive Data Types: Integers (int), decimals (float), text (str), and booleans 
(True/False). 
• String Manipulation: Slicing, methods (.upper(), .replace(), .split()), and f-strings. 
• Data Structures: * Lists (ordered, mutable). 
o Dictionaries (key-value pairs). 
o Tuples (ordered, immutable). 
o Sets (unique values, intersections). 
• Control Flow (Logic): Comparison/logical operators, and if, elif, else statements. 
• Loops: for loops and while loops for iteration. 
• Functions: def keyword, arguments/parameters, local vs. global scope, and return 
statements. 
Module 2: The Data Handling Toolkit NumPy and Pandas (Weeks 4-6) 
• NumPy Basics: Creating ndarrays, multidimensional arrays, and array broadcasting. 
• Pandas Core Objects: Series (1D) vs. DataFrame (2D). 
• Importing/Inspecting Data: pd.read_csv(), .head(), .info(), and .describe(). 
• Data Cleaning: Handling missing data with .isna(), .dropna(), and .fillna(). 
• Data Manipulation: Boolean indexing (filtering), aggregating with .groupby(), and 
combining datasets via .merge() and .concat(). 
Phase 2: The Analytical Mindset (Weeks 7–10) 
Module 3: Statistical Thinking, Data Prep, and ML Workflow (Weeks 7-10) 
• Descriptive Statistics: Mean, median, mode, variance, standard deviation, and 
percentiles. 
• Data Distribution: Normal distributions vs. skewed data. 
• Data Visualization: * Matplotlib (line charts, scatter plots, histograms). 
o Seaborn (boxplots, correlation heatmaps). 
• Feature Engineering/Scaling: One-Hot Encoding for categories, Min-Max 
Normalization, and Z-score Standardization (StandardScaler). 
• The ML Pipeline: Defining features (X) and targets (y). 
• Data Splitting: Using train_test_split for training, validation, and testing sets. 
Phase 3: Machine Learning Mastery (Weeks 11–20) 
Module 4: Core Supervised Learning: Regression and Classification (Weeks 11-15) 
• Supervised Learning: Regression (predicting numbers) vs. Classification (predicting 
categories). 
• Regression Algorithms: Simple and Multiple Linear Regression math and intuition. 
• Regression Metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean 
Squared Error (RMSE), and R-squared. 
• Classification Algorithms: Logistic Regression (Sigmoid curve) and Decision Trees. 
• Classification Metrics: Confusion Matrix, Accuracy, Precision, Recall, and F1-Score. 
Module 5: Advanced ML concepts and Unsupervised Learning (Weeks 16-20) 
• Model Robustness: Overfitting vs. Underfitting and the Bias-Variance Trade-off. 
• Cross-Validation: K-Fold Cross Validation. 
• Ensemble Methods: Bagging vs. Boosting, Random Forests, and Gradient Boosting 
(e.g., XGBoost). 
• Hyperparameter Tuning: Grid Search (GridSearchCV). 
• Unsupervised Learning: Working with unlabeled data. 
• Clustering: K-Means algorithm, centroids, and the "Elbow Method." 
Phase 4: The Modern AI Frontier (Weeks 21–26) 
Module 6: Advanced Generative AI Concepts and Tools (Weeks 21-24) 
• Foundation Models: LLM architecture basics and differences between GPT, Gemini, 
and Llama. 
• Prompt Engineering: Zero-shot, Few-shot, Chain-of-Thought (CoT), and system 
instructions. 
• Embeddings & Vector Databases: Text embeddings, Cosine Similarity, and Vector DBs 
(Chroma, Pinecone). 
• RAG (Retrieval-Augmented Generation): Grounding LLMs in private documents. 
• AI Agents: Tool-usage frameworks (LangChain, LlamaIndex) and multi-step planning. 
Module 7: Capstone Project and Final Presentation (Weeks 25-26) 
• Project Scoping: Translating a business problem into a data science problem. 
• End-to-End Execution: Building the full pipeline from data sourcing to model 
evaluation. 
• Version Control: Git/GitHub basics for portfolio hosting. 
• Storytelling with Data: Presenting technical metrics as actionable business insights."""


from langchain_text_splitters import RecursiveCharacterTextSplitter 
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 200
)
chunks = splitter.split_text(text)
print(*chunks)