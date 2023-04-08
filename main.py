import pandas as pd

df = pd.DataFrame(columns=['ID Number', 'Name', 'Age', 'Date of Birth', 'Profession', 'Gender'])

def menu():
    print("========= Program Menu =========")
    print("1 Register data")
    print("2 Print total data")
    print("3 Print data by age")
    print("4 Print data by gender")
    print("0 Exit")
    choice = input("Choose your option: ")
    return choice

def save_data():
    while True:
        id_num = input("Enter ID Number (number): ")
        if id_num.isdigit():
            break
        print("ID Number must be a number!")
    name = input("Enter your name (20 characters): ")
    while len(name) > 20:
        name = input("Enter your name (max 20 characters): ")
    age = int(input("Enter age: "))
    while age < 0:
        age = int(input("Invalid age, please enter a positive number: "))
    date_of_birth = input("Enter date of birth (yyyy-mm-dd): ")
    try:
        pd.to_datetime(date_of_birth)
    except ValueError:
        date_of_birth = input("Invalid date of birth, please enter date in yyyy-mm-dd format: ")
    profession = input("Enter profession: ")
    gender = input("Enter gender (M/F): ")
    while gender.upper() not in ['M', 'F']:
        gender = input("Invalid gender, please enter 'M' or 'F': ")
    df.loc[len(df)] = [id_num, name, age, date_of_birth, profession, gender.upper()]

def print_data_by_age(age_requested):
    people_with_this_age = df[df['Age'] == age_requested]
    num_people = len(people_with_this_age)
    if num_people == 0:
        print(f"No one with age {age_requested}")
    elif num_people == 1:
        print(f"There is 1 person with age {age_requested}:")
        for _, person in people_with_this_age.iterrows():
            print(person['ID Number'], person['Name'], person['Age'], person['Date of Birth'], person['Profession'], person['Gender'])
    else:
        print(f"There are {num_people} people with age {age_requested}:")
        for _, person in people_with_this_age.iterrows():
            print(person['ID Number'], person['Name'], person['Age'], person['Date of Birth'], person['Profession'], person['Gender'])

def print_data_by_gender():
    print("====== Data by gender ======")
    print(df.groupby(['Gender']).size())

while True:
    choice = menu()

    if choice == '1':
        save_data()
        print("Data saved successfully!")

    elif choice == '2':
        if not df.empty:
            print("Registered data are:")
            print(df)
            print(f"Total number of users is {len(df)}")
        else:
            print("No data to print")

    elif choice == '3':
        age_requested = int(input("Enter age: "))
        print_data_by_age(age_requested)

    elif choice == '4':
        print_data_by_gender()

    elif choice == '0':
        print("Thank you for using our program.")
        break

    else:
        print("Invalid choice!")
