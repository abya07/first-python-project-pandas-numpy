# first-python-project
1. Define a dataframe named 'Bank_df_1' that contains the first and last names for 5 bank clients with IDs = 1, 2, 3, 4, 5
2. Assume that the bank got 5 new clients, define another dataframe named 'Bank_df_2' that contains a new clients with IDs = 6, 7, 8, 9, 10
3. Let's assume we obtained additional information (Annual Salary) about all our bank customers (10 customers)
4. Concatenate both 'bank_df_1' and 'bank_df_2' dataframes
5. Merge client names and their newly added salary information using the 'Bank Client ID'
6. Let's assume that you became a new client to the bank
7. Define a new DataFrame that contains your information such as client ID (choose 11), first name, last name, and annual salary.
8. Add this new dataframe to the original dataframe 'bank_df_all'.




bank_df_1 = pd.DataFrame({ 'Bank Client ID':[1, 2, 3, 4, 5],
                        'Bank Client FirstName':['Phil', 'Claire', 'Haley', 'Alex', 'Luke'],
                        'Bank Client LastName': ['Dunphy', 'Prichett', 'Bixby', 'Rose', 'Andrews']})
                         


bank_df_2 = pd.DataFrame({ 'Bank Client ID':[6, 7, 8, 9, 10],
                        'Bank Client FirstName':['Jay', 'Gloria', 'Mitch', 'Cam', 'Manny'],
                        'Bank Client LastName': ['Prichett', 'Delgado', 'Willy', 'Smith', 'Delgado']})
                         


salary_df = pd.DataFrame({ 'Bank Client ID':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            'AnnualSalary':[ 40000, 50000, 12000, 10000, 8000, 55000, 45000, 50000, 30000, 15000 ]})                  


bank_df_all = pd.merge(bank_df_all, salary_df, on = 'Bank Client ID')


new_client_df = pd.DataFrame ({'Bank Client ID': [11],
             'Bank Client FirstName': ['Willy'],
             'Bank Client LastName': ['Wonka'],
            'AnnualSalary': [60000]},
                              index = [ 10 ])


new_client_details_df = pd.concat([ bank_df_all, new_client_df ])


