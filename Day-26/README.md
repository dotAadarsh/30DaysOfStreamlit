# 30DaysOfStreamlit | Day-26

## How to use API
### Bored API

[Bored API](boredapi.com) - The Bored API app suggests fun things for you to do when you are bored! Technically, it also demonstrates the usage of APIs from within a Streamlit app.
```
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
st.json(suggested_activity)
```
### Art Institute of Chicago API

[Art Institute of Chicago API](https://api.artic.edu/docs/#introduction) - The Art Institute of Chicago's API provides JSON-formatted data as a REST-style service that allows developers to explore and integrate the museum’s public data into their projects.
```
art_url = f'https://api.artic.edu/api/v1/artworks/search?q={option}&query[term][is_public_domain]=true&limit=20&fields=id,title,image_id'
json_data = requests.get(art_url)
art = json_data.json()
st.json(art)
```
### References 
- [Bored API](boredapi.com) 
- [Art Institute of Chicago API](https://api.artic.edu/docs/#introduction)
- [Image API 2.0](https://iiif.io/api/image/2.0/#uri-syntax)

## Result

![day26](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-26.PNG)