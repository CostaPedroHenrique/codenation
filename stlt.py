import streamlit as st

def main():
	st.title("Hello world")
	st.markdown('Botão')
	botao = st.button('Botao')
	if botao:
		st.markdown('Clicado')
	
	st.markdown('Checkbox')	
	check = st.checkbox("Checkbox")
	if check:
		st.markdown('Clicado')
		
	st.markdown("Radio")
	radio = st.radio("Escolha as opções", ("op1", "op2"))
	if radio == "op1":
		st.markdown("op1")
	if radio == "op2":
		st.markdown("op2")
		
	st.markdown("Selectbox")
	select = st.selectbox("Choose opt", ('opt1','opt2'))
	if select == "opt1":
		st.markdown("opt1")
	if select == "opt2":
		st.markdown("opt2")
		
	st.markdown("Selectbox")
	mult = st.multiselect("Coose", ("opc1","opc2"))
	if mult == "opc1":
		st.markdown("opc1")
	if mult == "opc2":
		st.markdown("opc2")
		
	st.markdown("File Uploand")
	fil = st.file_uploader("Choose your file", type ="csv")
	if fil is not None:
		st.markdown('Arquivo upado')
	
	
	
		
	
		
if __name__=="__main__":
	main()
