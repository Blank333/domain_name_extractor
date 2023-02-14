#https/http www/without-www). Examples 
#https://www.abc.com/random.html ⇒ abc.com 
#http://www.abc.com/random.html ⇒ abc.com 
#http://www.abc.com/hello/random.html ⇒ abc.com 
#www.abc.com ⇒ abc.com 
#http://abc.com ⇒ abc.com 
from tests import test, add_test
tests = [];
add_test()

def domain_name(url):
    parts = url.split("/")
    return parts


