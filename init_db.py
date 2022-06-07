"""
Initialize the database before running the API
"""

from db import Connection


def main() -> int:
    conn = Connection()

    conn.create_quotes_table()

    quotes = [
        "Be the change that you wish to see in the world.",
        "We accept the love we think we deserve.",
        "I have not failed. I've just found 10,000 ways that won't work.",
        "It is never too late to be what you might have been.",
        "Everything you can imagine is real.",
        "Life isn't about finding yourself. Life is about creating yourself.",
        "To the well-organized mind, death is but the next great adventure.",
        "Do what you can, with what you have, where you are.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    ]

    for quote in quotes:
        conn.insert_quote(quote)

    print("Successfully initialized database.")

    return 0


if __name__ == "__main__":
    main()
