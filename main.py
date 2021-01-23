import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
client = discord.Client()

sad = [
    "sad", "depressed", "depressing", "painful", "pissed", "fml", "lonely",
    "Lonely"
]

artifacts_bad = [
    "trash artifacts", "shit artifacts", "bad stats", "Fuck RNG",
    "Fuck rng"
]

artifacts_good = ["Noice"]

insult_bot = [
    "Fuck you bot", "Fuck off bot", "I hate this bot", "Fuck this bot"
]

praise_bot = [
    "This bot is awesome", "This bot is great", "This bot is nice",
    "Thanks bot", "Nice bot"
]

encourage = [
    "Cheer up!", "Hang in there.", "You'll get there", "You'll be fine",
    "It gets better", "I'm here for You", "Cheer Up"
]

encourage_art = [
    "Keep trying", "You will find something better", "Don't worry about it",
    "Chillax"
]

good_art = [
    "That's great", "Congratulations", "Keep it up", "GG", "Good for you !", "Toit"]

retort = [
    "Bitch please", "Fuck You M8", "Don't get sassy, my creator's a badass",
    "No U"
]

thanks = ["Thanks mah man", "Love you guys", "Thanks guys", "Anytime"]

hello = ["Hi! Nice to meet you!", "Hola!", "T'sup mah dude..", "Suh dude"]


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	return (quote)


@client.event
async def on_message(message):
  msg = message.content
  if msg.lower().startswith('$daily'):
    await message.channel.send(file=discord.File('daily.png'))
  if msg.lower().startswith('$talent'):
    await message.channel.send(file=discord.File('AXO-Genshin-Talent-Book.jpg'))
  if msg.lower().startswith('$drops'):
    await message.channel.send(file=discord.File('Drops.png'))
  if msg.lower().startswith('$respawn'):
    await message.channel.send(file=discord.File('Respawn.png'))  
  if msg.lower().startswith('$weapon'):
    await message.channel.send(file=discord.File('WeaponCheat.png'))
  if msg.lower().startswith('$char'):
    await message.channel.send(file=discord.File('Char_ascend.png'))
  if msg.lower().startswith('$currency'):
    await message.channel.send(file=discord.File('currency.png'))
  if msg.lower().startswith('$hello'):
    await message.channel.send(random.choice(hello))
  if msg.lower().startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  if msg.lower().startswith('$artifact'):
    await message.channel.send(file=discord.File('Artifact.jpg'))
  if msg.lower().startswith('$quantity'):
    await message.channel.send(file=discord.File('Quantity.jpg'))
  if any(word in msg for word in sad):
    await message.channel.send(random.choice(encourage))
  if any(word in msg for word in artifacts_bad):
    await message.channel.send(random.choice(encourage_art))
  if any(word in msg for word in artifacts_good):
    await message.channel.send(random.choice(good_art))
  if any(word in msg for word in insult_bot):
    await message.channel.send(random.choice(retort))
  if any(word in msg for word in praise_bot):
    await message.channel.send(random.choice(thanks))

  
  if msg.startswith('$buildamberdps'):
    embed = discord.Embed(
		    title="Amber Pyro/Support Build",
		    description=
		    "**This build empowers Amber's Elemental Skill and Burst abilities.**\n\nPreferred weapon: Stringless/ Skyward Harp\nPreferred artifacts:  4-set Noblesse Oblige OR 2-set Gladiator's Finale,2-set Crimson Witch of Flames",
		    color=0xFF0000)
    embed.add_field(name="**Recommended Stats**",value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nATK%, with the option for CRIT% on your helmet slot and Pyro Damage on your goblet. Secondary stats to focus on are CRIT%, CRIT DMG, and ATK or Elemental Recharge, depending on your build.",
		    inline=False)
    thumb = discord.File('Character_Amber_Card.jpg')
    embed.set_thumbnail(url='attachment://Character_Amber_Card.jpg')
    await message.channel.send(embed=embed, file=thumb)
  if msg.startswith('$buildambersupport'):
    embed = discord.Embed(title="Amber Aimed Shot Build",
		    description="**The idea behind this build is to fire a powerful, fully charged Aimed Shot with Amber every 10 seconds, taking advantage of the extra arrow from her first constellation, One Arrow to Rule Them All.**\n\nPreferred weapon: Sharpshooter's Oath/ Messenger\nPreferred artifacts: 4-set Wanderer's Troupe",color=0xFF0000)
    embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nStacking some Elemental Mastery, in which case you’d want to run an Artifact set like Instructor. Experiment with a few different builds and see what you enjoy playing most.",
		    inline=False)
    thumb = discord.File('Character_Amber_Card.jpg')
    embed.set_thumbnail(url='attachment://Character_Amber_Card.jpg')
    await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildjeandps'):
    embed = discord.Embed(
		    title="Jean Physical DPS Build",
		    description=
		    "**This build empowers Jean's physical damage output, turning her into a reliable hybrid between a DPS and a healer.**\n\nPreferred weapon: Aquila Favonia/ Prototype Rancour\nPreferred artifacts: 4-set Gladiator's Finale OR 2-set Bloodstained Chevalier, 2-set Gladiator's Finale",
		    color=0x98FB98)
    embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nDepending on how you want to play Jean, you may want to prioritize your stats a little differently. In general, we would recommend focusing on ATK%, CRIT%, CRIT DMG, and Energy Recharge. With these stats, you can focus on pumping out some serious damage while Jean’s out on the field and healing up the party.",
		    inline=False)
    thumb = discord.File('Character_Jean_Card.jpg')
    embed.set_thumbnail(url='attachment://Character_Jean_Card.jpg')
    await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildjeansupport'):
    embed = discord.Embed(
		    title="Jean Anemo Support Build",
		    description=
		    "**This build empowers Jean's Elemental Burst ability to maximize her healing, while simultaneously reducing enemies' Elemental RES for the rest of your party.**\n\nPreferred weapon: Skyward Blade/ Favonius Sword\nPreferred artifacts: 2,4-set Noblesse Oblige OR 2,4-set Viridescent Venerer",
		    color=0x98FB98)
    embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nStacking some Elemental Mastery, Energy Recharge, ATK% and Anemo DMG Bonus%, in which case you’d want to run an Artifact set as shown above. Experiment with a few different builds and see what you feel is best.",
		    inline=False)
    thumb = discord.File('Character_Jean_Card.jpg')
    embed.set_thumbnail(url='attachment://Character_Jean_Card.jpg')
    await message.channel.send(embed=embed, file=thumb)
  
  if msg.startswith('$buildlisasupport'):
    embed = discord.Embed(
		    title="Lisa Electro Support Build",
		    description=
		    "**This build empower's Lisa's Elemental Burst abilty. It would be much stronger if it didn't knock enemies out of it, but it can be very powerful on bosses.**\n\nPreferred weapon: The Widsith/ Mappa Mare\nPreferred artifacts: 2,4-set Noblesse Oblige or Thundering Fury",
		    color=0x800080)
    embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nAs far as primary stats go, it would help if you focused on ATK% on all your Artifacts, except for the Electro damage bonus on your Goblet, with some Energy Recharge.",
		    inline=False)
    thumb = discord.File('Character_Lisa_Card.jpg')
    embed.set_thumbnail(url='attachment://Character_Lisa_Card.jpg')
    await message.channel.send(embed=embed, file=thumb)
  if msg.startswith('$buildlisadps'):
	  embed = discord.Embed(
		    title="Lisa Electro DPS Build",
		    description=
		    "**This build empower's Lisa's Normal Attack, Charged Attack and Elemental Skill/Burst**\n\nPreferred weapon: Skyward Atlas/ Favonius Codex\nPreferred artifacts: 2,4-set Noblesse Oblige or Thundering Fury, The Exile and Wanderer's Troupe works too.",
		    color=0x800080)
	  embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nIf you plan to focus on doing pure DPS with Lisa, you could go for CRIT% on your Circlet Artifact instead of ATK. For secondary stats, try and beef up Lisa’s Elemental Mastery and Elemental Recharge to maximize damage and ability uptime.",
		    inline=False)
	  thumb = discord.File('Character_Lisa_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Lisa_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildkaeyadps'):
  	embed = discord.Embed(
		    title="Kaeya Cryo DPS Build",
		    description=
		    "**This build empower's Kaeya's Normal Attack, Charged Attack and Elemental Skill/Burst**\n\nPreferred weapon:  Cool Steel / Prototype Rancour\nPreferred artifacts: 2,4-set Noblesse Oblige or Gladiator's Finale, Berserker and Exile works too.",
		    color=0xd6ecef)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nKaeya’s elemental abilities do more damage based on your ATK stat. For that reason, the primary stat to focus on is ATK% for your Artifacts. You can also try and go for a Goblet with Cryo bonus damage if you can get lucky enough. For secondary stats, focus on CRIT%, CRIT damage, and ATK. You can throw on some Elemental Mastery or Energy Recharge if you must, but his cooldowns are already very short. ",
		    inline=False)
  	thumb = discord.File('Character_Kaeya_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Kaeya_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildkaeyasupport'):
    embed = discord.Embed(
  	    title="Kaeya Cryo Support Build",
  	    description=
		    "**This build empowers Kaeya's Elemental Burst ability which procs multiple times, leading to very consistent elemental reactions and damage. This build becomes much more powerful with Constellation level 6.**\n\nPreferred weapon:  Skyward Blade / Favonius Sword\nPreferred artifacts: 2,4-set Noblesse Oblige or 2,4-set Instructor's set.",
		    color=0xd6ecef)
    embed.add_field(name="**Recommended Stats**", value="*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nKaeya’s elemental abilities do more damage based on your ATK stat. For that reason, the primary stat to focus on is ATK% for your Artifacts. You can also try and go for a Goblet with Cryo bonus damage if you can get lucky enough. For secondary stats, focus on CRIT%, CRIT damage, and ATK. You can throw on some Elemental Mastery or Energy Recharge for most effective results.",inline=False)
    thumb = discord.File('Character_Kaeya_Card.jpg')
    embed.set_thumbnail(url='attachment://Character_Kaeya_Card.jpg')
    await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildbarbarasupport'):
	  embed = discord.Embed(
		    title="Barbara Hydro Healer Build",
		    description=
		    "**While she won't increase your team's damage output, Barbara will keep all your units alive and healthy. We empower her healing by stacking HP.**\n\nPreferred weapon:  Thrilling Tales of Dragon Slayers / Prototype Malice\nPreferred artifacts: 2,4-set Maiden's Beloved set, Scholar or Instructor sets.",
		    color=0x0000FF)
	  embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nBarbara’s healing abilities scale with her HP, so you want to max this stat and focus it on every piece of gear. You’ll want to roll double HP on all your artifacts, if possible. The more HP Barbara has, the more effective her healing numbers will be.",
		    inline=False)
	  thumb = discord.File('Character_Barbara_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Barbara_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildbarbaradps'):
    embed = discord.Embed(
		    title="WTF",
		    description="**Do you know how this character works?**\nBut to satisfy your urges, Barbara needs a very specific setup to deal those unrealistic numbers that youtubers and streamers influenced you with.\nPreferred Weapon: Widsith/Skyward Atlas/Lost Prayer of the Sacred Winds.\nPreferred Sets: 4-set Wanderer's Troupe, or 4-set Heart of Depth, either is fine.",
		    color=0x0000FF)
    embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nOverall, focus on ATK%, CRIT%, CRIT DMG and Hydro Dmg Bonus Goblet. Deciding between ATK% and CRIT% priority is up to you, as they seem to have around the same effect on damage. Elemental Mastery Substats are fine too.\nYou must keep in mind that the high dmg numbers are in conjuntion with food buffs, abnormal levels of crit rate and damage, with Bennet ult buff and sucrose to decrease hydro Resistance by 30% using the 4-set Viridescent Venerer. YOU HAVE BEEN WARNED",
		    inline=False)
    thumb = discord.File('Character_Barbara_Card.jpg')
    embed.set_thumbnail(url='attachment://Character_Barbara_Card.jpg')
    await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$builddilucsupport'):
	  embed = discord.Embed(
		    title="WTF",
		    description="**Do you know how this character works?**",
		    color=0xFF0000)
	  thumb = discord.File('Character_Diluc_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Diluc_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$builddilucdps'):
	  embed = discord.Embed(
		    title="Diluc Pyro DPS Build",
		    description=
		    "**This build can work without any constellations, making Diluc an unstoppable Pyro DMG dealing Machine !**\n\nPreferred weapon: Wolf's Gravestone / Prototype Aminus\nPreferred artifacts: 2,4-set Crimson Witch of Flames, 2,4-set Gladiator's Finale or Berserker sets.",
		    color=0xFF0000)
	  embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nOverall, focus on ATK%, CRIT%, CRIT DMG, and ATK in the endgame. Deciding between ATK% and CRIT% priority is up to you, as they seem to have around the same effect on damage. Diluc also benefits from Pyro damage increases, because he uses his elemental skill more than other characters.",
		    inline=False)
	  thumb = discord.File('Character_Diluc_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Diluc_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildrazordps'):
	  embed = discord.Embed(
		    title="Razor Electro DPS Build",
		    description=
		    "**This build empowers Razor's physical damage and electro damage output, synergising with the bonuses from his Lightning Fang burst skill.**\n\nPreferred weapon: Wolf's Gravestone / Prototype Aminus/ Debate Club\nPreferred artifacts: 2,4-set Thundering Fury, 2,4-set Gladiator's Finale or Berserker sets.",
		    color=0x800080)
	  embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nAs is the case with most carry DPS in Genshin Impact, you want to focus primarily on ATK and ATK% with Razor. His abilities scale with ATK, so pumping up these stats will give you a noticeable DPS increase. Both the Prototype Aminus and Wolf’s Gravestone claymores provide Base ATK and ATK, so make sure to use one of these two weapons.",
		    inline=False)
	  thumb = discord.File('Character_Razor_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Razor_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildrazorsupport'):
	  embed = discord.Embed(
		    title="Nope.",
		    description=
		    "**Razor is a solo DPS carry, and has no viable support builds whatsoever. Please use the characters as intended. Peace**",
		    color=0x800080)
	  thumb = discord.File('Character_Razor_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Razor_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildventidps'):
	  embed = discord.Embed(
		    title="Venti Anemo DPS Build",
		    description=
		    "**This build focuses mainly on dealing damage while providing skill support**\n\nPreferred weapon: Favonius Warbow/ Stringless\nPreferred artifacts: 2,4-set Instructor Set, 2,4-set Viridiscent Venerer",
		    color=0x98FB98)
	  embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nLike other carry units in Genshin Impact, you want to focus on ATK and ATK% early on in the game with Venti. As you get better gear and artifacts, we recommend focusing exclusively on ATK% and CRIT% to maximize your damage output. You may want to focus on sets with Elemental Mastery stats early in the game for significant elemental burst damage. Anemo dmg% on your goblet helps too.",
		    inline=False)
	  thumb = discord.File('Character_Venti_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Venti_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildventisupport'):
	  embed = discord.Embed(
		    title="Venti Anemo Support Build",
		    description=
		    "**This build focuses mainly on providing skill support and ULT spamming**\n\nPreferred weapon: Favonius Warbow/ Stringless\nPreferred artifacts: 2,4-set Noblesse Oblige, 2,4-set Viridiscent Venerer",
		    color=0x98FB98)
	  embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nWith Venti's support build, you need to focus on generating energy for your team and Venti him(her?)self. Spamming ULT while dishing out some damage should be your focal point. Energy recharge%,Elemental Mastery and some crit rate or dmg should do the trick. The goblet, ideally should have anemo dmg%",
		    inline=False)
	  thumb = discord.File('Character_Venti_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Venti_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildkleedps'):
	  embed = discord.Embed(
		    title="Klee Pyro DPS Build",
		    description=
		    "**Klee's highest damage source comes from spamming her charged attack and she really comes online when paired with Bennet's ultimate, more so than Diluc.**\n\nPreferred weapon: Mappa Mare/ Solar Pearl/ Widsith/ Lost Prayer to the Sacred Winds/ Skyward Atlas\nPreferred artifacts: 2-set Crimson witch of Flames+ 2-set Gladiator OR 4-set Crimson Witch of Flames OR 4-set Wanderer's Troupe(For increased charged atk damage)",
		    color=0xFF0000)
	  embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nThe main stats you want to focus on with Klee are CRIT chance and CRIT damage. Other stats to pay attention to are ATK%, followed by Energy Recharge and ATK. If you plan to go pure Pyro damage with Klee, look at the Crimson Witch of Flames set to boost your Pyro Damage and consider making Pyro damage another stat to focus on for your Goblet slot.",
		    inline=False)
	  thumb = discord.File('Character_Klee_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Klee_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildkleesupport'):
	  embed = discord.Embed(
		    title="Why ?",
		    description=
		    "**Why would you want her off the field ? She is a main DPS unit. Use others for support. Leave her alone.**",
		    color=0xFF0000)
	  thumb = discord.File('Character_Klee_Card.jpg')
	  embed.set_thumbnail(url='attachment://Character_Klee_Card.jpg')
	  await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildbennettdps'):
  	embed = discord.Embed(
		    title="Bennett Pyro DPS Build",
		    description=
		    "**This build empowers Bennett's physical damage output, ignoring his Elemental Skill completely. We're looking for the highest Base ATK possible to empower his Elemental Burst skill.**\n\nPreferred weapon: Aquila Favonia/ Skyward Blade/ Skyrider Sword/ The Flute\nPreferred artifacts: 2-set Gladiator+ 2-set Bloodstained Chivalry OR 4-set Gladiator",
		    color=0xFF0000)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nWhen it comes to stats, you’ll want to focus on the usual DPS carry stats, which are ATK%, CRIT%, CRIT DMG, and ATK. Instead of ATK, you can concentrate on Elemental Mastery or even Energy Recharge. Additionally, you can run Pyro Damage on your Goblet artifact to get a nice damage boost as support. Consider making Pyro damage another stat to focus on for your Goblet slot.",
		    inline=False)
  	thumb = discord.File('Character_Bennett_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Bennett_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildbennettsupport'):
  	embed = discord.Embed(
		    title="Bennett Pyro Support Build",
		    description=
		    "**This build focuses on empowering Bennett's burst skill by stacking Energy Recharge. Keep in mind that the bonus ATK given to his Elemental Burst skill only comes from Base ATK, not ATK%.**\n\nPreferred weapon: Aquila Favonia/ Skyward Blade/ Favonius Sword/ The Flute\nPreferred artifacts: 4-set Noblesse Oblige",
		    color=0xFF0000)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nWhen it comes to stats, you’ll want to focus on the usual DPS carry stats, which are ATK%, CRIT%, CRIT DMG, and ATK. Instead of ATK, you can concentrate on Elemental Mastery or even Energy Recharge. Additionally, you can run Pyro Damage on your Goblet artifact to get a nice damage boost as support. Consider making Pyro damage another stat to focus on for your Goblet slot.",
		    inline=False)
  	thumb = discord.File('Character_Bennett_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Bennett_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildnoellesupport'):
  	embed = discord.Embed(
		    title="Noelle Geo Support Build",
		    description=
		    "**Noelle can be used a great defensive healer.**\n\nPreferred weapon: Whiteblind/ Skyward Pride\nPreferred artifacts: 2-set Maiden Beloved,2-set Retracing Bolide",
		    color=0xcc7722)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nNoelle’s abilities scale off of defense stats, so for that reason, you want to make your primary stat DEF% on most Artifacts. Sprinkle in some critical chance and critical damage, along with some energy recharge for ability spamming potential, and you’re all set.",
		    inline=False)
  	thumb = discord.File('Character_Noelle_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Noelle_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildnoelledps'):
  	embed = discord.Embed(
		    title="Noelle Geo DPS Build",
		    description=
		    "**This is a build that really comes online when you unlock Noelle's 6th constellation, allowing her to convert a large portion of her DEF to ATK.**\n\nPreferred weapon: Whiteblind/ Skyward Pride\nPreferred artifacts: 4-set Retracing Bolide",
		    color=0xcc7722)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nNoelle’s healing potential is a bit slower than Barbara and Qiqi, for example. High atk% stats, forgoing Def% a little can help. Having a high CRIT chance and damage will help you pump out more damage while Noelle is out on the field. She is viable as a DPS character, so keep that in mind.",
		    inline=False)
  	thumb = discord.File('Character_Noelle_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Noelle_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildfischldps'):
  	embed = discord.Embed(
  	    title="Fischl Electro/Physical DPS Build",
		    description=
		    "**This build empowers Fischl's physical damage and electro damage output, synergising with the bonuses from Oz and Burst skill.**\n\nPreferred weapon: Stringless / Skyward Harp/ Slingshot\nPreferred artifacts: 2,4-set Thundering Fury, 2,4-set Gladiator's OR 4-set Gladiator's Finale.",
		    color=0x800080)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nFischl’s abilities scale off of the ATK stat. Ensure you prioritize gear with ATK and ATK%, followed by CRIT DMG and CRIT% in the late game.",
		    inline=False)
  	thumb = discord.File('Character_Fischl_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Fischl_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildfischlsupport'):
  	embed = discord.Embed(
		    title="Fischl Electro Support Build",
		    description=
		    "**This build empowers Fischl's Electro DMG on her skills.**\n\nPreferred weapon: Stringless / Skyward Harp/ Slingshot\nPreferred artifacts: 4-set Thundering Fury",
		    color=0x800080)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nFischl’s abilities scale off of the ATK stat. Ensure you prioritize gear with ATK and ATK%, followed by CRIT DMG and CRIT% in the late game. Electro Dmg cup is a nice addition.",
		    inline=False)
  	thumb = discord.File('Character_Fischl_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Fischl_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildsucrosesupport'):
  	embed = discord.Embed(
		    title="Sucrose Anemo Support Build",
		    description=
		    "**This build turns Sucrose's into an Elemental Mastery battery, increasing this stat as much as possible to share it with her party members.**\n\nPreferred weapon: Sacrificial Fragments/ Mappa Mare\nPreferred artifacts: 4-set Viridescent Venerer set, 4-set Instructor OR 2-set Instructor, 2-set Viridescent. Noblesse Oblige works too.",
		    color=0x98FB98)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nFor Sucrose’s stats, you want to focus primarily on Energy Recharge and Elemental Mastery to pump up the support. When it comes down to the sub stats, prioritize getting as much Elemental Mastery as possible.",
		    inline=False)
  	thumb = discord.File('Character_Sucrose_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Sucrose_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)
  
  if msg.startswith('$buildsucrosedps'):
    embed = discord.Embed(
		    title="Dude.",
		    description=
		    "**I won't support your craving to make all characters DPS.But anyway, here you go.**\nPreferred Weapon: Otherwordly Story/Sacrificial Fragments/Mappa Mare\n Preferred Sets: 2-set Gambler, 2-set Instructor or 4-set Viridescent Venerer.",
		    color=0x98FB98)
    embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nBasically tons of Elemental mastery in addition to crit rate and crit dmg, Atk% and energy regen substats,and Anemo dmg goblet. Sucrose's second talent gives 20% of her elemental mastery to all other party members.\nDPS sucrose needs a very specific team. Basically any team that has tons of elemental reactions, combination is upto you. Also, The EM build is only viable when used in teams with constant elemental applications, like xiangling,etc. If you dont have such characters, you are better off building traditional DPS stats like atk%, crit rate and crit dmg.",
		    inline=False)
    thumb = discord.File('Character_Sucrose_Card.jpg')
    embed.set_thumbnail(url='attachment://Character_Sucrose_Card.jpg')
    await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildmonasupport'):
  	embed = discord.Embed(
		    title="Mona Hydro Support Build",
		    description=
		    "**Mona excels at empowering DPS units through the use of her Burst Skill making energy recharge incredibly valuable.**\n\nPreferred weapon: Mappa Mare/ Solar Pearl/ Favonius Codex/ The Widsith\nPreferred artifacts: 2,4-set Noblesse Oblige.",
		    color=0x0000FF)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nMona’s stats will scale with Energy Recharge, so you want to have a good amount of it. You can get it from the set bonuses on Exile and make sure you have it as a minor stat on your artifacts.",
		    inline=False)
  	thumb = discord.File('Character_Mona_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Mona_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildmonadps'):
  	embed = discord.Embed(
		    title="Mona Hydro DPS Build",
		    description=
		    "** Using powerful Hydro elemental abilities, Mona can pump out some of the greatest damage in the game. It’s essential to build her correctly to maximize her damage potential and optimize party synergy.**\n\nPreferred weapon: Mappa Mare/ Solar Pearl/ Favonius Codex/The Widsith\nPreferred artifacts:Exile, Wanderer’s Troupe or Instructors",
		    color=0x0000FF)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nYour best bet is focusing on ATK, Crit Rate, Crit Dmg on your Artifacts. As you level and get some better gear, you can look at running Crit on all artifacts and Hydro bonus damage on the goblet. Eventually, you will need energy recharge too.",
		    inline=False)
  	thumb = discord.File('Character_Mona_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Mona_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$builddionasupport'):
  	embed = discord.Embed(
		    title="Diona Cryo Support Build",
		    description=
		    "**Diona can work great as a source superconductor and extra protection for physical carries like Razor. She can also be used to set up melt reactions for Pyro carries.**\n\nPreferred weapon: Sacrificial Bow / Favonius Warbow\nPreferred artifacts: 2,4-set Maiden Beloved or 2,4-set Noblesse Oblige",
		    color=0xd6ecef)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nDiona’s abilities all scale with her health pool. For that reason, you want to focus on double HP rolls on all your gear to make the best Diona build in Genshin Impact. Look for HP% as the main stat on your Sands of Eon, Goblet of Eonothem, and Circlet of Logos. The Flower will always roll flat HP, while the Plume of Death always rolls flat ATK.\nWhen you get HP% as your main stat, focus on flat HP as a secondary stat. To min-max the character, you want to get bonuses to your HP rolls when enhancing the artifacts.",
		    inline=False)
  	thumb = discord.File('Character_Diona_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Diona_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$builddionadps'):
  	embed = discord.Embed(
		    title="You sure ?",
		    description=
		    "**She is too tiny to be dps, leave her alone.**\n If you wanted to, put on a full Bolide set and see what happens.",
		    color=0xd6ecef)
  	thumb = discord.File('Character_Diona_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Diona_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildbeidoudps'):
  	embed = discord.Embed(
		    title="Beidou Electro DPS Build",
		    description=
		    "**Beidou's damage output spikes when perfectly timing the counterattack from her second skill, Tidecaller, after you've unlocked her 1st and 2nd passive talents. This will give you a 10 second window of increased damage from your normal and charged attacks.**\n\nPreferred weapon: Wolf's Gravestone/ Prototype Aminus\nPreferred artifacts: 4-set Gladiator's Finale",
		    color=0x800080)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nBeidou’s stat build follows the traditional DPS, meaning you should focus on raw damage in the form of ATK% and CRIT%. She deals Electro damage, meaning you could also use some plus Electro damage artifacts, but we’ll cover that in the artifacts section. For your third and fourth stat rolls, focus on CRIT DMG and ATK to further boost your DPS. These are the four main stats. All of Beidou’s move scale with ATK, except for her shield, which scales with HP. We would not recommend sacrificing ATK for HP, though.",
		    inline=False)
  	thumb = discord.File('Character_Beidou_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Beidou_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildbeidousupport'):
  	embed = discord.Embed(
		    title="Beidou Electro Support Build",
		    description=
		    "**Frankly, her skillset does not provide much support except for the parry shield, so just build her DPS instead.**",
		    color=0x800080)
  	thumb = discord.File('Character_Beidou_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Beidou_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildningguangsupport'):
  	embed = discord.Embed(
		    title="Umm....",
		    description=
		    "**Her jade screen buffs your other characters, blocks enemy attacks and she creates crystallize shields.**\nThats about it.",
		    color=0xcc7722)
  	thumb = discord.File('Character_Ningguang_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Ningguang_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildningguangdps'):
  	embed = discord.Embed(
		    title="Ningguang Geo DPS Build",
		    description=
		    "**Ningguang is a character that scales extremely well with high constellation levels, making her one of the burstier single target units in the game.**\n\nPreferred weapon: Solar Pearl/ The Widsith/ Lost Prayer to Sacred Winds\nPreferred artifacts: 2-set Gladiator's Finale + 2-set Archaic Petra OR 2-set Gladiator's + 2-set Noblesse Oblige",
		    color=0xcc7722)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nIn terms of stats, you want to focus primarily on critical hit chance and critical damage. Secondary to that, you’ll want to look for ATK% and ATK damage sub-stats. We recommend looking for a helmet Artifact with a primary CRIT% roll. We also recommend running plus Geo damage bonus as the primary stat on your Goblet.",
		    inline=False)
  	thumb = discord.File('Character_Ningguang_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Ningguang_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildxianglingdps'):
  	embed = discord.Embed(
		    title="Xiangling Pyro DPS Build",
		    description=
		    "**Xiangling has great damage scaling on her skills and normal attacks, and is quite viable as a DPS character.**\n\nPreferred weapon: Crescent Pike/ Skyward Spine\nPreferred artifacts: 2-set Gladiator's Finale + 2-set Crimson Witch of Flames.",
		    color=0xFF0000)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nXiangling’s moves primarily scale with ATK, so your main focus is on the ATK% stat. After that, you can go for CRIT%, CRIT DMG, and ATK. Another good option is running Pyro damage on the goblet since you’ll likely be using Xiangling mainly for her Pyro abilities. Focus on these four stats, and you will be on the right track.",
		    inline=False)
  	thumb = discord.File('Character_Xiangling_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Xiangling_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildxianglingsupport'):
  	embed = discord.Embed(
		    title="Xiangling Pyro Support Build",
		    description=
		    "**Xiangling's constant Pyro prescence on the field makes her a great Pyro Support character.**\n\nPreferred weapon: Crescent Pike/ Prototype Grudge\nPreferred artifacts: 2,4-set Noblesse Oblige OR 2,4-set Crimson Witch of Flames.",
		    color=0xFF0000)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nFor Support Xiangling, Focus mainly on energy recharge, Pyro DMG Bonus and Elemental Mastery.\nIf you’re running Xiangling as pure support, we recommend you farm some of your Crimson Witch of Flames set as soon as possible.The Crimson set gives you a massive DPS gain by buffing Xiangling’s innate Pyro abilities. Crimson Witch of Flames two-piece bonus boosts Pyro DMG by 15%. The real kicker is the four-piece bonus, though. It increases Overloaded and Burning DMG by 40% and increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases two-piece set effects by 50% for 10 seconds and stacks three times.",
		    inline=False)
  	thumb = discord.File('Character_Xiangling_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Xiangling_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildxingqiusupport'):
  	embed = discord.Embed(
		    title="Xingqiu Hydro Support Build",
		    description=
		    "**Xingqiu can be a reliable source of Hydro reactions thanks to his Elemental Burst ability, while providing useful damage reduction and healing to his party members. At Constellation level 2, he becomes incredible powerful when paired with a Hydro DPS unit.**\n\nPreferred weapon: Sacrificial Sword/ Favonius Sword\nPreferred artifacts: 2,4-set Noblesse Oblige.",
		    color=0x0000FF)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nOutside of ATK and CRIT, Xingqiu benefits from both Elemental Mastery and Energy Recharge. Focusing on recharge lets you spam abilities quicker, and mastery will help pump the damage slightly.",
		    inline=False)
  	thumb = discord.File('Character_Xingqiu_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Xingqiu_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildxingqiudps'):
  	embed = discord.Embed(
		    title="Xingqiu Hydro DPS Build",
		    description=
		    "**You can build him using the traditional melee damage build, which consists of stacking ATK on your artifacts, with optional Hydro bonus damage stats on your Goblet.**\n\nPreferred weapon: Prototype Rancour/ Skyward Blade/ Fillet Blade\nPreferred artifacts: 2,4-set Noblesse Oblige OR 2,4-set Exile Set",
		    color=0x0000FF)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nYou can follow the traditional ATK and CRIT oriented stat builds on your artifacts for Xingqiu. Considering his elemental abilities, you can also try farming for a Hydro bonus damage Goblet to utilize.",
		    inline=False)
  	thumb = discord.File('Character_Xingqiu_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Xingqiu_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildchongyunsupport'):
  	embed = discord.Embed(
		    title="Chongyun Cryo Support Build",
		    description=
		    "**Melt is one of the strongest Elemental Reactions in the game and Chongyun has a consistent method of applying the Cryo debuff with his Elemental Skill ability. This makes him a strong support character when paired with Pyro carries.**\n\nPreferred weapon:  Skyward Pride / Favonius Greatsword\nPreferred artifacts: 2,4-set Noblesse Oblige or 2,4-set Instructor's set.",
		    color=0xd6ecef)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nElemental Mastery is a nice stat to have on Chongyun, as you will be doing lots of Cryo-based damage. The Elemental Skill lasts for a while, so the benefit of running Elemental Mastery as a minor stat is excellent.",
		    inline=False)
  	thumb = discord.File('Character_Chongyun_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Chongyun_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildchongyundps'):
  	embed = discord.Embed(
  	    title="Chongyun Cryo DPS Build",
		    description=
		    "**While Chongyun can be built like other standard Claymore users with a Gladiator set, his true power comes from his Elemental Burst skill. A lot of his constellations also empower this ability. As such, this build piles on, making his Ultimate as strong as possible.**\n\nPreferred weapon:  Skyward Pride / Favonius Greatsword\nPreferred artifacts: 2,4-set Noblesse Oblige or 2,4-set Instructor's set.",
		    color=0xd6ecef)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nThe stats you want to focus on are ATK% on all Artifacts and Cryo damage on the Goblet. Chongyun’s abilities scale based on ATK, and that’s why you should focus on that as your main stat.",
		    inline=False)
  	thumb = discord.File('Character_Chongyun_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Chongyun_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildqiqidps'):
  	embed = discord.Embed(
		    title="Qiqi Cryo DPS Build",
		    description=
		    "**Qiqi doubles as a healer and DPS since her healing abilities scale off of ATK. She makes an excellent addition to any team, especially if you are looking to build a healer that can dish out the damage numbers. Qiqi is a well-rounded character, with some potent healing abilities capable of keeping a full team alive in any situation.**\n\nPreferred weapon: Sacrificial Sword/ Prototype Rancour/ Skyward Blade\nPreferred artifacts: 2,4-set Noblesse Oblige or 2,4-set Gladiator's set",
		    color=0xd6ecef)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nHer abilities scale with ATK, so the primary stat you’re looking for is ATK% and ATK. If you’re building Qiqi as a damage dealer, you’ll also want to throw on some CRIT and CRIT%. Stack all of your Artifacts with ATK as the main stat, and you won’t regret it.",
		    inline=False)
  	thumb = discord.File('Character_Qiqi_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Qiqi_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildqiqisupport'):
  	embed = discord.Embed(
		    title="Qiqi Cryo Support/Healer Build",
		    description=
		    "**Qiqi is the ultimate healing support thanks to her powerful healing and Cryo damage while not active.**\n\nPreferred weapon: Sacrificial Sword/ Prototype Rancour/ Skyward Blade\nPreferred artifacts: 2,4-set Noblesse Oblige or 2,4-set Maiden Beloved set",
		    color=0xd6ecef)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nHer abilities scale with ATK, so the primary stat you’re looking for is ATK% and ATK. Healing Bonus is also a nice stat to have on her.",
		    inline=False)
  	thumb = discord.File('Character_Qiqi_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Qiqi_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildkeqingdps'):
  	embed = discord.Embed(
		    title="Keqing Electro DPS Build",
		    description=
		    "**Keqing has the highest single target charged attack DPS in the game. This build turns Keqing into a crit machine, taking advantage of the boost to CRIT DMG she gets with every ascension level.**\n\nPreferred weapon: Lion's Roar/ Black Sword/ Iron Sting\nPreferred artifacts: 4-set Gladiator's Finale OR 4-set Thundering Fury Or 2-set Gladiator and Thundering Fury.",
		    color=0x800080)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nWhen it comes to stats, you want to go for ATK%, ATK, and Electro bonus damage on the Goblet Artifact. You can also look at picking up Physical bonus damage early on if you don’t get lucky with an Electro Goblet.\nAs you level up Keqing and get better and better gear, her elemental damage will be doing a bulk of the damage. Therefore, we think Electro bonus damage is an important stat. ",
		    inline=False)
  	thumb = discord.File('Character_Keqing_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Keqing_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildkeqingsupport'):
  	embed = discord.Embed(
		    title="BRUH",
		    description=
		    "**If you were lucky enough to get her, Why The F*ck ould you want to build her as support. She is a fast, hard-hitting, pretty little thing. Mess shit up with her, Don't mess shit for her.**",
		    color=0x800080)
  	thumb = discord.File('Character_Keqing_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Keqing_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildchildedps'):
  	embed = discord.Embed(
		    title="Childe Hydro DPS Build",
		    description=
		    "**With the highest scaling Elemental Burst skill multiplier in the game, Tartaglia is an incredible Hydro damage dealer. Like Diluc, he becomes unstoppable with high constellations but does not need them to be extremely powerful. If you're playing with Noelle or a Geo character on your team, consider running the Retracing Bolide set instead.**\n\nPreferred weapon: Rust/ Skyward Harp/Stringless\nPreferred artifacts: 2,4-set Heart of Depth, 2-set Gladiator's Finale, 2-set Noblesse Oblige or 4-set Wanderer's Troupe set. Use in combinations.",
		    color=0x0000FF)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nTo maximize the damage, you’ll stick with the traditional DPS stats, including ATK% and CRIT. Increasing Elemental Burst damage and Elemental Mastery should also be a priority because of how this character is designed.",
		    inline=False)
  	thumb = discord.File('Character_Tartaglia_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Tartaglia_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildchildesupport'):
  	embed = discord.Embed(
		    title="Dammit",
		    description=
		    "*He is a Dps Character. He has no support options available, he needs to be on the field to do SOMETHING*",
		    color=0x0000FF)
  	thumb = discord.File('Character_Tartaglia_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Tartaglia_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildzhonglidps'):
  	embed = discord.Embed(
		    title="Zhongli Geo DPS Build",
		    description=
		    "**This is a build that is really NOT recommended, because he isn't meant to do this, but doesn't mean he can't.**\n\nPreferred weapon: Primordial Jade Spear/ Crescent Pike\nPreferred artifacts: 2,4-set Retracing Bolide with 2,4-set Archaic Petra. 2 of each bring the best out of both his basic atk and skills. Go full Bolide for a Physical DPS build.",
		    color=0xcc7722)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !* Players looking to build him as a main DPS can focus on the traditional damage stats. These include ATK%, ATK, CRIT%, CRIT DMG, and secondary stats like HP% and Energy Recharge.",
		    inline=False)
  	thumb = discord.File('Character_Zhongli_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Zhongli_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildzhonglisupport'):
  	embed = discord.Embed(
		    title="Zhongli Geo Support Build",
		    description=
		    "**Definitely the best way to go about building Zhongli. Zhongli can be a great defensive support through the use of geo shields, pillars, and petrification.**\n\nPreferred weapon: Skyward Spine/ Crescent Pike/ Prototype Grudge\nPreferred artifacts: 2-set Retracing Bolide with 2-set Archaic Petra OR 2-set Archaic and 2-set Noblesse Oblige. Personally, I use the latter and is probably the best support build.",
		    color=0xcc7722)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !* While building him as support, stats like HP% and Energy Recharge are of primary importance. If you feel these stats have been covered in other artifacts, get some Crit Rate or Crit Dmg on your helmet artifact. Geo dmg bonus on your cup is a must.",
		    inline=False)
  	thumb = discord.File('Character_Zhongli_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Zhongli_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildxinyansupport'):
  	embed = discord.Embed(
		    title="Xinyan Pyro Support Build",
		    description=
		    "**She is a versatile character and can support as well as dish out some serious damage**\n\nPreferred weapon: Prototype Aminus/ Serpent Spine\nPreferred artifacts: 2-set Retracing Bolide with 2-set Gladiator OR 2-set Bolide and 2-set Bloodstained Chivalry.",
		    color=0xFF0000)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !* Pyro Dmg bonus on the goblet artifact, with Elemental Mastery and Energy Recharge stats.",
		    inline=False)
  	thumb = discord.File('Character_Xinyan_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Xinyan_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildxinyandps'):
  	embed = discord.Embed(
		    title="Xinyan Pyro DPS Build",
		    description=
		    "**Unlike Diluc who focuses on Pyro DPS, Xinyan excels when built around physical damage similar to Razor. Switch the circlet to CRIT DMG if you unlock constellation level 2.**\n\nPreferred weapon: Prototype Aminus/ Serpent Spine\nPreferred artifacts: 2-set Retracing Bolide with 2-set Gladiator with 2-set Bloodstained Chivalry OR 4-set Gladiator.",
		    color=0xFF0000)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts!* \n*You can rarely go wrong by focusing on primary damage stats like attack and critical. Considering Xinyan is dealing a lot of physical damage, you can go for a Physical DMG Bonus roll on the Goblet.\nFor secondary stats, you will almost certainly want to focus on DEF because it helps scale Xinyan’s shield. Another good option is Energy Recharge to help with the long cooldown times.*",
		    inline=False)
  	thumb = discord.File('Character_Xinyan_Card.jpg')
  	embed.set_thumbnail(url='attachment://Character_Xinyan_Card.jpg')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildalbedosupport'):
  	embed = discord.Embed(
		    title="Albedo Geo Support Build",
		    description=
		    "**Albedo has been released with version 1.2 and he looks really good ! Now, to make things clear, Albedo has been released with the intention of being a support for your team, with some carry potential.**\n\nPreferred weapon: Favonius Sword/ The Flute/ Festering Desire\nPreferred artifacts: 2,4-set Archaic Petra OR 2,4-set Noblesse Oblige.",
		    color=0xcc7722)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !* While building him as support, stats like DEF% and Energy Recharge become viable ! If you feel these stats have been covered in other artifacts, get some Crit Rate or Crit Dmg on your helmet artifact and ATK%. Geo dmg bonus on your cup is a must. Keep in mind DEF% becomes viable after C2.",
		    inline=False)
  	thumb = discord.File('Character_Albedo_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Albedo_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildalbedodps'):
  	embed = discord.Embed(
		    title="Albedo Geo DPS Build",
		    description=
		    "**Albedo has been released with version 1.2 and he looks really good ! Now, to make things clear, Albedo has been released with the intention of being a support for your team, with some carry potential.**\n\nPreferred weapon: Favonius Sword/ The Flute/ Festering Desire/ Aquila Favonia\nPreferred artifacts: 2,4-set Archaic Petra OR 2,4-set Noblesse Oblige. If you plan on using him a lot for plunge damage, Gladiator's Finale could work too.",
		    color=0xcc7722)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !* Albedo scales more with Physical DMG than DEF%, and its definitely not worth forgoing ATK%. While building him as DPS, stats like ATK%, Crit Rate and Crit DMG become necessary. Once you feel satisfied with these stats, go for a Physical DMG goblet instead of a Geo DMG goblet. Your substats on the artifacts can be DEF% and Energy Recharge. Keep in mind that these substats could also work as main stat in case you dont have the recommended stats, since his skills scale with these stats too. So don't strain your pretty little head too much.",
		    inline=False)
  	thumb = discord.File('Character_Albedo_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Albedo_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if msg.startswith('$buildganyudps'):
  	embed = discord.Embed(
		    title="Ganyu Cryo DPS Build",
		    description=
		    "**COCOGOAT Build!**\n\nPreferred weapon: Amos Bow/Prototype Crescent/Skyward Harp/Sharpshooter's Oath\nPreferred artifacts: 4-set Blizzard Strayer, 4-set Wanderer's",
		    color=0xd6ecef)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nNot much to think about. Just the usual. Atk%, Crit rate, Crit dmg, with cryo dmg bonus goblet.",
		    inline=False)
  	thumb = discord.File('Character_Ganyu_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Ganyu_Card.png')
  	await message.channel.send(embed=embed, file=thumb)
  
  if msg.startswith('$buildganyusupport'):
  	embed = discord.Embed(
		    title="Ganyu Cryo Support Build",
		    description=
		    "**COCOGOAT Build!**\n\nPreferred weapon: Stringless/Prototype Crescent/Favonius Warbow/Sacrificial Bow\nPreferred artifacts: 4-set Noblesse, OR 2-set Blizzard Strayer, 2-set Noblesse",
		    color=0xd6ecef)
  	embed.add_field(
		    name="**Recommended Stats**",
		    value=
		    "*In case set bonuses can't be achieved, focus on these stats on your artifacts !*\nFor the support build, Energy recharge, Elemental mastery and preferably crit rate and dmg substats would be ideal.",
		    inline=False)
  	thumb = discord.File('Character_Ganyu_Card.png')
  	embed.set_thumbnail(url='attachment://Character_Ganyu_Card.png')
  	await message.channel.send(embed=embed, file=thumb)

  if message.author == client.user:
    	return
  if msg.startswith('$help'):
  	embed = discord.Embed(
		    title="Outrider Commands",
		    description=
		    "\n1.$help- List of commands\n\n2.$hello- Greet the bot\n\n3.$inspire- Motivational Quote\n\n4.$daily- Most important Daily tasks ingame\n\n5.$talent- Talent Books Domain Guide\n\n6.$weapon- Weapon Ascension Material Guide\n\n7.$char- Character Ascension Material Requirements\n\n8.$currency- Details about in-game currencies\n\n9.$artifact- Artifact Domain list\n\n10.$respawn- Respawn Times for open-world resources\n\n11.$drops- All materials drop guides\n\n12.$quantity- Exacpt amounts of mora and materials required per level and ascension.\n\n**13.$build- Check for recommended builds according to role. For Example- $buildxinyandps will give you the DPS build for Xinyan. The roles are either Support or DPS, Support usually by default contains the DPS Support build.**\n\n**The bot talks to you upon encountering some keywords, so be on the hunt :)**",
		    color=0xC0C0C0)
  	thumb = discord.File('Character_Ganyu_Portraitcropped.png')
  	embed.set_thumbnail(
		    url='attachment://Character_Ganyu_Portraitcropped.png')
  	await message.channel.send(embed=embed, file=thumb)

keep_alive()
client.run(os.getenv('TOKEN'))
