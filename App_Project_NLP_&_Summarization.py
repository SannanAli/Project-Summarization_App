import streamlit as st
import streamlit.components.v1 as stc

from app_home_page import home


PAGE_CONFIG = {
    
    'page_title':'Config_Test',
    'page_icon':'random',
    'layout':'wide',
    'initial_sidebar_state':'expanded'

}

st.set_page_config(**PAGE_CONFIG,)

def main():
    
    stc.html(
        """
        <style>
div {
  color: red;
  width: 100px;
  height: 50px;
  font-weight: bold;
  position: relative;
  animation: mymove 5s infinite;
}
ul {
	
  list-style-type: none;
  margin: 0;
  padding: 50;
  overflow: hidden;
  background-color: #777;
}

li {
  float: left;
}

li a {
 	display: block;
  color: pink;
  text-align: center;
  padding: 10px 50px;
  text-decoration: none;
}

li a:hover {
  background-color: #111;
}
#div1 {animation-timing-function: linear;}


@keyframes mymove {
  from {left: 0px;}
  to {left: 600px;}
}
</style>
</head>
<body>
<ul>
  <li><a class="active"></a></li>
  <div id="div1">Sannan_Technologies</div>
</ul>

</body>
        """
    )

    menu = ['Home','About']
    choise = st.sidebar.selectbox('Menu',menu)

    if choise == 'Home':
        home()

    else:
        st.subheader('About')
    











if __name__ == '__main__':
    main()