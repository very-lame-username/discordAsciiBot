from discord.ext import commands
from pyfiglet import Figlet

# ---> USER VARIABLES <--- #

token = 'TOKEN GOES HERE'  # get a token from https://discord.com/developers/applications
prefix = '-'  # change to whatever prefix you want

fig = Figlet(font='standard')  # Change fonts here, try 'banner' for readability
fig_small = Figlet(font='small')  # use 'short' for very small text (doesn't work well with characters like 'Q')

# ------------------------ #

bot = commands.Bot(command_prefix=prefix)


def to_ascii(_input, small=False):
    if small:
        ascii_text = fig_small.renderText(_input)
    else:
        ascii_text = fig.renderText(_input)
    ascii_text = ascii_text.replace('```', '`​`​`')  # backticks with zero-width spaces just in case
    return'```\n' + ascii_text + '\n```'


@bot.command(name='ascii')
async def _ascii(ctx, *, _input):
    ascii_text = to_ascii(_input)
    if len(ascii_text) > 2000:
        ascii_text = to_ascii(_input, True)
        if len(ascii_text) > 2000:
            await ctx.send('Error: Input is too long')
            return
    await ctx.send(ascii_text)


@_ascii.error
async def ascii_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Error: Input not provided')

bot.run(token)
