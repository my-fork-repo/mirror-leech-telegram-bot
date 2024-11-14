from bot import bot
from pyrogram.filters import command

from ..helper.telegram_helper.message_utils import send_file, send_message
from ..helper.ext_utils.telegraph_helper import telegraph
from pyrogram.handlers import MessageHandler, EditedMessageHandler
from ..helper.telegram_helper.bot_commands import BotCommands
from ..helper.ext_utils.bot_utils import new_task
@new_task
async def ul(_,message):
  cmd = message.text.split(maxsplit=1)
  await send_message(message, cmd)


bot.add_handler(EditedMessageHandler(ul,filters=command(BotCommands.ulCommand, case_sensitive=True)))
