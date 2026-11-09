import streamlit as st

# BARRA LATERAL
# ==========================================
with st.sidebar:
  st.markdown("### Mi primera barra lateral de Streamlit")
  st.text("¡Hola, Barra Lateral!")
  st.text("Esto es una barra lateral")

  # Imagen (puedes reemplazar la ruta o URL por la imagen del logo)
  st.image(
      "logo_uss.jpg",
      width=200,
  )

  # Botón en la barra lateral
  if st.button("Haz clic pero en la barra lateral"):
    st.write("¡Botón de la barra lateral presionado!")

  # Campo de texto y su respectiva salida
  texto_barra = st.text_input("Escribe algo en la barra:")
  st.write(f"Escribiste en la barra: {texto_barra}")

# ==========================================
# ÁREA PRINCIPAL
# ==========================================
st.title("Mi primera aplicación de Streamlit")

st.markdown("### ¡Hola, Streamlit!")
st.text("Esta es una aplicación simple")

# Imagen en el área principal
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/e/ec/Logo_Universidad_San_Sebasti%C3%A1n.png",
    width=300,
)

# Botón principal
if st.button("Haz clic"):
  st.write("¡Botón principal presionado!")

# Campo de texto principal y su respectiva salida
texto_principal = st.text_input("Escribe algo:")
st.write(f"Escribiste: {texto_principal}")
