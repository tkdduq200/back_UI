from typing import Optional, List
from belong import db
from belong.models import Question
from .base_repository import BaseRepository


class QuestionRepository(BaseRepository):
    """
    Question 도메인의 DB 접근을 전담.
    Oracle-safe 페이징 방식 적용.
    """

    def get_by_id(self, question_id: int) -> Optional[Question]:
        return Question.query.get(question_id)

    def save(self, question: Question) -> Question:
        db.session.add(question)
        db.session.commit()
        return question

    def delete(self, question: Question) -> None:
        db.session.delete(question)
        db.session.commit()

    def get_list(self, page: int, per_page: int = 10) -> List[Question]:
        offset = (page - 1) * per_page

        return (
            Question.query
            .order_by(Question.create_date.desc())
            .limit(per_page)
            .offset(offset)
            .all()
        )

    def count(self) -> int:
        return Question.query.count()
