from aiogram import Bot, Dispatcher, types
import config

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)

# Helper: main menu keyboard
main_menu_keyboard = types.InlineKeyboardMarkup()
main_menu_keyboard.add(types.InlineKeyboardButton("Dashboard", callback_data="dashboard"))
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
        "Welcome to MemeCoinRugBot an all one bundler & Trading Bot\n"
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
        "30 Day License - 1 SOL.\n"
        "Ownership      - 4 SOL.\n"
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
