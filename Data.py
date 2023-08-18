from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("⩩ بدء استخراج الجلسة ☆.", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="⩩ الصفحة الرئيسية ☆.", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "ᥲ️᥎ᥲ️ƚᥲ️ᖇ 𖣂 ᥉᥆υᖇᥴᥱ", url="https://t.me/sourceav"
            )
        ],
        [
            InlineKeyboardButton("طريقة استخدام البوت ☆", callback_data="help"),
            InlineKeyboardButton("حول ⩩", callback_data="about"),
        ],
        [InlineKeyboardButton("َժٍᥱُ᥎", url="https://t.me/UP_UO")],
    ]

    START = """
أهلًا {} ♦
ومرحبًا بك عزيزي في {}
البوت متخصص في استخراج الجلسات
مثل: - البايروجرام ، التيرمكس
من خلال إرسال الأيبي ايدي والأيبي هاش ورقم هاتفك والكود والتحقق بخطوتين إذا كنت مفعله
َժٍᥱُ᥎ :- @UP_UO 
    """

    HELP = """
 **الأوامر المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ريبو البوت
/generate - لاستخراج الجلسات 
/cancel - لإلغاء الاستخراج 
/restart - لترسيت البوت
"""

    # About Message
    ABOUT = """
**حول البوت** 
╔━━━━━𓌹 ↱ 𝑍𝐸 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸 ↲ 𓌺━━━━━━╗  
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
⩩ انا بوت استخراج جلسات من سورس افاتار
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/UI_XB)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
َժٍᥱُ᥎ : @UP_UO
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
╚━━━━━𓌹 ↱ 𝑍𝐸 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸 ↲ 𓌺━━━━━━╝
    """

    # Repo Message
    REPO = """
⋖━━❲𖣂❳━━𖠙𝑍𝐸𖠙━━❲𖣂❳━━⋗
⩩ انا بوت استخراج جلسات خاص بسورس زد إي
╔━━━━━𓌹 ↱ 𝑍𝐸 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸 ↲ 𓌺━━━━━━╗  

⩩ السورس [𝑍𝐸 𖣂 𝑆𝑂𝐔𝑅𝐶𝐸](https://t.me/UI_XB)

╚━━━━━𓌹 ↱ ᥲ️᥎ᥲ️ƚᥲ️ᖇ 𖣂 ᥉᥆υᖇᥴᥱ ↲ 𓌺━━━━━━╝
إذا كان لديك أي سؤال ، فراسل » المطور » [َժٍᥱُ᥎] @UP_UO
⋖━━❲𖣂❳━━𖠙𝑍𝐸𖠙━━❲𖣂❳━━⋗
   """
