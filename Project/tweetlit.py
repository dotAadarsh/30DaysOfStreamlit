import requests
from requests.api import request
import os
import json
import streamlit as st
import streamlit.components.v1 as components
import random
from streamlit_option_menu import option_menu
from datetime import datetime , timedelta

bearer_token = st.secrets["bearer_token"]
with st.sidebar:
    selected = option_menu("#Tweetlit", ["Home", 'Search Tweet', 'Total tweet count', 'Spaces lookup'], 
        icons=['house', 'search', '123','mic-fill'], menu_icon="menu-app-fill", default_index=0,
    )

    with st.expander("#30DaysOfStreamlit", expanded=True):
        st.write('The #30DaysOfStreamlit is a coding challenge designed to help you get started in building Streamlit apps.')
        st.markdown('''
        - [Start the Challenge](https://share.streamlit.io/streamlit/30days)
        - [Streamlit Docs](https://docs.streamlit.io/)
        - [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
        ''')
    with st.expander('Buy me a coffee'):
        components.html('''
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="aadarshk" data-color="#5F7FFF" data-emoji=""  data-font="Lato" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>''',height = 100)

    with st.expander("Socials"):
            st.markdown('''
            [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dotaadarsh)
            [![Twitter](https://img.shields.io/badge/twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/dotaadarsh)
            [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dotaadarsh/)
            [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/dotaadarsh/)
            [![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/Jj8xeWpnEe)
            [![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)](https://open.spotify.com/user/w4vmhygkyyzefhe1u3bpqrlo6)

            ''')
               
def bearer_oauth(r):

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

if selected == 'Home':

    st.title("#Tweetlit")

    input = st.text_input("Enter your query", value = "#30DaysOfStreamlit")

    def theTweets(tweets_url):
        api =f'https://publish.twitter.com/oembed?url={tweets_url}&theme=dark'
        response_tweets = requests.get(api)
        res = response_tweets.json()["html"]
        return res

    def tweets():
        search_url = "https://api.twitter.com/2/tweets/search/recent"
        query_params_tweets = {'query': f'{input}','tweet.fields': 'author_id', 'max_results': 50}
        json_response = connect_to_endpoint(search_url, query_params_tweets)

        col1, col2 = st.columns(2)
        with col1:
            for i in range(0,20):
                author_id = json_response["data"][i]["author_id"]
                tweet_id = json_response["data"][i]["id"]
                url = f'https://twitter.com/{author_id}/status/{tweet_id}'
                res = theTweets(url)
                components.html(res, height = 600)
                
        with col2:
            for i in range(20,40):
                author_id = json_response["data"][i]["author_id"]
                tweet_id = json_response["data"][i]["id"]
                url = f'https://twitter.com/{author_id}/status/{tweet_id}'
                res = theTweets(url)
                components.html(res, height=600)

    def count():
        my_date = datetime.now() - timedelta(days=0, hours=0, minutes=5)
        date_format = my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%Z')  
        d = date_format+'Z'
        count_url = "https://api.twitter.com/2/tweets/counts/recent"
        query_params_count = {'query': f'{input}','end_time': f'{d}'}
        json_response = connect_to_endpoint(count_url, query_params_count)
        st.metric("Total Tweet count", value = json_response["meta"]["total_tweet_count"])

    def main():
        count()
        tweets()
        
    if __name__ == "__main__":
        main()

if selected == 'Search Tweet':
    st.title("#Search Tweets")
    input_tweet = st.text_input("Enter your query", value = "#30DaysOfStreamlit")

    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {'query': f'{input_tweet}','tweet.fields': 'author_id', 'max_results': 10}

    def theTweets(tweets_url):
        api =f'https://publish.twitter.com/oembed?url={tweets_url}&theme=dark'
        response = requests.get(api)
        res = response.json()["html"]
        return res

    def username(json_response):

        col1, col2 = st.columns(2)
        with col1:
            n = random.randint(0,9)
            author_id = json_response["data"][n]["author_id"]
            tweet_id = json_response["data"][n]["id"]
            url = f'https://twitter.com/{author_id}/status/{tweet_id}'
            res = theTweets(url)
            components.html(res,height=750)
                
        with col2:
            st.markdown('''
    ### GET /2/tweets/search/recent

    The recent search endpoint returns Tweets from the last seven days that match a search query.
    ### Endpoint URL
    > `https://api.twitter.com/2/tweets/search/recent`
    ''')
            st.json(json_response["data"][n])
            with st.expander("Reference", expanded=True):
                st.markdown('''
                    
                - [Twitter Docs | GET /2/tweets/search/recent](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)
                - [Getting started with the recent search endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/search/quick-start/recent-search)
                - [Github | Sample code for the Twitter API v2 endpoints](https://github.com/twitterdev/Twitter-API-v2-sample-code)
                    ''')
    json_response = connect_to_endpoint(search_url, query_params)
    tweets_url = username(json_response)

if selected == 'Total tweet count':
    st.title("#Tweet counts")
    input = st.text_input("Enter your query", value = "#30DaysOfStreamlit")

    def count():
        my_date = datetime.now() - timedelta(days=0, hours=0, minutes=5)
        date_format = my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%Z')  
        d = date_format+'Z'
        count_url = "https://api.twitter.com/2/tweets/counts/recent"
        query_params_count = {'query': f'{input}','end_time': f'{d}'}
        json_response = connect_to_endpoint(count_url, query_params_count)
        st.metric("Total Tweet count", json_response["meta"]["total_tweet_count"])
        st.info(f"The result is based on the past 7 days tweets")
        st.markdown('''

        ### GET /2/tweets/counts/recent

        The recent Tweet counts endpoint returns count of Tweets from the last seven days that match a query.
        ### Endpoint URL
        > `https://api.twitter.com/2/tweets/counts/recent`
        ''')
        st.json(json_response)
        with st.expander("Reference", expanded=True):
            st.markdown('''
            - [Twitter Docs | GET /2/tweets/counts/recent](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent)
            - [Getting started with the recent Tweet counts endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/quick-start/recent-tweet-counts)
            - [Github | Sample code for the Twitter API v2 endpoints](https://github.com/twitterdev/Twitter-API-v2-sample-code)
                ''')
    count()

if selected == 'Spaces lookup':
    st.header('Spaces lookup')
    input_space = st.text_input("Enter space id", value = "1dRJZlbglXMKB")
    search_url_space = "https://api.twitter.com/2/spaces"
    # Optional params: host_ids,conversation_controls,created_at,creator_id,id,invited_user_ids,is_ticketed,lang,media_key,participants,scheduled_start,speaker_ids,started_at,state,title,updated_at
    query_params = {'ids': f'{input_space}', 'space.fields': 'title,created_at,participant_count', 'expansions': 'creator_id'}
    json_response = connect_to_endpoint(search_url_space, query_params)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f'Title: {json_response["data"][0]["title"]}')
        st.text(f'Total participants: {json_response["data"][0]["participant_count"]}')
        st.text(f'Created at: {json_response["data"][0]["created_at"]}')
        st.text(f'Created by: @{json_response["includes"]["users"][0]["username"]}')
        st.markdown('''
            ### GET /2/spaces

            Returns details about multiple Spaces. Up to 100 comma-separated Spaces IDs can be looked up using this endpoint.
            ### Endpoint URL
            > `https://api.twitter.com/2/spaces`
            ''')
        with st.expander("Reference", expanded=True):
            st.markdown('''
            - [Twitter Docs | GET /2/spaces](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces)
            - [Getting started with the Spaces lookup endpoints](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/quick-start)
            - [Github | Sample code for the Twitter API v2 endpoints](https://github.com/twitterdev/Twitter-API-v2-sample-code)
                ''')
    with col2:
        st.json(json.dumps(json_response, indent=4, sort_keys=True))
        