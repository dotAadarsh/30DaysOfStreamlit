import streamlit as st

st.header('st.latex')

st.write('General Translation equation is given by') 
st.latex(r'''
\begin{bmatrix}
P^*
\end{bmatrix}
=
\begin{bmatrix}
T
\end{bmatrix}
\begin{bmatrix}
P
\end{bmatrix}
''')
st.text('where,\n [p*] =  Translated position matrix of an object \n [T] = Translation matrix\n [P] = Initial position matrix of an object') 
st.text("The final position vector [p*]of a point 'P' to its initial position vector after being translated by a distance 'd' will be:")
st.latex(r'''
p^* = p + d \\
where, \\x^* = x + x_d\\
      y^* = y + y_d\\
      z^* = z + z_d\\
''')
st.text('Matrix form of above equations equations can be written as:')
st.caption('For 2D Translation')
st.latex(r'''
    \begin{bmatrix}
    x^* \\
    y^* \\
    1 
    \end{bmatrix}
     = 
     \begin{bmatrix}
     1 & 0 & x_d \\
     0 & 1 & y_d \\
     0 & 0 & 1  \\     
     \end{bmatrix}
     \begin{bmatrix}
     x \\
     y \\
     1 \\
     \end{bmatrix} 
     ''')