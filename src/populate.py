from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Author, Book
engine = create_engine('sqlite:///source_library.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

author1 = Author(name='Пушкин')
author2 = Author(name='Есенин')

book1 = Book(title='Евгений Онегин', author=author1)
book2 = Book(title='Полтава', author=author2)
book3 = Book(title='Черный человек', author=author2)
session.commit()