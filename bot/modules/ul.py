from bot.helper.telegram_helper.message_utils import send_file, send_message
cmd = message.text.split(maxsplit=1)
if len(cmd) == 1:
  await send_message(message, "<code>No command to execute was given.</code>")
  return
await send_file(message, f"{cmd}")
