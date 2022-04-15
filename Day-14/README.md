
# 30DaysOfStreamlit | Day-14

## Streamlit Components

### streamlit_app_1.py

#### Streamlit Pandas Profiling 
> pip install streamlit-pandas-profiling 

[Streamlit Pandas Profiling](https://github.com/ydataai/pandas-profiling) - the pandas profiling report is generated via the `profile_report()` command and displayed using `st_profile_report`
```
pr = df.profile_report()
st_profile_report(pr)
```
#### Result - 1

![day14-1](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-14-1.PNG)

### streamlit_app_2.py

#### 
> pip install py3Dmol
pip install stmol==0.0.7

[streamlit_3dmol](https://github.com/napoles-uach/streamlit_3dmol) - provide an easy way to create a web app for interacting with molecular structures using Streamlit. Use `showmol` function to render py3Dmol objects!
*Example*
```
st.sidebar.title('Show Proteins')
prot_str='1A2C,1BML,1D5M,1D5X,1D5Z,1D6E,1DEE,1E9F,1FC2,1FCC,1G4U,1GZS,1HE1,1HEZ,1HQR,1HXY,1IBX,1JBU,1JWM,1JWS'
prot_list=prot_str.split(',')
bcolor = st.sidebar.color_picker('Pick A Color', '#00f900')
protein=st.sidebar.selectbox('select protein',prot_list)
style = st.sidebar.selectbox('style',['line','cross','stick','sphere','cartoon','clicksphere'])
xyzview = py3Dmol.view(query='pdb:'+protein)
xyzview.setStyle({style:{'color':'spectrum'}})
xyzview.setBackgroundColor(bcolor)
showmol(xyzview, height = 500,width=800)
```
#### Result - 2

![day14-2](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-14-2.PNG)
### streamlit_app_3.py

#### Components API
> st.components.v1.html(html, width=None, height=None, scrolling=False)

[st.components.v1.html](https://docs.streamlit.io/library/components/components-api) - Display an HTML string in an iframe. 
*example*
```
HtmlFile = open("/workspace/30DaysOfStreamlit/Day-14/index.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, width = None, height=500)
```
The above example uses [A-Frame](https://aframe.io/) - A web framework for building 3D/AR/VR experiences to create a 360° Image viewing experience.
#### Result - 3

![day14-3](https://github.com/dotaadarsh/30DaysOfStreamlit/blob/main/asserts/Day-14-3.PNG)