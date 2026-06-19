import streamlit as st
import json
import requests

st.set_page_config(layout="wide")

with open('pokemon_index.json', 'r', encoding='utf-8') as arquivo:
    nomes_pokemons = json.load(arquivo)

nome = st.selectbox('Escolha um Pokemon', nomes_pokemons.values())

url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
dados_pokemon = requests.get(url).json()

