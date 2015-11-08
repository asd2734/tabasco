import urllib, requests, sys, time, json, re
from PIL import Image

def getRequestURL(imageUrl, apiKey):
	retUrl = "https://api.havenondemand.com/1/api/sync/detectfaces/v1?url=" + urllib.quote(imageUrl) + "&additional=false&apikey=" + apiKey
	return retUrl

def makeRequest(requestURL):
	content = requests.get(requestURL)
	return content.json()

def downloadImage(imageUrl, imageName):
	# download image
	urllib.urlretrieve(imageUrl, imageName)

def cropImage(imageName, extension, count, left, top, width, height):
	with Image.open(imageName + extension, "r") as img:
		cropImage = img.crop((left, top, left + width, top + height))
		cropImage.save(imageName + "_" + str(count).zfill(3) + extension)

def getFaces(imageUrl):
	with open("../api_keys/hp_apikey", "r") as f:
		apiKey = f.readline().strip()

	facesJson = makeRequest(getRequestURL(imageUrl, apiKey))
	imageName = "cropped_faces/" + str(int(time.time() * 1000))
	#extension = imageUrl[imageUrl.rfind("."):]
	splitUrl = imageUrl.split("?")
	if re.search(r'\.{1}[0-9a-zA-Z]+$', splitUrl[len(splitUrl)-1], re.M|re.I):
		matchobj = re.search(r'\.{1}[0-9a-zA-Z]+$', splitUrl[len(splitUrl)-1], re.M|re.I)
	elif re.search(r'\.{1}[0-9a-zA-Z]+$', splitUrl[len(splitUrl)-2], re.M|re.I):
		matchobj = re.search(r'\.{1}[0-9a-zA-Z]+$', splitUrl[len(splitUrl)-2], re.M|re.I)
	else:
		return
	extension = matchobj.group()
	downloadImage(imageUrl, imageName + extension)
	
	count = 0

	if facesJson.get("face") is not None:
		for face in facesJson.get("face"):
			left = face.get("left")
			top = face.get("top")
			width = face.get("width")
			height = face.get("height")
			cropImage(imageName, extension, count, left, top, width, height)
			count += 1
