import pandas as pd
import random
import string

class KnowledgeEngine:
    def __init__(self, knowledge_path):
        self.knowledge_df = pd.read_csv(knowledge_path)

    def generate_ticket_id(self):
        return "TCKT-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def find_solution(self, user_query):
        user_query = user_query.lower()

        for index, row in self.knowledge_df.iterrows():
            if any(keyword in user_query for keyword in row['keywords'].lower().split(',')):
                return row['solution'], row['category']

        return "No exact match found. Ticket will be forwarded to support team.", "General"

    def create_ticket(self, user_query):
        solution, category = self.find_solution(user_query)
        ticket_id = self.generate_ticket_id()

        ticket_record = f"{ticket_id} | {category} | {user_query}\n"

        with open("tickets.txt", "a") as file:
            file.write(ticket_record)

        return ticket_id, solution, category
