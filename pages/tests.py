from django.test import TestCase # for tests with databases
# my edits from here to below
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class HomepageTests(SimpleTestCase):
    # This checks that the URL for the home page returns a '200' success status code response
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        # assertEqual() in Python is a unittest library function that is used in unit testing to check the equality of two values
        self.assertEqual(response.status_code, 200)

    
    # this tests the name of the url
    def test_url_available_by_name(self):
        # the reverse function allows to retrieve url details from url's.py file through the name value provided there
        response = self.client.get(reverse("home"))
        # assertEqual() in Python is a unittest library function that is used in unit testing to check the equality of two values
        self.assertEqual(response.status_code, 200)

    # test that the correct template is used
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        # Asserts that the template with the given name was used in rendering the response
        self.assertTemplateUsed(response, "home.html")

    # test that the template displays expected content
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        # Asserts that a response produced the given status_code and that text appears in its content
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    # This checks that the URL for the about page returns a '200' success status code respnose
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        # assertEqual() in Python is a unittest library function that is used in unit testing to check the equality of two values
        self.assertEqual(response.status_code, 200)

    # this tests the name of the url
    def test_url_available_by_name(self):
        # the reverse function allows to retrieve url details from url's.py file through the name value provided there
        response = self.client.get(reverse("about"))
        # assertEqual() in Python is a unittest library function that is used in unit testing to check the equality of two values
        self.assertEqual(response.status_code, 200)

    # test that the correct template is used
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        # Asserts that the template with the given name was used in rendering the response
        self.assertTemplateUsed(response, "about.html")

    # test that the template displays expected content
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        # Asserts that a response produced the given status_code and that text appears in its content
        self.assertContains(response, "<h1>About page</h1>")