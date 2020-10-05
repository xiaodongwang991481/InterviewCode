def getCategoryByUrl(url):
    return 1

def getSimilarUrls(url):
    return [url]

def getAllSimilarUrls(url):
    foundUrls = set([url])
    urls = [url]
    while urls:
        tryUrl = urls.pop()
        similarUrls = getSimilarUrls(tryUrl)
        for similarUrl in similarUrls:
            if similarUrl not in foundUrls:
                foundUrls.add(similarUrl)
                urls.append(similarUrl)
    urlByCategories = {}
    for foundUrl in foundUrls:
        category = getCategoryByUrl(foundUrl)
        urlByCategories.setdefault(category, set()).add(foundUrl)
    return urlByCategories

if __name__ == "__main__":
    urlByCategories = getAllSimilarUrls("http://www.google.com")
    print(urlByCategories)