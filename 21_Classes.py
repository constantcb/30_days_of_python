class User:
    def __init__(self, username, email, user_id, role):
        self.username = username
        self.email = email
        self.user_id = user_id
        self.role = role

    def print_information(self):
        print(f'{self.username} has contact {self.email} identified by {self.user_id} with role {self.role}')


class Administrator(User):
    def __init__(self, username, email, user_id, role, department):
        self.department = department
        super().__init__(username, email, user_id, role)

    def print_information(self):
        print(
            f'{self.username} has contact {self.email} identified by id {self.user_id} with role {self.role} from '
            f'department {self.department}')


class Operator(User):
    def __init__(self, username, email, user_id, role, service_access):
        self.service_access = service_access
        super().__init__(username, email, user_id, role)

    def print_information(self):
        print(
            f'{self.username} has contact {self.email} identified by id {self.user_id} with role {self.role} has access to {self.service_access}')


if __name__ == '__main__':
    admin = Administrator('pippo2000', 'some-email@hotmail.com', 21, 'Admin', 'Magic')
    operator = Operator('justoperatore', 'operatore@gmail.com', 12932, 'Operator', ['BILLING', 'SHIPPING'])

    admin.print_information()
    operator.print_information()
