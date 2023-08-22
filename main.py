from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData


bot = Bot(token="6339639367:AAFfRK1z6yhvaLTq55C8I42lpNUAgTEeGbM")
dp = Dispatcher(bot)
inline = CallbackData("post", "action", "data")
full_name, phone, email, complaint, user = '', '', '', '', ''
sent = False


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    next = types.KeyboardButton("Розпочати")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True).add(next)
    await bot.send_message(message.from_user.id, "Вас вітає бот «Поверни Своє».\n\n"
                                                 "Цей бот дозволить знайти допомогу людям, чиє майно постраждало внаслідок збройної агресії рф проти України.", reply_markup=mar)


@dp.message_handler(text="Розпочати")
@dp.message_handler(text="Назад🔙")
async def continues(message: types.Message):
    block1 = types.KeyboardButton("Підтвердження права вланості на майнo", callback_data="Підтвердження права вланості на майнo")
    block2 = types.KeyboardButton("Фіксація ДСНС", callback_data="Фіксація ДСНС")
    block3 = types.KeyboardButton("Фіксація сільською/селищною міською радою, у разі їх відсутності військовою адміністрацією або військово-цивільною адміністрацією", callback_data="Фіксація сільською/селищною міською радою, у разі їх відсутності військовою адміністрацією або військово-цивільною адміністрацією")
    block4 = types.KeyboardButton("Фіксація НПУ", callback_data="Фіксація НПУ")
    block5 = types.KeyboardButton("Фіксація державною екологічною інспекцією", callback_data="Фіксація державною екологічною інспекцією")
    block6 = types.KeyboardButton("Самостійна фіксація", callback_data="Самостійна фіксація")
    block7 = types.KeyboardButton("Збір пояснень свідків", callback_data="Збір пояснень свідків")
    block8 = types.KeyboardButton("Збір матеріалів зі ЗМІ", callback_data="Збір матеріалів зі ЗМІ")
    block9 = types.KeyboardButton("Збір  чеків на пошкоджене/зруйноване майно", callback_data="Збір  чеків на пошкоджене/зруйноване майно")
    block10 = types.KeyboardButton("Збір інформації про підключення комунальних послуг", callback_data="Збір інформації про підключення комунальних послуг")
    block11 = types.KeyboardButton("Збереження зібраних матеріалів", callback_data="Збереження зібраних матеріалів")
    block12 = types.KeyboardButton("Звернення до НПУ із заявою", callback_data="Звернення до НПУ із заявою")
    block13 = types.KeyboardButton("Подання онлайн заявок", callback_data="Подання онлайн заявок")
    support = types.KeyboardButton("Звернутися в підтримку")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, support)
    await bot.send_message(message.from_user.id, "Виберіть блок який вас цікавить:", reply_markup=mar)


@dp.message_handler(text="Звернутися в підтримку")
async def support(message: types.Message):
    global sent
    if not sent:
        sent = True
        await bot.send_message(message.from_user.id, "Напишіть ваше ім'я та прізвище")
        @dp.message_handler()
        async def fullName(message: types.Message):
            global full_name, phone, email, complaint, user
            user = message.from_user.id
            if full_name == '':
                full_name = message.text

                phone_butt = types.KeyboardButton("Відправити номер телефону", request_contact=True)
                mar = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(phone_butt)
                await bot.send_message(message.from_user.id, "Відправте ваш номер телефону", reply_markup=mar)
            elif email == '':
                email = message.text
                await bot.send_message(message.from_user.id, "Напишіть ваше повідомлення")
            elif complaint == '':
                complaint = message.text
                send = types.InlineKeyboardButton("Відправити📩", callback_data="complaint")
                send_mar = types.InlineKeyboardMarkup().add(send)
                await bot.send_message(message.from_user.id, f"{full_name}\n"
                                                                f"{phone}\n"
                                                                f"{email}\n"
                                                                f"{complaint}", reply_markup=send_mar)
            @dp.message_handler(content_types=types.ContentType.CONTACT)
            async def phone_func(message: types.Message):
                global phone
                phone = str(message.contact.phone_number)
                await bot.send_message(message.from_user.id, "Напишіть вашу почту")
    else:
        await bot.send_message(message.from_user.id, "Ваше повідомлення відправлено в роботу. Залишайтесь на зв’язку.")


@dp.callback_query_handler(text=["complaint"])
async def send_complaint(callback_data: types.CallbackQuery):
    work = types.InlineKeyboardButton("В роботі", callback_data="work")
    handled = types.InlineKeyboardButton("Оброблено", callback_data="handled")
    acceptance = types.InlineKeyboardButton("На підтвердження", callback_data="on_acceptance")
    finished = types.InlineKeyboardButton("Виконано", callback_data="finished")
    mar = types.InlineKeyboardMarkup(row_width=2).add(work, handled, acceptance, finished)
    await bot.send_message("-1001901159869", f"Ім'я, прізвище: {full_name}\n"
                                                                f"Номер телефону: {phone}\n"
                                                                f"Почта: {email}\n"
                                                                f"Повідомлення: {complaint}", reply_markup=mar)


@dp.callback_query_handler(text="work")
@dp.callback_query_handler(text="handled")
@dp.callback_query_handler(text="on_acceptance")
@dp.callback_query_handler(text="finished")
async def channel_handler(callback_data: types.CallbackQuery):
    if str(callback_data.data) == "work":
        await bot.send_message(user, "Вашу заявку взято до роботи")
    elif str(callback_data.data) == "handled":
        await bot.send_message(user, "Ваша заявка на обробці")
    elif str(callback_data.data) == "on_acceptance":
        await bot.send_message(user, "Ваша заявка на підтвердженні")
    elif str(callback_data.data) == "finished":
        await bot.send_message(user, "Відповідь на ваше запитання готове!")



@dp.message_handler(text="Підтвердження права вланості на майнo")
async def block1(message: types.Message):
    print(message)
    quest1 = types.KeyboardButton("Які основні правовстановлюючі документи підтверджують власність на майно?", callback_data="Які основні правовстановлюючі документи підтверджують власність на майно?")
    quest2 = types.KeyboardButton("Які документи потрібно зберегти для підтвердження права власності на майно?", callback_data="Які документи потрібно зберегти для підтвердження права власності на майно?")
    quest3 = types.KeyboardButton("Чи можна зберігати копії документів про право власності в електронному вигляді?", callback_data="Чи можна зберігати копії документів про право власності в електронному вигляді?")
    quest4 = types.KeyboardButton("Як поновити втрачені документи на майно?", callback_data="Як поновити втрачені документи на майно?")
    quest5 = types.KeyboardButton("Як зменшити ризик втрати документів?", callback_data="Як зменшити ризик втрати документів?")
    quest6 = types.KeyboardButton("Як отримати інформацію про майно з Державного реєстру речових прав на нерухоме майно?", callback_data="Як отримати інформацію про майно з Державного реєстру речових прав на нерухоме майно?")
    quest7 = types.KeyboardButton("Що робити у випадку втрати або пошкодження документа про право власності на майно?", callback_data="Що робити у випадку втрати або пошкодження документа про право власності на майно?")
    quest8 = types.KeyboardButton("Як діяти, якщо виникають проблеми з визнанням права власності на майно?", callback_data="Як діяти, якщо виникають проблеми з визнанням права власності на майно?")
    quest9 = types.KeyboardButton("Якщо є копії документів про право власності чи потрібно відновлювати оригінали?", callback_data="Якщо є копії документів про право власності чи потрібно відновлювати оригінали?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, back)
    await bot.send_message(text="Підтвердження права вланості на майнo", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які основні правовстановлюючі документи підтверджують власність на майно?")
async def quest1_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="-  Договір, за яким відповідно до законодавства передбачається перехід права власності, зокрема купівлі-продажу, міни, дарування, довічного утримання, лізингу, предметом якого є нерухоме майно, про припинення права на аліменти для дитини у зв'язку з передачею права власності на нерухоме майно, договір іпотеки, що містить застереження про задоволення вимог іпотекодержателя, договір про задоволення вимог іпотекодержателя, спадковий договір (за наявності свідоцтва органу реєстрації актів цивільного стану про смерть чи рішення суду про оголошення особи померлою), договір про виділ у натурі частки з нерухомого майна, що є у спільній власності, про поділ нерухомого майна, що є у спільній власності.\n"
                                "-  Свідоцтво про право власності на частку в спільному майні подружжя в разі смерті одного з подружжя, що видається нотаріусом.\n"
                                "-  Свідоцтво про право на спадщину, видане нотаріусом.\n"
                                "-  Свідоцтво про право власності на нерухоме майно, видане органом місцевого самоврядування.\n"
                                "-  Свідоцтво про право власності, видане органом приватизації наймачам житлових приміщень державного та комунального житлового фонду.\n"
                                "-  Рішення суду про визнання права власності на об'єкти нерухомого майна, про встановлення факту права власності на об'єкти нерухомого майна, про передачу безхазяйного нерухомого майна до комунальної власності.\n"
                                "-  Ухвала суду про затвердження (визнання) мирової угоди.\n"
                                "-  Дублікат правовстановлювального документа, виданий нотаріусом, органом місцевого самоврядування, органом приватизації, копія архівного правовстановлювального документа, видана державним архівом.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи потрібно зберегти для підтвердження права власності на майно?")
async def quest1_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="-  Договір, за яким відповідно до законодавства передбачається перехід права власності, зокрема купівлі-продажу, міни, дарування, довічного утримання, лізингу, предметом якого є нерухоме майно, про припинення права на аліменти для дитини у зв'язку з передачею права власності на нерухоме майно, договір іпотеки, що містить застереження про задоволення вимог іпотекодержателя, договір про задоволення вимог іпотекодержателя, спадковий договір (за наявності свідоцтва органу реєстрації актів цивільного стану про смерть чи рішення суду про оголошення особи померлою), договір про виділ у натурі частки з нерухомого майна, що є у спільній власності, про поділ нерухомого майна, що є у спільній власності.\n"
                                "-  Свідоцтво про право власності на частку в спільному майні подружжя в разі смерті одного з подружжя, що видається нотаріусом.\n"
                                "-  Свідоцтво про право на спадщину, видане нотаріусом.\n"
                                "-  Свідоцтво про право власності на нерухоме майно, видане органом місцевого самоврядування.\n"
                                "-  Свідоцтво про право власності, видане органом приватизації наймачам житлових приміщень державного та комунального житлового фонду.\n"
                                "-  Рішення суду про визнання права власності на об'єкти нерухомого майна, про встановлення факту права власності на об'єкти нерухомого майна, про передачу безхазяйного нерухомого майна до комунальної власності.\n"
                                "-  Ухвала суду про затвердження (визнання) мирової угоди.\n"
                                "-  Дублікат правовстановлювального документа, виданий нотаріусом, органом місцевого самоврядування, органом приватизації, копія архівного правовстановлювального документа, видана державним архівом.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи можна зберігати копії документів про право власності в електронному вигляді?")
async def quest1_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так, зробіть декілька примірників копій, які доцільно зберігати в різних місцях) та сканкопії (на різних пристроях та у хмарних сховищах). Це мінімізує ризик їх втрати", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як поновити втрачені документи на майно?")
async def quest1_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="За можливістю зробіть витяг щодо перебування майна у власності з Державного реєстру речових прав на нерухоме майно (подати запит на отримання інформації через персональний кабінет веб-сайту «Кабінет електронних сервісів» Міністерства юстиції України https://psjust.gov.ua/elektronni-posluhy/elektronni-servisy-on-layn/ або отримати довідку через додаток Дія https://diia.gov.ua/services/informaciya-z-derzhavnogo-reyestru-rechovih-prav-na-neruhome-majno).", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як зменшити ризик втрати документів?")
async def quest1_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="При можливості, зробіть декілька примірників копій, які доцільно зберігати в різних місцях) та сканкопії (на різних пристроях та у хмарних сховищах). Це мінімізує ризик їх втрати.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як отримати інформацію про майно з Державного реєстру речових прав на нерухоме майно?")
async def quest1_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Подати запит на отримання інформації через персональний кабінет веб-сайту «Кабінет електронних сервісів» Міністерства юстиції України https://psjust.gov.ua/elektronni-posluhy/elektronni-servisy-on-layn/ або отримати довідку через додаток Дія https://diia.gov.ua/services/informaciya-z-derzhavnogo-reyestru-rechovih-prav-na-neruhome-majno).", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Що робити у випадку втрати або пошкодження документа про право власності на майно?")
async def quest1_7(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Слід звернутися із письмовою заявою до органу місцевого самоврядування чи нотаріуса для отримання дублікату.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як діяти, якщо виникають проблеми з визнанням права власності на майно?")
async def quest1_8(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Ви маєте право звернутися до суду для визнання права власності на майно, яке не визнається чи оспорюється.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Якщо є копії документів про право власності чи потрібно відновлювати оригінали?")
async def quest1_9(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Підтвердження права вланості на майнo")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Фіксація ДСНС")
async def block2(message: types.Message):
    quest1 = types.KeyboardButton("Чи є обмеження в часі для фіксації пошкоджень/руйнування майна?", callback_data="Чи є обмеження в часі для фіксації пошкоджень/руйнування майна?")
    quest2 = types.KeyboardButton("Як швидко потрібно фіксувати факти руйнування/пошкодження майна?", callback_data="Як швидко потрібно фіксувати факти руйнування/пошкодження майна?")
    quest3 = types.KeyboardButton("Що робити у випадку пожежі або аварійної ситуації?", callback_data="Що робити у випадку пожежі або аварійної ситуації?")
    quest4 = types.KeyboardButton("Які відомості повинні бути включені до акту про пожежу або акту пошкодження майна?", callback_data="Які відомості повинні бути включені до акту про пожежу або акту пошкодження майна?")
    quest5 = types.KeyboardButton("Як отримати копії актів про пожежу або пошкодження майна?", callback_data="Як отримати копії актів про пожежу або пошкодження майна?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, back)
    await bot.send_message(text="Фіксація ДСНС", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи є обмеження в часі для фіксації пошкоджень/руйнування майна?")
@dp.message_handler(text="Як швидко потрібно фіксувати факти руйнування/пошкодження майна?")
async def quest2_1and2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація ДСНС")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Фіксацію фактів руйнування/пошкодження об'єктів нерухомого майна бажано здійснювати у максимально короткий час після вчинення акту агресії рф, що спричинив його руйнацію/пошкодження з урахуванням безпекової ситуації.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Що робити у випадку пожежі або аварійної ситуації?")
async def quest2_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація ДСНС")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Здійснити виклик Державної служби з надзвичайних ситуацій (зателефонувати за номером «101») для роЗМІнування, усунення наслідків та складання акту про пожежу та акту пошкодження або руйнування майна із зазначенням причини такого руйнування.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які відомості повинні бути включені до акту про пожежу або акту пошкодження майна?")
async def quest2_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація ДСНС")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="До такого акту вносяться відомості, зокрема, про дату, час, місце, опис знищеного та пошкодженого майна, прямі та побічні збитки, причину тощо.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як отримати копії актів про пожежу або пошкодження майна?")
async def quest2_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація ДСНС")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Якщо не отримано акт про пошкодження на місці, тоді вам потрібно звернутися до місцевого підрозділу ДСНС", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Фіксація сільською/селищною міською радою, у разі їх відсутності військовою адміністрацією або військово-цивільною адміністрацією")
async def block3(message: types.Message):
    quest1 = types.KeyboardButton("Чи встановлена форма заяви та де її можна знайти?", callback_data="Чи встановлена форма заяви та де її можна знайти?")
    quest2 = types.KeyboardButton("Чи є зразкова форма заяви для звернення?", callback_data="Чи є зразкова форма заяви для звернення?")
    quest3 = types.KeyboardButton("Які дані потрібно включити до заяви для звернення?", callback_data="Які дані потрібно включити до заяви для звернення?")
    quest4 = types.KeyboardButton("Як звернутися до посадових осіб сільської /селищної/міської ради або військово-цивільної адміністрації?", callback_data="Як звернутися до посадових осіб сільської /селищної/міської ради або військово-цивільної адміністрації?")
    quest5 = types.KeyboardButton("Які документи можуть знадобитись для надання до сільської /селищної/міської ради?", callback_data="Які документи можуть знадобитись для надання до сільської /селищної/міської ради?")
    quest6 = types.KeyboardButton("Чи потрібно надати додаткові документи разом із заявою до посадових осіб сільської /селищної/міської ради?", callback_data="Чи потрібно надати додаткові документи разом із заявою до посадових осіб сільської /селищної/міської ради?")
    quest7 = types.KeyboardButton("Що робити, якщо відсутні сільська /селищна/міська ради?", callback_data="Що робити, якщо відсутні сільська /селищна/міська ради?")
    quest8 = types.KeyboardButton("Чи можна отримати копії актів про пошкодження майна?", callback_data="Чи можна отримати копії актів про пошкодження майна?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, back)
    await bot.send_message(text="БЛОК 3 – ФІКСАЦІЯ СІЛЬСЬКОЮ/СЕЛИЩНОЮ МІСЬКОЮ РАДОЮ, У РАЗІ ЇХ ВІДСУТНОСТІ ВІЙСЬКОВОЮ АДМІНІСТРАЦІЄЮ АБО ВІЙСЬКОВО-ЦИВІЛЬНОЮ АДМІНІСТРАЦІЄЮ", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи встановлена форма заяви та де її можна знайти?")
@dp.message_handler(text="Чи є зразкова форма заяви для звернення?")
@dp.message_handler(text="Які дані потрібно включити до заяви для звернення?")
async def quests3_1_2_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація сільською/селищною міською радою, у разі їх відсутності військовою адміністрацією або військово-цивільною адміністрацією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Зразкову форму можна знайти за посиланням (Алгоритм дій з фіксації, Додаток 3)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як звернутися до посадових осіб сільської /селищної/міської ради або військово-цивільної адміністрації?")
async def quest3_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація сільською/селищною міською радою, у разі їх відсутності військовою адміністрацією або військово-цивільною адміністрацією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="особисто – шляхом звернення до загального відділу відповідної ради з заявою \nпоштою – шляхом направлення заяви поштовим відправленням (краще направляти цінним листом з описом вкладення).", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи можуть знадобитись для надання до сільської /селищної/міської ради?")
@dp.message_handler(text="Чи потрібно надати додаткові документи разом із заявою до посадових осіб сільської /селищної/міської ради?")
async def quest3_5_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація сільською/селищною міською радою, у разі їх відсутності військовою адміністрацією або військово-цивільною адміністрацією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="- заява на проведення обстеження житла;\n"
                                "-	копії документа, що підтверджує особу;\n"
                                "- копії документа з даними про реєстраційний номер облікової картки платника податків;\n"
                                "- копій документів, що підтверджують наявність права власності на житло на момент подання заяви.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Що робити, якщо відсутні сільська /селищна/міська ради?")
async def quest3_7(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація сільською/селищною міською радою, у разі їх відсутності військовою адміністрацією або військово-цивільною адміністрацією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Варто звернутися до військово-цивільної адміністрації або іншої компетентної установи на території вашого населеного пункту", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи можна отримати копії актів про пошкодження майна?")
async def quest3_8(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація сільською/селищною міською радою, у разі їх відсутності військовою адміністрацією або військово-цивільною адміністрацією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так, якщо не отримано акт про пошкодження на місці, тоді вам треба звернутися до міської або селищної ради, або військово-цивільної адміністрації.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Фіксація НПУ")
async def block4(message: types.Message):
    quest1 = types.KeyboardButton("Чи можна звернутися до поліції для фіксації?", callback_data="Чи можна звернутися до поліції для фіксації?")
    quest2 = types.KeyboardButton("Чи потрібно викликати поліцію для складення протоколу та фіксації?", callback_data="Чи потрібно викликати поліцію для складення протоколу та фіксації?")
    quest3 = types.KeyboardButton("Які документи має надати  поліція після звернення для фіксації?", callback_data="Які документи має надати  поліція після звернення для фіксації?")
    quest4 = types.KeyboardButton("Які інші ситуації можуть вимагати виклику поліції, окрім фіксації?", callback_data="Які інші ситуації можуть вимагати виклику поліції, окрім фіксації?")
    quest5 = types.KeyboardButton("Як отримати копію складеного протоколу, якщо вона не була видана на місці події?", callback_data="Як отримати копію складеного протоколу, якщо вона не була видана на місці події?")
    quest6 = types.KeyboardButton("Чи потрібно викликати поліцію в будь-якому випадку руйнувань/пошкоджень майна?", callback_data="Чи потрібно викликати поліцію в будь-якому випадку руйнувань/пошкоджень майна?")
    quest7 = types.KeyboardButton("Як зв’язатися з поліцією, якщо немає можливості зателефонувати на номер 102?", callback_data="Як зв’язатися з поліцією, якщо немає можливості зателефонувати на номер 102?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, back)
    await bot.send_message(text="Фіксація НПУ", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи можна звернутися до поліції для фіксації?")
async def quest4_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація НПУ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи потрібно викликати поліцію для складення протоколу та фіксації?")
async def quest4_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація НПУ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Для того, щоб зафіксувати інформацію про кримінальне правопорушення. На підставі заяви громадянина вноситься інформація в Єдиний реєстр досудових розслідувань (ЄРДР) за фактом знищення або пошкодження майна внаслідок воєнних дій.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи має надати  поліція після звернення для фіксації?")
async def quest4_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація НПУ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Копію протоколу та витяг з Єдиного реєстру досудових розслідувань", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які інші ситуації можуть вимагати виклику поліції, окрім фіксації?")
async def quest4_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація НПУ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Подати заяву в поліцію можна не тільки у випадку пошкодження майна внаслідок бойових дій, а також у випадках встановлення факту мародерства, пограбування або коли об’єктом пошкодження є транспортний засіб", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як отримати копію складеного протоколу, якщо вона не була видана на місці події?")
async def quest4_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація НПУ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Звернутись із заявою до територіального підрозділу у вашому регіоні", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи потрібно викликати поліцію в будь-якому випадку руйнувань/пошкоджень майна?")
async def quest4_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація НПУ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так, для фіксації скоєння кримінального правопорушення з подальшим внесенням відомостей до ЄРДР", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як зв’язатися з поліцією, якщо немає можливості зателефонувати на номер 102?")
async def quest4_7(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація НПУ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Звернутись із заявою до територіального підрозділу у вашому регіоні", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Фіксація державною екологічною інспекцією")
async def block5(message: types.Message):
    quest1 = types.KeyboardButton("Як зафіксувати завдану шкоду довкіллю?", callback_data="Як зафіксувати завдану шкоду довкіллю?")
    quest2 = types.KeyboardButton("Де отримати інформацію щодо фіксації та порядку отримання відшкодування завданої шкоди довкіллю?", callback_data="Де отримати інформацію щодо фіксації та порядку отримання відшкодування завданої шкоди довкіллю?")
    quest3 = types.KeyboardButton("Які збитки можуть виникнути на землі та ґрунті внаслідок надзвичайної ситуації та/або збройної агресії?", callback_data="Які збитки можуть виникнути на землі та ґрунті внаслідок надзвичайної ситуації та/або збройної агресії?")
    quest4 = types.KeyboardButton("Як зателефонувати на гарячу лінію Оперативного штабу при Державній екологічній інспекції України?", callback_data="Як зателефонувати на гарячу лінію Оперативного штабу при Державній екологічній інспекції України?")
    quest5 = types.KeyboardButton("Коли потрібно звернутися до Державної екологічної інспекції України?", callback_data="Коли потрібно звернутися до Державної екологічної інспекції України?")
    quest6 = types.KeyboardButton("Чи можна надіслати на електронну пошту звернення до Державної екологічної інспекції?", callback_data="Чи можна надіслати на електронну пошту звернення до Державної екологічної інспекції?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, back)
    await bot.send_message(text="Фіксація державною екологічною інспекцією", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як зафіксувати завдану шкоду довкіллю?")
async def quest5_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація державною екологічною інспекцією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Для зафіксування завданої шкоди довкіллю, земельній ділянці, водним об'єктам ви можете виконати наступні кроки: 1. Зробіть фотографії або відеозаписи, які чітко демонструють пошкодження або знищення. 2. Відзначте місце події на мапі або визначте його географічні координати. 3. Запишіть дату та час виникнення події, а також будь-які інші важливі деталі, що стосуються завданої шкоди.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Де отримати інформацію щодо фіксації та порядку отримання відшкодування завданої шкоди довкіллю?")
async def quest5_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація державною екологічною інспекцією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Інформацію щодо фіксації та порядку отримання відшкодування завданої шкоди довкіллю, земельній ділянці, водним об'єктам можна отримати в Державній екологічній інспекції України. Вони надають консультації та інформаційну підтримку стосовно процедури звернення, документації та відшкодування збитків.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які збитки можуть виникнути на землі та ґрунті внаслідок надзвичайної ситуації та/або збройної агресії?")
async def quest5_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація державною екологічною інспекцією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Збитки, які можуть виникнути на землі та ґрунті внаслідок надзвичайної ситуації та/або збройної агресії, можуть включати:\n"
                                "1. Забруднення ґрунту хімічними речовинами або іншими токсичними речовинами.\n"
                                "2. Пошкодження верхнього шару ґрунту або його ерозія.\n"
                                "3. Втрата родючості ґрунту та його негативний вплив на сільськогосподарські угіддя.\n"
                                "4. Втрата розсіяних посівів, знищення сільськогосподарської техніки або будівель.\n"
                                "5. Інші збитки, пов'язані з псуванням або втратою використовуваної земельної ділянки.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як зателефонувати на гарячу лінію Оперативного штабу при Державній екологічній інспекції України?")
async def quest5_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація державною екологічною інспекцією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Щоб зателефонувати на гарячу лінію Оперативного штабу при Державній екологічній інспекції України, ви можете скористатися наступними кроками:\n"
                                "Введіть номер +38 096 756 83 66 з телефону.\n"
                                "Зачекайте на відповідь оператора гарячої лінії.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Коли потрібно звернутися до Державної екологічної інспекції України?")
async def quest5_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація державною екологічною інспекцією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Пошкодження або забруднення земельної ділянки, водних об’єктів", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи можна надіслати на електронну пошту звернення до Державної екологічної інспекції?")
async def quest5_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Фіксація державною екологічною інспекцією")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так. Електронна пошта eco@shtab.gov.ua", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Самостійна фіксація")
async def block6(message: types.Message):
    quest1 = types.KeyboardButton("Якими технічними засобами можливо здійснювати самостійну фіксацію?", callback_data="Якими технічними засобами можливо здійснювати самостійну фіксацію?")
    quest2 = types.KeyboardButton("Чи є рекомендації щодо порядку фіксації ?", callback_data="Чи є рекомендації щодо порядку фіксації ?")
    quest3 = types.KeyboardButton("Чи достатньо відео фіксації чи фото фіксації?", callback_data="Чи достатньо відео фіксації чи фото фіксації?")
    quest4 = types.KeyboardButton("Як дії рекомендується здійснити самостійно при руйнуванні або пошкодженні майна?", callback_data="Як дії рекомендується здійснити самостійно при руйнуванні або пошкодженні майна?")
    quest5 = types.KeyboardButton("Як правильно здійснити фотофіксацію завданих збитків?", callback_data="Як правильно здійснити фотофіксацію завданих збитків?")
    quest6 = types.KeyboardButton("Як правильно здійснити відеофіксацію завданих збитків?", callback_data="Як правильно здійснити відеофіксацію завданих збитків?")
    quest7 = types.KeyboardButton("Чи потрібно отримати згоду від осіб, які потрапили на фото чи відео під час фіксації?", callback_data="Чи потрібно отримати згоду від осіб, які потрапили на фото чи відео під час фіксації?")
    quest8 = types.KeyboardButton("Як правильно проводити фото та відеофіксацію завданих збитків?", callback_data="Як правильно проводити фото та відеофіксацію завданих збитків?")
    quest9 = types.KeyboardButton("Навіщо потрібно ввімкнути геолокацію на пристрої під час фіксації?", callback_data="Навіщо потрібно ввімкнути геолокацію на пристрої під час фіксації?")
    quest10 = types.KeyboardButton("Чому потрібно зберігати зібрані матеріали після проведення фіксації?", callback_data="Чому потрібно зберігати зібрані матеріали після проведення фіксації?")
    quest11 = types.KeyboardButton("Де потрібно зберігати зібрані матеріали з фіксації?", callback_data="Де потрібно зберігати зібрані матеріали з фіксації?")
    quest12 = types.KeyboardButton("Чи обов’язково під час відеофіксації описувати в голос усі пошкодження?", callback_data="Чи обов’язково під час відеофіксації описувати в голос усі пошкодження?")
    quest13 = types.KeyboardButton("Що робити з усіма зібраними матеріалами?", callback_data="Що робити з усіма зібраними матеріалами?")
    quest14 = types.KeyboardButton("Чи є зразок акту, який необхідно скласти самостійно?", callback_data="Чи є зразок акту, який необхідно скласти самостійно?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, quest10, quest11, quest12, quest13, quest14, back)
    await bot.send_message(text="Самостійна фіксація", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Якими технічними засобами можливо здійснювати самостійну фіксацію?")
async def quest6_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Телефон, фото- чи відеокамера", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи є рекомендації щодо порядку фіксації ?")
async def quest6_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так. Рекомендації можна знайти за посиланням (Алгоритм дій з фіксації)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи достатньо відео фіксації чи фото фіксації?")
async def quest6_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Ні. Потрібно також зібрати необхідні документи. Детальніше за посиланням (Алгоритм дій з фіксації)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як дії рекомендується здійснити самостійно при руйнуванні або пошкодженні майна?")
async def quest6_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Рекомендації можна знайти за посиланням (Алгоритм дій з фіксації)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як правильно здійснити фотофіксацію завданих збитків?")
async def quest6_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Порядок дій за посиланням (Алгоритм дій з фіксації)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як правильно здійснити відеофіксацію завданих збитків?")
async def quest6_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Порядок дій за посиланням (Алгоритм дій з фіксації)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи потрібно отримати згоду від осіб, які потрапили на фото чи відео під час фіксації?")
async def quest6_7(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як правильно проводити фото та відеофіксацію завданих збитків?")
async def quest6_8(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Порядок дій за посиланням (Алгоритм дій з фіксації)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Навіщо потрібно ввімкнути геолокацію на пристрої під час фіксації?")
async def quest6_9(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Геолокація дозволить в майбутньому об'єктивно перевірити та підтвердити місце зйомки", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чому потрібно зберігати зібрані матеріали після проведення фіксації?")
async def quest6_10(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Це допоможе в майбутньому підтвердити факт руйнування/пошкодження саме внаслідок бойових дій та отримати компенсацію", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Де потрібно зберігати зібрані матеріали з фіксації?")
async def quest6_11(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Для зменшення ризику втрати зібраних матеріалів, рекомендовано зберігати їх на декількох пристроях та у хмарних сховищах", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи обов’язково під час відеофіксації описувати в голос усі пошкодження?")
async def quest6_12(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так, потрібно описати та відобразити у відеофайлі  характер пошкодження або знищення : яке пошкодження, в якому приміщенні або частині будинку", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Що робити з усіма зібраними матеріалами?")
async def quest6_13(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Збережіть зібрані матеріали на декількох пристроях та у хмарних сховищах", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи є зразок акту, який необхідно скласти самостійно?")
async def quest6_14(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Самостійна фіксація")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Акт складається в довільній формі. Зразок форми можна знайти тут (посиланням на Алгоритм дій з фіксації)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Збір пояснень свідків")
async def block7(message: types.Message):
    quest1 = types.KeyboardButton("Хто має право отримати пояснення у свідків?", callback_data="Хто має право отримати пояснення у свідків?")
    quest2 = types.KeyboardButton("Яку інформацію потрібно та можна викласти в поясненнях свідка?", callback_data="Яку інформацію потрібно та можна викласти в поясненнях свідка?")
    quest3 = types.KeyboardButton("Яка основна інформація повинна міститись в поясненнях свідків?", callback_data="Яка основна інформація повинна міститись в поясненнях свідків?")
    quest4 = types.KeyboardButton("Чи можуть свідки використовувати фото та відеозаписи як додаткове підтвердження події?", callback_data="Чи можуть свідки використовувати фото та відеозаписи як додаткове підтвердження події?")
    quest5 = types.KeyboardButton("Як слід зберігати фото та відеозаписи свідків?", callback_data="Як слід зберігати фото та відеозаписи свідків?")
    quest6 = types.KeyboardButton("Чи будуть пояснення свідків додатковими доказами?", callback_data="Чи будуть пояснення свідків додатковими доказами?")
    quest7 = types.KeyboardButton("Як представити паспортні дані та контактну інформацію свідків у поясненнях?", callback_data="Як представити паспортні дані та контактну інформацію свідків у поясненнях?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, back)
    await bot.send_message(text="Збір пояснень свідків", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Хто має право отримати пояснення у свідків?")
async def quest7_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір пояснень свідків")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Власники майна, посадові особи сільської /селищної/міської ради, працівники правоохоронних органів", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Яку інформацію потрібно та можна викласти в поясненнях свідка?")
@dp.message_handler(text="Яка основна інформація повинна міститись в поясненнях свідків?")
async def quest7_3_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір пояснень свідків")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Опис обставини пошкодження житла, характеру пошкоджень, майна, яке знаходилось в будинку, дата, час та місце його складення, паспортні дані, місце проживання та контактну інформацію осіб, що підписують такий документ", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи можуть свідки використовувати фото та відеозаписи як додаткове підтвердження події?")
async def quest7_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір пояснень свідків")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так, свідки подій  також можуть мати фото- та відеозаписи", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як слід зберігати фото та відеозаписи свідків?")
async def quest7_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір пояснень свідків")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Збережіть зібрані матеріали на декількох пристроях та у хмарних сховищах", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи будуть пояснення свідків додатковими доказами?")
async def quest7_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір пояснень свідків")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message("Так", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як представити паспортні дані та контактну інформацію свідків у поясненнях?")
async def quest7_7(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір пояснень свідків")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Власноручно написану заяву, в якій будуть відображені повні відомості про свідка (П.І.Б., адреса проживання, всі наявні засоби зв’язку) з детальним викладенням обставин події, безпосереднім свідком яких стала особа. Письмове пояснення свідку необхідно підписати власноруч", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Збір матеріалів зі ЗМІ")
async def block8(message: types.Message):
    quest1 = types.KeyboardButton("Чи може інформація з ЗМІ бути підтвердженням завданих збитків?", callback_data="Чи може інформація з ЗМІ бути підтвердженням завданих збитків?")
    quest2 = types.KeyboardButton("Що робити, якщо в ЗМІ побачив інформацію про руйнування?", callback_data="Що робити, якщо в ЗМІ побачив інформацію про руйнування?")
    quest3 = types.KeyboardButton("Чому важливо зберігати публікації ЗМІ?", callback_data="Чому важливо зберігати публікації ЗМІ?")
    quest4 = types.KeyboardButton("Які матеріали від ЗМІ слід зберегти?", callback_data="Які матеріали від ЗМІ слід зберегти?")
    quest5 = types.KeyboardButton("Як можна зберегти опубліковані матеріали?", callback_data="Як можна зберегти опубліковані матеріали?")
    quest6 = types.KeyboardButton("Чи є обмеження щодо кількості публікацій, які слід зберегти?", callback_data="Чи є обмеження щодо кількості публікацій, які слід зберегти?")
    quest7 = types.KeyboardButton("Чи є необхідність зберігати оригінальні версії руйнувань?", callback_data="Чи є необхідність зберігати оригінальні версії руйнувань?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, back)
    await bot.send_message(text="Збір матеріалів зі ЗМІ", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи може інформація з ЗМІ бути підтвердженням завданих збитків?")
async def quest8_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір матеріалів зі ЗМІ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Що робити, якщо в ЗМІ побачив інформацію про руйнування?")
async def quest8_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір матеріалів зі ЗМІ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Необхідно намагатися зберегти посилання на такі інформаційні ресурси (скріншоти веб-сторінок, збереження відеозаписів, фото, зафіксувати попередньо дату та час доступу до інформаційного ресурсу, адресу ресурсу)", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чому важливо зберігати публікації ЗМІ?")
async def quest8_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір матеріалів зі ЗМІ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Такі матеріали стануть додатковим аргументом на підтвердження факту руйнування/пошкодження майна", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які матеріали від ЗМІ слід зберегти?")
async def quest8_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір матеріалів зі ЗМІ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Статті. Публікації. Скріншоти веб-сторінок", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як можна зберегти опубліковані матеріали?")
async def quest8_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір матеріалів зі ЗМІ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Скріншоти вебсторінок, збереження відеозаписів, фото, зафіксувати попередньо дату та час доступу до інформаційного ресурсу, адресу ресурсу", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи є обмеження щодо кількості публікацій, які слід зберегти?")
async def quest8_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір матеріалів зі ЗМІ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Ні, чим більше доказової бази буде зібрано одразу, тим легше та швидше буде потім пройти процедуру отримання компенсації", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи є необхідність зберігати оригінальні версії руйнувань?")
async def quest8_7(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір матеріалів зі ЗМІ")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Збір  чеків на пошкоджене/зруйноване майно")
async def block9(message: types.Message):
    quest1 = types.KeyboardButton("Якщо немає чеків /документів  на пошкоджено майно, що можна використовувати як доказ приналежності майна потерпілому та його вартість?", callback_data="Якщо немає чеків /документів  на пошкоджено майно, що можна використовувати як доказ приналежності майна потерпілому та його вартість?")
    quest2 = types.KeyboardButton("Які документи слід зберегти, щоб підтвердити вартість пошкодженого або знищеного майна?", callback_data="Які документи слід зберегти, щоб підтвердити вартість пошкодженого або знищеного майна?")
    quest3 = types.KeyboardButton("Які можуть бути переваги зберігання чеків купівлі майна?", callback_data="Які можуть бути переваги зберігання чеків купівлі майна?")
    quest4 = types.KeyboardButton("Чи можна використовувати як доказ фотографії майна до його руйнування, якщо немає чеків про їх купівлю?", callback_data="Чи можна використовувати як доказ фотографії майна до його руйнування, якщо немає чеків про їх купівлю?")
    quest5 = types.KeyboardButton("Чи можна використовувати електронні копії чеків?", callback_data="Чи можна використовувати електронні копії чеків?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, back)
    await bot.send_message(text="9	БЛОК – ЗБІР  ЧЕКІВ НА ПОШКОДЖЕНЕ/ЗРУЙНОВАНЕ МАЙНО", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Якщо немає чеків /документів  на пошкоджено майно, що можна використовувати як доказ приналежності майна потерпілому та його вартість?")
async def quest9_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір  чеків на пошкоджене/зруйноване майно")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Якщо відсутні чеки або інші документи, які підтверджують приналежність майна потерпілому та його вартість, можна спробувати скористатися такими доказами:\n"
                                "1. Фотографії: Збереження фотографій майна до пошкодження може служити доказом його наявності та стану. Якщо у вас є фотографії майна, на яких відображено його цілісність та стан, вони можуть бути використані для документування пошкоджень.\n"
                                "2. Витяги з банківських виписок: Якщо покупка майна була здійснена за допомогою банківського переказу або оплати з банківської картки, можна намагатися знайти відповідні витяги з банківських виписок, які підтверджують здійснення операції та вартість майна.\n"
                                "3. Свідчення свідків: Якщо є свідки, які можуть підтвердити приналежність майна потерпілому або його вартість, їхні свідчення можуть бути використані як доказ.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи слід зберегти, щоб підтвердити вартість пошкодженого або знищеного майна?")
async def quest9_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір  чеків на пошкоджене/зруйноване майно")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="1. Супутніми доводами можуть виступати квитанції на рухоме майно (техніку, речі та інше, що знаходилось в будинку), фото майна до та після руйнування.\n"
                                "2. Також необхідно зібрати за наявності будь-які чеки (квитанції, фактури) на пошкоджене чи знищене майно, яке знаходилося в нерухомості, зробити з них копії.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які можуть бути переваги зберігання чеків купівлі майна?")
async def quest9_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір  чеків на пошкоджене/зруйноване майно")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Ви зможете підтвердити вартість пошкодженого чи втраченого майна для отримання компенсації", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи можна використовувати як доказ фотографії майна до його руйнування, якщо немає чеків про їх купівлю?")
async def quest9_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір  чеків на пошкоджене/зруйноване майно")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так, фотографії майна до його руйнування можуть бути використані як доказ, навіть якщо відсутні чеки про їх купівлю. Фотографії можуть документувати наявність та стан майна до події, а також служити для порівняння з фактичним станом після пошкодження чи знищення.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи можна використовувати електронні копії чеків?")
async def quest9_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір  чеків на пошкоджене/зруйноване майно")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="1. В деяких випадках електронні копії чеків можуть бути прийняті як доказ при заяві про пошкодження або знищення майна, особливо якщо вони мають дату, підпис або печатку магазину.\n"
                                "2. Проте, в інших випадках можуть бути встановлені певні вимоги щодо збереження оригінальних чеків або їх паперових копій.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Збір інформації про підключення комунальних послуг")
async def block10(message: types.Message):
    quest1 = types.KeyboardButton("Які документи необхідно надати про підключення комунальних послуг?", callback_data="Які документи необхідно надати про підключення комунальних послуг?")
    quest2 = types.KeyboardButton("Які документи слід додати до акту?", callback_data="Які документи слід додати до акту?")
    quest3 = types.KeyboardButton("Де отримати документи про підключення комунальних послуг, якщо не збереглися?", callback_data="Де отримати документи про підключення комунальних послуг, якщо не збереглися?")
    quest4 = types.KeyboardButton("Як отримати необхідні документи у разі їх втрати?", callback_data="Як отримати необхідні документи у разі їх втрати?")
    quest5 = types.KeyboardButton("Які комунальні послуги потрібно зазначати в акті?", callback_data="Які комунальні послуги потрібно зазначати в акті?")
    quest6 = types.KeyboardButton("Які документи можуть підтверджувати індивідуальне опалення?", callback_data="Які документи можуть підтверджувати індивідуальне опалення?")
    quest7 = types.KeyboardButton("Якщо відсутні необхідні документи про підключення комунальних послуг?", callback_data="Якщо відсутні необхідні документи про підключення комунальних послуг?")
    quest8 = types.KeyboardButton("Чи є обов’язковими акти опломбування всіх лічильників?", callback_data="Чи є обов’язковими акти опломбування всіх лічильників?")
    quest9 = types.KeyboardButton("Як можуть допомогти документи про підключення комунальних послуг у складанні акту?", callback_data="Як можуть допомогти документи про підключення комунальних послуг у складанні акту?")
    quest10 = types.KeyboardButton("Якщо відсутні документи про підключення комунальних послуг, це вплине на процес отримання акту про пошкоджене майно?", callback_data="Якщо відсутні документи про підключення комунальних послуг, це вплине на процес отримання акту про пошкоджене майно?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, quest10, back)
    await bot.send_message(text="Збір інформації про підключення комунальних послуг", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи необхідно надати про підключення комунальних послуг?")
async def quest10_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="1. Документ, що підтверджує право власності або користування житловою одиницею (наприклад, договір купівлі-продажу, орендний договір).\n"
                                "2. Заява на підключення комунальних послуг до відповідних підрозділів (наприклад, газової компанії, енергопостачальної компанії, водопостачальної компанії тощо).\n"
                                "3. Документи, які засвідчують технічну можливість підключення (наприклад, акт технічної можливості на встановлення лічильника).\n"
                                "4. Інші документи, які можуть бути вимогами конкретної комунальної компанії або організації.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи слід додати до акту?")
async def quest10_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="За наявності вузлів розподільного обліку води (квартирних лічильників) – паспорти на лічильники та/або свідоцтво про повірку. Для власників вузлів розподільного обліку теплової енергії (квартирних лічильників опалення) – акт технічної можливості на встановлення лічильника, паспорт на встановлений лічильник та акт введення лічильника в експлуатацію; проєктно-технічну документацію на індивідуальне опалення (якщо воно є); акти опломбування всіх лічильників.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Де отримати документи про підключення комунальних послуг, якщо не збереглися?")
@dp.message_handler(text="Як отримати необхідні документи у разі їх втрати?")
async def quest10_3_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Якщо документи про підключення комунальних послуг були втрачені, їх можна отримати наступними способами:\n"
                                "1. Звернутися до відповідних комунальних компаній або організацій і запитати копії документів.\n"
                                "2. Зателефонувати до служби підтримки або відділу обслуговування і запросити відновлення документів.\n"
                                "3. Звернутися до органів місцевого самоврядування або відповідних відділів з питань комунальних послуг і отримати необхідну інформацію та документи.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які комунальні послуги потрібно зазначати в акті?")
async def quest10_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Газопостачання, електропостачання, водопостачання, водовідведення, теплопостачання", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи можуть підтверджувати індивідуальне опалення?")
async def quest10_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Проєктно-технічну документацію на індивідуальне опалення. Паспорти на лічильники та/або свідоцтво про повірку для власників лічильників опалення – акт технічної можливості на встановлення вузла розподільного обліку теплової енергії, паспорт на встановлений лічильник опалення та акт введення лічильника в експлуатацію, проектно-технічну документацію на індивідуальне опалення (якщо воно є), акти опломбування всіх лічильників", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Якщо відсутні необхідні документи про підключення комунальних послуг?")
async def quest10_7(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Якщо відсутні необхідні документи про підключення комунальних послуг, можна звернутися до відповідних комунальних компаній або організацій і запитати про можливість надання копій або дублікатів документів. Також можна звернутися до органів місцевого самоврядування або відділів з питань комунальних послуг і отримати необхідну допомогу у відновленні документів.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи є обов’язковими акти опломбування всіх лічильників?")
async def quest10_8(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як можуть допомогти документи про підключення комунальних послуг у складанні акту?")
async def quest10_9(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Документи про підключення комунальних послуг можуть допомогти у складанні акту про пошкоджене майно, оскільки вони підтверджують факт підключення, наявність лічильників і технічну можливість встановлення. Вони слугують основою для визначення обсягу та стану комунальних послуг до пошкодження і після нього.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Якщо відсутні документи про підключення комунальних послуг, це вплине на процес отримання акту про пошкоджене майно?")
async def quest10_10(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збір інформації про підключення комунальних послуг")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Відсутність документів про підключення комунальних послуг може вплинути на процес отримання акту про пошкоджене майно, оскільки недостатньо доказів та інформації про стан підключених послуг. Проте, в такому випадку можна звернутися до відповідних комунальних компаній, органів місцевого самоврядування або відділів з питань комунальних послуг, щоб провести додаткову перевірку та отримати необхідну інформацію та документи, які можуть замінити відсутні документи про підключення комунальних послуг.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Збереження зібраних матеріалів")
async def block11(message: types.Message):
    quest1 = types.KeyboardButton("Чи потрібно зберігати зібрані документи в електронному форматі?", callback_data="Чи потрібно зберігати зібрані документи в електронному форматі?")
    quest2 = types.KeyboardButton("Які документи потрібно сканувати та зберігати?", callback_data="Які документи потрібно сканувати та зберігати?")
    quest3 = types.KeyboardButton("На яких пристроях зберігати скани документів?", callback_data="На яких пристроях зберігати скани документів?")
    quest4 = types.KeyboardButton("Які хмарні сховища використовувати для зберігання сканів документів?", callback_data="Які хмарні сховища використовувати для зберігання сканів документів?")
    quest5 = types.KeyboardButton("Чи обов’язково відправляти скани документів комусь ще?", callback_data="Чи обов’язково відправляти скани документів комусь ще?")
    quest6 = types.KeyboardButton("Як забезпечити доступ до сканів документів в разі потреби?", callback_data="Як забезпечити доступ до сканів документів в разі потреби?")
    quest7 = types.KeyboardButton("Як забезпечити безпеку сканованих документів?", callback_data="Як забезпечити безпеку сканованих документів?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, back)
    await bot.send_message(text="Збереження зібраних матеріалів", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи потрібно зберігати зібрані документи в електронному форматі?")
async def quest11_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збереження зібраних матеріалів")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Так, рекомендується зберігати зібрані документи в електронному форматі для забезпечення зручності доступу та запобігання втрати фізичних копій.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи потрібно сканувати та зберігати?")
async def quest11_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збереження зібраних матеріалів")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Потрібно сканувати та зберігати всі зібрані матеріали, включаючи документи, фотографії, акти, листи тощо", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="На яких пристроях зберігати скани документів?")
async def quest11_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збереження зібраних матеріалів")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Скани документів можна зберігати на різних пристроях, таких як комп'ютери, ноутбуки, смартфони, планшети, зовнішні накопичувачі або спеціальні пристрої для зберігання документів.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які хмарні сховища використовувати для зберігання сканів документів?")
async def quest11_4(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збереження зібраних матеріалів")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Для зберігання сканів документів в електронному вигляді можна використовувати різні хмарні сховища, такі як Google Drive, Dropbox, Microsoft OneDrive, iCloud тощо. Вибір конкретного хмарного сховища залежатиме від ваших вподобань та вимог щодо безпеки та доступності.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чи обов’язково відправляти скани документів комусь ще?")
async def quest11_5(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збереження зібраних матеріалів")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Надсилання сканів документів комусь ще є необов'язковим, але може бути корисним для забезпечення додаткової копії та запобігання можливій втраті. Розгляньте можливість надіслати скани родичам або довіреним особам, які можуть бути вам підтримкою.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як забезпечити доступ до сканів документів в разі потреби?")
async def quest11_6(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збереження зібраних матеріалів")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Для забезпечення доступу до сканів документів в разі потреби, ви можете використовувати паролі, шифрування або інші методи захисту своїх електронних пристроїв та хмарних сховищ. Забезпечте безпеку своїх пристроїв та не розголошуйте конфіденційну інформацію", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Як забезпечити безпеку сканованих документів?")
async def quest11_7(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Збереження зібраних матеріалів")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Рекомендується регулярно перевіряти та оновлювати збережені скани, особливо в разі змін у ваших документах або додавання нових важливих документів, а також робити резервні копії важливих даних.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Звернення до НПУ із заявою")
async def block12(message: types.Message):
    quest1 = types.KeyboardButton("Чому і для чого необхідно звернутися до НП?", callback_data="Чому і для чого необхідно звернутися до НП?")
    quest2 = types.KeyboardButton("Які документи необхідно надати до НП?", callback_data="Які документи необхідно надати до НП?")
    quest3 = types.KeyboardButton("Для чого потрібен витяг з ЄРДР?", callback_data="Для чого потрібен витяг з ЄРДР?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, quest2, quest3, back)
    await bot.send_message(text="Звернення до НПУ із заявою", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Чому і для чого необхідно звернутися до НП?")
async def quest12_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Звернення до НПУ із заявою")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Звернення до Національної поліції необхідне для відкриття кримінального провадження за ст. 438 Кримінального кодексу України («Порушення законів та звичаїв війни»), об’єктивна сторона даного злочину може виражатись у таких діях, як мародерство, пошкодження, знищення цивільних об’єктів.\n"
                                "Заявнику має бути наданий витяг з Єдиного реєстру досудових розслідувань (ЄРДР), який доцільно зберігти. У ході процесу заявник набуде статусу потерпілого та може бути вирішене питання щодо стягнення спричиненої шкоди з відповідальної особи (питання щодо винної особи буде вирішуватись у ході процесу шляхом проведення слідчих дій та оцінки доказів).", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Які документи необхідно надати до НП?")
async def quest12_2(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Звернення до НПУ із заявою")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Заява, в якій слід детально описати ситуацію, порушення законів та звичаїв війни і надати всі відомості про події.\n"
                                "Документи, що підтверджують факти порушення, такі як фотографії, відеозаписи, свідчення свідків тощо.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Для чого потрібен витяг з ЄРДР?")
async def quest12_3(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Звернення до НПУ із заявою")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Витяг з Єдиного реєстру досудових розслідувань (ЄРДР) є важливим документом, який надається заявнику. Він містить інформацію про відкрите кримінальне провадження і є підтвердженням того, що ваша заява прийнята та зареєстрована. Витяг з ЄРДР може бути використаний для подальшого взаємодії з поліцією, статусу потерпілого та вирішення питань щодо стягнення спричиненої шкоди.", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="Подання онлайн заявок")
async def block13(message: types.Message):
    quest1 = types.KeyboardButton("В які онлайн-ресурси можна подати заявку про пошкоджене/зруйноване майно?", callback_data="В які онлайн-ресурси можна подати заявку про пошкоджене/зруйноване майно?")
    back = types.KeyboardButton("Назад🔙", callback_data="back")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(quest1, back)
    await bot.send_message(text="Подання онлайн заявок", chat_id=message.from_user.id, reply_markup=mar)


@dp.message_handler(text="В які онлайн-ресурси можна подати заявку про пошкоджене/зруйноване майно?")
async def quest13_1(message: types.Message):
    back = types.KeyboardButton("Назад🔙", callback_data="Подання онлайн заявок")
    mar = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(back)
    await bot.send_message(text="Для здійснення повідомлень використовується Єдиний портал державних послуг «Дія». Подати інформаційне повідомлення про зруйноване внаслідок військової агресії рф житло можна онлайн (через мобільний застосунок «Дія» чи через портал державних послуг «Дія» – diia.gov.ua) або офлайн: звернувшись до ЦНАПу чи нотаріуса особисто або через уповноваженого представника.\n"
                                "В рамках програми «єВідновлення» можна отримати компенсації на відновлення пошкодженого майна через війну.", chat_id=message.from_user.id, reply_markup=mar)


if __name__ == "__main__":
    executor.start_polling(dp)
