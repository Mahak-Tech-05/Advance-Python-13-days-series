import pandas as pd

#----creating a data------
data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Karan"],#this dictornary key-> column(name,marks,age)
    "Marks": [85, 90, None, 40, 75],
    "Age": [20, 21, 19, 18, None]
}

#creating  datafram->table format
#dictionary-> table format convert
df = pd.DataFrame(data)

print("----- Original Data -----")
print(df)

# ✅ Correct way (NO warning)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())#calculating average marks .fina()-> replaces missing values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\n----- After Cleaning -----")
print(df)

print("\n----- Analysis -----")
print("Average Marks:", df["Marks"].mean())#average
print("Maximum Marks:", df["Marks"].max())#highest
print("Minimum Marks:", df["Marks"].min())#lowest

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")#apply()-> runs functions on each row,lambda->short function

print("\n----- With Result Column -----")
print(df)

print("\n----- Students Who Passed -----")
print(df[df["Result"] == "Pass"])

df.to_csv("student_output.csv", index=False)

print("\nData saved to student_output.csv")
