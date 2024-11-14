from bot.helper.telegram_helper.message_utils import send_file, send_message
assync def ul(_,message):
  cmd = message.text.split(maxsplit=1)
  if len(cmd) == 1:
    await send_message(message, "<code>No command to execute was given.</code>")
    return
  await send_file(message, f"{cmd}")


bot.add_handler(EditedMessageHandler(ul,filters=command(BotCommands.ulCommand, case_sensitive=True)))
