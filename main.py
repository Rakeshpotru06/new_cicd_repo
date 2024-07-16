# import pandas as pd
#
# df_initial = pd.DataFrame({
#     'Seat Number': range(1, 9),
#     'Seat Type': ['lower', 'middle', 'upper', 'lower', 'middle', 'upper', 'side lower', 'side upper']
# })
#
# print(df_initial)
# length_seat_number = len(df_initial['Seat Number'])
#
# num_seats = 72
# extended_seat_types = [df_initial['Seat Type'][i % length_seat_number] for i in range(num_seats)]
# df_extended = pd.DataFrame({
#     'Seat Number': range(1, num_seats + 1),
#     'Seat Type': extended_seat_types
# })
#
# lower_seats = df_extended[df_extended['Seat Type'] == 'lower']
# upper_seats = df_extended[df_extended['Seat Type'] == 'upper']
# middle_seats = df_extended[df_extended['Seat Type'] == 'middle']
#
# pc_lower = lower_seats.iloc[::3][:14]
# sr_citizen_lower = lower_seats.iloc[1::3][:7]
# gen_lower = lower_seats.iloc[2::3][:6]
#
# pc_middle = middle_seats.iloc[::2][:10]
# sr_citizen_middle = middle_seats.iloc[1::2][:8]
#
# def booking():
#     name = input('Enter Your Name: ').strip()
#     age = int(input('Enter your age: ').strip())
#     is_pc = input('Are you Physically Challenged? Choose Y/N: ').strip().upper()
#
#     if is_pc == 'Y':
#         seat = allocate_seat(pc_lower, pc_middle)
#         if seat:
#             print(f'Allocated Seat for {name}: {seat}')
#         else:
#             print('No seats available for physically challenged passengers.')
#     else:
#         if age > 60:
#             seat = allocate_seat(sr_citizen_lower, sr_citizen_middle)
#             if seat:
#                 print(f'Allocated Seat for {name}: {seat}')
#             else:
#                 print('No seats available for senior citizens.')
#         else:
#             has_preference = input('Do you have any preference? Choose Y/N: ').strip().upper()
#             seat = None
#             if has_preference == 'Y':
#                 prefer = input('Do you have any preference? Choose U/L/M: ').strip().upper()
#                 if prefer == 'L':
#                     seat = allocate_seat(gen_lower)
#                 elif prefer == 'M':
#                     seat = allocate_seat(middle_seats)
#                 elif prefer == 'U':
#                     seat = allocate_seat(upper_seats)
#             else:
#                 seat = allocate_seat(upper_seats)
#
#             if seat:
#                 print(f'Allocated Seat for {name}: {seat}')
#             else:
#                 print('No seats available for general passengers.')
#
#
# def allocate_seat(*seat_groups):
#     for seats in seat_groups:
#         if not seats.empty:
#             seat = seats.iloc[0]
#             return seat['Seat Number']
#     return None
#
#
# booking()


# samp_dataframe = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5, '6'],
#     'B': [10, 20, 30, 40, 50, 60],
#     'C': ['a', 'b', 'c', 'd', 'e','m']
# })
# samp_series = pd.Series([100, 200, 300, 400, 500,'test', 'rakesh','m'], name='D')


# print(samp_dataframe)
# print('---------------------------------------')
# print(samp_series)
# print((samp_series.shape))
# print(samp_series.count())
# print(samp_series.index)
# print(samp_series.iat[3])
# remove_str=pd.to_numeric(samp_series,errors='coerce').dropna()
# print(remove_str)
# print(remove_str.sum())
# print(samp_series.iat[1])
# print(samp_series.at[1])
# print(samp_dataframe.loc[1])
# print(samp_series.iloc[1])

# print(samp_dataframe.shape) #displays rows and columns
# print(samp_dataframe.index) # displays start/stop / step for the index
# print(samp_dataframe.values) # displays only values
# print(samp_dataframe.count(),'te')
# print(samp_dataframe.iloc[1])
# print(samp_dataframe.loc[1])
# print(samp_dataframe.size) # displays total size rows*columns
# print(samp_dataframe.axes) # Displays indexes(start stop step) - index and datatype
# print(samp_dataframe.info)
# print(samp_dataframe.describe())
# print(samp_dataframe.head(6)) # default first five
# print(samp_dataframe.tail(6)) # default last five
# print(samp_dataframe)


# samp_emp_data = pd.DataFrame({
#     'Name': ['Sowjanya', 'Swagini', 'Jaswith','Phani','Vasanthi'],
#     'Age': [26, 35, 2, 51, 38],
#     'Salary': [45000, 32000, 28000, 120000, 100000]
# })
#
# x = pd.to_numeric(samp_emp_data['Salary'])
# print(x)
# print(x.nlargest(3).iloc[-1])
print("Hello world")