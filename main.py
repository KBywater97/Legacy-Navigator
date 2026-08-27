from pathlib import Path
import json
from datetime import datetime


def show_menu():
    print("Welcome to the Error Code Ticketing System")
    print("1. Create a new ticket")
    print("2. View all tickets")
    print("3. Update Ticket Status")
    print("4. Search for Ticket")
    print("5. Exit")
    print()

print("Error Code Ticketing System")

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "tickets.json"

def create_ticket():
    error_message = input("Please enter your error message: ")

    ticket = {
     "id": int(datetime.now().timestamp()),
     "error": error_message,
     "severity": None,
     "status": "open",
     "created_at": datetime.now().isoformat()
}

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            tickets = json.load(file)
    else:
        tickets = []

    tickets.append(ticket)

    with open(DATA_FILE, "w") as file:
        json.dump(tickets, file, indent=4)


    print()
    print("Ticket Created Successfully!")
    print(f"Ticket ID: {ticket['id']}")
    print(f"Error: {ticket['error']}")
    print(f"Severity: {ticket['severity']}")
    print(f"Status: {ticket['status']}")

while True:
    show_menu()
    choice = input("Please select an option (1-5): ")
    if choice == "1":
         create_ticket()
    elif choice == "2":
        if DATA_FILE.exists():
            with open(DATA_FILE, "r") as file:
                tickets = json.load(file)
                if tickets:
                    print("All Tickets:")
                    for ticket in tickets:
                        print(f"Ticket ID: {ticket['id']}")
                        print(f"Error: {ticket['error']}")
                        print(f"Severity: {ticket['severity']}")
                        print(f"Status: {ticket['status']}")
                        print(f"Created At: {ticket['created_at']}")
                        print()
                else:
                   print("No tickets found.")
        else:
            print("No tickets found.")
    elif choice == "3":
        if DATA_FILE.exists():
            with open(DATA_FILE, "r") as file:
                tickets = json.load(file)

            if tickets:
                ticket_id = input("Enter the Ticket ID to update: ")

                for ticket in tickets:
                    if str(ticket["id"]) == ticket_id:
                        print("Ticket found:")
                        print(f"Ticket ID: {ticket['id']}")
                        print(f"Error: {ticket['error']}")
                        print(f"Severity: {ticket['severity']}")
                        print(f"Status: {ticket['status']}")
                        print(f"Created At: {ticket['created_at']}")

                        new_status = input("Enter the new status (open/closed): ")
                        ticket["status"] = new_status

                        with open(DATA_FILE, "w") as file:
                            json.dump(tickets, file, indent=4)

                        print("Ticket status updated successfully!")
                        break

                else:
                    print("Ticket not found.")

            else:
                print("No tickets found.")
        else:
            print("No tickets found.")
    elif choice == "4":
       search_term = input("Enter the error message to search for: ")
       if DATA_FILE.exists():
           with open(DATA_FILE, "r") as file:
               tickets = json.load(file)
               found_tickets = [ticket for ticket in tickets if search_term.lower() in ticket['error'].lower()]
               if found_tickets:
                   print("Search Results:")
                   for ticket in found_tickets:
                       print(f"Ticket ID: {ticket['id']}")
                       print(f"Error: {ticket['error']}")
                       print(f"Severity: {ticket['severity']}")
                       print(f"Status: {ticket['status']}")
                       print(f"Created At: {ticket['created_at']}")
                       print()
               else:
                   print("No tickets found.")
       else:
            print("No tickets found.")
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
         print("Invalid option. Please select a valid option (1-5).")
    