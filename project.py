class Human:

    
    def __init__(self, full_name: str, balance: float, mood: str, health: int):
        self.full_name = full_name
        self.balance = balance
        self.mood = mood
        self.health = min(100, max(0, health))

    def rest(self, hours: int):
        self.mood = "happy" if hours == 7 else "tired" if hours < 7 else "lazy"

    def consume_meals(self, meals: int):
        self.health = {1: 50, 2: 75, 3: 100}.get(meals, self.health)

    def purchase(self, count: int):
        self.balance -= count * 10


class Vehicle:

    
    def __init__(self, model: str, fuel: int, speed: int):
        self.model = model
        self.fuel = min(100, max(0, fuel))
        self.speed = min(200, max(0, speed))

    def travel(self, speed: int, km: float):
        self.speed = min(200, max(0, speed))

        while km > 0 and self.fuel > 0:
            km -= 10
            self.fuel -= 10

        self.halt(km)

    def halt(self, remaining_km: float):
        self.speed = 0
        msg = "Trip completed." if remaining_km <= 0 else f"Stopped with {remaining_km} km left (fuel empty)."
        print(msg)


class Staff(Human):
    
    
    def __init__(self, full_name: str, balance: float, mood: str, health: int,
                 emp_id: int, vehicle: Vehicle, email: str, pay: float, commute: float):
        super().__init__(full_name, balance, mood, health)
        self.emp_id = emp_id
        self.vehicle = vehicle
        self.email = email
        self.salary = max(1000, pay)
        self.commute_distance = commute

    def perform_work(self, hours: int):
        self.mood = "happy" if hours == 8 else "tired" if hours > 8 else "lazy"

    def commute(self):
        self.vehicle.travel(self.vehicle.speed, self.commute_distance)

    def refuel_vehicle(self, amount: int = 100):
        self.vehicle.fuel = min(100, self.vehicle.fuel + amount)

    def send_email(self, recipient: str, subject: str, content: str, recipient_name: str):
        with open("mail_output.txt", "w") as mail:
            mail.write(f"To: {recipient}\nSubject: {subject}\nContent: {content}\nReceiver: {recipient_name}")


class Workplace:

    
    total_staff = 0

    def __init__(self, company_name: str):
        self.company_name = company_name
        self.staff_list = []

    def list_staff(self):
        return self.staff_list

    def find_staff(self, emp_id: int):
        return next((s for s in self.staff_list if s.emp_id == emp_id), None)

    def recruit(self, staff: Staff):
        self.staff_list.append(staff)
        Workplace.total_staff += 1

    def terminate(self, emp_id: int):
        self.staff_list = [s for s in self.staff_list if s.emp_id != emp_id]
        Workplace.total_staff = max(0, Workplace.total_staff - 1)

    def reduce_salary(self, emp_id: int, amount: float):
        staff = self.find_staff(emp_id)
        if staff:
            staff.salary = max(0, staff.salary - amount)

    def increase_salary(self, emp_id: int, bonus: float):
        staff = self.find_staff(emp_id)
        if staff:
            staff.salary += bonus

    def evaluate_punctuality(self, emp_id: int, departure_time: float):
        staff = self.find_staff(emp_id)
        if staff and staff.vehicle.speed > 0:
            late = self._is_late(9, departure_time, staff.commute_distance, staff.vehicle.speed)
            if late:
                self.reduce_salary(emp_id, 10)
            else:
                self.increase_salary(emp_id, 10)

    @staticmethod
    def _is_late(target_time: float, start_time: float, km: float, speed: float):
        if speed == 0:
            return True
        arrival = start_time + (km / speed)
        return arrival > target_time

    @classmethod
    def update_staff_count(cls, new_count: int):
        cls.total_staff = max(0, new_count)
