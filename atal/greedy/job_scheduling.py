# # 1: Sort decrescente a partir do Profit.
# # 2: Olhar o Deadline de cima para baixo.
# # 3: Se houver tempo para um Job de menor Profit ser executado, adicionar à lista. 
# #    Se não, adicionar o de maior Profit.
# # 4: Checar opções inviáveis por Deadline e remover.
# # 5: Repetir a partir do passo 2.

from time import time
start = time()
class Job:
    def __init__(self, id, profit, deadline):
        self.id = id
        self.profit = profit
        self.deadline = deadline
        

def job_scheduling(jobs):
    jobs.sort(key=lambda job: job.profit, reverse=True)
    
    max_deadline = max(job.deadline for job in jobs)
    schedule = [None] * max_deadline
    total_profit = 0
    
    loc = 1
    while loc <= max_deadline:
        job = jobs[0]
        
        j = 1
        while j < len(jobs):
            if job.deadline > jobs[j].deadline and jobs[j].deadline == loc:
                new_job = jobs.pop(j)
                schedule[loc-1] = new_job.id
                total_profit += new_job.profit
                loc += 1
            elif jobs[j].deadline < loc:
                jobs.pop(j)
            else:
                j += 1

        print(list(map(lambda job: job.id, jobs)))
        if job.deadline == loc:
            job = jobs.pop(0)
            schedule[loc-1] = job.id
            total_profit += job.profit
            loc += 1
        elif job.deadline < loc:
            jobs.pop(0)
             
    
    schedule = [job for job in schedule if job is not None]
    return schedule, total_profit


jobs = [
    Job("A", 100, 2),
    Job("B", 120, 1),
    Job("C", 60, 3),
    Job("D", 150, 2),
    Job("E", 90, 1),
    Job("F", 70, 3),
]

    # Job("D", 150, 2),
    # Job("B", 120, 1),
    # Job("A", 100, 2),
    # Job("E", 90, 1),
    # Job("F", 70, 3),
    # Job("C", 60, 3),

# Run job scheduling
scheduled_jobs, total_profit = job_scheduling(jobs)

# Output results
print("Scheduled Jobs Order:", " -> ".join(scheduled_jobs))
print("Total Profit:", total_profit)
print(f"Time: {time()-start}")


# Job Scheduling Problem (Greedy Approach)
# from time import time
# start = time()
# class Job:
#     def __init__(self, id, profit, deadline):
#         self.id = id
#         self.profit = profit
#         self.deadline = deadline

# def job_scheduling(jobs):
#     # Step 1: Sort jobs in descending order of profit
#     jobs.sort(key=lambda job: job.profit, reverse=True)
    
#     # Step 2: Find the maximum deadline to determine scheduling slots
#     max_deadline = max(job.deadline for job in jobs)
#     schedule = [None] * max_deadline  # Time slots (None = free)
    
#     total_profit = 0

#     # Step 3: Assign jobs greedily
#     for job in jobs:
#         # Find the latest available slot before or at the job's deadline
#         for i in range(job.deadline - 1, -1, -1):
#             if schedule[i] is None:
#                 schedule[i] = job.id  # Assign job to slot
#                 total_profit += job.profit
#                 break  # Move to the next job
    
#     # Step 4: Print results
#     scheduled_jobs = [job for job in schedule if job is not None]
#     return scheduled_jobs, total_profit

# # Example job list (Job ID, Profit, Deadline)
# jobs = [
#     Job("A", 100, 2),
#     Job("B", 120, 1),
#     Job("C", 60, 3),
#     Job("D", 150, 2),
#     Job("E", 90, 1),
#     Job("F", 70, 3),
# ]

# # Run job scheduling
# scheduled_jobs, total_profit = job_scheduling(jobs)

# # Output results
# print("Scheduled Jobs Order:", " -> ".join(scheduled_jobs))
# print("Total Profit:", total_profit)
# print(f"Time: {time()-start}")
