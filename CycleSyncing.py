from datetime import datetime, timedelta

class MenstrualCycle:
    PHASES= {
        "Luteal Phase": {
            "advice": "The luteal phase is like the fall of our bodies. It's time to take care of yourself and prepare for winter, AKA your period. Organizing, deep cleaning, and completing the tasks you've been procrastinating with will be beneficial for this time."
        },
        "Menstrual Phase": {
            "advice": "You may not feel like doing much of anything right now and that's okay! The menstrual phase is a great time to retreat inward and allow yourself to rest."
        },
        "Ovulatory Phase": {
            "advice": "You're possibly feeling the most energized and extroverted at this time. Take advantage of this to plan dates and meetings and collaborate with others!"
        },
        "Follicular Phase": {
            "advice": "You may be feeling more inspired recently! This is a great time to set intentions and plan for new ventures, clarify your visions, and engage with your curiosity."
        },
    }
    def __init__(self, lp, cycle_length):
        self.lp= lp
        self.cycle_length= cycle_length

    def cycle_calculator(self):
        today= datetime.today().date()
        start= self.lp
        end= self.lp + timedelta(days=5)
        cycle_end= self.lp + timedelta(days=self.cycle_length)

        if today< start:
            return "Luteal Phase"
        elif start <= today <= end:
            return "Menstrual Phase"
        elif end< today< cycle_end - timedelta(days=14):
            return "Ovulatory Phase"
        else: 
            return "Follicular Phase"

    def return_advice(self):
        phase= self.cycle_calculator()
        return self.PHASES[phase]["advice"]


def main():
    try:
        print("This calculator determines what phase of the menstraul cycle you're in and offers tailored advice to optimize your lifestyle accordingly.")
        lp= input("What was the first day of your last period? (dd/mm/yyyy): ")
        cycle_length= int(input("What was the length of your last menstrual cycle in days? "))

        lp= datetime.strptime(lp, "%d/%m/%Y").date()
        cycle= MenstrualCycle(lp, cycle_length)

        current_phase= cycle.cycle_calculator()
        advice= cycle.return_advice()
        
        print(f"You're currently in the: {current_phase}")
        print(f"Here's some advice for this phase :) {advice}")
    except ValueError:
        print("Please make sure your last period is in dd-mm-yyyy format and your cycle length is a number.")

if __name__ == "__main__":
    main()



