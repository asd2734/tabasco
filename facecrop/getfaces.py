import urllib, urllib2, sys, calendar, time, json
from PIL import Image

def getRequestURL(imageUrl, apiKey):
	retUrl = "https://api.havenondemand.com/1/api/sync/detectfaces/v1?url=" + urllib.quote(imageUrl) + "&additional=false&apikey=" + apiKey
	return retUrl

def makeRequest(requestURL):
	content = urllib2.urlopen(requestURL).read()
	return content

def downloadImage(imageUrl, imageName):
	# download image
	urllib.urlretrieve(imageUrl, imageName)

def cropImage(imageName, extension, count, left, top, width, height):
	with Image.open(imageName + extension, "r") as img:
		cropImage = img.crop((left, top, left + width, top + height))
		cropImage.save(imageName + "_" + str(count).zfill(3) + extension)




if __name__ == "__main__":
	imageUrl = sys.argv[1]
	apiKey = sys.argv[2]

	facesJson = json.loads(makeRequest(getRequestURL(imageUrl, apiKey)))
	imageName = "cropped_faces/" + str(calendar.timegm(time.strptime('Jul 9, 2009 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC')))
	extension = imageUrl[imageUrl.rfind("."):]
	downloadImage(imageUrl, imageName + extension)
	
	count = 0
	for face in facesJson.get("face"):
		left = face.get("left")
		top = face.get("top")
		width = face.get("width")
		height = face.get("height")
		cropImage(imageName, extension, count, left, top, width, height)
		count += 1