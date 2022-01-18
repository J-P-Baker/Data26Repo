import csv
#"user_details.csv"
def transform_user_details(csv_file_name):
    new_user_data=[]

    with open(csv_file_name, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        for row in csv_reader:
            print(row)
            new_user_data.append([row[1], row[2], row[-1]])

        return new_user_data

def create_new_user_data(old_data_file="user_details.csv", new_file="new_user_data.csv"):
    new_user_data = transform_user_details(old_data_file)
    new_file_open = open(new_file, 'w', newline='')

    with new_file_open:
        csv_writer = csv.writer(new_file_open)
        csv_writer.writerows(new_user_data)

create_new_user_data()