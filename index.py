import requests
import streamlit as st

BASE_URL = "https://api.github.com"

def selecionarUsuario(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"',unsafe_allow_html=True)
    
    st.title('Consulta Github')
    st.subheader("Degmar Barbosa - API GITHUB")
    username = st.text_input('Insira o usaername de usuario do github')

    if st.button('consultar'):
        infoUsuario = selecionarUsuario(username)
        if infoUsuario is not None:
            st.markdown(f'''
            <div class="card" style="width: 18rem;">
                        <img class="card-img-top" src="{infoUsuario['avatar_url']}" alt="Card image cap">
           
            
            <div class="card-body">
            <h5 class="card-title">{infoUsuario['login']}</h5>
            <p class="card-text">{infoUsuario['bio']}</p>
            <a href="{infoUsuario['html_url']}" class="btn btn-primary">Ver Perfil</a>
            </div>
            
            </div>          

                        ''',unsafe_allow_html=True)

ui()
