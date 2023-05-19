#pandas and numpy

import pandas as pd 
import numpy as np 

bank_df_1 = pd.DataFrame({ 'Bank Client ID':[1, 2, 3, 4, 5],
                        'Bank Client FirstName':['Phil', 'Claire', 'Haley', 'Alex', 'Luke'],
                        'Bank Client LastName': ['Dunphy', 'Prichett', 'Bixby', 'Rose', 'Andrews']})
print(bank_df_1)


bank_df_2 = pd.DataFrame({ 'Bank Client ID':[6, 7, 8, 9, 10],
                        'Bank Client FirstName':['Jay', 'Gloria', 'Mitch', 'Cam', 'Manny'],
                        'Bank Client LastName': ['Prichett', 'Delgado', 'Willy', 'Smith', 'Delgado']})
print(bank_df_2)

salary_df = pd.DataFrame({ 'Bank Client ID':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            'AnnualSalary':[ 40000, 50000, 12000, 10000, 8000, 55000, 45000, 50000, 30000, 15000 ]})     
print(salary_df)

bank_df_all = pd.concat([bank_df_1, bank_df_2])
print(bank_df_all)


bank_df_all = pd.merge(bank_df_all, salary_df, on = 'Bank Client ID')
print(bank_df_all)

new_client_df = pd.DataFrame ({'Bank Client ID': [11],
             'Bank Client FirstName': ['Willy'],
             'Bank Client LastName': ['Wonka'],
            'AnnualSalary': [60000]},
                              index = [ 10 ])
print(new_client_df)

new_client_details_df = pd.concat([ bank_df_all, new_client_df ])
print(new_client_details_df)





