from storage.database import Database


class TradeRepository:

    @staticmethod
    def save(trade):

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            """

            INSERT INTO trades (

                strategy_name,

                instrument,

                quantity,

                signal,

                entry_price,

                exit_price,

                stop_loss,

                target_price,

                pnl_points,

                pnl_amount,

                result,

                entry_time,

                exit_time

            )

            VALUES (

                ?,?,?,?,?,?,?,?,?,?,?,?,?

            )

            """,

            (

                trade["strategy_name"],

                trade["instrument"],

                trade["quantity"],

                trade["signal"],

                trade["entry_price"],

                trade["exit_price"],

                trade["stop_loss"],

                trade["target_price"],

                trade["pnl_points"],

                trade["pnl_amount"],

                trade["result"],

                str(
                    trade["entry_time"]
                ),

                str(
                    trade["exit_time"]
                )

            )

        )

        conn.commit()

        conn.close()

    @staticmethod
    def get_all():

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            "SELECT * FROM trades"

        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def delete_all():

        conn = Database.connect()

        cursor = conn.cursor()

        cursor.execute(

            "DELETE FROM trades"

        )

        conn.commit()

        conn.close()