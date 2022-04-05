from discordwebhook import Discord

base_url = "https://discord.com/api/webhooks/"
server = "960993855371616266/"
webhook = "dCku3ViLwsPPjY897qXUHuUgS3E_3-YcumVTtoPqmmMt8tFb4NUpzeLJK1JkF0qxXy0v"
url = base_url+server+webhook


discord = Discord(url=url)
discord.post(content="Hello, world.")