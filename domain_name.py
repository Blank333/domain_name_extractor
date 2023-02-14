#Find domain name of a URL

#creating tests
from tests import test, add_test

tests = []
add_test("https://www.abc.com/random.html", "abc.com", tests)
add_test("http://www.abc.com/random.html", "abc.com", tests)
add_test("http://www.abc.com/hello/random.html", "abc.com", tests)
add_test("http://www.abc.com/hello/random.html", "abc.com", tests)
add_test("www.abc.com", "abc.com", tests)
add_test("http://mdn.firefox.com", "mdn.firefox.com", tests)
add_test("", "", tests)
add_test("www.google.co.in", "google.co.in", tests)
add_test("https://internshala.com/internship/detail/python-development-backend-work-from-home-job-internship-at-primenumbers-technologies1676367769", "internshala.com", tests)

def domain_name(url):
    parts = url.split("/")
    if(parts[0] == "https:" or parts[0] == "http:"): 
        full_domain = parts[2].split(".")
    else:
        full_domain = parts[0].split(".")
    
    if full_domain[0] == "www":
        full_domain.remove("www")
    
    result = ".".join(full_domain).strip()
    return result
        
print(test(domain_name, tests))

