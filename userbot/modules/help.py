# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CHANNEL
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, ICON_HELP
from userbot.utils import edit_delete, edit_or_reply, man_cmd

modules = CMD_HELP


@man_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, f"`{args}` **Bukan Nama Modul yang Valid.**")
    else:
        user = await event.client.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{ICON_HELP}\t\t\t"
        await edit_or_reply(
            event,
            f"**✦ Daftar Perintah Untuk [Adam-Userbot](https://github.com/UserKontol/Dion-Userbot):**\n"
            f"**✦ Jumlah** `{len(modules)}` **Modules**\n"
            f"**✦ Owner:** [Adam](tg://user?id=1878075436) & [Dion](tg://user?id=1780335957) 🔥\n\n"
            f"{ICON_HELP}   {string}"
            f"\n\nSupport @wibu_telegram",
        )
        await event.reply(
            f"\n**Contoh Ketik** `{cmd}help ping` **Untuk Melihat Informasi Module Adam-Userbot**"
        )
