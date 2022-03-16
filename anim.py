from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Heart's"}
	@loader.owner
	async def heartscmd(self, message):
		for _ in range(10):
			for heart in ['Привет❤', '️Привет🧡', 'Привет💛', 'Привет💚', 'Привет💙', 'Привет💜']:
				await message.edit(heart)
				await sleep(0.05)
