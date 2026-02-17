import pandas as pd
df=pd.read_csv("dirty_sales.csv")
print(df.head())
print("\n")
print(df.info())
print("\n")
print(df.isnull().sum())
print(df.dtypes)
print(df["unit_price"].unique()) 
df["unit_price"]=df["unit_price"].str.replace("TL","")
print(df["unit_price"].unique())
df["unit_price"]=df["unit_price"].str.replace(".","",regex=False)
print(df["unit_price"].unique())
df["unit_price"]=df["unit_price"].astype(str).str.replace(",",".",regex=False)
print(df["unit_price"].unique())
df["unit_price"]=df["unit_price"].str.replace(r"[^\d,\.]","", regex=True)
df["unit_price"]=pd.to_numeric(df["unit_price"], errors="coerce")
print(df["unit_price"])
print(df["unit_price"].describe())
q1=df["unit_price"].quantile(0.25)
q3=df["unit_price"].quantile(0.75)
print("Q1",q1,"Q3",q3)
iqr=q3-q1
print("IQR",iqr)
lower_bound=q1-1.5*iqr
upper_bound=q3+1.5*iqr
print("Lower:",lower_bound,"Upper:",upper_bound)
outliers=df[(df["unit_price"]<lower_bound)|(df["unit_price"]>upper_bound)]
print(outliers[["unit_price"]])
print("Outlier sayısı:",outliers.shape[0])

df["is_outlier_unit_price"]=(
    (df["unit_price"]<lower_bound)|
    (df["unit_price"]>upper_bound)
)
print(df["is_outlier_unit_price"].value_counts())
print(df[df["is_outlier_unit_price"]==True][["unit_price"]])
print(df["quantity"].dtype)
print(df["quantity"].unique())
df["quantity"]=df["quantity"].replace("two","2")
df["quantity"]=pd.to_numeric(df["quantity"], errors="coerce")
print(df["quantity"].dtype)
print(df["quantity"].unique())
Q1_q=df["quantity"].quantile(0.25)
Q3_q=df["quantity"].quantile(0.75)
IQR_q=Q3_q-Q1_q

lower_q=Q1_q-1.5*IQR_q
upper_q=Q3_q+1.5*IQR_q
print(lower_q,upper_q)
df["is_outlies_quantity"]=(
    (df["quantity"]<lower_q)|
    (df["quantity"]>upper_q)
)
print(df["is_outlies_quantity"].value_counts())
print(df["discount_pct"].unique())
df["is_outlier_discount"]=(df["discount_pct"]<0)|(df["discount_pct"]>100)
print(df["is_outlier_discount"].value_counts())
df.loc[df["is_outlier_discount"],"discount_pct"]=pd.NA
print(df["discount_pct"].isna().sum())
df_clean=df.dropna(subset=["discount_pct"])
print(df.shape)
print(df_clean.shape)
print(df_clean[["unit_price","quantity","discount_pct"]].dtypes)
df_clean["net_revenue"]=(
    df_clean["unit_price"]*
    df_clean["quantity"]*
    (1-df_clean["discount_pct"]/100)
)
print(df_clean[["unit_price","quantity","discount_pct","net_revenue"]].head())
print(df_clean["net_revenue"].describe())
print("Toplam Net Revenue:", df_clean["net_revenue"].sum())
print("Ortalama Net Revenue:", df_clean["net_revenue"].mean())
print(
    df_clean.sort_values("net_revenue", ascending=False)
    [["unit_price","quantity","discount_pct","net_revenue"]].head(5)
)
df_clean["has_discount"]=df_clean["discount_pct"]>0
print(df_clean.groupby("has_discount")["net_revenue"].agg(["count","mean","sum"]))
print(df_clean.groupby("quantity")["net_revenue"].mean())
print(df_clean.groupby("unit_price")["net_revenue"].sum().sort_values(ascending=False))
df_clean.to_csv("clean_sales_csv",index=False)
