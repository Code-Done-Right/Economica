# 📑 Preface

The head bot developer, Science Done Right, is going to spend a couple days brainstorming all the commands, their functionality, how to make them work as they do, et cetera. Currently, Science Done Right (whom we'll abbreviate as SDR), is learning about discord buttons using a unofficial third party module called **discord_components.** Huge thanks to *Developer kiki7000* (@devkiki7000) for making the module.

[Discord Components Documentaion](https://gitlab.com/discord.py-components/discord.py-components)

# ❗ Issues

We have some issues about the button interaction, specifically the blue "Primary call-to-action" buttons.

![An image showing the Primary button.](Button.png)

The `discord_components` module currently does not support it's way of sending private messages to the user using the command.

As of now, this is not in our hands and we cannot fix this.
The commented line needs the interaction message.

```py
button = await ctx.send(
		embed = embed,
		components = [
		#	Button(style = 1, label = 'Info', disabled = True),
			Button(style = 5, label = 'Click to invite me!', url = f'{INVITE_URL}')
			]
		)
```
