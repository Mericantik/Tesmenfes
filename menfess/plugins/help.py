from pyrogram import Client, enums, types
from menfess.helpers import Database, Helper
from menfess.helpers.decorators import Bot
from menfess.dk import Dk


@Bot("help")
async def on_help_handler(client: Client, msg: types.Message, db: Database):
    member = db.get_data_pelanggan()
    pesan = "Supported commands\n"
    pesan += '/status — melihat status\n'
    pesan += '/topup — top up coin\n'
    pesan += '/tf_coin — transfer coin\n'
    pesan += '/coget — untuk memberikan koin random kepada penguna yang tercepat dan beruntung\n'
    if member.status == 'owner':
        pesan += '\n=====OWNER COMMAND=====\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/stats — melihat statistik bot\n'
        pesan += '/bot — setbot (on|off)\n'
        pesan += '\n=====BROADCAST OWNER=====\n'
        pesan += '/broadcast — mengirim pesan broadcast kesemua user\n'
        pesan += '\n=====SET BOT=====\n'
        pesan += '/setbiayapinnedmenfes — mengirim mengubah biaya pinned\n'
        pesan += '/setbiayahapusmenfes — mengirim mengubah biaya hapus\n'
        pesan += '/setbiayasendmenfes — mengirim mengubah biaya kirim menfes\n'
        pesan += '/setdailysend — mengirim mengubah biaya daily send\n'
        pesan += '/setchannellog — mengirim mengubah channel log\n'
        pesan += '/setchannelorgrub — mengirim mengubah channel 2\n'
        pesan += '/setchannelpost — mengirim mengubah channel post\n'
        pesan += '/profilbot — melihat bot\n'


    await msg.reply(pesan, True)

@Dk.Bot("help")
async def on_topup_module_handler(client: Dk, msg: types.Message, db: Database = None):
    db_user = db.get_data_pelanggan()
    anu = Helper(client, msg)
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    fullname = first_name if not last_name else first_name + ' ' + last_name
    username = '@nazhak' if not msg.from_user.username else '@' + msg.from_user.username
    mention = msg.from_user.mention
    markup = types.InlineKeyboardMarkup([
        [types.InlineKeyboardButton('rules', callback_data='rules'),
         types.InlineKeyboardButton('help', callback_data='help'),
         types.InlineKeyboardButton('status', callback_data='status')]
    ])
    return await client.send_message(db_user.id, client.rules.format(
        id=msg.from_user.id,
        mention=mention,
        username=username,
        first_name=await anu.escapeHTML(first_name),
        last_name=await anu.escapeHTML(last_name),
        fullname=await anu.escapeHTML(fullname)
    ), reply_markup=markup)
