#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    url = url.split('.')

    point = ''
    for i in url:
        if 'http' in i or 'www' in i:
            point += i

    ind_p = 0
    for i in range(len(url)):
        if i == point:
            ind_p += i

    k = url[ind_p]
    c = k.rfind('/')
    r = k[c+1::]

    if len(r) > 0 and r not in 'www':
        return r
    else:
        return url[ind_p+1]

print(domain_name("http://google.com"))