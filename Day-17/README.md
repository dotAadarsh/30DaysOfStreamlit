# 30DaysOfStreamlit | Day-17

## st.secrets

`st.secrets` allows you to store confidential information such as API keys, database passwords or other credentials.
 "Secrets" field is written using [TOML](https://toml.io/en/latest) format
 
 ### Use secrets in your app
```
[owner]
name = "Johnny Silverhand"
dob = 1988-11-16T07:32:00-08:00
password = "E9BD1C5B"
```
Access your secrets as environment variables or by querying the  `st.secrets`  dict. For example, if you enter the secrets from the section above, the code below shows you how you can access them within your Streamlit app.
```
st.write("DB username: ", st.secrets["owner"]["name"])
st.write("DB password: ", st.secrets["owner"]["password"])
```

### Develop locally with secrets

When developing your app locally, add a file called  `secrets.toml`  in a folder called  `.streamlit`  at the root of your app repo, and copy/paste your secrets into that file.

Reference - [Secrets management](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)

## Result

![day17](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-17.PNG)