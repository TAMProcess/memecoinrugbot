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
        "Hello, Guest!\n"
        "Welcome to the bot. Use the menu below to navigate:\n"
        "Dashboard - Overview\n"
        "Features - Learn what this bot can do\n"
        "Purchase & Pricing - Buy access or features\n"
        "More Info - Additional information\n"
        "Vouches - See user testimonials"
    )
    # Send welcome message with main menu inline keyboard
    await message.answer(welcome_text, reply_markup=main_menu_keyboard)

# Callback handler for main menu navigation (Dashboard and Back both lead to main menu)
@dp.callback_query_handler(lambda c: c.data in ['dashboard', 'back'])
async def back_to_main(callback: types.CallbackQuery):
    """Handles 'Dashboard' and 'Back' button presses by returning to main menu."""
    # Edit the message to show the main menu again
    main_text = (
        "Hello, Guest!\n"
        "You are back at the main menu (Dashboard). Please choose an option:"
    )
    # Re-use the same main menu keyboard
    await callback.message.edit_text(main_text, reply_markup=main_menu_keyboard)
    await callback.answer()

# Callback handler for Features section
@dp.callback_query_handler(lambda c: c.data == 'features')
async def features_section(callback: types.CallbackQuery):
    """Shows the Features section and a back button."""
    features_text = (
        "📋 *Features:*\n"
        "- Feature 1: Description of feature 1.\n"
        "- Feature 2: Description of feature 2.\n"
        "- Feature 3: Description of feature 3.\n\n"
        "Explore the above features of the bot."
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
        "To purchase, please send the required amount in SOL to the address below.\n"
        f"*SOL Address:* `{config.SOL_ADDRESS}`\n\n"
        "After sending payment, click Refresh to check for updates.\n"
        "_Note: Payment verification is manual. This bot does not automatically verify payments._"
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
        "This bot is designed to help users with X, Y, Z (additional info about the bot or usage).\n"
        "It does not store any personal data or logs, ensuring your privacy.\n\n"
        "For any questions, contact support or refer to the documentation."
    )
    back_btn = types.InlineKeyboardButton("Back", callback_data="back")
    info_kb = types.InlineKeyboardMarkup().add(back_btn)
    await callback.message.edit_text(info_text, reply_markup=info_kb)
    await callback.answer()
