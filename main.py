import json
from datetime import datetime, timedelta
from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData


bot = Bot(token="6261075365:AAHyWCLtWfJ_eR8W44DoCEcxWXs1PXpKoEQ")
dp = Dispatcher(bot)
inline = CallbackData("post", "action", "data")
full_name, phone, email, complaint, user, deleting_mes, mess, channel_id, count = '', '', '', '', '', types.Message, types.Message, "-1001901159869", 0
sent = False
texts_file = open("texts.json", encoding="utf-8")
texts = json.load(texts_file)

# statistics variables
question_count = 0
all_follows = 0
day_follows = 0
week_follows = 0
follows = []
start_date_week = ""
start_date_day = ""


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global follows, all_follows, day_follows, week_follows
    if message.from_user.id not in follows:
        follows.append(message.from_user.id)
        all_follows += 1
        day_follows += 1
        week_follows += 1
    next = types.KeyboardButton("📲Розпочати")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True).add(next)
    await bot.send_message(message.from_user.id, "👋🏻Вас вітає бот «Віднови Своє».\n\n"
                                                 "Цей бот дозволить знайти допомогу людям, чиє майно постраждало внаслідок збройної агресії рф проти України.", reply_markup=mar)


@dp.message_handler(text="Статистика")
async def statistic(message: types.Message):
    global day_follows, week_follows, start_date_day, start_date_week
    week_time = start_date_week + timedelta(days=7)
    day_time = start_date_day + timedelta(hours=24)
    if start_date_week < week_time and start_date_day < day_time:
        await bot.send_message(channel_id, f"Кількість заданих питань - {question_count}"
                                               f"Кількість людей за 1 день - {day_follows}"
                                               f"Кількість людей за тиждень - {week_follows}"
                                               f"Загальна кількість людей - {all_follows}")
    elif start_date_week < week_time and start_date_day == day_time:
        start_date_day = day_time
        day_follows = 0
        await bot.send_message(channel_id, f"Кількість заданих питань - {question_count}"
                                               f"Кількість людей за 1 день - {day_follows}"
                                               f"Кількість людей за тиждень - {week_follows}"
                                               f"Загальна кількість людей - {all_follows}")
    elif start_date_week == week_time and start_date_day < day_time:
        start_date_week = week_time
        week_follows = 0
        await bot.send_message(channel_id, f"Кількість заданих питань - {question_count}"
                                               f"Кількість людей за 1 день - {day_follows}"
                                               f"Кількість людей за тиждень - {week_follows}"
                                               f"Загальна кількість людей - {all_follows}")
    else:
        start_date_day = day_time
        start_date_week = week_time
        day_follows = 0
        week_follows = 0
        await bot.send_message(channel_id, f"Кількість заданих питань - {question_count}"
                                               f"Кількість людей за 1 день - {day_follows}"
                                               f"Кількість людей за тиждень - {week_follows}"
                                               f"Загальна кількість людей - {all_follows}")


@dp.message_handler(text="📲Розпочати")
@dp.message_handler(text="Назад🔙")
async def continues(message: types.Message):
    global mess
    mess = message
    block1 = types.KeyboardButton(texts['block1']['title'], callback_data=texts['block1']['title'])
    block2 = types.KeyboardButton(texts['block2']['title'], callback_data=texts['block2']['title'])
    block3 = types.KeyboardButton(texts['block3']['title'], callback_data=texts['block3']['title'])
    block4 = types.KeyboardButton(texts['block4']['title'], callback_data=texts['block4']['title'])
    block5 = types.KeyboardButton(texts['block5']['title'], callback_data=texts['block5']['title'])
    block6 = types.KeyboardButton(texts['block6']['title'], callback_data=texts['block6']['title'])
    block7 = types.KeyboardButton(texts['block7']['title'], callback_data=texts['block7']['title'])
    block8 = types.KeyboardButton(texts['block8']['title'], callback_data=texts['block8']['title'])
    block9 = types.KeyboardButton(texts['block9']['title'], callback_data=texts['block9']['title'])
    block10 = types.KeyboardButton(texts['block10']['title'], callback_data=texts['block10']['title'])
    block11 = types.KeyboardButton(texts['block11']['title'], callback_data=texts['block11']['title'])
    block12 = types.KeyboardButton(texts['block12']['title'], callback_data=texts['block12']['title'])
    block13 = types.KeyboardButton(texts['block13']['title'], callback_data=texts['block13']['title'])
    support = types.KeyboardButton("📲Звернутися в підтримку")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, support)
    await bot.send_message(message.from_user.id, "Виберіть блок, який вас цікавить👇", reply_markup=mar)


@dp.message_handler(text="📲Звернутися в підтримку")
async def support(message: types.Message):
    leave_report = types.KeyboardButton("📝Залишити заявку")
    leave_mar = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(leave_report)
    await bot.send_message(message.from_user.id, "Якщо Ви не знайшли відповідь на своє питання, Ви можете:\n\n"
                                                 "1. Написати нам на e-mail:\n"
                                                 "📧shtab.uaror@gmail.com\n"
                                                 "2. Звернутись на гарячу лінію:\n"
                                                 "📞 099 737 75 72", reply_markup=leave_mar)

@dp.message_handler(text="📝Залишити заявку")
async def report(message: types.Message):
    await bot.send_message(message.from_user.id, "Напишіть ваше ім'я та прізвище")

    @dp.message_handler()
    async def fullName(message: types.Message):
        global full_name, phone, email, complaint, user, deleting_mes
        user = message.from_user.id
        if full_name == '':
            full_name = message.text
            phone_butt = types.KeyboardButton("Відправити номер телефону", request_contact=True)
            mar = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(phone_butt)
            await bot.send_message(message.from_user.id, "Відправте ваш номер телефону", reply_markup=mar)
        elif email == '':
            email = message.text
            await bot.send_message(message.from_user.id, "Напишіть ваше повідомлення")
        elif complaint == '':
            complaint = message.text
            send = types.InlineKeyboardButton("Відправити📩", callback_data="complaint")
            send_mar = types.InlineKeyboardMarkup().add(send)
            deleting_mes = await bot.send_message(message.from_user.id, f"{full_name}\n"
                                                                        f"{phone}\n"
                                                                        f"{email}\n"
                                                                        f"{complaint}", reply_markup=send_mar)

        @dp.message_handler(content_types=types.ContentType.CONTACT)
        async def phone_func(message: types.Message):
            global phone
            phone = str(message.contact.phone_number)
            await bot.send_message(message.from_user.id, "Напишіть вашу почту")


@dp.callback_query_handler(text=["complaint"])
async def send_complaint(callback_data: types.CallbackQuery):
    global mess, sent, count
    if not sent:
        sent = True
        work = types.InlineKeyboardButton("В роботі", callback_data="work")
        handled = types.InlineKeyboardButton("Оброблено", callback_data="handled")
        acceptance = types.InlineKeyboardButton("На підтвердження", callback_data="on_acceptance")
        finished = types.InlineKeyboardButton("Виконано", callback_data="finished")
        mar = types.InlineKeyboardMarkup(row_width=2).add(work, handled, acceptance, finished)
        count += 1
        await bot.send_message(channel_id, f"Заявка {count}\n"
                                                f"Ім'я, прізвище: {full_name}\n"
                                                f"Номер телефону: {phone}\n"
                                                f"Почта: {email}\n"
                                                f"Повідомлення: {complaint}", reply_markup=mar)
        await bot.delete_message(callback_data.from_user.id, deleting_mes.message_id)
        await continues(mess)
    else:
        await bot.send_message(mess.from_user.id, "Ваше повідомлення відправлено в роботу. Залишайтесь на зв’язку.")
        await continues(mess)


@dp.callback_query_handler(text="work")
@dp.callback_query_handler(text="handled")
@dp.callback_query_handler(text="on_acceptance")
@dp.callback_query_handler(text="finished")
async def channel_handler(callback_data: types.CallbackQuery):
    global sent
    stat = types.KeyboardButton("Статистика")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True).add(stat)
    if str(callback_data.data) == "work":
        await bot.send_message(user, "В роботі")
        await bot.send_message(channel_id, f"Заявка {count}\n"
                                            "Статус: В роботі\n"
                                            f"Менеджер: {callback_data.from_user.full_name}", reply_markup=mar)
    elif str(callback_data.data) == "handled":
        await bot.send_message(user, "На обробці")
        await bot.send_message(channel_id, f"Заявка {count}\n"
                                            "Статус: На обробці\n"
                                            f"Менеджер: {callback_data.from_user.full_name}", reply_markup=mar)
    elif str(callback_data.data) == "on_acceptance":
        await bot.send_message(user, "На затвердженні")
        await bot.send_message(channel_id, f"Заявка {count}\n"
                                            "Статус: На затвердженні\n"
                                            f"Менеджер: {callback_data.from_user.full_name}", reply_markup=mar)
    elif str(callback_data.data) == "finished":
        await bot.send_message(user, "Завершено")
        await bot.send_message(channel_id, f"Заявка {count}\n"
                                            "Статус: Завершено\n"
                                            f"Менеджер: {callback_data.from_user.full_name}", reply_markup=mar)
        sent = False


@dp.message_handler(text=texts['block1']['title'])
@dp.callback_query_handler(text=texts['block1']['title'])
async def block1(message: types.Message=None, callback_data: types.CallbackQuery=None):
    print(message)
    quest1 = types.KeyboardButton(texts['block1']['questions']['question1'], callback_data=texts['block1']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block1']['questions']['question2'], callback_data=texts['block1']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block1']['questions']['question3'], callback_data=texts['block1']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block1']['questions']['question4'], callback_data=texts['block1']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block1']['questions']['question5'], callback_data=texts['block1']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block1']['questions']['question6'], callback_data=texts['block1']['questions']['question6'])
    quest7 = types.KeyboardButton(texts['block1']['questions']['question7'], callback_data=texts['block1']['questions']['question7'])
    quest8 = types.KeyboardButton(texts['block1']['questions']['question8'], callback_data=texts['block1']['questions']['question8'])
    quest9 = types.KeyboardButton(texts['block1']['questions']['question9'], callback_data=texts['block1']['questions']['question9'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block1']['title'], chat_id=callback_data.from_user.id,
                               reply_markup=mar)


@dp.message_handler(text=texts['block1']['questions']['question1'])
async def quest1_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block1']['questions']['question2'])
async def quest1_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block1']['questions']['question3'])
async def quest1_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block1']['questions']['question4'])
async def quest1_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block1']['questions']['question5'])
async def quest1_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block1']['questions']['question6'])
async def quest1_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer6']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block1']['questions']['question7'])
async def quest1_7(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer7']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block1']['questions']['question8'])
async def quest1_8(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer8']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block1']['questions']['question9'])
async def quest1_9(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block1']['answers']['answer9']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block2']['title'])
@dp.callback_query_handler(text=texts['block2']['title'])
async def block2(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block2']['questions']['question1'], callback_data=texts['block2']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block2']['questions']['question2'], callback_data=texts['block2']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block2']['questions']['question3'], callback_data=texts['block2']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block2']['questions']['question4'], callback_data=texts['block2']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block2']['questions']['question5'], callback_data=texts['block2']['questions']['question5'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block2']['title'], chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block2']['questions']['question1'])
async def quest2_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block2']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block2']['questions']['question2'])
async def quest2_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block2']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block2']['questions']['question3'])
async def quest2_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block2']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block2']['questions']['question4'])
async def quest2_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block2']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block2']['questions']['question5'])
async def quest2_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block2']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block3']['title'])
@dp.callback_query_handler(text=texts['block3']['title'])
async def block3(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block3']['questions']['question1'], callback_data=texts['block3']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block3']['questions']['question2'], callback_data=texts['block3']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block3']['questions']['question3'], callback_data=texts['block3']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block3']['questions']['question4'], callback_data=texts['block3']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block3']['questions']['question5'], callback_data=texts['block3']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block3']['questions']['question6'], callback_data=texts['block3']['questions']['question6'])
    quest7 = types.KeyboardButton(texts['block3']['questions']['question7'], callback_data=texts['block3']['questions']['question7'])
    quest8 = types.KeyboardButton(texts['block3']['questions']['question8'], callback_data=texts['block3']['questions']['question8'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(
            text=texts['block3']['title'],
            chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block3']['questions']['question1'])
async def quests3_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block3']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block3']['questions']['question2'])
async def quests3_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block3']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block3']['questions']['question3'])
async def quests3_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block3']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block3']['questions']['question4'])
async def quest3_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block3']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block3']['questions']['question5'])
async def quest3_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block3']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block3']['questions']['question6'])
async def quest3_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block3']['answers']['answer6']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block3']['questions']['question7'])
async def quest3_7(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block3']['answers']['answer7']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block3']['questions']['question8'])
async def quest3_8(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block3']['answers']['answer8']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block4']['title'])
@dp.callback_query_handler(text=texts['block4']['title'])
async def block4(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block4']['questions']['question1'], callback_data=texts['block4']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block4']['questions']['question2'], callback_data=texts['block4']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block4']['questions']['question3'], callback_data=texts['block4']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block4']['questions']['question4'], callback_data=texts['block4']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block4']['questions']['question5'], callback_data=texts['block4']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block4']['questions']['question6'], callback_data=texts['block4']['questions']['question6'])
    quest7 = types.KeyboardButton(texts['block4']['questions']['question7'], callback_data=texts['block4']['questions']['question7'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block4']['title'], chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block4']['questions']['question1'])
async def quest4_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block4']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block4']['questions']['question2'])
async def quest4_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block4']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block4']['questions']['question3'])
async def quest4_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block4']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block4']['questions']['question4'])
async def quest4_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block4']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block4']['questions']['question5'])
async def quest4_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block4']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block4']['questions']['question6'])
async def quest4_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block4']['answers']['answer6']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block4']['questions']['question7'])
async def quest4_7(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block4']['answers']['answer7']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block5']['title'])
@dp.callback_query_handler(text=texts['block5']['title'])
async def block5(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block5']['questions']['question1'], callback_data=texts['block5']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block5']['questions']['question2'], callback_data=texts['block5']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block5']['questions']['question3'], callback_data=texts['block5']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block5']['questions']['question4'], callback_data=texts['block5']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block5']['questions']['question5'], callback_data=texts['block5']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block5']['questions']['question6'], callback_data=texts['block5']['questions']['question6'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block5']['title'], chat_id=callback_data.from_user.id,
                               reply_markup=mar)


@dp.message_handler(text=texts['block5']['questions']['question1'])
async def quest5_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block5']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block5']['questions']['question2'])
async def quest5_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block5']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block5']['questions']['question3'])
async def quest5_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block5']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block5']['questions']['question4'])
async def quest5_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block5']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block5']['questions']['question5'])
async def quest5_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block5']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block5']['questions']['question6'])
async def quest5_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block5']['answers']['answer6']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['title'])
@dp.callback_query_handler(text=texts['block6']['title'])
async def block6(message: types.Message=None, callback_data:types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block6']['questions']['question1'], callback_data=texts['block6']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block6']['questions']['question2'], callback_data=texts['block6']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block6']['questions']['question3'], callback_data=texts['block6']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block6']['questions']['question4'], callback_data=texts['block6']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block6']['questions']['question5'], callback_data=texts['block6']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block6']['questions']['question6'], callback_data=texts['block6']['questions']['question6'])
    quest7 = types.KeyboardButton(texts['block6']['questions']['question7'], callback_data=texts['block6']['questions']['question7'])
    quest8 = types.KeyboardButton(texts['block6']['questions']['question8'], callback_data=texts['block6']['questions']['question8'])
    quest9 = types.KeyboardButton(texts['block6']['questions']['question9'], callback_data=texts['block6']['questions']['question9'])
    quest10 = types.KeyboardButton(texts['block6']['questions']['question10'], callback_data=texts['block6']['questions']['question10'])
    quest11 = types.KeyboardButton(texts['block6']['questions']['question11'], callback_data=texts['block6']['questions']['question11'])
    quest12 = types.KeyboardButton(texts['block6']['questions']['question12'], callback_data=texts['block6']['questions']['question12'])
    quest13 = types.KeyboardButton(texts['block6']['questions']['question13'], callback_data=texts['block6']['questions']['question13'])
    quest14 = types.KeyboardButton(texts['block6']['questions']['question14'], callback_data=texts['block6']['questions']['question14'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, quest10, quest11, quest12, quest13, quest14, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block6']['title'], chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block6']['questions']['question1'])
async def quest6_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question2'])
async def quest6_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question3'])
async def quest6_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question4'])
async def quest6_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question5'])
async def quest6_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question6'])
async def quest6_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer6']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question7'])
async def quest6_7(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer7']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question8'])
async def quest6_8(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer8']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question9'])
async def quest6_9(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer9']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question10'])
async def quest6_10(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer10']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question11'])
async def quest6_11(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer11']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question12'])
async def quest6_12(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer12']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question13'])
async def quest6_13(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer13']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block6']['questions']['question14'])
async def quest6_14(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block6']['answers']['answer14']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block7']['title'])
@dp.callback_query_handler(text=texts['block7']['title'])
async def block7(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block7']['questions']['question1'], callback_data=texts['block7']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block7']['questions']['question2'], callback_data=texts['block7']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block7']['questions']['question3'], callback_data=texts['block7']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block7']['questions']['question4'], callback_data=texts['block7']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block7']['questions']['question5'], callback_data=texts['block7']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block7']['questions']['question6'], callback_data=texts['block7']['questions']['question6'])
    quest7 = types.KeyboardButton(texts['block7']['questions']['question7'], callback_data=texts['block7']['questions']['question7'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block7']['title'], chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block7']['questions']['question1'])
async def quest7_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block7']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block7']['questions']['question2'])
async def quest7_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block7']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block7']['questions']['question3'])
async def quest7_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block7']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block7']['questions']['question4'])
async def quest7_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block7']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block7']['questions']['question5'])
async def quest7_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block7']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block7']['questions']['question6'])
async def quest7_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(message.from_user.id, "\n".join(texts['block7']['answers']['answer6']))


@dp.message_handler(text=texts['block7']['questions']['question7'])
async def quest7_7(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block7']['answers']['answer7']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block8']['title'])
@dp.callback_query_handler(text=texts['block8']['title'])
async def block8(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block8']['questions']['question1'], callback_data=texts['block8']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block8']['questions']['question2'], callback_data=texts['block8']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block8']['questions']['question3'], callback_data=texts['block8']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block8']['questions']['question4'], callback_data=texts['block8']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block8']['questions']['question5'], callback_data=texts['block8']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block8']['questions']['question6'], callback_data=texts['block8']['questions']['question6'])
    quest7 = types.KeyboardButton(texts['block8']['questions']['question7'], callback_data=texts['block8']['questions']['question7'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block8']['title'], chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block8']['questions']['question1'])
async def quest8_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block8']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block8']['questions']['question2'])
async def quest8_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block8']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block8']['questions']['question3'])
async def quest8_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block8']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block8']['questions']['question4'])
async def quest8_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block8']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block8']['questions']['question5'])
async def quest8_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block8']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block8']['questions']['question6'])
async def quest8_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block8']['answers']['answer6']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block8']['questions']['question7'])
async def quest8_7(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block8']['answers']['answer7']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block9']['title'])
@dp.callback_query_handler(text=texts['block9']['title'])
async def block9(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block9']['questions']['question1'], callback_data=texts['block9']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block9']['questions']['question2'], callback_data=texts['block9']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block9']['questions']['question3'], callback_data=texts['block9']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block9']['questions']['question4'], callback_data=texts['block9']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block9']['questions']['question5'], callback_data=texts['block9']['questions']['question5'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block9']['title'], chat_id=callback_data.from_user.id,
                               reply_markup=mar)


@dp.message_handler(text=texts['block9']['questions']['question1'])
async def quest9_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block9']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block9']['questions']['question2'])
async def quest9_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block9']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block9']['questions']['question3'])
async def quest9_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block9']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block9']['questions']['question4'])
async def quest9_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block9']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block9']['questions']['question5'])
async def quest9_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block9']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['title'])
@dp.callback_query_handler(text=texts['block10']['title'])
async def block10(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block10']['questions']['question1'], callback_data=texts['block10']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block10']['questions']['question2'], callback_data=texts['block10']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block10']['questions']['question3'], callback_data=texts['block10']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block10']['questions']['question4'], callback_data=texts['block10']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block10']['questions']['question5'], callback_data=texts['block10']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block10']['questions']['question6'], callback_data=texts['block10']['questions']['question6'])
    quest7 = types.KeyboardButton(texts['block10']['questions']['question7'], callback_data=texts['block10']['questions']['question7'])
    quest8 = types.KeyboardButton(texts['block10']['questions']['question8'], callback_data=texts['block10']['questions']['question8'])
    quest9 = types.KeyboardButton(texts['block10']['questions']['question9'], callback_data=texts['block10']['questions']['question9'])
    quest10 = types.KeyboardButton(texts['block10']['questions']['question10'], callback_data=texts['block10']['questions']['question10'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, quest10, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block10']['title'], chat_id=callback_data.from_user.id,
                               reply_markup=mar)


@dp.message_handler(text=texts['block10']['questions']['question1'])
async def quest10_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question2'])
async def quest10_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question3'])
async def quest10_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question4'])
async def quest10_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question5'])
async def quest10_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question6'])
async def quest10_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer6']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question7'])
async def quest10_7(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer7']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question8'])
async def quest10_8(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer8']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question9'])
async def quest10_9(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer9']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block10']['questions']['question10'])
async def quest10_10(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block10']['answers']['answer10']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block11']['title'])
@dp.callback_query_handler(text=texts['block11']['title'])
async def block11(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block11']['questions']['question1'], callback_data=texts['block11']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block11']['questions']['question2'], callback_data=texts['block11']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block11']['questions']['question3'], callback_data=texts['block11']['questions']['question3'])
    quest4 = types.KeyboardButton(texts['block11']['questions']['question4'], callback_data=texts['block11']['questions']['question4'])
    quest5 = types.KeyboardButton(texts['block11']['questions']['question5'], callback_data=texts['block11']['questions']['question5'])
    quest6 = types.KeyboardButton(texts['block11']['questions']['question6'], callback_data=texts['block11']['questions']['question6'])
    quest7 = types.KeyboardButton(texts['block11']['questions']['question7'], callback_data=texts['block11']['questions']['question7'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block11']['title'], chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block11']['questions']['question1'])
async def quest11_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block11']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block11']['questions']['question2'])
async def quest11_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block11']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block11']['questions']['question3'])
async def quest11_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block11']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block11']['questions']['question4'])
async def quest11_4(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block11']['answers']['answer4']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block11']['questions']['question5'])
async def quest11_5(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block11']['answers']['answer5']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block11']['questions']['question6'])
async def quest11_6(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block11']['answers']['answer6']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block11']['questions']['question7'])
async def quest11_7(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block11']['answers']['answer7']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block12']['title'])
@dp.callback_query_handler(text=texts['block12']['title'])
async def block12(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block12']['questions']['question1'], callback_data=texts['block12']['questions']['question1'])
    quest2 = types.KeyboardButton(texts['block12']['questions']['question2'], callback_data=texts['block12']['questions']['question2'])
    quest3 = types.KeyboardButton(texts['block12']['questions']['question3'], callback_data=texts['block12']['questions']['question3'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block12']['title'], chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block12']['questions']['question1'])
async def quest12_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block12']['answers']['answer1']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block12']['questions']['question2'])
async def quest12_2(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block12']['answers']['answer2']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block12']['questions']['question3'])
async def quest12_3(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block12']['answers']['answer3']), chat_id=message.from_user.id)


@dp.message_handler(text=texts['block13']['title'])
@dp.callback_query_handler(text=texts['block13']['title'])
async def block13(message: types.Message=None, callback_data: types.CallbackQuery=None):
    quest1 = types.KeyboardButton(texts['block13']['questions']['question1'], callback_data=texts['block13']['questions']['question1'])
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, back)
    if message:
        await bot.send_message(text="Оберіть питання для отримання консультації👇", chat_id=message.from_user.id, reply_markup=mar)
    else:
        await bot.send_message(text=texts['block13']['title'], chat_id=callback_data.from_user.id, reply_markup=mar)


@dp.message_handler(text=texts['block13']['questions']['question1'])
async def quest13_1(message: types.Message):
    global question_count
    question_count += 1
    await bot.send_message(text="\n".join(texts['block13']['answers']['answer1']), chat_id=message.from_user.id)


if __name__ == "__main__":
    start_date_day, start_date_week = datetime.now(), datetime.now()
    executor.start_polling(dp)
