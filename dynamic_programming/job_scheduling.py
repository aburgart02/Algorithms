def job_scheduling(task_times, size):
    tasks_numbers = len(task_times)
    dp = [-1] * (size + 1)
    dp[size] = tasks_numbers
    for task_number in range(tasks_numbers - 1, -1, -1):
        for i in range(task_times[task_number], size + 1):
            if dp[i] > task_number and dp[i - task_times[task_number]] == -1:
                dp[i - task_times[task_number]] = task_number
    free = 0
    while dp[free] == -1:
        free += 1
    tasks = []
    i = dp[free]
    while i != tasks_numbers:
        tasks.append(i)
        free += task_times[i]
        i = dp[free]
    return tasks


task_times = [4, 2, 3]
size = 5
tasks = job_scheduling(task_times, size)
downtime = size - sum([task_times[task] for task in tasks])
runtime_array = [task for task in tasks for _ in range(task_times[task])] + [0] * downtime
print('Downtime:', downtime)
print('Task numbers in the schedule:', tasks)
print('Runtime array:', runtime_array)