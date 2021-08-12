#testing wtf forms
#app.config['WTF_CSRF_ENABLED'] = False to disable token checking, since POST isn't a real POST
#put the app.config into test.py file

class SnackViewsTestCase(TestCase): #this checks a GET request
"""tests for views of snacks"""
    def test_snack_add_form(self):
        with app.test_client() as test_client:
            resp = client.get("/add")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="snack-add-form"', hmtl)

    def test_snack_add(self): #checks POST request for a route
        with app.test_client() as test_client:
            d = {"name": "Test2", "price": 2}
            resp = client.get("/add", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Added Test2 at 2", hmtl)
