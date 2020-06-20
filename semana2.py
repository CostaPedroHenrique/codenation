import streamlit as st
import pandas as pd
import base64

def main():
	st.image("images/codenation.png")
	st.title("Aceleradev Data Science")
	st.image("images/panda.gif")
	arq = st.file_uploader("Escolha um arquivo para analisar", type="csv")
	if arq is not None:
		df = pd.read_csv(arq)
		lines = df.shape[0]
		cols = df.shape[1]
		st.markdown("**Numero de linhas**: {}".format(lines))
		st.markdown("**Numero de colunas**: {}".format(cols))
		st.markdown("Colunas")
		dados = pd.DataFrame({"Colunas": df.columns, "Tipos": df.dtypes[2]})
		n_lines = st.slider("Numeros de linhas", 1, lines)
		n_cols = st.slider("Numero de colunas", 1, cols)
		st.markdown("Colunas X Tipos")
		st.table(dados.iloc[ :n_cols , : ])
		radio = st.radio("Como deseja visualizar o dataframe?", ("Dataframe", "Tabela"))
		if radio == "Dataframe":
			st.dataframe(df.iloc[:,:n_cols].head(n_lines))
		if radio == "Tabela":
			st.markdown("Table")
			st.table(df.iloc[:,:n_cols].head(n_lines))
		
	
if __name__=="__main__":
	main()
