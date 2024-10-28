import pandas as pd
arr = [10,20,30]
# series

var =pd.Series(arr)
print(var)
# output:-
# 0    10
# 1    20
# 2    30
# dtype: int64

print(var[0])
var = pd.Series(arr,index=["x","y","z"])
print(var)
# OUTPUT:-
# x    10
# y    20
# z    30
# dtype: int64

data = {"calories ":[200,700,1000],"Duration ":[20,35,40]}
frame = pd.DataFrame(data)
print(frame)

# OUTPUT:-
#     calories   Duration 
# 0        200         20
# 1        700         35
# 2       1000         40

print("\nSelecting the row by integer location (iloc):")
print(frame.iloc[1])

# print("\nFiltering rows where calories > 500:")
# print([frame["calories "] > 500)
            
# mean_duration = frame["Duration "].mean()
# print("\nMean Duration:")
# print(mean_duration)
# frame.drop(columns=["Intensity"], inplace=True)
# print("\nDataFrame after dropping the 'Intensity' column:")
# print()