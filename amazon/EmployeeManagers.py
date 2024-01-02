from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Employee:
    id: int
    manager_id: Optional[int]
    salary: int


class Solution:
    def __init__(self, employees: List[Employee]) -> List[str]:
        self.dict = {}
        self.adj = {}
        self.ceo = None
        for employee in employees:
            self.adj[employee.manager_id].append(employee.id)
            self.dict[employee.id] = employee
            if employee.manager_id is None:
                self.ceo = employee


    def get_management_hierarchy(self, employee: Employee) -> List[str]:
        result = []

        def dfs(node):
            if node is None:
                return
            
            result.append(node.id)
            
            if node.manager_id:            
                dfs(self.dict[node.manager_id])

        dfs(employee)
        return result


    def get_highest_group_salary(self):
        # implement



employee1 = Employee(1, 2, 500)
employee2 = Employee(2, 3, 700)
employee3 = Employee(3, None, 900)

solution = Solution([employee1, employee2, employee3])
solution.get_management_hierarchy(employee1)