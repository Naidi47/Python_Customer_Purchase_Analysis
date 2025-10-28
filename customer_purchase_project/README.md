# 🐍 Customer Purchase Analysis using Python & Pandas  

## 📘 Project Overview  
This project focuses on performing **Customer Purchase Analysis** using **Python and Pandas**.  
It uses your uploaded dataset (`data/raw/dataset_original.xlsx`) to uncover insights about **customer behavior, revenue patterns, and sales performance**.  

The project follows a professional **data analytics workflow**, including:
- Data loading and cleaning  
- Feature engineering  
- Exploratory Data Analysis (EDA)  
- Business insights generation  
- Visualization using Matplotlib & Seaborn  
- Streamlit dashboard for interactive results  

---

## 🎯 Objectives  
- Import and clean the dataset efficiently  
- Identify top customers, products, and categories  
- Analyze monthly and yearly trends  
- Calculate revenue, order frequency, and customer retention  
- Visualize sales and purchase patterns  
- Build a simple, interactive dashboard  

---

## 🏗️ Project Structure  

```
customer_purchase_project_with_dataset/
├─ data/
│  ├─ raw/
│  │  ├─ dataset_original.xlsx         ← uploaded dataset
│  │  └─ dataset_preview.csv           ← sample preview
│  └─ processed/
│     └─ dataset_clean.csv             ← cleaned dataset
│
├─ src/
│  ├─ data_prep.py                     ← load & clean dataset
│  ├─ features.py                      ← create date & revenue features
│  ├─ analysis.py                      ← summary tables & insights
│  ├─ viz.py                           ← charts using matplotlib & seaborn
│  └─ app.py                           ← streamlit dashboard app
│
├─ reports/
│  └─ project_summary.md               ← written insights summary
│
├─ notebooks/
│  └─ exploration.ipynb                ← Jupyter notebook for EDA
│
├─ README.md                           ← project documentation
└─ requirements.txt                    ← dependencies list
```

---

## ⚙️ Installation Guide  

### 1️⃣ Clone or Download Repository  
```bash
git clone https://github.com/Naidi47/customer_purchase_project_with_dataset.git
cd customer_purchase_project_with_dataset
```

### 2️⃣ Create Virtual Environment  
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On Mac/Linux
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

Example `requirements.txt`  
```
pandas
numpy
matplotlib
seaborn
streamlit
openpyxl
```

---

## 📊 How It Works  

### Step 1 — Data Preparation (`src/data_prep.py`)
- Loads Excel dataset using `pd.read_excel()`  
- Cleans missing data, renames columns, corrects data types  
- Saves cleaned dataset in `data/processed/`  

### Step 2 — Feature Engineering (`src/features.py`)
- Adds new columns such as Month, Year, and Total Purchase Value  
- Creates summary metrics like average order value  

### Step 3 — Data Analysis (`src/analysis.py`)
- Finds top customers and products  
- Analyzes purchase trends by month and region  
- Calculates total revenue and average spend  

### Step 4 — Visualization (`src/viz.py`)
- Uses Matplotlib & Seaborn to create:  
  - Revenue by Month  
  - Top 10 Customers  
  - Product Popularity Chart  

### Step 5 — Streamlit Dashboard (`src/app.py`)
Run the app:
```bash
streamlit run src/app.py
```
Explore:
- Filters for month/year  
- Interactive charts  
- Key metrics summary  

---

## 📈 Example Insights  
- 🏆 **Top 5 Customers** contribute 42% of total sales.  
- 📅 **Most purchases** occur between **June–September**.  
- 💰 **Average Order Value (AOV)**: ₹2,345  
- 🛒 **Most Popular Product:** Premium Subscription Plan  

---

## 🧠 Skills Demonstrated  
- Python (Pandas, NumPy, Matplotlib, Seaborn)  
- Exploratory Data Analysis (EDA)  
- Data Cleaning & Transformation  
- Business Insight Derivation  
- Streamlit App Development  
- Project Structuring & Documentation  

---

## 🗂️ Dataset Information  
File: `dataset_original.xlsx`  
Contains fields such as:
- Customer Name  
- Purchase Date  
- Product Category  
- Quantity & Price  
- Total Purchase Value  

---

## 📢 Author  
**Brahmanaidu **  
📧 muchukuntlabrahmanaidu@gmail.com  
📍 Data Analyst | Python Enthusiast | Future Innovator  

---

## 📜 License  
This project is open-source and available under the **MIT License**.  
You are free to modify and use it for educational or portfolio purposes.  
