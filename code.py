from os import stat
import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go


df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()


mean = sum(data)/len(data)
std = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)


print("Mean , median and mode of the data are {},{},{} respectively".format(mean,median,mode))
print("Standard deviation of this data is {}".format(std))


first_std_start,first_std_end = mean-std,mean+std
second_std_start , second_std_end = mean-2*(std),mean+2*(std)
third_std_start , third_std_end = mean-3*(std),mean+3*(std)


fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()


list_of_data_within_1_std = [result for result in data if result > first_std_start and result < first_std_end]
list_of_data_within_2_std = [result for result in data if result > second_std_start and result < second_std_end]
list_of_data_within_3_std = [result for result in data if result > third_std_start and result < third_std_end]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std)*100/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std)*100/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std)*100/len(data)))