import urllib, urllib2, sys

def getRequestURL(imageUrl, apiKey):
	retUrl = "https://api.havenondemand.com/1/api/sync/detectfaces/v1?url=" + urllib.quote(imageUrl) + "&additional=false&apikey=" + apiKey
	return retUrl

def makeRequest(requestURL):
	content = urllib2.urlopen(requestURL).read()
	return content

def cropImage(imageUrl):
	# download image
	with open("sample.jpg", "r") as f:
		f.write(urllib.urlopen(imageUrl))


if __name__ == "__main__":
	print(makeRequest(getRequestURL(sys.argv[1], sys.argv[2])))