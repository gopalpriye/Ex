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
from Extractor.modules.pw import  pw_login
from Extractor.modules.careerwill import career_will
from Extractor.modules.getappxotp import send_otp
from Extractor.modules.findapi import findapis_extract
from Extractor.modules.utk import handle_utk_logic
from Extractor.modules.iq import handle_iq_logic
from Extractor.modules.adda import adda_command_handler
log_channel = (-1002385747075)
# ------------------------------------------------------------------------------- #

buttons = InlineKeyboardMarkup([[
                    InlineKeyboardButton("🌟 𝐀𝐏𝐏𝐗 𝐀𝐏𝐏𝐒 🌟", callback_data="manual_"),
                  ],[
                    InlineKeyboardButton("🌟 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐀𝐏𝐏𝐒 🌟", callback_data="premium_apps"),
                  ],[
                    InlineKeyboardButton("👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/YourDeveloperUsername"),
                    InlineKeyboardButton("📢 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/YourChannelUsername"),
                  ]])

premium_apps_button = InlineKeyboardMarkup([[
                    InlineKeyboardButton("🏆 𝐌𝐀𝐃𝐄 𝐄𝐀𝐒𝐘", callback_data="made_easy"),
                    InlineKeyboardButton("📚 𝐈𝐀𝐒 𝐌𝐀𝐒𝐓𝐄𝐑", callback_data="ias_master"),
                  ],[
                    InlineKeyboardButton("🚀 𝐔𝐍𝐀𝐂𝐀𝐃𝐄𝐌𝐘", callback_data="unacademy"),
                    InlineKeyboardButton("🩺 𝐀𝐋𝐋𝐄𝐍", callback_data="allen"),
                  ],[
                    InlineKeyboardButton("🌟 𝐍𝐄𝐗𝐇 𝐈𝐀𝐒", callback_data="next_ias"),
                  ],[
                    InlineKeyboardButton("🔙 𝐁𝐚𝐜𝐤", callback_data="home_"),
                  ]])

modes_button = InlineKeyboardMarkup([[
                  InlineKeyboardButton("⚙️ 𝐂𝐮𝐬𝐭𝐨𝐦 𝐌𝐨𝐝𝐞", callback_data="custom_"),
                  InlineKeyboardButton("📋 𝐌𝐚𝐧𝐮𝐚𝐥/𝐋𝐢𝐬𝐭", callback_data="manual_"),
                ],[
                  InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="home_")
                ]])

custom_button = InlineKeyboardMarkup([[
                  InlineKeyboardButton("🔥 𝐀𝐩𝐩𝐞𝐱 𝐕𝟐", callback_data="v2_"),
                  InlineKeyboardButton("🚀 𝐀𝐩𝐩𝐞𝐱 𝐕𝟑", callback_data="v3_"),
                  InlineKeyboardButton("✨ 𝐀𝐩𝐩𝐞𝐱 𝐕𝟒", callback_data="v4_"),
                ],[
                  InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="home_")
                ]])

button1 = [              
    [
        InlineKeyboardButton("🏆 Achievers Academy", callback_data="achievers_acc"),
        InlineKeyboardButton("📚 Adhyayan Mantra", callback_data="adhyan_mantra"),
        InlineKeyboardButton("👨‍🏫 Aman Sir", callback_data="aman_sir"),
    ],
    [
        InlineKeyboardButton("🔧 Anil Sir ITI", callback_data="anilsir_iti"),
        InlineKeyboardButton("🎯 App Exampur", callback_data="app_exampur"),
        InlineKeyboardButton("🪖 Army Study", callback_data="army_study"),
    ],
    [
        InlineKeyboardButton("📖 Ashish Singh Lec", callback_data="Ashish_lec"),
        InlineKeyboardButton("🧑‍🏫 Bharti Sir", callback_data="bharti_sir"),
        InlineKeyboardButton("🚀 Booster Academy", callback_data="booster_academy"),
    ],
    [
        InlineKeyboardButton("🛡️ Cadet Defence", callback_data="cadet_defence"),
        InlineKeyboardButton("⚔️ Commando Academy", callback_data="commando_acc"),
        InlineKeyboardButton("✝️ Christopher", callback_data="christopher_acc"),
    ],
    [
        InlineKeyboardButton("🏛️ Dhananjay IAS", callback_data="dhananjay_ias"),
        InlineKeyboardButton("📱 E1 Coaching", callback_data="e1_coaching"),
        InlineKeyboardButton("🎓 Examo Academy", callback_data="examo_acc"),
    ],
    [
        InlineKeyboardButton("✅ Exampur", callback_data="exampur_"),
        InlineKeyboardButton("🎯 Goal Yaan", callback_data="goal_yaan"),
        InlineKeyboardButton("☕ Gk Cafe", callback_data="gk_cafe"),
    ],
    [
        InlineKeyboardButton("🌱 Grow Academy", callback_data="grow_acc"),
        InlineKeyboardButton("📖 Gyan Bindu", callback_data="gyan_bindu"),
        InlineKeyboardButton("📊 KTDT", callback_data="kt_dt"),
    ],
    [
        InlineKeyboardButton("📚 Md Classes", callback_data="md_classes"),
        InlineKeyboardButton("💡 Mg Concept", callback_data="mg_concept"),
        InlineKeyboardButton("👩‍🏫 Mother's Live", callback_data="mothers_live"),
    ],
    [
        InlineKeyboardButton("⚡️ Neo Spark", callback_data="neo_spark"),
        InlineKeyboardButton("🌟 Neon Classes", callback_data="neon_classes"),
        InlineKeyboardButton("🩺 Neet Kakajee", callback_data="neet_kakajee"),
    ],
    [
        InlineKeyboardButton("🌍 Ng Learners", callback_data="ng_learners"),
        InlineKeyboardButton("🏫 Nidhi Academy", callback_data="nidhi_academy"),
        InlineKeyboardButton("📝 Nimisha Bansal", callback_data="nimisha_bansal"),
    ],
    [
        InlineKeyboardButton("🏛️ Nirman IAS", callback_data="nirman_ias"),
        InlineKeyboardButton("📓 Note Book", callback_data="note_book"),
        InlineKeyboardButton("🌊 Ocean Gurukul", callback_data="ocean_gurukul"),
    ],
    [
        InlineKeyboardButton("🎖️ Officers Academy", callback_data="officers_acc"),
        InlineKeyboardButton("📚 Parmar SSC", callback_data="permar_ssc"),
        InlineKeyboardButton("🌟 Perfect Academy", callback_data="perfect_acc"),
    ],
    [
        InlineKeyboardButton("🔬 PHYSICSASINGH", callback_data="physics_asingh"),
        InlineKeyboardButton("🏫 Platform", callback_data="platform_"),
        InlineKeyboardButton("👨‍🏫 RG Vikramjeet", callback_data="rg_vikramjeet"),
    ],
    [
        InlineKeyboardButton("📖 Rk Sir", callback_data="rk_sir"),
        InlineKeyboardButton("💼 Rwa", callback_data="rwa_"),
        InlineKeyboardButton("🏆 Sachin Academy", callback_data="sachin_acc"),
    ],
    [
        InlineKeyboardButton("📚 Samyak", callback_data="samyak_ras"),
        InlineKeyboardButton("🎯 Sankalp", callback_data="sankalp_"),
        InlineKeyboardButton("🔬 Science Fun", callback_data="science_fun"),
    ],
    [
        InlineKeyboardButton("📖 Singhkori", callback_data="singhkori_education"),
        InlineKeyboardButton("🚀 Space IAS", callback_data="space_ias"),
        InlineKeyboardButton("📚 Study Mantra", callback_data="study_mantra"),
    ],
    [
        InlineKeyboardButton("🏫 Ssc Gurkul", callback_data="ssc_gurukul"),
        InlineKeyboardButton("🎯 Ssc Maker", callback_data="ss_maker"),
        InlineKeyboardButton("🌟 Target Plus", callback_data="target_plus"),
    ],
    [
        InlineKeyboardButton("🏛️ Target Upsc", callback_data="target_upsc"),
        InlineKeyboardButton("👩‍🏫 TeachingPariksha", callback_data="teaching_"),
        InlineKeyboardButton("📚 Think Ssc", callback_data="think_ssc"),
    ],
    [
        InlineKeyboardButton("📖 Tutors Adda", callback_data="tutors_adda"),
        InlineKeyboardButton("📱 Uc Live", callback_data="uc_live"),
        InlineKeyboardButton("💡 Vasu Concept", callback_data="vasu_concept"),
    ],
    [
        InlineKeyboardButton("🏫 Vidya Bihar", callback_data="vidya_bihar"),
        InlineKeyboardButton("📚 Vidya Education", callback_data="vidya_education"),
        InlineKeyboardButton("🌟 Vj Education", callback_data="vj_education"),
    ],
    [
        InlineKeyboardButton("🏆 Winners", callback_data="winners_"),
        InlineKeyboardButton("⚔️ Yodha", callback_data="yodha_"),
    ],
    [
        InlineKeyboardButton("⬅️", callback_data="prev"),
        InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="home_"),
        InlineKeyboardButton("➡️", callback_data="next"),
    ]
]

back_button  = [[
                    InlineKeyboardButton("🔙 𝐁𝐚𝐜𝐤", callback_data="home_"),                    
                ]]

# Store user state to track which app they selected
user_states = {}

# ------------------------------------------------------------------------------- #
captionn =("🌟 **Welcome to COBRA TXT Extractor Bot** 🌟\n\n"
           "Explore a world of educational resources with ease! 📚\n\n"
           "🔹 **Available Commands**:\n"
           "  /appx - Master Appx Access\n"
           "  /appxlist - View Appx List\n"
           "  /appxotp - Appx OTP Login\n"
           "  /adda - Adda 247 Access\n"
           "  /cp - Classplus Access\n"
           "  /getapi - Find Appx API\n"
           "  /iq - Study IQ Access\n"
           "  /kd - KD Campus Access\n"
           "  /kgs - Khan GS App Access\n"
           "  /pw - Physics Wallah Access\n"
           "  /utkarsh - Utkarsh Access\n\n"
           "🚀 **Get Started Now!**")

@app.on_message(filters.command("start"))
async def start(_,message):
  join = await subscribe(_,message)
  if join ==1:
    return
  await message.reply_photo(photo=random.choice(script.IMG), 
                            caption=captionn,
                            reply_markup=buttons)
  

@app.on_message(filters.command("apps"))
async def start(_,message):
  await message.reply_photo(photo=random.choice(script.IMG), 
                            caption=captionn,
                           reply_markup=buttons)
  

@app.on_message(filters.command("appxlist"))
async def start(_,message):
  await message.reply_text(script.MANUAL_TXT,
                           reply_markup=InlineKeyboardMarkup(button1))

# Handle credentials for premium apps
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
            f"🔐 **Credentials**:\n\n{credentials}\n\n"
            f"👨‍💻 **Provided by**: @SEM2JOB_SERVICE_BOT"
        )
        
        await app.send_message(log_channel, log_message)
        await message.reply_text(
            f"✅ **Credentials Submitted for {selected_app}!**\n\nThank you! We'll process your request soon. 📡",
            reply_markup=back_button
        )
        # Remove user from state after handling
        del user_states[user_id]
  
@app.on_callback_query()
async def handle_callback(_, query):

    if query.data=="home_": 
       await query.message.delete(True)
  
      
    elif query.data=="modes_":
        
        reply_markup = InlineKeyboardMarkup(modes_button)
        await query.message.edit_text(
              script.MODES_TXT,
              reply_markup=reply_markup)
        
        
    elif query.data=="custom_":        
        reply_markup = InlineKeyboardMarkup(custom_button)
        await query.message.edit_text(
              script.CUSTOM_TXT,
              reply_markup=reply_markup
            )
        
     
    elif query.data=="manual_":        
        reply_markup = InlineKeyboardMarkup(button1)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )

    elif query.data=="premium_apps":
        reply_markup = InlineKeyboardMarkup(premium_apps_button)
        await query.message.edit_text(
              "🌟 **Premium Apps** 🌟\n\nSelect a premium app to proceed:",
              reply_markup=reply_markup
            )

    elif query.data in ["made_easy", "ias_master", "unacademy", "allen", "next_ias"]:
        app_names = {
            "made_easy": "MADE EASY",
            "ias_master": "IAS MASTER",
            "unacademy": "UNACADEMY",
            "allen": "ALLEN",
            "next_ias": "NEXT IAS"
        }
        selected_app = app_names[query.data]
        user_states[query.from_user.id] = selected_app
        await query.message.edit_text(
            f"🔑 **Send Your Login Credentials (ID & Password) for {selected_app}**",
            reply_markup=back_button
        )

    elif query.data=="appxotp_": 
        api = await app.ask(query.message.chat.id, text="**🔑 SEND APPX API**\n\n✅ Example: tcsexamzoneapi.classx.co.in")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if api else api_txt.split('.')[0]
        if "api" in api_txt:
          await send_otp(app, query.message, api_txt)
        else:
          return await app.send_message(query.message.chat.id, "❌ INVALID INPUT! IF YOU DON'T KNOW API, GO TO FIND API OPTION")
    
    elif query.data=="v2_": 
        api = await app.ask(query.message.chat.id, text="**🔑 SEND APPX API Without https://**\n\n✅ Example: tcsexamzoneapi.classx.co.in")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if api else api_txt.split('.')[0]
        if "api" in api_txt:
          
          await appex_v3_txt(app, query.message, api_txt, name)
        else:
          return await app.send_message(query.message.chat.id, "❌ INVALID INPUT! IF YOU DON'T KNOW API, GO TO FIND API OPTION")

    elif query.data=="v3_": 
        api = await app.ask(query.message.chat.id, text="**🔑 SEND APPX API Without https://**\n\n✅ Example: tcsexamzoneapi.classx.co.in")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if api else api_txt.split('.')[0]
        if "api" in api_txt:
          await appex_v3_txt(app, query.message, api_txt, name)
        else:
          return await app.send_message(query.message.chat.id, "❌ INVALID INPUT! IF YOU DON'T KNOW API, GO TO FIND API OPTION")
      
    elif query.data=="next_1":        
        reply_markup = InlineKeyboardMarkup(button2)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_2":        
        reply_markup = InlineKeyboardMarkup(button3)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_3":        
        reply_markup = InlineKeyboardMarkup(button4)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )

    elif query.data=="next_4":        
        reply_markup = InlineKeyboardMarkup(button5)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )

          
        
    elif query.data=="maintainer_":     
        await query.answer(("⚠️ Bot Under Maintenance ⚠️\n📡 Updates Coming Soon!"), show_alert=True)


    
    
    elif query.data=="my_":
        await my_pathshala_login(app, query.message)
      
    elif query.data=="findapi_":
        await findapis_extract(app, query.message)
    
    elif query.data=="kdlive_":
        await kdlive(app, query.message)
    
    elif query.data=="careerwill_":
        await career_will(app, query.message)
  
    elif query.data=="khan_":
        await khan_login(app, query.message)
      

    elif query.data=="vidya_education":     
        api = "vidyaeducationrahulsirapi.akamai.net.in"
        name = "VIDYA EDUCATION"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="platform_":     
        api = "platformnavinkumarsinghapi.classx.co.in"
        name = "Platform"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="teaching_":     
        api = "teachingparikshaapi.classx.co.in"
        name = "Teaching Parikhsha"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="ss_maker":     
        api = "sscmakerexampreparationapi.classx.co.in"
        name = "SSC Makers"
        await appex_v3_txt(app, query.message, api, name)
           
           
      
    elif query.data=="teaching_":     
        api = "teachingparikshaapi.classx.co.in"
        name = "Teaching Parikhsha"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="vasu_concept":     
        api = "vasuconceptapi.classx.co.in"
        name = "Vasu Concept"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="mothers_live":     
        api = "mothersliveapi.classx.co.in"
        name = "Mother's Live"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="examo_acc":     
        api = "examoapi.classx.co.in"
        name = "Examo Academy"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="neon_claases":     
        api = "neonclassesapi.classx.co.in"
        name = "Neon Classes"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="adhyan_mantra":     
        api = "adhyayanmantraapi.appx.co.in"
        name = "Adhyayan Mantra"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="perfect_acc":     
        api = "perfectionacademyapi.appx.co.in"
        name = "Perfection Academy"
        await appex_v3_txt(app, query.message, api, name)

  
      
      
    elif query.data=="bharti_sir":     
        api = "bhartilearningapi.classx.co.in"
        name = "Bharti"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="nidhi_mam":     
        api = "nidhiacademyapi.akamai.net.in"
        name = "NIDHI ACADEMY"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="physics_asingh":     
        api = "physicsasinghsirapi.cloudflare.net.in"
        name = "PHYSICSASINGH"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="booster_academy":     
        api = "boosteracademyapi.classx.co.in"
        name = "Booster Academy"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="cadet_defence":     
        api = "cadetdefenceacademyapi.classx.co.in"
        name = "Cadet Defence"
        await appex_v3_txt(app, query.message, api, name)
    
    elif query.data=="e1_coaching":     
        api = "e1coachingcenterapi.cloudflare.net.in"
        name = "e1 coaching"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="samyak_ras":     
        api = "samyakapi.classx.co.in"
        name = "Samyak"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="vj_education":     
        api = "vjeducationapi.appx.co.in"
        name = "VJ Education"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="gyan_bindu":     
        api = "gyanbinduapi.appx.co.in"
        name = "Gyan Bindu"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="dhananjay_ias":     
        api = "dhananjayiasacademyapi.classx.co.in"
        name = "Dhananjay IAS"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="think_ssc":     
        api = "thinksscapi.classx.co.in"
        name = "Think SSC"
        await appex_v3_txt(app, query.message, api, name)

  

    elif query.data=="Sahil_sir":     
        api = "quicktrickssahilsirapi.classx.co.in"
        name = "Sahil Sir"
        await appex_v3_txt(app, query.message, api, name)
        
    elif query.data=="Ashish_lec":     
        api = "ashishsinghlecturesapi.classx.co.in"
        name = "Ashish Singh"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="tutors_adda":     
        api = "tutorsaddaapi.classx.co.in"
        name = "Tutors Adda"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="nimisha_bansal":     
        api = "nimishabansalapi.appx.co.in"
        name = "Nimisha Bansal"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="sachin_acc":     
        api = "sachinacademyapi.classx.co.in"
        name = "Sachin Academy"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="acharya_classes":     
        api = "acharyaclassesapi.classx.co.in"
        name = "Acharya Classes"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="target_plus":     
        api = "targetpluscoachingapi.classx.co.in"
        name = "Target Plus Coaching"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="rwa_":   
        api = "rozgarapinew.teachx.in"
        name = "Rojgar with Ankit"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="winners_":     
        api = "winnersinstituteapi.classx.co.in"
        name = "Winners"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="ocean_gurukul":     
        api = "oceangurukulsapi.classx.co.in"
        name = "Ocean Gurukul"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="mg_concept":     
        api = "mgconceptapi.classx.co.in"
        name = "MG Concept"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="yodha_":     
        api = "yodhaappapi.classx.co.in"
        name = "Yodha"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="note_book":     
        api = "notebookapi.classx.co.in"
        name = "Note Book"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="uc_live":     
        api = "ucliveapi.classx.co.in"
        name = "UC LIVE"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="space_ias":     
        api = "spaceiasapi.classx.co.in"
        name = "Space IAS"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="rg_vikramjeet":     
        api = "rgvikramjeetapi.akamai.net.in/"
        name = "RG Vikramjeet"
        await appex_v3_txt(app, query.message, api, name)
        
        

      
    elif query.data=="vidya_bihar":     
        api = "vidyabiharapi.teachx.in"
        name = "Vidya Vihar"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="aman_sir":     
        api = "amansirenglishapi.classx.co.in"
        name = "Aman Sir English"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="nirman_ias":     
        api = "nirmaniasapi.classx.co.in"
        name = "Nirman IAS"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="permar_ssc":     
        api = "parmaracademyapi.cloudflare.net.in"
        name = "Parmar Academy"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="neo_spark":     
        api = "neosparkapi.classx.co.in"
        name = "Neo Spark"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="md_classes":     
        api = "mdclassesapi.classx.co.in"
        name = "MD Classes"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="ng_learners":     
        api = "nglearnersapi.classx.co.in"
        name = "NG Learners"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="ssc_gurukul":     
        api = "ssggurukulapi.appx.co.in"
        name = "SSC Gurukul"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="army_study":     
        api = "armystudyliveclassesapi.classx.co.in"
        name = "Army Study Live"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="sankalp_":     
        api = "sankalpclassesapi.classx.co.in"
        name = "Sankalp"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="target_upsc":     
        api = "targetupscapi.classx.co.in"
        name = "Target UPSC"
        await appex_v3_txt(app, query.message, api, name)
      
    elif query.data=="gk_cafe":     
        api = "gkcafeapi.classx.co.in"
        name = "GK Cafe"
        await appex_v3_txt(app, query.message, api, name)

    elif query.data == 'officers_acc':
        api = "theofficersacademyapi.classx.co.in"
        name = "Officers Academy"
        await appex_v3_txt(app, query.message, api, name)

    elif query.data == 'rk_sir':
        api = "rksirofficialapi.classx.co.in"
        name = "Rk Sir Official"
        await appex_v3_txt(app, query.message, api, name) 
      
    elif query.data == 'study_mantra':
        api = "studymantraapi.classx.co.in"
        name = "Study Mantra"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'science_fun':
        api = "sciencefunapi.classx.co.in"
        name = "Science Fun"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'grow_acc':
        api = "growacademyapi.classx.co.in"
        name = "Grow Academy"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'goal_yaan':
        api = "goalyaanapi.appx.co.in"
        name = "Goal Yaan"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'anilsir_iti':
        api = "anilsiritiapi.classx.co.in"
        name = "Anil Sir Iti"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'education_adda':
        api = "educationaddaplusapi.classx.co.in"
        name = "Education Adda Plus"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'achievers_acc':
        api = "achieversacademyapi.classx.co.in"
        name = "Achievers Academy"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'commando_acc':
        api = "commandoacademyapi.appx.co.in"
        name = "Commando Academy"
        await appex_v3_txt(app, query.message, api, name) 


    elif query.data == 'exampur_':
        await appex_v3_txt(app, query.message)

    elif query.data == 'neet_kakajee':
        api = "neetkakajeeapi.classx.co.in"
        name = "Neet Kaka JEE"
        await appex_v3_txt(app, query.message, api, name) 

    elif query.data == 'app_exampur':
        api = "exampurapi.classx.co.in"
        name = "App Exampur"
        await appex_v3_txt(app, query.message, api, name) 
  
    elif query.data=="pw_":
      await pw_login(app,query.message)
  
    elif query.data=="classplus_":          
        await classplus_txt(app, query.message)
  
    elif query.data=="close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()