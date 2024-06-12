# -*- coding: UTF-8 -*-
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils .keyboard import ReplyKeyboardBuilder



main = ReplyKeyboardMarkup(
    keyboard=[
    #    [
    #         KeyboardButton(text="Найти Мангу/Аниме"),
    #     ], 
        [
            KeyboardButton(text="Топ манги"),
            KeyboardButton(text="Топ аниме"),
        ],
        [
            KeyboardButton(text="Читать мангу"),
            KeyboardButton(text="Смотреть Аниме")
        ]

    ],
    resize_keyboard=True,
    input_field_placeholder="Что вам нужно, сударь?",
    selective=True
)

meme = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="lesson№1", url="https://www.youtube.com/watch?v=qVMfHnSxlGk"),
            InlineKeyboardButton(text="lesson№2", url="https://www.youtube.com/watch?v=xLJ9MNygr88")
        
        ]
    ]
)

