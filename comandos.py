import discord
from main import bot


class MenuView(discord.ui.View):
    def __init__(self, custom_id):
        super().__init__()
        self.custom_id = custom_id
    @discord.ui.button(label="Fantasmas", style=discord.ButtonStyle.primary, custom_id="botao_fantasmas")
    async def button_fantasmas(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.custom_id == "menu_inicial":
            await menu_fantasmas(interaction, ephemeral=True)
            
    @discord.ui.button(label="Equipamentos", style=discord.ButtonStyle.primary, custom_id="botao_equipamentos")
    async def button_equipamentos(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.custom_id == "menu_inicial":
            await interaction.response.send_message("Você clicou em Equipamentos!", ephemeral=True)

    @discord.ui.button(label="Dicas", style=discord.ButtonStyle.primary, custom_id="botao_dicas")
    async def button_dicas(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.custom_id == "menu_inicial":
            await interaction.response.send_message("Você clicou em Dicas!", ephemeral=True)


class MenuFantasmas(discord.ui.Select):

    def __init__(self):
        
        options = [
            discord.SelectOption(label="Spirit", value="Spirit"),
            discord.SelectOption(label="Wraith", value="Wraith"),
            discord.SelectOption(label="Phantom", value="Phantom"),
            discord.SelectOption(label="Poltergeist", value="Poltergeist"),
            discord.SelectOption(label="Banshee", value="Banshee"),
            discord.SelectOption(label="Jinn", value="Jinn"),
            discord.SelectOption(label="Mare", value="Mare"),
            discord.SelectOption(label="Revenant", value="Revenant"),
            discord.SelectOption(label="Shade", value="Shade"),
            discord.SelectOption(label="Demon", value="Demon"),
            discord.SelectOption(label="Yurei", value="Yurei"),
            discord.SelectOption(label="Oni", value="Oni"),
            discord.SelectOption(label="Yokai", value="Yokai"),
            discord.SelectOption(label="Hantu", value="Hantu"),
            discord.SelectOption(label="Goryo", value="Goryo"),
            discord.SelectOption(label="Myling", value="Myling"),
            discord.SelectOption(label="Onryo", value="Onryo"),
            discord.SelectOption(label="The Twins", value="The Twins"),
            discord.SelectOption(label="Raiju", value="Raiju"),
            discord.SelectOption(label="Obake", value="Obake"),
            discord.SelectOption(label="The Mimic", value="The Mimic"),
            discord.SelectOption(label="Moroi", value="Moroi"),
            discord.SelectOption(label="Deogen", value="Deogen"),
            discord.SelectOption(label="Thaye", value="Thaye"),
        ]
        super().__init__(placeholder="Escolha uma opção...", options=options)

    async def callback(self, interaction: discord.Interaction):
        selected_value = self.values[0]
        if selected_value == "Spirit":
            await menu_spirit(interaction, ephemeral=True)
        elif selected_value == "Wraith":
            await menu_wraith(interaction, ephemeral=True)
        elif selected_value == "Phantom":
            await menu_phantom(interaction, ephemeral=True)
        else:
            await interaction.response.send_message(f"Você escolheu: {selected_value}", ephemeral=True)
class ViewFantasmas(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(MenuFantasmas())



async def menu_fantasmas(interaction, ephemeral):
        with open('imgs\Screenshot_18.png', 'rb') as background_img, \
             open('imgs\Screenshot_13.png', 'rb') as autor_img, \
             open('imgs\pentagram_PNG3.png', 'rb') as thumbnail_img:    
                
                autor_file = discord.File(autor_img, filename="autor.png")
                thumbnail_file = discord.File(thumbnail_img, filename="thumbnail.png")
                background_file = discord.File(background_img, filename="background.png")

                embed = discord.Embed(title="Fantasmas", description="Fantasmas presentes na versão atual:", color=discord.Color.red())

                embed.set_author(name="PhasmoBuster 0.1", icon_url="attachment://autor.png")

                embed.set_footer(text="Versão: 0.1", icon_url="attachment://autor.png")
                embed.set_thumbnail(url="attachment://thumbnail.png")
                embed.set_image(url="attachment://background.png")

                view = ViewFantasmas()
                await interaction.response.send_message(embed=embed, files=[autor_file, thumbnail_file, background_file], view=view, ephemeral=ephemeral)



async def menu_spirit(interaction, ephemeral):
         with open('imgs\spirit.png', 'rb') as background_img, \
             open('imgs\Screenshot_13.png', 'rb') as autor_img, \
             open('imgs\spirit_icon.png', 'rb') as thumbnail_img:    
                
                autor_file = discord.File(autor_img, filename="autor.png")
                thumbnail_file = discord.File(thumbnail_img, filename="thumbnail.png")
                background_file = discord.File(background_img, filename="background.png")

                embed = discord.Embed(title="SPIRIT", description="São fantasmas muito comuns. Eles são muito poderosos, mas passivos, atacando apenas quando necessário. Eles defendem seu local de morte ao máximo, matando qualquer um que seja pego ultrapassando o tempo de suas boas-vindas.”", color=discord.Color.red())

                embed.set_author(name="PhasmoBuster 0.1", icon_url="attachment://autor.png")

                embed.add_field(name="Habilidade", value="Nenhuma.", inline=True)
                embed.add_field(name="Fraquezas", value="Mais fracos a INCENSOS, prevenindo caçadas por mais tempo (180 segundos).", inline=False)
                embed.add_field(name="Evidências", value="EMF (5) - Spirit Box - Escrita Fantasma", inline=False)
                embed.add_field(name="Dados", value="Caça: 50% de sanidade\n Velocidade: Normal (1.7 metros p/segundo)\n  ", inline=False)
                embed.add_field(name="Dicas", value="Como não possui nenhuma habilidade caracteristica, a melhor forma de se realizar um teste contra uma Spirit é utilizando o incenso. Caso o fantasma cace em menos de 3 minutos após o uso, não é uma Spirit.", inline=False)

                embed.set_footer(text="Versão: 0.1", icon_url="attachment://autor.png")
                embed.set_thumbnail(url="attachment://thumbnail.png")
                embed.set_image(url="attachment://background.png")

                view = ViewFantasmas()
                await interaction.response.send_message(embed=embed, files=[autor_file, thumbnail_file, background_file], view=view, ephemeral=ephemeral)    

async def menu_wraith(interaction, ephemeral):
         with open('imgs\wraith.png', 'rb') as background_img, \
             open('imgs\Screenshot_13.png', 'rb') as autor_img, \
             open('imgs\wraith_icon.png', 'rb') as thumbnail_img:    
                
                autor_file = discord.File(autor_img, filename="autor.png")
                thumbnail_file = discord.File(thumbnail_img, filename="thumbnail.png")
                background_file = discord.File(background_img, filename="background.png")

                embed = discord.Embed(title="WRAITH", description="São um dos fantasmas mais perigosos que você encontrará. É também o único fantasma conhecido que tem a habilidade de voar e às vezes é conhecido por viajar através de paredes.", color=discord.Color.red())

                embed.set_author(name="PhasmoBuster 0.1", icon_url="attachment://autor.png")

                embed.add_field(name="Habilidade", value="Não pode ser rastreada por pegadas\n Ocasionalmente vai se teleportar para algum jogador", inline=True)
                embed.add_field(name="Fraquezas", value="Nunca pisará no sal.", inline=False)
                embed.add_field(name="Evidências", value="EMF (5) - Spirit Box - Projetor DOTS", inline=False)
                embed.add_field(name="Dados", value="Caça: 50% de sanidade\n Velocidade: Normal (1.7 metros p/segundo)\n  ", inline=False)
                embed.add_field(name="\n\nDicas - TELEPORTE", value="**Formas de se identificar uma Wraith devido sua habilidade de teleporte:**\n   \n-> Ao se teleportar para algum jogador, o EMF apitará no nível 2 ou 5 na sua nova localização\n    -> Não se teleporta durante caçadas\n    -> Caso ocorram muitas interações longe do quarto favorito do fantasma e perto de onde algum jogador esteja, talvez seja sua habilidade de teleporte\n    -> EMF apitando aleatoriamente no nível 2 ou 5, sem que nenhuma interação do fantasma tenha ocorrido (especialmente longe do quarto favorito do fantasma)\n", inline=False)
                embed.add_field(name="Dicas - SAL", value="**Formas de se identificar uma Wraith utilizando sal (independente do tier):**\n   \n-> Não sofrerá a lentidão causada pelo sal (tier 3) durante uma caçada\n    -> Deixando o sal abaixo de um sensor de movimento, caso o fantasma passe pelo sensor e o sal continue intacto, é uma Wraith. \n    -> Deixando o sal no centro de um circulo de invocação e summonando o fantasma, caso ele continue intacto, é uma Wraith \n", inline=False)
                embed.add_field(name="Cuidados a se tomar", value="Embora o teletransporte da Wraith não desencadeie por si só uma chance de caçar, ela poderia caçar do local para onde se teletransportou se atender aos requisitos normais de caça. Isso torna perigoso estar em quase qualquer lugar dentro da área de investigação quando a sanidade média estiver baixa o suficiente (50%); evite ser pego de surpresa pela Wraith.", inline=False)
                embed.set_footer(text="Versão: 0.1", icon_url="attachment://autor.png")
                embed.set_thumbnail(url="attachment://thumbnail.png")
                embed.set_image(url="attachment://background.png")

                view = ViewFantasmas()
                await interaction.response.send_message(embed=embed, files=[autor_file, thumbnail_file, background_file], view=view, ephemeral=ephemeral)    

async def menu_phantom(interaction, ephemeral):
         with open('imgs\phantom.png', 'rb') as background_img, \
             open('imgs\Screenshot_13.png', 'rb') as autor_img, \
             open('imgs\phantom_icon.png', 'rb') as thumbnail_img:    
                
                autor_file = discord.File(autor_img, filename="autor.png")
                thumbnail_file = discord.File(thumbnail_img, filename="thumbnail.png")
                background_file = discord.File(background_img, filename="background.png")

                embed = discord.Embed(title="PHANTOM", description="São um dos fantasmas mais perigosos que você encontrará. É também o único fantasma conhecido que tem a habilidade de voar e às vezes é conhecido por viajar através de paredes.", color=discord.Color.red())

                embed.set_author(name="PhasmoBuster 0.1", icon_url="attachment://autor.png")

                embed.add_field(name="Habilidade", value="Não pode ser rastreada por pegadas\n Ocasionalmente vai se teleportar para algum jogador", inline=True)
                embed.add_field(name="Fraquezas", value="Nunca pisará no sal.", inline=False)
                embed.add_field(name="Evidências", value="EMF (5) - Spirit Box - Projetor DOTS", inline=False)
                embed.add_field(name="Dados", value="Caça: 50% de sanidade\n Velocidade: Normal (1.7 metros p/segundo)\n  ", inline=False)
                embed.add_field(name="\n\nDicas - TELEPORTE", value="**Formas de se identificar uma Wraith devido sua habilidade de teleporte:**\n   \n-> Ao se teleportar para algum jogador, o EMF apitará no nível 2 ou 5 na sua nova localização\n    -> Não se teleporta durante caçadas\n    -> Caso ocorram muitas interações longe do quarto favorito do fantasma e perto de onde algum jogador esteja, talvez seja sua habilidade de teleporte\n    -> EMF apitando aleatoriamente no nível 2 ou 5, sem que nenhuma interação do fantasma tenha ocorrido (especialmente longe do quarto favorito do fantasma)\n", inline=False)
                embed.add_field(name="Dicas - SAL", value="**Formas de se identificar uma Wraith utilizando sal (independente do tier):**\n   \n-> Não sofrerá a lentidão causada pelo sal (tier 3) durante uma caçada\n    -> Deixando o sal abaixo de um sensor de movimento, caso o fantasma passe pelo sensor e o sal continue intacto, é uma Wraith. \n    -> Deixando o sal no centro de um circulo de invocação e summonando o fantasma, caso ele continue intacto, é uma Wraith \n", inline=False)
                embed.add_field(name="Cuidados a se tomar", value="Embora o teletransporte da Wraith não desencadeie por si só uma chance de caçar, ela poderia caçar do local para onde se teletransportou se atender aos requisitos normais de caça. Isso torna perigoso estar em quase qualquer lugar dentro da área de investigação quando a sanidade média estiver baixa o suficiente (50%); evite ser pego de surpresa pela Wraith.", inline=False)
                embed.set_footer(text="Versão: 0.1", icon_url="attachment://autor.png")
                embed.set_thumbnail(url="attachment://thumbnail.png")
                embed.set_image(url="attachment://background.png")

                view = ViewFantasmas()
 
                await interaction.response.send_message(embed=embed, files=[autor_file, thumbnail_file, background_file], view=view, ephemeral=ephemeral)


@bot.command()
async def sobre(ctx):  
        with  open('imgs\Screenshot_13.png', 'rb') as autor_img, \
                open('imgs\pentagram_PNG3.png', 'rb') as thumbnail_img:
                
                autor_file = discord.File(autor_img, filename="autor.png")
                thumbnail_file = discord.File(thumbnail_img, filename="thumbnail.png")

                embed = discord.Embed(description="Sobre:", color=discord.Color.blue())

                embed.set_author(name="PhasmoBuster 0.1", icon_url="attachment://autor.png")

                embed.add_field(name="Versão 0.1 (Atual)", value="Conteúdo adicionado na 0.1: Menu de Fantasmas (Em construção)")
                embed.add_field(name="Versão 0.2 (EM BREVE)", value="Conteúdo previsto para a 0.2: Menu de Equipamentos", inline=False)
                embed.set_footer(text="Versão: 0.1", icon_url="attachment://autor.png")
                embed.set_thumbnail(url="attachment://thumbnail.png")

                await ctx.send(embed=embed, files=[autor_file, thumbnail_file])

 
@bot.command()
async def ajuda(ctx):
    
    with  open('imgs\Screenshot_13.png', 'rb') as autor_img, \
          open('imgs\pentagram_PNG3.png', 'rb') as thumbnail_img:
        
        autor_file = discord.File(autor_img, filename="autor.png")
        thumbnail_file = discord.File(thumbnail_img, filename="thumbnail.png")

        embed = discord.Embed(description="Primeiros passos:", color=discord.Color.green())

        embed.set_author(name="PhasmoBuster 0.1", icon_url="attachment://autor.png")

        embed.add_field(name="Menu", value="Para começar, digite !menu")
        embed.add_field(name="Sobre", value="Informações sobre o BOT, digite !sobre", inline=False)
        embed.set_footer(text="Versão: 0.1", icon_url="attachment://autor.png")
        embed.set_thumbnail(url="attachment://thumbnail.png")

        await ctx.send(embed=embed, files=[autor_file, thumbnail_file])

#Menu
@bot.command()
async def menu(ctx):
    with open('imgs\Screenshot_17.png', 'rb') as background_img, \
         open('imgs\Screenshot_13.png', 'rb') as autor_img, \
         open('imgs\pentagram_PNG3.png', 'rb') as thumbnail_img:
        
        autor_file = discord.File(autor_img, filename="autor.png")
        thumbnail_file = discord.File(thumbnail_img, filename="thumbnail.png")
        background_file = discord.File(background_img, filename="background.png")

        embed = discord.Embed(title="MENU", description="Todos os comandos disponíveis:", color=discord.Color.green())

        embed.set_author(name="PhasmoBuster 0.1", icon_url="attachment://autor.png")

        embed.add_field(name="Fantasmas", value="Todas as informações dos fantasmas reunidas.", inline=True)
        embed.add_field(name="Equipamentos", value="Informações de equipamentos.", inline=True)
        embed.add_field(name="Dicas", value="Dicas ''secretas'' que o jogo esconde.", inline=True)

        embed.set_footer(text="Versão: 0.1", icon_url="attachment://autor.png")
        embed.set_thumbnail(url="attachment://thumbnail.png")
        embed.set_image(url="attachment://background.png")

        view = MenuView(custom_id="menu_inicial")
        await ctx.send(embed=embed, files=[autor_file, thumbnail_file, background_file], view=view)


@bot.command()
async def fantasmas(interaction, ephemeral):
                await interaction.response.send_message(menu_fantasmas)    
    