"""
db.py — All database logic for Salary Quest.

WHY A SEPARATE FILE?
Keeping every SQL statement in one place means:
  1. app.py (the UI) never has to know HOW data is stored — it just calls
     functions like get_user_by_mobile() or add_expense().
  2. If you ever move from SQLite to a bigger database (Postgres, MySQL),
     you only rewrite this one file — app.py stays untouched.

DATABASE ENGINE: SQLite
  - SQLite is a single file on disk (salary_quest.db). No server to install,
    no username/password — perfect for a single-machine app or a small
    number of users. Python has it built in (the `sqlite3` module),
    so nothing extra needs installing.
  - If you later deploy this online and need MANY concurrent users, you'd
    swap SQLite for Postgres — but the table design below stays the same.

TABLES
  users     -> one row per person, identified by their mobile number
  expenses  -> one row per logged expense, linked to a user via user_id
               (this is called a "foreign key" relationship — expenses
               "belong to" a user)
"""

import sqlite3
from datetime import datetime

DB_PATH = "salary_quest.db"

# Every column in `users` that the app is allowed to read/write in bulk.
# Keeping this list in one place avoids typos scattered across the file.
USER_FIELDS = [
    "name", "salary", "rent", "groceries_fix", "transport_fix", "utilities",
    "phone", "grooming", "other_fixed", "gold_inv", "rd_inv", "mutual_fund",
    "emergency_add", "savings_goal_pct", "emergency_months", "current_ef_saved",
]


def get_connection():
    """Open a connection to the .db file. row_factory lets us read rows
    like a dictionary (row['salary']) instead of by position (row[3])."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the tables if they don't already exist. Safe to call every
    time the app starts — CREATE TABLE IF NOT EXISTS does nothing if the
    table is already there."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id                 INTEGER PRIMARY KEY AUTOINCREMENT,
            mobile             TEXT UNIQUE NOT NULL,   -- login key, must be unique
            name               TEXT,
            salary             REAL DEFAULT 0,
            rent               REAL DEFAULT 0,
            groceries_fix      REAL DEFAULT 0,
            transport_fix      REAL DEFAULT 0,
            utilities          REAL DEFAULT 0,
            phone              REAL DEFAULT 0,
            grooming           REAL DEFAULT 0,
            other_fixed        REAL DEFAULT 0,
            gold_inv           REAL DEFAULT 0,
            rd_inv             REAL DEFAULT 0,
            mutual_fund        REAL DEFAULT 0,
            emergency_add      REAL DEFAULT 0,
            savings_goal_pct   REAL DEFAULT 20,
            emergency_months   INTEGER DEFAULT 6,
            current_ef_saved   REAL DEFAULT 0,
            created_at         TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,          -- links back to users.id
            date        TEXT,
            place       TEXT,
            amount      REAL,
            payment     TEXT,
            category    TEXT,
            type        TEXT,                      -- 'Need' or 'Want'
            note        TEXT,
            created_at  TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    conn.commit()
    conn.close()


# ───────────────────────── USERS ─────────────────────────

def validate_mobile(mobile: str) -> bool:
    """Basic Indian mobile number check: exactly 10 digits, starting 6-9."""
    mobile = mobile.strip()
    return mobile.isdigit() and len(mobile) == 10 and mobile[0] in "6789"


def get_user_by_mobile(mobile: str):
    """Returns a dict of the user's saved data, or None if this mobile
    number has never registered before."""
    conn = get_connection()
    row = conn.execute("SELECT * FROM users WHERE mobile = ?", (mobile,)).fetchone()
    conn.close()
    return dict(row) if row else None


def create_user(mobile: str, data: dict) -> int:
    """Insert a brand-new user row. `data` is a dict of {column: value}
    covering the USER_FIELDS. Returns the new user's id."""
    conn = get_connection()
    columns = ["mobile"] + list(data.keys()) + ["created_at"]
    values = [mobile] + list(data.values()) + [datetime.now().isoformat()]
    placeholders = ",".join(["?"] * len(values))
    conn.execute(
        f"INSERT INTO users ({','.join(columns)}) VALUES ({placeholders})",
        values,
    )
    conn.commit()
    new_id = conn.execute("SELECT id FROM users WHERE mobile = ?", (mobile,)).fetchone()["id"]
    conn.close()
    return new_id


def update_user(user_id: int, data: dict):
    """Update an existing user's row — this is what makes sidebar edits
    'save to the database' instead of disappearing when you close the tab."""
    if not data:
        return
    conn = get_connection()
    set_clause = ",".join([f"{key}=?" for key in data.keys()])
    values = list(data.values()) + [user_id]
    conn.execute(f"UPDATE users SET {set_clause} WHERE id = ?", values)
    conn.commit()
    conn.close()


# ─────────────────────── EXPENSES ────────────────────────

def add_expense(user_id: int, exp: dict):
    conn = get_connection()
    conn.execute(
        """INSERT INTO expenses (user_id, date, place, amount, payment, category, type, note, created_at)
           VALUES (?,?,?,?,?,?,?,?,?)""",
        (
            user_id, str(exp["Date"]), exp["Place"], exp["Amount"],
            exp["Payment"], exp["Category"], exp["Type"], exp.get("Note", ""),
            datetime.now().isoformat(),
        ),
    )
    conn.commit()
    conn.close()


def get_expenses(user_id: int):
    """Returns every expense row for this user, most recent first."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM expenses WHERE user_id = ? ORDER BY date DESC, id DESC",
        (user_id,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def clear_expenses(user_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM expenses WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()


def delete_expense(expense_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()