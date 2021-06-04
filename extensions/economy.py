from discord.ext import commands
from replit import db
import random


def get_econ_key(member):
    return f'economy_{member.id}'


class Economy(commands.Cog, name='Economy'):
    def __init__(self, bot):
        self.bot = bot
    
    # Helper methods:
    async def get_balance(self, member):
        key = get_econ_key(member)
        if key not in db.keys():
            db[key] = 0.0
        return db[key]

    async def deposit_amount(self, member, amount):
        key = get_econ_key(member)
        if key not in db.keys():
            db[key] = amount
        else:
            db[key] += amount

    async def withdraw_amount(self, member, amount):
        key = get_econ_key(member)
        if key in db.keys() and amount >= db[key]:
            db[key] -= amount

    # Normal users:
    @commands.command(
        help='Check your balance.',
        name='check_balance'
        )
    async def check_balance(self, ctx):
        b = await self.get_balance(ctx.author)
        await ctx.send(f'Your balance is {b}')

    @commands.command(
        help='Make payments to users by mentioning them.',
    )
    async def pay(self, ctx, amount: float):
        if len(ctx.message.mentions) < 1:
            await ctx.send(
                f'Invalid: You must specify users by mentioning them.')
            return
        balance = await self.get_balance(ctx.author)
        total =  len(ctx.message.mentions) * amount
        if balance < total:
            await ctx.send(
                f'Invalid: You only have {balance} but are trying to pay {total}.')
            return
        await self.withdraw_amount(ctx.author, total)
        for member in ctx.message.mentions:
            await self.deposit_amount(member, amount)
        await ctx.reply('Payment completed.', mention_author=True)

    # Bot owner only:
    @commands.group(
        help='Manage member balances. Bot owner only.'
    )
    @commands.is_owner()
    async def balance(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(self.balance)

    
    @balance.command(
        help='Check balance by mentioning users. Bot owner only.'
    )
    @commands.is_owner()
    async def check(self, ctx):
        if len(ctx.message.mentions) < 1:
            await ctx.send(
                f'Invalid: You must specify users by mentioning them.')
            return
        for member in ctx.message.mentions:
            b = await self.get_balance(member)
            await ctx.send(f"{member}'s balance is {b:.2f}")

    @commands.is_owner()
    @balance.command(
        help='Deposit into someones account by mentioning them. Bot owner only.'
    )
    async def deposit(self, ctx, amount: float):
        if len(ctx.message.mentions) < 1:
            await ctx.send(
                f'Invalid: You must specify users by mentioning them.')
            return
        for member in ctx.message.mentions:
            await self.deposit_amount(member, amount)
        await ctx.send(f'Deposited {amount}')

    @commands.is_owner()
    @balance.command(
        help='Withdraw from someones account by mentioning them. Bot owner only.'
    )
    async def withdraw(self, ctx, amount: float):
        if len(ctx.message.mentions) < 1:
            await ctx.send(
                f'Invalid: You must specify users by mentioning them.')
            return
        for member in ctx.message.mentions:
            await self.withdraw_amount(member, amount)
        await ctx.send(f'Withdrew {amount}')

    


class Gambling(commands.Cog, name='Gambling'):
    def __init__(self, bot):
        self.bot = bot

    def coinflip(self):
        return random.randint(0, 1)

    @commands.command(
        help = 'Gamble.'
    )
    async def gamble(self, ctx, amount: float):
        """Gambles some money."""
        economy = self.bot.get_cog('Economy')
        won = False
        if economy is not None:
            await economy.withdraw_amount(ctx.author, amount)
            if self.coinflip() == 1:
                await economy.deposit_amount(ctx.author, amount * 1.5)
                won = True
        win_lose = f'won {amount * 1.5}!!!' if won else 'lost it all. Try again!'
        await ctx.send(f'You gambled {amount} and {win_lose}')


def setup(bot):
    bot.add_cog(Economy(bot))
    bot.add_cog(Gambling(bot))
