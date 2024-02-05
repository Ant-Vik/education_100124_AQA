# Нарушение принципа SRP

class Employee:
    def calculate_salary(self):
        # Расчет зарплаты
        pass
    def generate_report(self):
        # Отправка отчета
        pass



# Соблюдение принципа SRP

class Staff:
    def calculate_salary(self):
        # Расчет зарплаты
        pass

class Reporting:
    def generate_report(self):
        # Отправка отчета
        pass

class SalaryCalc(Staff):
    def calculate_salary(self):
        # Расчет зарплаты
        return "Общая сумма"

class ReportGenerate(Reporting):
    def generate_report(self):
        # Отправка отчета
        return "Отчет"

# Вывод: Один клас должен содержать только относящиеся к нему функции

