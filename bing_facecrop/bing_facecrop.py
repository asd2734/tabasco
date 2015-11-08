import urllib, json, requests, sys, getfaces
from requests.auth import HTTPBasicAuth
 
def bing_api(query, api_key, source_type = "Image", top = 10, format = 'json'):
    global API_KEY
    """Returns the decoded json response content
 
    :param query: query for search
    :param source_type: type for seacrh result
    :param top: number of search result
    :param format: format of search result
    """
    # set search url
    query = '%27' + urllib.quote(query) + '%27'
    # web result only base url
    base_url = 'https://api.datamarket.azure.com/Bing/Search/v1/' + source_type
    url = base_url + '?Query=' + query + '&$top=' + str(top) + '&$format=' + format
 
    # create credential for authentication
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    # create auth object
    auth = HTTPBasicAuth(api_key, api_key)
    # set headers
    headers = {'User-Agent': user_agent}
 
    # get response from search url
    response_data = requests.get(url, headers=headers, auth = auth)
    print response_data
    # decode json response content
    json_result = response_data.json()
 
    return json_result

def get_img_urls(query,num_search, api_key):
    photos = []
    results=bing_api(query, api_key, top=num_search)['d']['results']

    for i in range(len(results)):
        if int(results[i]['FileSize']) > 1048576:
            print "File skipped; file size > 1 mb:", results[i]['MediaUrl']
            continue
        photos.append(results[i]['MediaUrl'])
        
    return photos

if __name__ == "__main__":
    with open("../api_keys/bing_apikey", "r") as f:
        api_key = f.readline().strip()

    query = ""
    for i in range(1, len(sys.argv)-1):
        query += sys.argv[i]
        if i == len(sys.argv)-2:
            continue
        query += " "

    num_search = int(sys.argv[len(sys.argv)-1])

    img_urls = get_img_urls(query, num_search, api_key)

    for img in img_urls:
        getfaces.getFaces(img)
