from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Length, DataRequired, Optional

from .models import Category


def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class NewsForm(FlaskForm):
    title = StringField('Название',
                        validators=[DataRequired(message='Это поле не должно быть пустым!'),
                                    Length(max=255, message='Заголовок не более 255 символов!')])
    text = TextAreaField('Текст новости',
                         validators=[DataRequired(message='Это поле не должно быть пустым!'),
                                     Length(min=10)])

    category = SelectField('Категория', choices=get_categories(), validators=[Optional()])
    submit = SubmitField('Подтвердить')
