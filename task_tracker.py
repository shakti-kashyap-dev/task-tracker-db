import sqlite3

def init_db():
    # Connects to database file (creates it if it doesn't exist)
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    # Create tasks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()
    print(f"✔️ Task '{title}' added successfully!")

def view_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("📭 No tasks found.")
        return
        
    print("\n--- YOUR TASK LIST ---")
    for row in rows:
        print(f"[{row[0]}] {row[1]} - Status: {row[2]}")
    print("----------------------\n")

def main():
    init_db()
    while True:
        print("1. Add Task  |  2. View Tasks  |  3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            if title.strip():
                add_task(title)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == '__main__':
    main()
