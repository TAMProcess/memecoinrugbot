from aiogram import Bot, Dispatcher, types
import config

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)

# Helper: main menu keyboard
main_menu_keyboard = types.InlineKeyboardMarkup()
main_menu_keyboard.add(types.InlineKeyboardButton("RugBot", callback_data="RugBot"))
main_menu_keyboard.add(types.InlineKeyboardButton("Features", callback_data="features"))
main_menu_keyboard.add(types.InlineKeyboardButton("Purchase & Pricing", callback_data="purchase"))
main_menu_keyboard.add(types.InlineKeyboardButton("More Info", callback_data="moreinfo"))
main_menu_keyboard.add(types.InlineKeyboardButton("Vouches", url="https://t.me/vouchesrugbot"))

# /start command handler
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    """Handle /start command: greets the user as 'Guest' and shows main menu."""
    welcome_text = (
        "-Main Menu-\n"
        "User: 92033820\n"
        "Version: 4.88.00\n"
        "@RugbotHelp\n"
        "Welcome to MemeCoinRugBot an all one Bundler & Trading Bot\n"
    )
    # Send welcome message with main menu inline keyboard
    await message.answer(welcome_text, reply_markup=main_menu_keyboard)

# Callback handler for main menu navigation (Dashboard and Back both lead to main menu)
@dp.callback_query_handler(lambda c: c.data in ['dashboard', 'back'])
async def back_to_main(callback: types.CallbackQuery):
    """Handles 'Dashboard' and 'Back' button presses by returning to main menu."""
    # Edit the message to show the main menu again
    main_text = (
        "-Main Menu-\n"
        "User: 92033820\n"
        "Version: 4.88.00\n"
        "@RugbotHelp\n"
        "Welcome to MemeCoinRugBot an all one bundler & Trading Bot\n"
    )
    # Re-use the same main menu keyboard
    await callback.message.edit_text(main_text, reply_markup=main_menu_keyboard)
    await callback.answer()

# Callback handler for Features section
@dp.callback_query_handler(lambda c: c.data == 'features')
async def features_section(callback: types.CallbackQuery):
    """Shows the Features section and a back button."""
    features_text = (
        "📋 *Features:*\n\n"
        "Pump.fun Volume + Bundler + Bump It + Comment Bot\n\n"
        "► Volume Modes:\n\n"
            "• Gen Volume 🎛️\n"
            "• Auto Volume\n"
            "• Human Mode 🤖\n"
            "• Micro Buy\n"
            "• Sell All 💸\n"
            "• Single Wallet Sell\n\n"
        "► Bundler:\n\n"
           "• Safe Mode 🛟\n"
           "• Experimental Mode ✏️\n"
           "• Dump All 🏳️\n"
           "• Dump All %\n"
           "• Delay Sell 📉\n"
           "• Delay Sell %\n"
           "• Single Sell\n"
           "• Raydium Sell 💰\n"
           "• Send SPL\n\n"
        "► Comments:\n\n"
           "• Custom Commenter 💬\n\n"
        "► Bump It:\n\n"
           "• Custom Bump It (set username) ✅\n\n"
    )
    # Keyboard with only a Back button
    back_btn = types.InlineKeyboardButton("Back", callback_data="back")
    features_kb = types.InlineKeyboardMarkup().add(back_btn)
    await callback.message.edit_text(features_text, reply_markup=features_kb)
    await callback.answer()

# Callback handler for Purchase & Pricing section (also handles Refresh)
@dp.callback_query_handler(lambda c: c.data in ['purchase', 'refresh'])
async def purchase_section(callback: types.CallbackQuery):
    """Shows the Purchase & Pricing section with payment info and a refresh option."""
    purchase_text = (
        "💰 *Purchase & Pricing:*\n"
        "3 Day Trial License - 1 SOL.\n"
        "Ownership           - 4 SOL.\n"
        f"*SOL Address:* `{config.SOL_ADDRESS}`\n\n"
        "Message @Rugbothelp for support\n"
        "After sending payment, click Refresh to check for updates.\n"
        "Note: Payment verification is manual. This bot does not automatically verify payments\n"
    )
    # Keyboard with Refresh and Back buttons
    refresh_btn = types.InlineKeyboardButton("Refresh 🔄", callback_data="refresh")
    back_btn = types.InlineKeyboardButton("Back", callback_data="back")
    purchase_kb = types.InlineKeyboardMarkup()
    purchase_kb.add(refresh_btn)
    purchase_kb.add(back_btn)
    await callback.message.edit_text(purchase_text, reply_markup=purchase_kb)
    await callback.answer()

# Callback handler for More Info section
@dp.callback_query_handler(lambda c: c.data == 'moreinfo')
async def more_info_section(callback: types.CallbackQuery):
    """Shows the More Info section and a back button."""
    info_text = (
        "ℹ️ *More Information:*\n"
        "Our tool allows you to easily launch your own memecoin on Pump.fun, Raydium, and Moonshot\n"
        "with built-in features to manipulate the price at launch.\n"
        "By bundle-buying your own token, you create the illusion of an organic pump, attracting new investors.\n"
        "With this bot you don’t need marketing or a following – the price action itself generates FOMO among traders.\n"
        "Once the price surges and investors jump in, you can strategically dump your holdings for maximum profit.\n"
        "If you have any questions don't hesitate to reach out: @Rugbothelp\n\n"
    )
    back_btn = types.InlineKeyboardButton("Back", callback_data="back")
    info_kb = types.InlineKeyboardMarkup().add(back_btn)
    await callback.message.edit_text(info_text, reply_markup=info_kb)
    await callback.answer()

# Callback handler for RugBot section (Main RugBot Menu)
@dp.callback_query_handler(lambda c: c.data == 'RugBot')
async def rugbot_section(callback: types.CallbackQuery):
    """Main RugBot Menu: Provides access to all RugBot features."""
    rugbot_keyboard = types.InlineKeyboardMarkup()
    rugbot_keyboard.add(types.InlineKeyboardButton("License Key", callback_data="license_key"))
    rugbot_keyboard.add(types.InlineKeyboardButton("Add Funds", callback_data="add_funds"))
    rugbot_keyboard.add(types.InlineKeyboardButton("Proxys & Node", callback_data="proxys_node"))
    rugbot_keyboard.add(types.InlineKeyboardButton("🏦 Bundler Menu", callback_data="bundler_menu"))
    rugbot_keyboard.add(types.InlineKeyboardButton("🔙 Back to Dashboard", callback_data="dashboard"))

    await callback.message.edit_text("📌 *RugBot Menu:*", reply_markup=rugbot_keyboard)
    await callback.answer()

# Callback handler for License key section
@dp.callback_query_handler(lambda c: c.data == 'license_key')
async def license_key(callback: types.CallbackQuery):
    """Handles license input."""
    await callback.message.edit_text(
        "💰 *Add License Key:*\n\n"
        "Input License Key: `Insert Key Here`\n\n"
        "Input your license key to begin.",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("🔙 Back to Main RugBot Menu", callback_data="RugBot")
        )
    )
    await callback.answer()

# Callback handler for Add Funds section
@dp.callback_query_handler(lambda c: c.data == 'add_funds')
async def add_funds(callback: types.CallbackQuery):
    """Displays the funder wallet address."""
    await callback.message.edit_text(
        "💰 *Add Funds:*\n\n"
        "Generated Wallet: `authentication key required`\n\n"
        "Generated funder wallet is used to fund the bot.",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("🔙 Back to Main RugBot Menu", callback_data="RugBot")
        )
    )
    await callback.answer()

# Callback handler for Proxy & Nodes Menu
@dp.callback_query_handler(lambda c: c.data == 'proxys_node')
async def proxys_node(callback: types.CallbackQuery):
    """menu for Proxy & Nodes."""
    settings_keyboard = types.InlineKeyboardMarkup()
    settings_keyboard.add(types.InlineKeyboardButton("Input Custom Proxy's", callback_data="proxy_not_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Input Custom Node", callback_data="node_not_required"))
    types.InlineKeyboardButton("🔙 Back to Main RugBot Menu", callback_data="RugBot")

    await callback.message.edit_text("*proxys & node:*", reply_markup=proxys_keyboard)
    await callback.answer()
    
# Callback handler for Bundler Menu section
@dp.callback_query_handler(lambda c: c.data == 'bundler_menu')
async def bundler_menu(callback: types.CallbackQuery):
    """Main Bundler Menu."""
    bundler_keyboard = types.InlineKeyboardMarkup()
    bundler_keyboard.add(types.InlineKeyboardButton("Settings ⚙️", callback_data="bundler_settings"))
    bundler_keyboard.add(types.InlineKeyboardButton("Generate Wallets", callback_data="generate_wallets"))
    bundler_keyboard.add(types.InlineKeyboardButton("Launch Coin 💰", callback_data="launch_coin"))
    bundler_keyboard.add(types.InlineKeyboardButton("Manage Token", callback_data="manage_token"))
    bundler_keyboard.add(types.InlineKeyboardButton("Export Private Keys", callback_data="export_keys"))
    bundler_keyboard.add(types.InlineKeyboardButton("🔙 Back to Main RugBot Menu", callback_data="RugBot"))

    await callback.message.edit_text("🏦 *Bundler Menu:*", reply_markup=bundler_keyboard)
    await callback.answer()

# Callback handler for Settings Menu
@dp.callback_query_handler(lambda c: c.data == 'bundler_settings')
async def bundler_settings(callback: types.CallbackQuery):
    """Settings menu for Bundler features."""
    settings_keyboard = types.InlineKeyboardMarkup()
    settings_keyboard.add(types.InlineKeyboardButton("Safe Mode 🛟", callback_data="authentication_key_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Experimental Mode ✏️", callback_data="authentication_key_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Custom Commenter 💬", callback_data="authentication_key_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Auto Volume 🤖", callback_data="authentication_key_required"))
    settings_keyboard.add(types.InlineKeyboardButton("Return to Funder 💸", callback_data="insufficient_funds"))
    settings_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))

    await callback.message.edit_text("⚙️ *Settings:*", reply_markup=settings_keyboard)
    await callback.answer()

# Callback handler for Generate Wallets section
@dp.callback_query_handler(lambda c: c.data == 'generate_wallets')
async def generate_wallets(callback: types.CallbackQuery):
    """Handles wallet generation requests."""
    wallets_keyboard = types.InlineKeyboardMarkup()
    wallets_keyboard.add(types.InlineKeyboardButton("Generate Bundler Wallets", callback_data="wallet_input"))
    wallets_keyboard.add(types.InlineKeyboardButton("Generate Wallets", callback_data="authentication_key_required"))
    wallets_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))

    await callback.message.edit_text("💳 *Generate Wallets:*", reply_markup=wallets_keyboard)
    await callback.answer()

# Callback handler for Launch Coin section
@dp.callback_query_handler(lambda c: c.data == 'launch_coin')
async def launch_coin(callback: types.CallbackQuery):
    """Handles token launch setup."""
    token_keyboard = types.InlineKeyboardMarkup()
    token_keyboard.add(types.InlineKeyboardButton("Token Name", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Symbol", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Image", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Description", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Website", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Twitter", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Token Telegram", callback_data="authentication_key_required"))
    token_keyboard.add(types.InlineKeyboardButton("Launch Token", callback_data="insufficient_funds"))
    token_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))

    await callback.message.edit_text("🚀 *Launch Coin:*", reply_markup=token_keyboard)
    await callback.answer()

# Callback handler for Manage Token section
@dp.callback_query_handler(lambda c: c.data == 'manage_token')
async def manage_token(callback: types.CallbackQuery):
    """Handles token management options."""
    manage_keyboard = types.InlineKeyboardMarkup()
    manage_keyboard.add(types.InlineKeyboardButton("Dump All 🏳️", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Dump All %", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Delay Sell 📉", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Delay Sell %", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Single Sell", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Raydium Sell 💰", callback_data="authentication_key_required"))
    manage_keyboard.add(types.InlineKeyboardButton("Send SPL", callback_data="Token_Balance_0"))
    manage_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))
    
    await callback.message.edit_text("📉 *Manage Token:*", reply_markup=manage_keyboard)
    await callback.answer()

# Callback handler for Export Private Keys section
@dp.callback_query_handler(lambda c: c.data == 'export_keys')
async def export_keys(callback: types.CallbackQuery):
    """Handles private key export requests."""
    export_keyboard = types.InlineKeyboardMarkup()
    export_keyboard.add(types.InlineKeyboardButton("Export Generated Wallets", callback_data="authentication_key_required"))
    export_keyboard.add(types.InlineKeyboardButton("Export Funder Wallet", callback_data="authentication_key_required"))
    export_keyboard.add(types.InlineKeyboardButton("🔙 Back to Bundler Menu", callback_data="bundler_menu"))

    await callback.message.edit_text("🔑 *Export Private Keys:*", reply_markup=export_keyboard)
    await callback.answer()

# Error Messages
@dp.callback_query_handler(lambda c: c.data == 'funder_empty')
async def funder_empty(callback: types.CallbackQuery):
    await callback.answer("Funder Wallet Empty", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'node_not_required')
async def node_not_required(callback: types.CallbackQuery):
    await callback.answer("Input License Key To Edit Node, note: custom nodes are optional", show_alert=True)  
        
@dp.callback_query_handler(lambda c: c.data == 'proxy_not_required')
async def proxy_not_required(callback: types.CallbackQuery):
    await callback.answer("Input License Key To Edit Proxy, note: proxy are optional", show_alert=True)        

@dp.callback_query_handler(lambda c: c.data == 'no_tokens')
async def no_tokens(callback: types.CallbackQuery):
    await callback.answer("No tokens created", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'insufficient_funds')
async def insufficient_funds(callback: types.CallbackQuery):
    await callback.answer("Insufficient Funds, Please Add Funds", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == 'authentication_key_required')
async def authentication_key_required(callback: types.CallbackQuery):
    await callback.answer("Authetication Key Required, Please Input License", show_alert=True)
        
# Universal Back Button Handlers
@dp.callback_query_handler(lambda c: c.data == 'back_to_rugbot')
async def back_to_rugbot(callback: types.CallbackQuery):
    """Returns the user to the Main RugBot Menu."""
    await rugbot_section(callback)

@dp.callback_query_handler(lambda c: c.data == 'back_to_bundler')
async def back_to_bundler(callback: types.CallbackQuery):
    """Returns the user to the Bundler Menu."""
    await bundler_menu(callback)

@dp.callback_query_handler(lambda c: c.data == 'back_to_generate_wallets')
async def back_to_generate_wallets(callback: types.CallbackQuery):
    """Returns the user to the Generate Wallets Menu."""
    await generate_wallets(callback)

# Confirm Handlers Are Loaded
print("RugBot Handlers successfully loaded.")
