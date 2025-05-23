import streamlit as st

st.sidebar.image('movida_logo.png')
st.sidebar.title('Aluguel de carros')
carros= ['bmw','mustang','hb20','civic','fusca']
carro= st.sidebar.selectbox('selecione o carro alugado',carros)

valor_por_dia=0
if carro == 'bmw':
    valor_por_dia =450
elif carro == 'mustang':
    valor_por_dia = 330
elif carro == 'hb20':
    valor_por_dia = 300
elif carro == 'civic':
    valor_por_dia = 200
elif carro == 'fusca':
    valor_por_dia = 200

st.title('aluguel de carro')
st.write('seja bem vindo(a)')

st.write(f'você selcionou: {carro}')
st.image(f'{carro.upper()}.png')

dias=st.text_input('informe a quantidade de dias')
km=st.text_input('informe a quantidade de quilómetros rodados')

if st.button('calcular'):
    dias= int(dias)
    km= float(km)

    total_dias=valor_por_dia*dias
    total_km=km*0.15
    valor_total= total_dias+total_km

    st.warning(f'Você rodou {km}km por {dias} dias. O valor a pagar é R${valor_total}')
