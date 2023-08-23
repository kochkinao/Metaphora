import logging
from aiogram import executor
from create_bot import dp
from bd import *
from set_default_commands import set_default_commands

create_table()

#create log
logging.basicConfig(level=logging.INFO)

#handlers
from handlers import thems_and_answer_your_question, estimate, help_with_card_description, main_menu, cards_in_deck, decks, backs, where_are_you_able_to_answer, deck_day, admin_panel
thems_and_answer_your_question.register_handler_thems_and_answer_your_question(dp)
estimate.register_handler_estimate(dp)
help_with_card_description.register_handler_help_with_card_description(dp)
main_menu.register_handler_main_menu(dp)
cards_in_deck.register_handler_cards_in_deck(dp)
decks.register_handler_decks(dp)
backs.regiser_handler_backs(dp)
where_are_you_able_to_answer.register_handler_where_are_you_able_to_answer(dp)
deck_day.register_handler_deck_day(dp)
admin_panel.register_handler_admin_panel(dp)

async def on_startup(dp):
    await set_default_commands(dp)


#start polling
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)