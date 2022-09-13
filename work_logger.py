"""Main module for work logger"""

import datetime

class JobItem:

    num_ids = 0

    def __init__(self, client, job, work_date, work_note):
        self.client = client
        self.job = job
        self.work_date = work_date
        self.work_note = work_note
        self.job_id = str(self.num_ids)

        self.start_time = None
        self.end_time = None
        self.item_duration = None

        #self.duration_hours = None
        self.duration_mins = None

        self.set_start_time()

        self.num_ids += 1

    def set_start_time(self):
        self.start_time = datetime.datetime.utcnow()

    def set_end_time_and_duration(self):
        self.end_time = datetime.datetime.utcnow()
        self.item_duration = self.end_time - self.start_time

        #self.duration_hours = self.item_duration.hours
        one_min = datetime.timedelta(minutes=1)
        self.duration_mins = self.item_duration / one_min

    def __repr__(self):
        return f"""{str(self.job_id)} | {self.client} | {self.job} | {str(self.work_date)} | \n
                   {self.work_note} | \n
                   {str(self.start_time)} | {str(self.end_time)} | {str(self.item_duration)} | \n
                Dur_mins: {str(self.duration_mins)}"""


class WorkContainer:
    def __init__(self):

        self.work_items = []

        self.current_work_item = None

    def start_new_item(self, client_name, job_name, work_note):
        work_date = datetime.datetime.utcnow().date()
        self.current_work_item = JobItem(client_name, job_name, work_date, work_note)

    def end_current_work(self):
        #Create finish time
        self.current_work_item.set_end_time_and_duration()

        #Move to container
        self.work_items.append(self.current_work_item)

        #Reset holders
        self.current_work_item = None


#Temporary CLI

def run_main_cli_loop():
    current_work = WorkContainer()

    input_text = "Run command:\n\tOptions are STARTNEW:client_name:job_name:work_note\n" +\
                 "\tOr FINISHCURRENT\n"

    while True:

        user_in = input(input_text)

        if "STARTNEW" in user_in:
            print("Starting new job...")

            arguments = user_in.split(':')
            client_name = arguments[1]
            job_name = arguments[2]
            work_note = arguments[3]

            current_work.start_new_item(client_name, job_name, work_note)

        elif "FINISHCURRENT" in user_in:
            current_work.end_current_work()
            print(current_work.work_items)

        else:
            print("Command unrecognized.  Try again!")


if __name__ == "__main__":
    run_main_cli_loop()
