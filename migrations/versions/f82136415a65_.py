"""empty message

Revision ID: f82136415a65
Revises: 
Create Date: 2022-07-17 14:31:59.630249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f82136415a65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ru_ques', sa.String(length=255), nullable=False),
    sa.Column('en_ques', sa.String(length=255), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('main_title_ru', sa.String(length=255), nullable=True),
    sa.Column('main_title_en', sa.String(length=255), nullable=True),
    sa.Column('main_des_ru', sa.String(length=255), nullable=True),
    sa.Column('main_des_en', sa.String(length=255), nullable=True),
    sa.Column('about_title_ru', sa.String(length=255), nullable=True),
    sa.Column('about_title_en', sa.String(length=255), nullable=True),
    sa.Column('about_des_ru', sa.String(length=255), nullable=True),
    sa.Column('about_des_en', sa.String(length=255), nullable=True),
    sa.Column('tours_title_ru', sa.String(length=255), nullable=True),
    sa.Column('tours_title_en', sa.String(length=255), nullable=True),
    sa.Column('tours_des_ru', sa.String(length=255), nullable=True),
    sa.Column('tours_des_en', sa.String(length=255), nullable=True),
    sa.Column('hotels_title_ru', sa.String(length=255), nullable=True),
    sa.Column('hotels_title_en', sa.String(length=255), nullable=True),
    sa.Column('hotels_des_ru', sa.String(length=255), nullable=True),
    sa.Column('hotels_des_en', sa.String(length=255), nullable=True),
    sa.Column('article_title_ru', sa.String(length=255), nullable=True),
    sa.Column('article_title_en', sa.String(length=255), nullable=True),
    sa.Column('article_des_ru', sa.String(length=255), nullable=True),
    sa.Column('article_des_en', sa.String(length=255), nullable=True),
    sa.Column('faq_title_ru', sa.String(length=255), nullable=True),
    sa.Column('faq_title_en', sa.String(length=255), nullable=True),
    sa.Column('faq_des_ru', sa.String(length=255), nullable=True),
    sa.Column('faq_des_en', sa.String(length=255), nullable=True),
    sa.Column('contact_title_ru', sa.String(length=255), nullable=True),
    sa.Column('contact_title_en', sa.String(length=255), nullable=True),
    sa.Column('contact_des_ru', sa.String(length=255), nullable=True),
    sa.Column('contact_des_en', sa.String(length=255), nullable=True),
    sa.Column('toursdetail_title_ru', sa.String(length=255), nullable=True),
    sa.Column('toursdetail_title_en', sa.String(length=255), nullable=True),
    sa.Column('toursdetail_des_ru', sa.String(length=255), nullable=True),
    sa.Column('toursdetail_des_en', sa.String(length=255), nullable=True),
    sa.Column('hoteldetail_title_ru', sa.String(length=255), nullable=True),
    sa.Column('hoteldetail_title_en', sa.String(length=255), nullable=True),
    sa.Column('hoteldetail_des_ru', sa.String(length=255), nullable=True),
    sa.Column('hoteldetail_des_en', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('job', sa.String(length=50), nullable=False),
    sa.Column('photo', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tourscat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.Column('en_cat', sa.String(length=100), nullable=False),
    sa.Column('ru_cat', sa.String(length=100), nullable=False),
    sa.Column('day_pack', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('travlio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('ru_address', sa.String(length=255), nullable=False),
    sa.Column('en_address', sa.String(length=255), nullable=False),
    sa.Column('tel1', sa.Integer(), nullable=True),
    sa.Column('tel2', sa.Integer(), nullable=True),
    sa.Column('ru_about', sa.String(length=255), nullable=False),
    sa.Column('en_about', sa.String(length=255), nullable=False),
    sa.Column('facebook', sa.String(length=255), nullable=False),
    sa.Column('telegram', sa.String(length=255), nullable=False),
    sa.Column('instagram', sa.String(length=255), nullable=False),
    sa.Column('youtube', sa.String(length=255), nullable=False),
    sa.Column('usd', sa.Integer(), nullable=True),
    sa.Column('eur', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('photo', sa.LargeBinary(), nullable=True),
    sa.Column('login', sa.String(length=50), nullable=False),
    sa.Column('psw', sa.String(length=50), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ru_ans', sa.String(length=255), nullable=False),
    sa.Column('en_ans', sa.String(length=255), nullable=False),
    sa.Column('que_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['que_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('toursinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ru_loc', sa.String(length=100), nullable=False),
    sa.Column('en_loc', sa.String(length=100), nullable=False),
    sa.Column('adult_pr', sa.Integer(), nullable=True),
    sa.Column('kids_pr', sa.Integer(), nullable=True),
    sa.Column('photos', sa.String(length=255), nullable=False),
    sa.Column('ru_des', sa.Text(), nullable=False),
    sa.Column('en_des', sa.Text(), nullable=False),
    sa.Column('cat_id', sa.Integer(), nullable=True),
    sa.Column('reviews', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cat_id'], ['tourscat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('packday',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Пакет', sa.Integer(), nullable=True),
    sa.Column('first_city', sa.String(length=50), nullable=False),
    sa.Column('first', sa.String(length=255), nullable=False),
    sa.Column('enfirstcity', sa.String(length=50), nullable=False),
    sa.Column('second_city', sa.String(length=50), nullable=False),
    sa.Column('second', sa.String(length=255), nullable=False),
    sa.Column('ensecondcity', sa.String(length=50), nullable=False),
    sa.Column('ensecond', sa.String(length=255), nullable=False),
    sa.Column('third_city', sa.String(length=50), nullable=False),
    sa.Column('third', sa.String(length=255), nullable=False),
    sa.Column('enthirdcity', sa.String(length=50), nullable=False),
    sa.Column('enthird', sa.String(length=255), nullable=False),
    sa.Column('four_city', sa.String(length=50), nullable=False),
    sa.Column('four', sa.String(length=255), nullable=False),
    sa.Column('enfourcity', sa.String(length=50), nullable=False),
    sa.Column('enfour', sa.String(length=255), nullable=False),
    sa.Column('five_city', sa.String(length=50), nullable=False),
    sa.Column('five', sa.String(length=255), nullable=False),
    sa.Column('enfivecity', sa.String(length=50), nullable=False),
    sa.Column('enfive', sa.String(length=255), nullable=False),
    sa.Column('six_city', sa.String(length=50), nullable=False),
    sa.Column('six', sa.String(length=255), nullable=False),
    sa.Column('ensixcity', sa.String(length=50), nullable=False),
    sa.Column('ensix', sa.String(length=255), nullable=False),
    sa.Column('seven_city', sa.String(length=50), nullable=False),
    sa.Column('seven', sa.String(length=255), nullable=False),
    sa.Column('ensevencity', sa.String(length=50), nullable=False),
    sa.Column('enseven', sa.String(length=255), nullable=False),
    sa.Column('eight_city', sa.String(length=50), nullable=False),
    sa.Column('eight', sa.String(length=255), nullable=False),
    sa.Column('eneightcity', sa.String(length=50), nullable=False),
    sa.Column('eneight', sa.String(length=255), nullable=False),
    sa.Column('nine_city', sa.String(length=50), nullable=False),
    sa.Column('nine', sa.String(length=255), nullable=False),
    sa.Column('enninecity', sa.String(length=50), nullable=False),
    sa.Column('ennine', sa.String(length=255), nullable=False),
    sa.Column('ten_city', sa.String(length=50), nullable=False),
    sa.Column('ten', sa.String(length=255), nullable=False),
    sa.Column('entencity', sa.String(length=50), nullable=False),
    sa.Column('enten', sa.String(length=255), nullable=False),
    sa.Column('eleven_city', sa.String(length=50), nullable=False),
    sa.Column('eleven', sa.String(length=255), nullable=False),
    sa.Column('enelevencity', sa.String(length=50), nullable=False),
    sa.Column('eneleven', sa.String(length=255), nullable=False),
    sa.Column('thirdteen_city', sa.String(length=50), nullable=False),
    sa.Column('thirdteen', sa.String(length=255), nullable=False),
    sa.Column('enthirdteencity', sa.String(length=50), nullable=False),
    sa.Column('enthirdteen', sa.String(length=255), nullable=False),
    sa.Column('fourteen_city', sa.String(length=50), nullable=False),
    sa.Column('fourteen', sa.String(length=255), nullable=False),
    sa.Column('enfourteencity', sa.String(length=50), nullable=False),
    sa.Column('enfourteen', sa.String(length=255), nullable=False),
    sa.Column('fiveteen_city', sa.String(length=50), nullable=False),
    sa.Column('fiveteen', sa.String(length=255), nullable=False),
    sa.Column('enfiveteencity', sa.String(length=50), nullable=False),
    sa.Column('enfiveteen', sa.String(length=255), nullable=False),
    sa.Column('sixteen_city', sa.String(length=50), nullable=False),
    sa.Column('sixteen', sa.String(length=255), nullable=False),
    sa.Column('ensixteencity', sa.String(length=50), nullable=False),
    sa.Column('ensixteen', sa.String(length=255), nullable=False),
    sa.Column('seventeen_city', sa.String(length=50), nullable=False),
    sa.Column('seventeen', sa.String(length=255), nullable=False),
    sa.Column('enseventeencity', sa.String(length=50), nullable=False),
    sa.Column('enfirst', sa.String(length=255), nullable=False),
    sa.Column('eightteen_city', sa.String(length=50), nullable=False),
    sa.Column('eightteen', sa.String(length=255), nullable=False),
    sa.Column('eneightteencity', sa.String(length=50), nullable=False),
    sa.Column('eneightteen', sa.String(length=255), nullable=False),
    sa.Column('nineteen_city', sa.String(length=50), nullable=False),
    sa.Column('nineteen', sa.String(length=255), nullable=False),
    sa.Column('ennineteencity', sa.String(length=50), nullable=False),
    sa.Column('ennineteen', sa.String(length=255), nullable=False),
    sa.Column('twelve_city', sa.String(length=50), nullable=False),
    sa.Column('twelve', sa.String(length=255), nullable=False),
    sa.Column('entwelvecity', sa.String(length=50), nullable=False),
    sa.Column('entwelve', sa.String(length=255), nullable=False),
    sa.Column('twentyone_city', sa.String(length=50), nullable=False),
    sa.Column('twentyone', sa.String(length=255), nullable=False),
    sa.Column('entwentyonecity', sa.String(length=50), nullable=False),
    sa.Column('entwentyone', sa.String(length=255), nullable=False),
    sa.Column('twentytwo_city', sa.String(length=50), nullable=False),
    sa.Column('twentytwo', sa.String(length=255), nullable=False),
    sa.Column('entwentytwocity', sa.String(length=50), nullable=False),
    sa.Column('entwentytwo', sa.String(length=255), nullable=False),
    sa.Column('twentythree_city', sa.String(length=50), nullable=False),
    sa.Column('twentythree', sa.String(length=255), nullable=False),
    sa.Column('entwentythreecity', sa.String(length=50), nullable=False),
    sa.Column('entwentythree', sa.String(length=255), nullable=False),
    sa.Column('twentyfour_city', sa.String(length=50), nullable=False),
    sa.Column('twentyfour', sa.String(length=255), nullable=False),
    sa.Column('entwentyfourcity', sa.String(length=50), nullable=False),
    sa.Column('entwentyfour', sa.String(length=255), nullable=False),
    sa.Column('twentyfive_city', sa.String(length=50), nullable=False),
    sa.Column('twentyfive', sa.String(length=255), nullable=False),
    sa.Column('entwentyfivecity', sa.String(length=50), nullable=False),
    sa.Column('entwentyfive', sa.String(length=255), nullable=False),
    sa.Column('twentysix_city', sa.String(length=50), nullable=False),
    sa.Column('twentysix', sa.String(length=255), nullable=False),
    sa.Column('entwentysixcity', sa.String(length=50), nullable=False),
    sa.Column('entwentysix', sa.String(length=255), nullable=False),
    sa.Column('twentyseven_city', sa.String(length=50), nullable=False),
    sa.Column('twentyseven', sa.String(length=255), nullable=False),
    sa.Column('entwentysevencity', sa.String(length=50), nullable=False),
    sa.Column('entwentyseven', sa.String(length=255), nullable=False),
    sa.Column('twentyeight_city', sa.String(length=50), nullable=False),
    sa.Column('twentyeight', sa.String(length=255), nullable=False),
    sa.Column('entwentyeightcity', sa.String(length=50), nullable=False),
    sa.Column('entwentyeight', sa.String(length=255), nullable=False),
    sa.Column('twentynine_city', sa.String(length=50), nullable=False),
    sa.Column('twentynine', sa.String(length=255), nullable=False),
    sa.Column('entwentyninecity', sa.String(length=50), nullable=False),
    sa.Column('entwentynine', sa.String(length=255), nullable=False),
    sa.Column('thirty_city', sa.String(length=50), nullable=False),
    sa.Column('thirty', sa.String(length=255), nullable=False),
    sa.Column('enthirtycity', sa.String(length=50), nullable=False),
    sa.Column('enthirty', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['Пакет'], ['toursinfo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('packday')
    op.drop_table('toursinfo')
    op.drop_table('answer')
    op.drop_table('user')
    op.drop_table('travlio')
    op.drop_table('tourscat')
    op.drop_table('team')
    op.drop_table('seo')
    op.drop_table('question')
    # ### end Alembic commands ###