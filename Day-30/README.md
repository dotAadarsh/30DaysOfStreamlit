
# 30DaysOfStreamlit | Day-30
## The Art of Creating Streamlit Apps
### Thumbnail images from YouTube videos

[Challenge Link](https://share.streamlit.io/streamlit/30days?challenge=Day+30)

```
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```
### References

- [Streamlit Documentation](hhttps://docs.streamlit.io/)

- [Streamlit cloud](https://streamlit.io/cloud)

## Result

![day30](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-30.PNG)