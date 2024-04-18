import unittest
from contact_manager import ContactManager

# Test cases for ContactManager class
class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.manager = ContactManager()

    def test_add_contact_new(self):
        result = self.manager.add_contact("Alice", "123-456-7890")
        self.assertEqual(result, "Contact 'Alice' added successfully.")
        self.assertIn("Alice", self.manager.contacts)

    def test_add_contact_duplicate(self):
        self.manager.add_contact("Bob", "234-567-8901")
        result = self.manager.add_contact("Bob", "234-567-8901")
        self.assertEqual(result, "Contact 'Bob' already exists.")

    def test_remove_contact_exists(self):
        self.manager.add_contact("Charlie", "345-678-9012")
        result = self.manager.remove_contact("Charlie")
        self.assertEqual(result, "Contact 'Charlie' removed successfully.")
        self.assertNotIn("Charlie", self.manager.contacts)

    def test_remove_contact_not_found(self):
        result = self.manager.remove_contact("David")
        self.assertEqual(result, "Contact 'David' not found.")

    def test_search_contact_found(self):
        self.manager.add_contact("Eve", "456-789-0123")
        result = self.manager.search_contact("Eve")
        self.assertEqual(result, "Name: Eve, Phone Number: 456-789-0123")

    def test_search_contact_not_found(self):
        result = self.manager.search_contact("Frank")
        self.assertEqual(result, "Contact 'Frank' not found.")

    def test_display_contacts_multiple(self):
        self.manager.add_contact("Gina", "567-890-1234")
        self.manager.add_contact("Hank", "678-901-2345")
        result = self.manager.display_contacts()
        expected_output = "Contacts:\nName: Gina, Phone Number: 567-890-1234\nName: Hank, Phone Number: 678-901-2345"
        print("Aslani: " + result)
        self.assertEqual(result, expected_output)

    def test_display_contacts_none(self):
        result = self.manager.display_contacts()
        self.assertEqual(result, "No contacts found.")

# This will run the test when the script is run (normally).
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
