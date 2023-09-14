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
                "𝖲𝖮𝖴𝖱𝖢𝖤 𖣂 𝖲𝖮𝖫𝖬", url="https://t.me/Zz_Z_Z2"
            )
        ],
        [
            InlineKeyboardButton("طريقة استخدام البوت ☆", callback_data="help"),
            InlineKeyboardButton("حول ⩩", callback_data="about"),
        ],
        [InlineKeyboardButton("َժٍᥱُ᥎", url="https://t.me/icccc0")],
    ]

    START = """
أهلًا {} ♦
ومرحبًا بك عزيزي في {}
البوت متخصص في استخراج الجلسات
مثل: - البايروجرام ، التيرمكس
من خلال إرسال الأيبي ايدي والأيبي هاش ورقم هاتفك والكود والتحقق بخطوتين إذا كنت مفعله
َժٍᥱُ᥎ :- @icccc0 
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
╔━━━━━𓌹 ↱ 𝖲𝖮𝖴𝖱𝖢𝖤 𖣂 𝖲𝖮𝖫𝖬 ↲ 𓌺━━━━━━╗  
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
⩩ انا بوت استخراج جلسات من سورس افاتار
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Zz_Z_Z2)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
َժٍᥱُ᥎ : @icccc0
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
╚━━━━━𓌹 ↱ 𝖲𝖮𝖴𝖱𝖢𝖤 𖣂 𝖲𝖮𝖫𝖬 ↲ 𓌺━━━━━━╝
    """

    # Repo Message
    REPO = """
⋖━━❲𖣂❳━━𖠙𝖲𝖮𝖫𝖬𖠙━━❲𖣂❳━━⋗
⩩ انا بوت استخراج جلسات خاص بسورس زد إي
╔━━━━━𓌹 ↱ 𝖲𝖮𝖴𝖱𝖢𝖤 𖣂 𝖲𝖮𝖫𝖬 ↲ 𓌺━━━━━━╗  

⩩ السورس [𝖲𝖮𝖴𝖱𝖢𝖤 𖣂 𝖲𝖮𝖫𝖬](https://t.me/Zz_Z_Z2)

╚━━━━━𓌹 ↱ 𝖲𝖮𝖴𝖱𝖢𝖤 𖣂 𝖲𝖮𝖫𝖬 ↲ 𓌺━━━━━━╝
إذا كان لديك أي سؤال ، فراسل » المطور » [َժٍᥱُ᥎] @icccc0
⋖━━❲𖣂❳━━𖠙𝖲𝖮𝖫𝖬𖠙━━❲𖣂❳━━⋗
   """
