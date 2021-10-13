import unittest

def get_domain(email):
    idx = email.find('@')
    
    if idx != -1:
        return email[idx+1:]
    else:
        return ""

class TestMain(unittest.TestCase):
    def test_cpp_domain(self, email):
        domain = get_domain(email)
        self.assertEquals(domain, "cpp.edu")