from faker import Faker

class MyFaker(Faker):
    """
    Faker sub-class with couple of new methods especially w/ random numbers in names.
    """

    # Declaring the dictionary keys
    # Ignore the phone number field. It is not a required field.
    FAKER_CUSTOMER_KEYS = ["firstname", "lastname", "streetaddress", "city",
                           "state", "postcode", "ssn", "username", "password",
                           "confirm"]
    # Declaring the form field names (used for error messages)
    FAKER_CUSTOMER_FIELD_NAMES = {"firstname" : "First name", "lastname" : "Last name",
                                  "streetaddress" : "Address", "city" : "City", "state": "State",
                                  "postcode" : "Zip Code", "phonenumber" : "Phone number",
                                  "ssn" : "Social Security Number", "username" : "Username",
                                  "password" : "Password", "confirm" : "Password confirmation"}

    @staticmethod
    def customer_data_one_empty_field(locale: str = "pl_PL") -> list[dict]:
        """
        Generates the customer data w/ one empty field.
        :param locale: Lets you define the locale of the fake data. Default value is pl_Pl.
        :return:
        """
        cust_data: list = []
        # TC's number starts at 1
        for i in range(len(MyFaker.FAKER_CUSTOMER_KEYS)):
            temp_dict: dict = {}
            temp_dict["tc"] = i + 1
            temp_dict["empty"] = MyFaker.FAKER_CUSTOMER_FIELD_NAMES[MyFaker.FAKER_CUSTOMER_KEYS[i]]
            temp_dict["firstname"] = MyFaker(locale).unique.first_name()
            temp_dict["lastname"] = MyFaker(locale).unique.last_name()
            temp_dict["address"] = MyFaker(locale).unique.street_address()
            temp_dict["city"] = MyFaker(locale).unique.city()
            temp_dict["state"] = MyFaker(locale).unique.administrative_unit()
            temp_dict["postcode"] = MyFaker(locale).unique.postalcode()
            temp_dict["phonenumber"] = MyFaker(locale).unique.phone_number()
            temp_dict["ssn"] = MyFaker(locale).unique.ssn()
            temp_dict["username"] = MyFaker(locale).unique.user_name()
            temp_dict["password"] = MyFaker(locale).unique.password()
            temp_dict["confirm"] = temp_dict["password"]
            temp_dict[MyFaker.FAKER_CUSTOMER_KEYS[i]] = ""
            cust_data.append(temp_dict)
        return cust_data

    @staticmethod
    def customer_data_all_fields(locale: str = "pl_PL", number: int = 5) -> list[dict]:
        """
        Generates the customer data w/ all fields w/ proper values.
        :param locale: Lets you define the locale of the fake data. Default value is pl_Pl.
        :param number: Describes the number of customer data generated.
        :return:
        """
        cust_data: list = []
        for i in range(number):
            temp_dict: dict = {}
            temp_dict["firstname"] = MyFaker(locale).unique.first_name()
            temp_dict["lastname"] = MyFaker(locale).unique.last_name()
            temp_dict["address"] = MyFaker(locale).unique.street_address()
            temp_dict["city"] = MyFaker(locale).unique.city()
            temp_dict["state"] = MyFaker(locale).unique.administrative_unit()
            temp_dict["postcode"] = MyFaker(locale).unique.postalcode()
            temp_dict["phonenumber"] = MyFaker(locale).unique.phone_number()
            temp_dict["ssn"] = MyFaker(locale).unique.ssn()
            temp_dict["username"] = MyFaker(locale).unique.user_name()
            temp_dict["password"] = MyFaker(locale).unique.password()
            temp_dict["confirm"] = temp_dict["password"]
            cust_data.append(temp_dict)
        return cust_data

    def name_with_random_no(self) -> str:
        """
        Returns random name with random number at the end.
        :return: string
        """
        return self.name() + str(int(self.randint(0, 1000)))

    def name_with_random_digits(self) -> str:
        """
        Returns random name with random numbers inside the name.
        :return: string
        """
        name: str = self.name()
        first: int = self.randint(0, len(name))
        return name[:first] + "".join([str(self.randint(0, 9)) for i in range(first, first + 3)]) + name[first+3:]

