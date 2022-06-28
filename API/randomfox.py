import requests
import webbrowser

"""response = requests.get('https://randomfox.ca/floof')

print("Returned response status code is: ", response.status_code)
print("Returned response text is: ", response.text)
print("Headers")

headers = response.headers
# print(headers)

print(headers['Date'])

json_response = response.json()
print(json_response.get('link'))

link = json_response.get('link')
image = json_response.get('image')

# webbrowser.open(image, new = 2, autoraise=True)
# webbrowser.open_new_tab(link)

"""



res = requests.get('https://xkcd.com')

# print(res)

# print(res.headers)
# print(dir(res)) # methods and attributes with response method we can use
# print(help(res)) # detail of response methods, we can use

# print(res.content)


# res = requests.get('https://www.pixelstalk.net/wp-content/uploads/2016/04/Fantasy-wallpapers-HD.jpg')

# print(res)
# print(res.ok)

# with open('fantasy2.png', 'wb') as f:
#     f.write(res.content)



# Generating appropriate url with parameters

payload = {'page':2, 'count':25}
response = requests.get('https://httpbin.org/get', params = payload)
print(response.url)

payload = {'username':'corey', 'password':'testing'}
response = requests.post('https://httpbin.org/post', data = payload)

res_dict = response.json()
print(res_dict['form']['password'])



# Basic Auth

resp = requests.get('https://httpbin.org/basic-auth/corey/testing', timeout=3)

print(resp)
print(resp.text)
