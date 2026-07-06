import pandas as pd
df = pd.read_csv("Dataset.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\n" + "="*60)
print("FEATURE ENGINEERING")
print("="*60)

# Restaurant Name Length
df["Restaurant Name Length"] = df["Restaurant Name"].str.len()

# Address Length
df["Address Length"] = df["Address"].str.len()

# Locality Length
df["Locality Length"] = df["Locality"].str.len()

print("\nText-based features created successfully!")

print("\n" + "="*60)
print("ENCODING CATEGORICAL FEATURES")
print("="*60)

# Encode 'Has Table booking'
df["Has Table Booking Encoded"] = df["Has Table booking"].map({
    "Yes": 1,
    "No": 0
})

# Encode 'Has Online delivery'
df["Has Online Delivery Encoded"] = df["Has Online delivery"].map({
    "Yes": 1,
    "No": 0
})

print("\nCategorical features encoded successfully!")

print("\n" + "="*60)
print("NEW FEATURES CREATED")
print("="*60)

print(df[[
    "Restaurant Name",
    "Restaurant Name Length",
    "Address Length",
    "Locality Length",
    "Has Table Booking Encoded",
    "Has Online Delivery Encoded"
]].head(10))
df.to_csv("Feature_Engineered_Dataset.csv", index=False)

print("\nFeature engineered dataset saved successfully as 'Feature_Engineered_Dataset.csv'")

print("\n" + "="*60)
print("TASK COMPLETED SUCCESSFULLY")
print("="*60)