
members_id={
    "m1":{
        "name":"raja",
        "role":"coding",
        "skill_set":"python",
        "hourly_rate":"6%",
        "assigned_task": []
        }
    } 


project_id={
    "p1":{
        "name":"project",
        "start_date":"30-05",
        "end_date":"30-06",
        "priority":1,
        "status":"active"
            
        }
    }

tasks={
    "t1":{
        "title":"task-1",
        "description":"complete task",
        "estimated_hours":10, #hours
        "remaining_hours":10, #hours
        "project_id":"p1",
        "assigned_to": None
        }
}


def log_time(member_id, task_id, hours_worked, date=0):
    if member_id not in members_id:
        return "'MEMBER ID' is not registered."
    if task_id not in tasks:
        return "'TASK ID' is not registered. "

    tasks[task_id]["remaining_hours"]-=hours_worked
    print(1)  

log_time('m1',"t1",3)
print(tasks["t1"]["remaining_hours"])




def update_task_progress(task_id):
    estimated_time  = tasks[task_id]["estimated_hours"]
    remaining_time= tasks[task_id]["remaining_hours"]
    if task_id in  tasks:
        completed_time = (remaining_time/estimated_time)*100
        completion_percentage = 100-completed_time
        print(completion_percentage)
    
update_task_progress('t1')