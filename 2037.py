class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # max_index = max(max(seats), max(students)) + 1
        # seat_count = [0] * max_index
        # student_count = [0] * max_index
        
        # for seat in seats:
        #     seat_count[seat] += 1

        # for student in students:
        #     student_count[student] += 1
        # res = 0
        # i, j = 0, 0
        # remain = len(students)
        # while remain:
        #     if seat_count[i] == 0:
        #         i += 1

        #     if student_count[j] == 0:
        #         j += 1

        #     if seat_count[i] and student_count[j]:
        #         res += abs(i - j)
        #         seat_count[i] -= 1
        #         student_count[j] -= 1
        #         remain -= 1

        # return res
###################Second Approach with optimal time complexity#######################
        seats.sort()
        students.sort()

        res = 0
        for i in range(len(students)):
            res += abs(seats[i] - students[i])

        return res
