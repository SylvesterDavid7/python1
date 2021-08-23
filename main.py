import re
stringpattern = re.compile('\w*[_]\w*')
ippattern = re.compile('\d\[\.\]\d\[\.\]\d\[\.\]\d')
indicators = re.compile('\S*\[\.\]\S*')
domain = re.compile('\D\w*\[\.\]\D\w*')
urls = re.compile('\S*\[\.\]\D\S*')
with open('Text.txt', 'r') as n:
    n = n.read()
    result = re.findall(stringpattern, n);
    ip = re.findall(ippattern, n);
    indc = re.findall(indicators, n);
    dom = re.findall(domain, n);
    urlres = re.findall(urls, n);

    finalip = str(ip).replace("[", "").replace("]","");
    finaldom = str(dom).replace("[","").replace("]","");
    finalurl = str(urlres).replace("xx","tt").replace("]","").replace("[","");

    print("The Strings that matches STRING_5CHAR Pattern are:", result);
    print("Valid Indicators :", indc)
    print("The IP addresses :", finalip)
    print("The Domain : ", finaldom)
    print("The URL :", finalurl)


    


