import re

def extractLinksRegEx(text):
    tgs = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)
    
    return [match[1] for match in tgs.findall(text)]
