import discord  

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} đã kết nối'.format(client)) 
@client.event
async def on_message(tn):
    if tn.author ==  client.user:
        return 
    if tn.content == 'lo':
        await tn.channel.send('chào bạn')
    if 'ngu' in tn.content.lower():
        await tn.channel.send('việt NGU vãi loz')
    if 'thắng ngáo' in tn.content.lower():
        await tn.channel.send('thắng ngáo như việt')
    if 'alo' in tn.content.lower():
        await tn.channel.send('lo con CẶC')
client.run('ODkxNTIwMjkyNDc0NzMyNTg1.YU_i-Q.i6yXAH3JmdkLXMmTzBqFwSbS3dM')