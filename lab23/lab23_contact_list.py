def csv_import(file) -> list:
    """Imports CSV File, using filename in current directory, splits first line into header and subsequent lines as values"""
    with open(file, 'r') as file:
        # Name, Phone, City, State
        contacts = file.read().split('\n')
        header = contacts[0].split(',')
        my_contacts = []

        for lines in contacts[1:]:
            contact = {}
            values = lines.split(',')
            for key, value in zip(header, values):
                contact[key] = value
            my_contacts.append(contact)
    return my_contacts


# Create
def create_contact(contact_list: list):
    header = str(contact_list[0]).split(',')
    name = input('What is your name?: ')
    phone = input('What is your phone number?: ')
    city = input('What city do you reside?: ')
    state = input('What state do you live in?: ')

    contact = str(f'{name},{phone},{city},{state}')

    new_contact = list(zip(header,contact))

    contact_list.append(new_contact)
    return contact_list


# Read
def read_contact():
    pass


# Update
def update_contact():
    pass


# Delete
def delete_contact():
    pass


def save_contact_list(contact_list):
    pass


def main():
    my_contacts = csv_import('contacts.csv')
    print(my_contacts)
    create_contact(my_contacts)
    print(my_contacts)


main()
