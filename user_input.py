# import datetime
# from random import randint

# # Function to generate invoice number
# def generate_invoice_number():
#     return ''.join([str(randint(0, 9)) for _ in range(9)])

# # Function to get current date in a specific format
# def get_current_date():
#     return datetime.datetime.now().strftime("%d/%m/%Y")

# # Function to collect user inputs
# def collect_user_inputs():
#     data = {
#         "firstNameValue": input("Enter your first name: "),
#         "lastNameValue": input("Enter your last name: "),
#         "numberOfItemsValue": input("Enter the number of items: "),
#         "articleNumberValue": input("Enter the article number: "),
#         "descriptionValue": input("Enter the description: "),
#         "qtyValue": input("Enter the quantity: ")
#     }
#     data["invoiceNumberValue"] = generate_invoice_number()
#     data["dateFieldValue"] = get_current_date()
#     return data

# # Function to update the specific lines in the file
# def update_file(data, file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     new_lines = []
#     for line in lines:
#         if "=" in line and ";" in line:
#             key = line.split("=")[0].split(".")[-1].strip()
#             if key in data:
#                 new_line = f'{line.split("=")[0]} = "{data[key]}";\n'
#                 new_lines.append(new_line)
#             else:
#                 new_lines.append(line)
#         else:
#             new_lines.append(line)

#     with open(file_path, 'w') as file:
#         file.writelines(new_lines)

# if __name__ == "__main__":
#     data = collect_user_inputs()
#     file_path = change for file path"
#     update_file(data, file_path)
#     print("File has been successfully updated.")
