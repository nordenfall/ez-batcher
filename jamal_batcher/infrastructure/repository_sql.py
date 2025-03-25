from typing import List
import psycopg2
from ..domain.image import Image
from ..domain.repository import AbstractImageRepository


class SQLOperationRepository(AbstractImageRepository):
    def __init__(self, db_url:str):
        self.conn = psycopg2.connect(db_url)
        self.cur = self.conn.cursor()

    def get_unused_images(self, batch_size:int, stone_type:str):
        count_query = f"SELECT COUNT (*) FROM {stone_type} WHERE used = FALSE"
        self.cur.execute(count_query)
        if self.cur.fetchall()[0][0] < batch_size:
            print("Недостаточно объектов для обучения, сброс репозитория . . .")
            reset_query = f"UPDATE {stone_type} SET used = FALSE WHERE used = TRUE"
            self.cur.execute(reset_query)
            self.conn.commit()

        query = f"SELECT id, used FROM {stone_type} WHERE used = FALSE LIMIT %s"
        self.cur.execute(query, (batch_size,))
        return [Image(id=r[0],stone_type=stone_type) for r in self.cur.fetchall()]

    def mark_as_used(self, images:List[Image]):
        stone_type = images[0].stone_type
        query = f"UPDATE {stone_type} SET used = TRUE WHERE id = ANY(%s)"
        self.cur.execute(query, ([img.id for img in images],))
        self.conn.commit()

    def close_connection(self):
        self.cur.close()
        self.conn.close()



