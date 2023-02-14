#Find domain name of a URL

#creating tests
from tests import test, add_test

tests = []
add_test("https://www.abc.com/random.html", "abc.com", tests)
add_test("http://www.abc.com/random.html", "abc.com", tests)
add_test("http://www.abc.com/hello/random.html", "abc.com", tests)
add_test("http://www.abc.com/hello/random.html", "abc.com", tests)
add_test("www.abc.com", "abc.com", tests)
add_test("http://abc.com", "abc.com", tests)

def domain_name(url):
    parts = url.split("/")
    if(parts[0] == "https:" or parts[0] == "http:"): 
        full_domain = parts[2].split(".")
    else:
        full_domain = parts[0].split(".")
    
    if full_domain[0] == "www":
        full_domain.remove("www")
    
    result = ".".join(full_domain).strip()
    print(url + " => " + result)
    return result
        

# for i in range(len(tests)):
#     print(domain_name(**tests[i]["input"]))

print(test(domain_name, tests))

