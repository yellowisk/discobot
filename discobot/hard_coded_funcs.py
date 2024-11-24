from discobot.hard_coded_games import games

def por_promocao(ta_em_promocao):
    em_promo = []
    
    for game in games:
        if game['on_promotion'] == ta_em_promocao:
            em_promo.append(game)
    return em_promo

def por_genero(este_genero):
    do_genero = []
    
    for game in games:
        if este_genero in game['genres']:
            do_genero.append(game)
    return do_genero

def por_nome(nome_do_jogo: str):
    com_nome = []
    
    for game in games:
        if nome_do_jogo.lower() in game['name'].lower():
            com_nome.append(game)
    return com_nome

def por_nota(nota_min: int, nota_max: int):
    jogos_com_nota = []
    
    for game in games:
        if nota_min <= game['rating'] <= nota_max:
            jogos_com_nota.append(game)
    return jogos_com_nota

def gen_mensagem(jogos: list) -> str:
    mensagens = []
    for jogo in jogos:
        mensagem = f"🎮 **{jogo['name']}**\n" 
        mensagem += f"🌟 **Nota**: {jogo['rating']}/100\n"
        
        if jogo.get("genres"):
            genres_text = ", ".join(jogo["genres"])
            mensagem += f"🗂️ **Gêneros**: {genres_text}\n"
        
        if jogo.get("storyline"):
            mensagem += f"📖 **Storyline**: {jogo['storyline']}\n"
        
        if jogo.get("on_promotion"):
            mensagem += "💸 **Em promoção!** 🎉\n"
        else:
            mensagem += "🛒 **Preço Normal**\n"
        
        mensagens.append(mensagem + "──────────────────────────")
    return "\n\n".join(mensagens) if mensagens else "Nenhum jogo encontrado!"