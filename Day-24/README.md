# 30DaysOfStreamlit | Day-24

## st.cache

[st.cache](https://docs.streamlit.io/library/api-reference/performance/st.cache) - Function decorator to memoize function executions.

> st.cache(func=None, persist=False, allow_output_mutation=False, show_spinner=True, suppress_st_warning=False, hash_funcs=None, max_entries=None, ttl=None)

[st.experimental_memo](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo) - Function decorator to memoize function executions - Memoized data is stored in "pickled" form, which means that the return value of a memoized function must be pickleable. Each caller of a memoized function gets its own copy of the cached data.
> st.experimental_memo(func=None, *, persist=None, show_spinner=True, suppress_st_warning=False, max_entries=None, ttl=None)
### Further reading
-   [`st.cache`  API Documentation](https://docs.streamlit.io/library/api-reference/performance/st.cache)
-   [Optimize performance with  `st.cache`](https://docs.streamlit.io/library/advanced-features/caching)
-   [Experimental cache primitives](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
-   [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
-   [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)

## Result

![day24](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-24.PNG)