from storage.database import Database


class PositionRepository:

    @staticmethod
    def save(position):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO positions (
                strategy_name,
                instrument,
                quantity,
                signal,
                entry_price,
                stop_loss,
                target_price,
                entry_time,
                status
            )
            VALUES (
                ?,?,?,?,?,?,?,?,?
            )
            """,
            (
                position["strategy_name"],
                position["instrument"],
                position["quantity"],
                position["signal"],
                position["entry_price"],
                position["stop_loss"],
                position["target_price"],
                str(position["entry_time"]),
                position["status"]
            )
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_open_positions():

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM positions
            WHERE status='OPEN'
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def close_position(position_id):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE positions
            SET status='CLOSED'
            WHERE id=?
            """,
            (position_id,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def delete_all():

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM positions"
        )

        conn.commit()
        conn.close()