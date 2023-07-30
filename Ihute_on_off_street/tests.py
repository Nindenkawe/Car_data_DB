from django.test import TestCase

# Create test for my views here.
class TestViews(TestCase):
     def test_index(self):
         response = self.client.get('/ihute/index/')
         self.assertEqual(response.status_code, 200)
# 
     def test_signin(self):
         response = self.client.get('/ihute/signin/')
         self.assertEqual(response.status_code, 200)
# 
     def test_signup(self):
         response = self.client.get('/ihute/signup/')
         self.assertEqual(response.status_code, 200)
# 

# 
     def test_sub_profile(self):
         response = self.client.get('/ihute/sub_profile/')
         self.assertEqual(response.status_code, 200)
 
     def test_dashboard(self):
         response = self.client.get('/ihute/dashboard/')
         self.assertEqual(response.status_code, 200)

        