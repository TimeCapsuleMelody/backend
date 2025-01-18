from sqlalchemy import TIMESTAMP, Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Memory(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    msuicTitle = Column(String(255), nullable=False)

    created_at = Column(Date, nullable=False)

    friend = Column(String(255), nullable=False)
    diary = Column(String(255), nullable=False)
    feeling = Column(Integer, nullable=False)
    keywords = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    auth_id = Column(String(255), nullable=False)
    auth_type = Column(String(20), nullable=False, default="FIREBASE")
    email = Column(String(100), nullable=False)
    user_name = Column(String(45), nullable=False)
    github_id = Column(String(100), nullable=True)
    instagram_id = Column(String(100), nullable=True)
    is_active = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False,
                        default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.current_timestamp(
    ), onupdate=func.current_timestamp())
    is_deleted = Column(Boolean, nullable=False, default=False)
    password = Column(Text, nullable=False)
    # Relationships
    admin = relationship("Admin", back_populates="user")
    requested_books = relationship("RequestedBook", back_populates="user")
    loans = relationship("Loan", back_populates="user")
    book_reviews = relationship("BookReview", back_populates="user")
    food_orders = relationship("FoodOrder", back_populates="user")


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    admin_status = Column(Boolean, nullable=False)
    expiration_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False,
                        default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.current_timestamp(
    ), onupdate=func.current_timestamp())
    is_deleted = Column(Boolean, nullable=False, default=False)

    # Relationship
    user = relationship("User", back_populates="admin")


class RequestedBook(Base):
    __tablename__ = "requested_book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    book_title = Column(String(255), nullable=False)
    publication_year = Column(Integer)
    reject_reason = Column(String(20))
    request_link = Column(String(255), nullable=False)
    reason = Column(Text, nullable=False)
    request_date = Column(Date, nullable=False)
    processing_status = Column(Integer, nullable=False, default=0)
    processed_date = Column(Date)
    created_at = Column(TIMESTAMP, nullable=False,
                        default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.current_timestamp(
    ), onupdate=func.current_timestamp())

    is_deleted = Column(Boolean, nullable=False, default=False)

    # Relationship
    user = relationship("User", back_populates="requested_books")


class Loan(Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    loan_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    extend_status = Column(Boolean, nullable=False, default=False)
    return_status = Column(Boolean, nullable=False, default=False)
    return_date = Column(Date)
    overdue_days = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, nullable=False,
                        default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.current_timestamp(
    ), onupdate=func.current_timestamp())
    is_deleted = Column(Boolean, nullable=False, default=False)

    # Relationships
    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")


class BookReview(Base):
    __tablename__ = "book_review"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    review_content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False,
                        default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.current_timestamp(
    ), onupdate=func.current_timestamp())
    is_deleted = Column(Boolean, nullable=False, default=False)
    # Relationships
    user = relationship("User", back_populates="book_reviews")
    book = relationship("Book", back_populates="book_reviews")


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_title = Column(String(255), nullable=False)
    code = Column(String(20), nullable=False)
    category_name = Column(String(50), nullable=False)
    subtitle = Column(String(255))
    author = Column(String(100), nullable=False)
    publisher = Column(String(45), nullable=False)
    publication_year = Column(Integer, nullable=False)
    image_url = Column(String(255))
    version = Column(String(45))
    major = Column(Boolean, default=False)
    language = Column(String(20), nullable=False, default="KOREAN")
    book_status = Column(Boolean, nullable=False, default=True)
    donor_name = Column(String(20))
    created_at = Column(TIMESTAMP, nullable=False,
                        default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.current_timestamp(
    ), onupdate=func.current_timestamp())
    is_deleted = Column(Boolean, nullable=False, default=False)

    # Relationships
    book_reviews = relationship("BookReview", back_populates="book")
    loans = relationship("Loan", back_populates="book",
                         order_by="Loan.updated_at.desc()")  # order_by 적용


class Notice(Base):
    __tablename__ = "notice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    admin_id = Column(Integer, ForeignKey("admin.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False,
                        default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=func.current_timestamp(
    ), onupdate=func.current_timestamp())
    is_deleted = Column(Boolean, nullable=False, default=False)
    # Relationships
    admin = relationship("Admin", foreign_keys=[admin_id])
    user = relationship("User", foreign_keys=[user_id])


class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    extend_days = Column(TINYINT(unsigned=True), nullable=False)
    extend_max_count = Column(TINYINT(unsigned=True), nullable=False)
    loan_days = Column(TINYINT(unsigned=True), nullable=False)
    loan_max_book = Column(TINYINT(unsigned=True), nullable=False)
    request_max_count = Column(TINYINT(unsigned=True), nullable=False)
    request_max_price = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False,
                        server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)


# 여기서부터는 예시로 작성한 코드입니다.


class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String(255), nullable=False)
    food_type = Column(String(20), nullable=False)
    food_price = Column(Integer, nullable=False)
    food_description = Column(Text, nullable=False)
    food_image_url = Column(String(255))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False,
                        server_default=func.now(), onupdate=func.now())

    orders = relationship("FoodOrder", back_populates="food")


class FoodOrder(Base):
    __tablename__ = "food_order"

    id = Column(Integer, primary_key=True, autoincrement=True)
    food_id = Column(Integer, ForeignKey("food.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)

    user = relationship("User", back_populates="food_orders")
    food = relationship("Food", back_populates="orders")
