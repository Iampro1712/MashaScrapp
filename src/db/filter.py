from pyrogram import Client, filters

#Tiene que poner solamente el api_id y api_hash porque solo se usa la cuenta, no un bot en especifico, para quitar el error de is not defined tienes que hacer las variables con sus respectivos valores o configurar con env.
app = Client("my_account", api_id=api_id, api_hash=api_hash)
#Editar array id_group para que funcione el id_group
id_group = []
@app.on_message(filters.chat(id_group))
def handle_messages(client, message):
    app.send_message(chat_id = id_group, text = message.text)

app.run()