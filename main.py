from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token="6339639367:AAFfRK1z6yhvaLTq55C8I42lpNUAgTEeGbM")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    block1 = types.KeyboardButton("1 БЛОК – ПІДТВЕРДЖЕННЯ ПРАВА ВЛАНОСТІ НА МАЙНО", callback_data="block1")
    block2 = types.KeyboardButton("2 БЛОК – ФІКСАЦІЯ ДСНС", callback_data="block2")
    block3 = types.KeyboardButton("3 БЛОК – ФІКСАЦІЯ СІЛЬСЬКОЮ/СЕЛИЩНОЮ МІСЬКОЮ РАДОЮ, У РАЗІ ЇХ ВІДСУТНОСТІ ВІЙСЬКОВОЮ АДМІНІСТРАЦІЄЮ АБО ВІЙСЬКОВО-ЦИВІЛЬНОЮ АДМІНІСТРАЦІЄЮ", callback_data="block3")
    block4 = types.KeyboardButton("4 БЛОК – ФІКСАЦІЯ НПУ", callback_data="block4")
    block5 = types.KeyboardButton("5 БЛОК – ФІКСАЦІЯ ДЕРЖАВНОЮ ЕКОЛОГІЧНОЮ ІНСПЕКЦІЄЮ", callback_data="block5")
    block6 = types.KeyboardButton("6 БЛОК – САМОСТІЙНА ФІКСАЦІЯ", callback_data="block6")
    block7 = types.KeyboardButton("7 БЛОК – ЗБІР ПОЯСНЕНЬ СВІДКІВ", callback_data="block7")
    block8 = types.KeyboardButton("8 БЛОК – ЗБІР МАТЕРІАЛІВ ЗІ ЗМІ", callback_data="block8")
    block9 = types.KeyboardButton("9 БЛОК – ЗБІР  ЧЕКІВ НА ПОШКОДЖЕНЕ/ЗРУЙНОВАНЕ МАЙНО", callback_data="block9")
    block10 = types.KeyboardButton("10 БЛОК – ЗБІР ІНФОРМАЦІЇ ПРО ПІДКЛЮЧЕННЯ КОМУНАЛЬНИХ ПОСЛУГ", callback_data="block10")
    block11 = types.KeyboardButton("11 БЛОК – ЗБЕРЕЖЕННЯ ЗІБРАНИХ МАТЕРІАЛІВ", callback_data="block11")
    block12 = types.KeyboardButton("12 БЛОК – ЗВЕРНЕННЯ ДО НПУ ІЗ ЗАЯВОЮ", callback_data="block12")
    block13 = types.KeyboardButton("13 БЛОК – ПОДАННЯ ОНЛАЙН ЗАЯВОК", callback_data="block13")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13)
    await bot.send_message(message.from_user.id, "Виберіть блок який вас цікавить:", reply_markup=mar)


@dp.callback_query_handler(text="block1")
async def block1(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Які основні правовстановлюючі документи підтверджують власність на майно?", callback_data="quest1_1")
    quest2 = types.KeyboardButton("Які документи потрібно зберегти для підтвердження права власності на майно?", callback_data="quest1_2")
    quest3 = types.KeyboardButton("Чи можна зберігати копії документів про право власності в електронному вигляді?", callback_data="quest1_3")
    quest4 = types.KeyboardButton("Як поновити втрачені документи на майно?", callback_data="quest1_4")
    quest5 = types.KeyboardButton("Як зменшити ризик втрати документів?", callback_data="quest1_5")
    quest6 = types.KeyboardButton("Як отримати інформацію про майно з Державного реєстру речових прав на нерухоме майно?", callback_data="quest1_6")
    quest7 = types.KeyboardButton("Що робити у випадку втрати або пошкодження документа про право власності на майно?", callback_data="quest1_7")
    quest8 = types.KeyboardButton("Як діяти, якщо виникають проблеми з визнанням права власності на майно?", callback_data="quest1_8")
    quest9 = types.KeyboardButton("Якщо є копії документів про право власності чи потрібно відновлювати оригінали?", callback_data="quest1_9")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9)
    await bot.edit_message_text("1 БЛОК – ПІДТВЕРДЖЕННЯ ПРАВА ВЛАНОСТІ НА МАЙНО", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_1")
async def quest1_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("-  Договір, за яким відповідно до законодавства передбачається перехід права власності, зокрема купівлі-продажу, міни, дарування, довічного утримання, лізингу, предметом якого є нерухоме майно, про припинення права на аліменти для дитини у зв'язку з передачею права власності на нерухоме майно, договір іпотеки, що містить застереження про задоволення вимог іпотекодержателя, договір про задоволення вимог іпотекодержателя, спадковий договір (за наявності свідоцтва органу реєстрації актів цивільного стану про смерть чи рішення суду про оголошення особи померлою), договір про виділ у натурі частки з нерухомого майна, що є у спільній власності, про поділ нерухомого майна, що є у спільній власності.\n"
                                "-  Свідоцтво про право власності на частку в спільному майні подружжя в разі смерті одного з подружжя, що видається нотаріусом.\n"
                                "-  Свідоцтво про право на спадщину, видане нотаріусом.\n"
                                "-  Свідоцтво про право власності на нерухоме майно, видане органом місцевого самоврядування.\n"
                                "-  Свідоцтво про право власності, видане органом приватизації наймачам житлових приміщень державного та комунального житлового фонду.\n"
                                "-  Рішення суду про визнання права власності на об'єкти нерухомого майна, про встановлення факту права власності на об'єкти нерухомого майна, про передачу безхазяйного нерухомого майна до комунальної власності.\n"
                                "-  Ухвала суду про затвердження (визнання) мирової угоди.\n"
                                "-  Дублікат правовстановлювального документа, виданий нотаріусом, органом місцевого самоврядування, органом приватизації, копія архівного правовстановлювального документа, видана державним архівом.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_2")
async def quest1_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("-  Договір, за яким відповідно до законодавства передбачається перехід права власності, зокрема купівлі-продажу, міни, дарування, довічного утримання, лізингу, предметом якого є нерухоме майно, про припинення права на аліменти для дитини у зв'язку з передачею права власності на нерухоме майно, договір іпотеки, що містить застереження про задоволення вимог іпотекодержателя, договір про задоволення вимог іпотекодержателя, спадковий договір (за наявності свідоцтва органу реєстрації актів цивільного стану про смерть чи рішення суду про оголошення особи померлою), договір про виділ у натурі частки з нерухомого майна, що є у спільній власності, про поділ нерухомого майна, що є у спільній власності.\n"
                                "-  Свідоцтво про право власності на частку в спільному майні подружжя в разі смерті одного з подружжя, що видається нотаріусом.\n"
                                "-  Свідоцтво про право на спадщину, видане нотаріусом.\n"
                                "-  Свідоцтво про право власності на нерухоме майно, видане органом місцевого самоврядування.\n"
                                "-  Свідоцтво про право власності, видане органом приватизації наймачам житлових приміщень державного та комунального житлового фонду.\n"
                                "-  Рішення суду про визнання права власності на об'єкти нерухомого майна, про встановлення факту права власності на об'єкти нерухомого майна, про передачу безхазяйного нерухомого майна до комунальної власності.\n"
                                "-  Ухвала суду про затвердження (визнання) мирової угоди.\n"
                                "-  Дублікат правовстановлювального документа, виданий нотаріусом, органом місцевого самоврядування, органом приватизації, копія архівного правовстановлювального документа, видана державним архівом.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_3")
async def quest1_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так, зробіть декілька примірників копій, які доцільно зберігати в різних місцях) та сканкопії (на різних пристроях та у хмарних сховищах). Це мінімізує ризик їх втрати", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_4")
async def quest1_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("За можливістю зробіть витяг щодо перебування майна у власності з Державного реєстру речових прав на нерухоме майно (подати запит на отримання інформації через персональний кабінет веб-сайту «Кабінет електронних сервісів» Міністерства юстиції України https://psjust.gov.ua/elektronni-posluhy/elektronni-servisy-on-layn/ або отримати довідку через додаток Дія https://diia.gov.ua/services/informaciya-z-derzhavnogo-reyestru-rechovih-prav-na-neruhome-majno).", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_5")
async def quest1_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("При можливості, зробіть декілька примірників копій, які доцільно зберігати в різних місцях) та сканкопії (на різних пристроях та у хмарних сховищах). Це мінімізує ризик їх втрати.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_6")
async def quest1_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Подати запит на отримання інформації через персональний кабінет веб-сайту «Кабінет електронних сервісів» Міністерства юстиції України https://psjust.gov.ua/elektronni-posluhy/elektronni-servisy-on-layn/ або отримати довідку через додаток Дія https://diia.gov.ua/services/informaciya-z-derzhavnogo-reyestru-rechovih-prav-na-neruhome-majno).", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_7")
async def quest1_7(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Слід звернутися із письмовою заявою до органу місцевого самоврядування чи нотаріуса для отримання дублікату.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_8")
async def quest1_8(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Ви маєте право звернутися до суду для визнання права власності на майно, яке не визнається чи оспорюється.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest1_9")
async def quest1_9(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block2")
async def block2(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Чи є обмеження в часі для фіксації пошкоджень/руйнування майна?", callback_data="quest2_1")
    quest2 = types.KeyboardButton("Як швидко потрібно фіксувати факти руйнування/пошкодження майна?", callback_data="quest2_2")
    quest3 = types.KeyboardButton("Що робити у випадку пожежі або аварійної ситуації?", callback_data="quest2_3")
    quest4 = types.KeyboardButton("Які відомості повинні бути включені до акту про пожежу або акту пошкодження майна?", callback_data="quest2_4")
    quest5 = types.KeyboardButton("Як отримати копії актів про пожежу або пошкодження майна?", callback_data="quest2_5")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5)
    await bot.edit_message_text("2 БЛОК – ФІКСАЦІЯ ДСНС", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest2_1")
@dp.callback_query_handler(text="quest2_2")
async def quest2_1and2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block2")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Фіксацію фактів руйнування/пошкодження об'єктів нерухомого майна бажано здійснювати у максимально короткий час після вчинення акту агресії рф, що спричинив його руйнацію/пошкодження з урахуванням безпекової ситуації.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest2_3")
async def quest2_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block2")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Здійснити виклик Державної служби з надзвичайних ситуацій (зателефонувати за номером «101») для розмінування, усунення наслідків та складання акту про пожежу та акту пошкодження або руйнування майна із зазначенням причини такого руйнування.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest2_4")
async def quest2_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block2")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("До такого акту вносяться відомості, зокрема, про дату, час, місце, опис знищеного та пошкодженого майна, прямі та побічні збитки, причину тощо.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest2_5")
async def quest2_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block2")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Якщо не отримано акт про пошкодження на місці, тоді вам потрібно звернутися до місцевого підрозділу ДСНС", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block3")
async def block3(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Чи встановлена форма заяви та де її можна знайти?", callback_data="quest3_1")
    quest2 = types.KeyboardButton("Чи є зразкова форма заяви для звернення?", callback_data="quest3_2")
    quest3 = types.KeyboardButton("Які дані потрібно включити до заяви для звернення?", callback_data="quest3_3")
    quest4 = types.KeyboardButton("Як звернутися до посадових осіб сільської /селищної/міської ради або військово-цивільної адміністрації?", callback_data="quest3_4")
    quest5 = types.KeyboardButton("Які документи можуть знадобитись для надання до сільської /селищної/міської ради?", callback_data="quest3_5")
    quest6 = types.KeyboardButton("Чи потрібно надати додаткові документи разом із заявою до посадових осіб сільської /селищної/міської ради?", callback_data="quest3_6")
    quest7 = types.KeyboardButton("Що робити, якщо відсутні сільська /селищна/міська ради?", callback_data="quest3_7")
    quest8 = types.KeyboardButton("Чи можна отримати копії актів про пошкодження майна?", callback_data="quest3_8")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8)
    await bot.edit_message_text("БЛОК 3 – ФІКСАЦІЯ СІЛЬСЬКОЮ/СЕЛИЩНОЮ МІСЬКОЮ РАДОЮ, У РАЗІ ЇХ ВІДСУТНОСТІ ВІЙСЬКОВОЮ АДМІНІСТРАЦІЄЮ АБО ВІЙСЬКОВО-ЦИВІЛЬНОЮ АДМІНІСТРАЦІЄЮ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest3_1")
@dp.callback_query_handler(text="quest3_2")
@dp.callback_query_handler(text="quest3_3")
async def quests3_1_2_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block3")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Зразкову форму можна знайти за посиланням (Алгоритм дій з фіксації, Додаток 3)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest3_4")
async def quest3_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block3")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("особисто – шляхом звернення до загального відділу відповідної ради з заявою \nпоштою – шляхом направлення заяви поштовим відправленням (краще направляти цінним листом з описом вкладення).", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest3_5")
@dp.callback_query_handler(text="quest3_6")
async def quest3_5_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block3")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("- заява на проведення обстеження житла;\n"
                                "-	копії документа, що підтверджує особу;\n"
                                "- копії документа з даними про реєстраційний номер облікової картки платника податків;\n"
                                "- копій документів, що підтверджують наявність права власності на житло на момент подання заяви.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest3_7")
async def quest3_7(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block3")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Варто звернутися до військово-цивільної адміністрації або іншої компетентної установи на території вашого населеного пункту", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest3_8")
async def quest3_8(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block3")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так, якщо не отримано акт про пошкодження на місці, тоді вам треба звернутися до міської або селищної ради, або військово-цивільної адміністрації.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block4")
async def block4(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Чи можна звернутися до поліції для фіксації?", callback_data="quest4_1")
    quest2 = types.KeyboardButton("Чи потрібно викликати поліцію для складення протоколу та фіксації?", callback_data="quest4_2")
    quest3 = types.KeyboardButton("Які документи має надати  поліція після звернення для фіксації?", callback_data="quest4_3")
    quest4 = types.KeyboardButton("Які інші ситуації можуть вимагати виклику поліції, окрім фіксації?", callback_data="quest4_4")
    quest5 = types.KeyboardButton("Як отримати копію складеного протоколу, якщо вона не була видана на місці події?", callback_data="quest4_5")
    quest6 = types.KeyboardButton("Чи потрібно викликати поліцію в будь-якому випадку руйнувань/пошкоджень майна?", callback_data="quest4_6")
    quest7 = types.KeyboardButton("Як зв’язатися з поліцією, якщо немає можливості зателефонувати на номер 102?", callback_data="quest4_7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7)
    await bot.edit_message_text("4 БЛОК – ФІКСАЦІЯ НПУ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest4_1")
async def quest4_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block4")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest4_2")
async def quest4_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block4")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Для того, щоб зафіксувати інформацію про кримінальне правопорушення. На підставі заяви громадянина вноситься інформація в Єдиний реєстр досудових розслідувань (ЄРДР) за фактом знищення або пошкодження майна внаслідок воєнних дій.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest4_3")
async def quest4_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block4")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Копію протоколу та витяг з Єдиного реєстру досудових розслідувань", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest4_4")
async def quest4_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block4")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Подати заяву в поліцію можна не тільки у випадку пошкодження майна внаслідок бойових дій, а також у випадках встановлення факту мародерства, пограбування або коли об’єктом пошкодження є транспортний засіб", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest4_5")
async def quest4_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block4")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Звернутись із заявою до територіального підрозділу у вашому регіоні", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest4_6")
async def quest4_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block4")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так, для фіксації скоєння кримінального правопорушення з подальшим внесенням відомостей до ЄРДР", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest4_7")
async def quest4_7(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block4")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Звернутись із заявою до територіального підрозділу у вашому регіоні", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block5")
async def block5(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Як зафіксувати завдану шкоду довкіллю?", callback_data="quest5_1")
    quest2 = types.KeyboardButton("Де отримати інформацію щодо фіксації та порядку отримання відшкодування завданої шкоди довкіллю?", callback_data="quest5_2")
    quest3 = types.KeyboardButton("Які збитки можуть виникнути на землі та ґрунті внаслідок надзвичайної ситуації та/або збройної агресії?", callback_data="quest5_3")
    quest4 = types.KeyboardButton("Як зателефонувати на гарячу лінію Оперативного штабу при Державній екологічній інспекції України?", callback_data="quest5_4")
    quest5 = types.KeyboardButton("Коли потрібно звернутися до Державної екологічної інспекції України?", callback_data="quest5_5")
    quest6 = types.KeyboardButton("Чи можна надіслати на електронну пошту звернення до Державної екологічної інспекції?", callback_data="quest5_6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6)
    await bot.edit_message_text("5 БЛОК – ФІКСАЦІЯ ДЕРЖАВНОЮ ЕКОЛОГІЧНОЮ ІНСПЕКЦІЄЮ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest5_1")
async def quest5_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block5")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Для зафіксування завданої шкоди довкіллю, земельній ділянці, водним об'єктам ви можете виконати наступні кроки: 1. Зробіть фотографії або відеозаписи, які чітко демонструють пошкодження або знищення. 2. Відзначте місце події на мапі або визначте його географічні координати. 3. Запишіть дату та час виникнення події, а також будь-які інші важливі деталі, що стосуються завданої шкоди.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest5_2")
async def quest5_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block5")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Інформацію щодо фіксації та порядку отримання відшкодування завданої шкоди довкіллю, земельній ділянці, водним об'єктам можна отримати в Державній екологічній інспекції України. Вони надають консультації та інформаційну підтримку стосовно процедури звернення, документації та відшкодування збитків.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest5_3")
async def quest5_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block5")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Збитки, які можуть виникнути на землі та ґрунті внаслідок надзвичайної ситуації та/або збройної агресії, можуть включати:\n"
                                "1. Забруднення ґрунту хімічними речовинами або іншими токсичними речовинами.\n"
                                "2. Пошкодження верхнього шару ґрунту або його ерозія.\n"
                                "3. Втрата родючості ґрунту та його негативний вплив на сільськогосподарські угіддя.\n"
                                "4. Втрата розсіяних посівів, знищення сільськогосподарської техніки або будівель.\n"
                                "5. Інші збитки, пов'язані з псуванням або втратою використовуваної земельної ділянки.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest5_4")
async def quest5_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block5")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Щоб зателефонувати на гарячу лінію Оперативного штабу при Державній екологічній інспекції України, ви можете скористатися наступними кроками:\n"
                                "Введіть номер +38 096 756 83 66 з телефону.\n"
                                "Зачекайте на відповідь оператора гарячої лінії.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest5_5")
async def quest5_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block5")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Пошкодження або забруднення земельної ділянки, водних об’єктів", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest5_6")
async def quest5_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block5")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так. Електронна пошта eco@shtab.gov.ua", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block6")
async def block6(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Якими технічними засобами можливо здійснювати самостійну фіксацію?", callback_data="quest6_1")
    quest2 = types.KeyboardButton("Чи є рекомендації щодо порядку фіксації ?", callback_data="quest6_2")
    quest3 = types.KeyboardButton("Чи достатньо відео фіксації чи фото фіксації?", callback_data="quest6_3")
    quest4 = types.KeyboardButton("Як дії рекомендується здійснити самостійно при руйнуванні або пошкодженні майна?", callback_data="quest6_4")
    quest5 = types.KeyboardButton("Як правильно здійснити фотофіксацію завданих збитків?", callback_data="quest6_5")
    quest6 = types.KeyboardButton("Як правильно здійснити відеофіксацію завданих збитків?", callback_data="quest6_6")
    quest7 = types.KeyboardButton("Чи потрібно отримати згоду від осіб, які потрапили на фото чи відео під час фіксації?", callback_data="quest6_7")
    quest8 = types.KeyboardButton("Як правильно проводити фото та відеофіксацію завданих збитків?", callback_data="quest6_8")
    quest9 = types.KeyboardButton("Навіщо потрібно ввімкнути геолокацію на пристрої під час фіксації?", callback_data="quest6_9")
    quest10 = types.KeyboardButton("Чому потрібно зберігати зібрані матеріали після проведення фіксації?", callback_data="quest6_10")
    quest11 = types.KeyboardButton("Де потрібно зберігати зібрані матеріали з фіксації?", callback_data="quest6_11")
    quest12 = types.KeyboardButton("Чи обов’язково під час відеофіксації описувати в голос усі пошкодження?", callback_data="quest6_12")
    quest13 = types.KeyboardButton("Що робити з усіма зібраними матеріалами?", callback_data="quest6_13")
    quest14 = types.KeyboardButton("Чи є зразок акту, який необхідно скласти самостійно?", callback_data="quest6_14")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, quest10, quest11, quest12, quest13, quest14)
    await bot.edit_message_text("6 БЛОК – САМОСТІЙНА ФІКСАЦІЯ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_1")
async def quest6_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Телефон, фото- чи відеокамера", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_2")
async def quest6_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так. Рекомендації можна знайти за посиланням (Алгоритм дій з фіксації)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_3")
async def quest6_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Ні. Потрібно також зібрати необхідні документи. Детальніше за посиланням (Алгоритм дій з фіксації)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_4")
async def quest6_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Рекомендації можна знайти за посиланням (Алгоритм дій з фіксації)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_5")
async def quest6_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Порядок дій за посиланням (Алгоритм дій з фіксації)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_6")
async def quest6_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Порядок дій за посиланням (Алгоритм дій з фіксації)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_7")
async def quest6_7(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_8")
async def quest6_8(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Порядок дій за посиланням (Алгоритм дій з фіксації)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_9")
async def quest6_9(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Геолокація дозволить в майбутньому об'єктивно перевірити та підтвердити місце зйомки", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_10")
async def quest6_10(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Це допоможе в майбутньому підтвердити факт руйнування/пошкодження саме внаслідок бойових дій та отримати компенсацію", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_11")
async def quest6_11(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Для зменшення ризику втрати зібраних матеріалів, рекомендовано зберігати їх на декількох пристроях та у хмарних сховищах", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_12")
async def quest6_12(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так, потрібно описати та відобразити у відеофайлі  характер пошкодження або знищення : яке пошкодження, в якому приміщенні або частині будинку", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_13")
async def quest6_13(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Збережіть зібрані матеріали на декількох пристроях та у хмарних сховищах", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest6_14")
async def quest6_14(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block6")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Акт складається в довільній формі. Зразок форми можна знайти тут (посиланням на Алгоритм дій з фіксації)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block7")
async def block7(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Хто має право отримати пояснення у свідків?", callback_data="quest7_1")
    quest2 = types.KeyboardButton("Яку інформацію потрібно та можна викласти в поясненнях свідка?", callback_data="quest7_2")
    quest3 = types.KeyboardButton("Яка основна інформація повинна міститись в поясненнях свідків?", callback_data="quest7_3")
    quest4 = types.KeyboardButton("Чи можуть свідки використовувати фото та відеозаписи як додаткове підтвердження події?", callback_data="quest7_4")
    quest5 = types.KeyboardButton("Як слід зберігати фото та відеозаписи свідків?", callback_data="quest7_5")
    quest6 = types.KeyboardButton("Чи будуть пояснення свідків додатковими доказами?", callback_data="quest7_6")
    quest7 = types.KeyboardButton("Як представити паспортні дані та контактну інформацію свідків у поясненнях?", callback_data="quest7_7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7)
    await bot.edit_message_text("7 БЛОК – ЗБІР ПОЯСНЕНЬ СВІДКІВ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest7_1")
async def quest7_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Власники майна, посадові особи сільської /селищної/міської ради, працівники правоохоронних органів", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest7_2")
@dp.callback_query_handler(text="quest7_3")
async def quest7_3_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Опис обставини пошкодження житла, характеру пошкоджень, майна, яке знаходилось в будинку, дата, час та місце його складення, паспортні дані, місце проживання та контактну інформацію осіб, що підписують такий документ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest7_4")
async def quest7_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так, свідки подій  також можуть мати фото- та відеозаписи", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest7_5")
async def quest7_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Збережіть зібрані матеріали на декількох пристроях та у хмарних сховищах", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest7_6")
async def quest7_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest7_7")
async def quest7_7(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Власноручно написану заяву, в якій будуть відображені повні відомості про свідка (П.І.Б., адреса проживання, всі наявні засоби зв’язку) з детальним викладенням обставин події, безпосереднім свідком яких стала особа. Письмове пояснення свідку необхідно підписати власноруч", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block8")
async def block8(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Чи може інформація з ЗМІ бути підтвердженням завданих збитків?", callback_data="quest8_1")
    quest2 = types.KeyboardButton("Що робити, якщо в ЗМІ побачив інформацію про руйнування?", callback_data="quest8_2")
    quest3 = types.KeyboardButton("Чому важливо зберігати публікації ЗМІ?", callback_data="quest8_3")
    quest4 = types.KeyboardButton("Які матеріали від ЗМІ слід зберегти?", callback_data="quest8_4")
    quest5 = types.KeyboardButton("Як можна зберегти опубліковані матеріали?", callback_data="quest8_5")
    quest6 = types.KeyboardButton("Чи є обмеження щодо кількості публікацій, які слід зберегти?", callback_data="quest8_6")
    quest7 = types.KeyboardButton("Чи є необхідність зберігати оригінальні версії руйнувань?", callback_data="quest8_7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7)
    await bot.edit_message_text("8 БЛОК – ЗБІР МАТЕРІАЛІВ ЗІ ЗМІ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest8_1")
async def quest8_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block8")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest8_2")
async def quest8_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block8")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Необхідно намагатися зберегти посилання на такі інформаційні ресурси (скріншоти веб-сторінок, збереження відеозаписів, фото, зафіксувати попередньо дату та час доступу до інформаційного ресурсу, адресу ресурсу)", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest8_3")
async def quest8_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block8")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Такі матеріали стануть додатковим аргументом на підтвердження факту руйнування/пошкодження майна", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest8_4")
async def quest8_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block8")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Статті. Публікації. Скріншоти веб-сторінок", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest8_5")
async def quest8_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block8")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Скріншоти вебсторінок, збереження відеозаписів, фото, зафіксувати попередньо дату та час доступу до інформаційного ресурсу, адресу ресурсу", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest8_6")
async def quest8_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block8")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Ні, чим більше доказової бази буде зібрано одразу, тим легше та швидше буде потім пройти процедуру отримання компенсації", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest8_7")
async def quest8_7(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block8")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block9")
async def block9(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Якщо немає чеків /документів  на пошкоджено майно, що можна використовувати як доказ приналежності майна потерпілому та його вартість?", callback_data="quest7_1")
    quest2 = types.KeyboardButton("Які документи слід зберегти, щоб підтвердити вартість пошкодженого або знищеного майна?", callback_data="quest7_2")
    quest3 = types.KeyboardButton("Які можуть бути переваги зберігання чеків купівлі майна?", callback_data="quest7_3")
    quest4 = types.KeyboardButton("Чи можна використовувати як доказ фотографії майна до його руйнування, якщо немає чеків про їх купівлю?", callback_data="quest7_4")
    quest5 = types.KeyboardButton("Чи можна використовувати електронні копії чеків?", callback_data="quest7_5")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5)
    await bot.edit_message_text("9	БЛОК – ЗБІР  ЧЕКІВ НА ПОШКОДЖЕНЕ/ЗРУЙНОВАНЕ МАЙНО", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest9_1")
async def quest9_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block9")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Якщо відсутні чеки або інші документи, які підтверджують приналежність майна потерпілому та його вартість, можна спробувати скористатися такими доказами:\n"
                                "1. Фотографії: Збереження фотографій майна до пошкодження може служити доказом його наявності та стану. Якщо у вас є фотографії майна, на яких відображено його цілісність та стан, вони можуть бути використані для документування пошкоджень.\n"
                                "2. Витяги з банківських виписок: Якщо покупка майна була здійснена за допомогою банківського переказу або оплати з банківської картки, можна намагатися знайти відповідні витяги з банківських виписок, які підтверджують здійснення операції та вартість майна.\n"
                                "3. Свідчення свідків: Якщо є свідки, які можуть підтвердити приналежність майна потерпілому або його вартість, їхні свідчення можуть бути використані як доказ.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest9_2")
async def quest9_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block9")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("1. Супутніми доводами можуть виступати квитанції на рухоме майно (техніку, речі та інше, що знаходилось в будинку), фото майна до та після руйнування.\n"
                                "2. Також необхідно зібрати за наявності будь-які чеки (квитанції, фактури) на пошкоджене чи знищене майно, яке знаходилося в нерухомості, зробити з них копії.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest9_3")
async def quest9_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block9")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Ви зможете підтвердити вартість пошкодженого чи втраченого майна для отримання компенсації", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest9_4")
async def quest9_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block9")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так, фотографії майна до його руйнування можуть бути використані як доказ, навіть якщо відсутні чеки про їх купівлю. Фотографії можуть документувати наявність та стан майна до події, а також служити для порівняння з фактичним станом після пошкодження чи знищення.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest9_5")
async def quest9_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block9")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("1. В деяких випадках електронні копії чеків можуть бути прийняті як доказ при заяві про пошкодження або знищення майна, особливо якщо вони мають дату, підпис або печатку магазину.\n"
                                "2. Проте, в інших випадках можуть бути встановлені певні вимоги щодо збереження оригінальних чеків або їх паперових копій.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block10")
async def block10(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Які документи необхідно надати про підключення комунальних послуг?", callback_data="quest10_1")
    quest2 = types.KeyboardButton("Які документи слід додати до акту?", callback_data="quest10_2")
    quest3 = types.KeyboardButton("Де отримати документи про підключення комунальних послуг, якщо не збереглися?", callback_data="quest10_3")
    quest4 = types.KeyboardButton("Як отримати необхідні документи у разі їх втрати?", callback_data="quest10_4")
    quest5 = types.KeyboardButton("Які комунальні послуги потрібно зазначати в акті?", callback_data="quest10_5")
    quest6 = types.KeyboardButton("Які документи можуть підтверджувати індивідуальне опалення?", callback_data="quest10_6")
    quest7 = types.KeyboardButton("Якщо відсутні необхідні документи про підключення комунальних послуг?", callback_data="quest10_7")
    quest8 = types.KeyboardButton("Чи є обов’язковими акти опломбування всіх лічильників?", callback_data="quest10_8")
    quest9 = types.KeyboardButton("Як можуть допомогти документи про підключення комунальних послуг у складанні акту?", callback_data="quest10_9")
    quest10 = types.KeyboardButton("Якщо відсутні документи про підключення комунальних послуг, це вплине на процес отримання акту про пошкоджене майно?", callback_data="quest10_10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7, quest8, quest9, quest10)
    await bot.edit_message_text("10 БЛОК – ЗБІР ІНФОРМАЦІЇ ПРО ПІДКЛЮЧЕННЯ КОМУНАЛЬНИХ ПОСЛУГ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_1")
async def quest10_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("1. Документ, що підтверджує право власності або користування житловою одиницею (наприклад, договір купівлі-продажу, орендний договір).\n"
                                "2. Заява на підключення комунальних послуг до відповідних підрозділів (наприклад, газової компанії, енергопостачальної компанії, водопостачальної компанії тощо).\n"
                                "3. Документи, які засвідчують технічну можливість підключення (наприклад, акт технічної можливості на встановлення лічильника).\n"
                                "4. Інші документи, які можуть бути вимогами конкретної комунальної компанії або організації.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_2")
async def quest10_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("За наявності вузлів розподільного обліку води (квартирних лічильників) – паспорти на лічильники та/або свідоцтво про повірку. Для власників вузлів розподільного обліку теплової енергії (квартирних лічильників опалення) – акт технічної можливості на встановлення лічильника, паспорт на встановлений лічильник та акт введення лічильника в експлуатацію; проєктно-технічну документацію на індивідуальне опалення (якщо воно є); акти опломбування всіх лічильників.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_3")
@dp.callback_query_handler(text="quest10_4")
async def quest10_3_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Якщо документи про підключення комунальних послуг були втрачені, їх можна отримати наступними способами:\n"
                                "1. Звернутися до відповідних комунальних компаній або організацій і запитати копії документів.\n"
                                "2. Зателефонувати до служби підтримки або відділу обслуговування і запросити відновлення документів.\n"
                                "3. Звернутися до органів місцевого самоврядування або відповідних відділів з питань комунальних послуг і отримати необхідну інформацію та документи.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_5")
async def quest10_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Газопостачання, електропостачання, водопостачання, водовідведення, теплопостачання", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_6")
async def quest10_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Проєктно-технічну документацію на індивідуальне опалення. Паспорти на лічильники та/або свідоцтво про повірку для власників лічильників опалення – акт технічної можливості на встановлення вузла розподільного обліку теплової енергії, паспорт на встановлений лічильник опалення та акт введення лічильника в експлуатацію, проектно-технічну документацію на індивідуальне опалення (якщо воно є), акти опломбування всіх лічильників", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_7")
async def quest10_7(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Якщо відсутні необхідні документи про підключення комунальних послуг, можна звернутися до відповідних комунальних компаній або організацій і запитати про можливість надання копій або дублікатів документів. Також можна звернутися до органів місцевого самоврядування або відділів з питань комунальних послуг і отримати необхідну допомогу у відновленні документів.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_8")
async def quest10_8(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_9")
async def quest10_9(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Документи про підключення комунальних послуг можуть допомогти у складанні акту про пошкоджене майно, оскільки вони підтверджують факт підключення, наявність лічильників і технічну можливість встановлення. Вони слугують основою для визначення обсягу та стану комунальних послуг до пошкодження і після нього.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest10_10")
async def quest10_10(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block10")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Відсутність документів про підключення комунальних послуг може вплинути на процес отримання акту про пошкоджене майно, оскільки недостатньо доказів та інформації про стан підключених послуг. Проте, в такому випадку можна звернутися до відповідних комунальних компаній, органів місцевого самоврядування або відділів з питань комунальних послуг, щоб провести додаткову перевірку та отримати необхідну інформацію та документи, які можуть замінити відсутні документи про підключення комунальних послуг.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block11")
async def block11(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Чи потрібно зберігати зібрані документи в електронному форматі?", callback_data="quest11_1")
    quest2 = types.KeyboardButton("Які документи потрібно сканувати та зберігати?", callback_data="quest11_2")
    quest3 = types.KeyboardButton("На яких пристроях зберігати скани документів?", callback_data="quest11_3")
    quest4 = types.KeyboardButton("Які хмарні сховища використовувати для зберігання сканів документів?", callback_data="quest11_4")
    quest5 = types.KeyboardButton("Чи обов’язково відправляти скани документів комусь ще?", callback_data="quest11_5")
    quest6 = types.KeyboardButton("Як забезпечити доступ до сканів документів в разі потреби?", callback_data="quest11_6")
    quest7 = types.KeyboardButton("Як забезпечити безпеку сканованих документів?", callback_data="quest11_7")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3, quest4, quest5, quest6, quest7)
    await bot.edit_message_text("11 БЛОК – ЗБЕРЕЖЕННЯ ЗІБРАНИХ МАТЕРІАЛІВ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest11_1")
async def quest11_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block11")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Так, рекомендується зберігати зібрані документи в електронному форматі для забезпечення зручності доступу та запобігання втрати фізичних копій.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest11_2")
async def quest11_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block11")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Потрібно сканувати та зберігати всі зібрані матеріали, включаючи документи, фотографії, акти, листи тощо", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest11_3")
async def quest11_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block11")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Скани документів можна зберігати на різних пристроях, таких як комп'ютери, ноутбуки, смартфони, планшети, зовнішні накопичувачі або спеціальні пристрої для зберігання документів.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest11_4")
async def quest11_4(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block11")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Для зберігання сканів документів в електронному вигляді можна використовувати різні хмарні сховища, такі як Google Drive, Dropbox, Microsoft OneDrive, iCloud тощо. Вибір конкретного хмарного сховища залежатиме від ваших вподобань та вимог щодо безпеки та доступності.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest11_5")
async def quest11_5(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block11")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Надсилання сканів документів комусь ще є необов'язковим, але може бути корисним для забезпечення додаткової копії та запобігання можливій втраті. Розгляньте можливість надіслати скани родичам або довіреним особам, які можуть бути вам підтримкою.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest11_6")
async def quest11_6(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block11")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Для забезпечення доступу до сканів документів в разі потреби, ви можете використовувати паролі, шифрування або інші методи захисту своїх електронних пристроїв та хмарних сховищ. Забезпечте безпеку своїх пристроїв та не розголошуйте конфіденційну інформацію", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest11_7")
async def quest11_7(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block11")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Рекомендується регулярно перевіряти та оновлювати збережені скани, особливо в разі змін у ваших документах або додавання нових важливих документів, а також робити резервні копії важливих даних.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block12")
async def block12(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("Чому і для чого необхідно звернутися до НП?", callback_data="quest12_1")
    quest2 = types.KeyboardButton("Які документи необхідно надати до НП?", callback_data="quest12_2")
    quest3 = types.KeyboardButton("Для чого потрібен витяг з ЄРДР?", callback_data="quest12_3")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1, quest2, quest3)
    await bot.edit_message_text("12 БЛОК – ЗВЕРНЕННЯ ДО НПУ ІЗ ЗАЯВОЮ", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest12_1")
async def quest12_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block12")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Звернення до Національної поліції необхідне для відкриття кримінального провадження за ст. 438 Кримінального кодексу України («Порушення законів та звичаїв війни»), об’єктивна сторона даного злочину може виражатись у таких діях, як мародерство, пошкодження, знищення цивільних об’єктів.\n"
                                "Заявнику має бути наданий витяг з Єдиного реєстру досудових розслідувань (ЄРДР), який доцільно зберігти. У ході процесу заявник набуде статусу потерпілого та може бути вирішене питання щодо стягнення спричиненої шкоди з відповідальної особи (питання щодо винної особи буде вирішуватись у ході процесу шляхом проведення слідчих дій та оцінки доказів).", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest12_2")
async def quest12_2(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block12")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Заява, в якій слід детально описати ситуацію, порушення законів та звичаїв війни і надати всі відомості про події.\n"
                                "Документи, що підтверджують факти порушення, такі як фотографії, відеозаписи, свідчення свідків тощо.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest12_3")
async def quest12_3(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block12")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Витяг з Єдиного реєстру досудових розслідувань (ЄРДР) є важливим документом, який надається заявнику. Він містить інформацію про відкрите кримінальне провадження і є підтвердженням того, що ваша заява прийнята та зареєстрована. Витяг з ЄРДР може бути використаний для подальшого взаємодії з поліцією, статусу потерпілого та вирішення питань щодо стягнення спричиненої шкоди.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="block13")
async def block13(callback_data: types.CallbackQuery):
    quest1 = types.KeyboardButton("В які онлайн-ресурси можна подати заявку про пошкоджене/зруйноване майно?", callback_data="quest13_1")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(quest1)
    await bot.edit_message_text("13 БЛОК – ПОДАННЯ ОНЛАЙН ЗАЯВОК", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


@dp.callback_query_handler(text="quest13_1")
async def quest13_1(callback_data: types.CallbackQuery):
    back = types.KeyboardButton("Назад🔙", callback_data="block13")
    mar = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1).add(back)
    await bot.edit_message_text("Для здійснення повідомлень використовується Єдиний портал державних послуг «Дія». Подати інформаційне повідомлення про зруйноване внаслідок військової агресії рф житло можна онлайн (через мобільний застосунок «Дія» чи через портал державних послуг «Дія» – diia.gov.ua) або офлайн: звернувшись до ЦНАПу чи нотаріуса особисто або через уповноваженого представника.\n"
                                "В рамках програми «єВідновлення» можна отримати компенсації на відновлення пошкодженого майна через війну.", callback_data.from_user.id, callback_data.message.message_id, reply_markup=mar)


if __name__ == "__main__":
    executor.start_polling(dp)
