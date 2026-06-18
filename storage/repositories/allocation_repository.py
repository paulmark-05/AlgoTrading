from storage.database import Database

class AllocationRepository:

    @staticmethod
    def save(

        strategy_name,

        allocated_lots,

        capital_per_lot,

        enabled=1

    ):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            """

            INSERT INTO strategy_allocations (

                strategy_name,

                allocated_lots,

                capital_per_lot,

                enabled

            )

            VALUES (

                ?,?,?,?

            )

            """,

            (

                strategy_name,

                allocated_lots,

                capital_per_lot,

                enabled

            )

        )

        conn.commit()

        conn.close()

    @staticmethod
    def get_all():

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            """

            SELECT *

            FROM strategy_allocations

            """

        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def delete_all():

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            """

            DELETE FROM strategy_allocations

            """

        )

        conn.commit()

        conn.close()

