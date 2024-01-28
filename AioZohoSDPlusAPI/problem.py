from .sdp_aio_api_core import SDP


class Problem(SDP):

    async def get_all_problems_data(self, input_data=None):
        '''
        Эта операция используется для получения подробной информации обо всех проблемах.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem.html#get-list-problem
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": "10",
                                        "get_total_count": "true",
                                        "sort_field": "id",
                                        "sort_order": "asc",
                                        "search_criteria": {"field": "status.name",
                                                            "condition": "is",
                                                            "value": "Open"}
                                       }}
        return await self.get_data(f'problems', input_data)
    
    async def get_problem_data(self, problem_id):
        '''
        Эта операция используется для получения сведений о проблеме с данным problem_id
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem.html#get-problem
        '''
        return await self.get_data(f'problems/{problem_id}')
    
    async def add_problem(self, input_data):
        '''
        Эта операция используется для добавления новой проблемы.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem.html#add-problem
        '''
        return await self.post_data(f'problems', input_data)
    
    async def update_problem(self, problem_id, input_data):
        '''
        Эта операция используется для обновления Проблемы с использованием уникального problem_id.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem.html#edit-problem
        '''
        return await self.put_data(f'problems/{problem_id}', input_data)

    async def delete_problem(self, problem_id):
        '''
        Эта операция используется для удаления Проблемы с использованием уникального problem_id.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem.html#delete-problem
        '''
        return await self.delete_data(f'problems/{problem_id}')
    
    async def pickup_problem(self, problem_id):
        '''
        Эта операция позволяет взять проблему на ваше имя как технического специалиста (В данном случае Administrator).
        '''
        return await self.put_data(f'problems/{problem_id}/pickup')
    
    async def close_problem(self, problem_id):
        '''
        Эта операция позволяет закрыть проблему, используя уникальный problem_id.
        '''
        return await self.put_data(f'problems/{problem_id}/close')
    
    async def assign_problem(self, problem_id):
        '''
        Эта операция позволяет назначить группу и технического специалиста для решения проблемы с помощью уникального problem_id.
        '''
        return await self.put_data(f'problems/{problem_id}/assign')
    
    async def get_root_cause_for_problem(self, problem_id):
        '''
        Эта операция используется для получения основной причины problem_id.
        '''
        return await self.get_data(f'problems/{problem_id}/root_cause')
    
    async def add_root_cause_for_problem(self, problem_id, input_data):
        '''
        Эта операция позволяет добавить основную причину этой проблемы.
        см. input_data в доках к api
        '''
        return await self.post_data(f'problems/{problem_id}/root_cause', input_data)
    
    async def update_root_cause_for_problem(self, problem_id, input_data):
        '''
        Эта операция позволяет добавить основную причину этой проблемы.
        см. input_data в доках к api
        '''
        return await self.put_data(f'problems/{problem_id}/root_cause', input_data)
    
    async def get_impact_details_for_problem(self, problem_id):
        '''
        Эта операция используется для получения сведений о влиянии данного problem_id.
        '''
        return await self.get_data(f'problems/{problem_id}/impact_details')
    
    async def add_impact_details_for_problem(self, problem_id, input_data):
        '''
        Эта операция позволяет добавить сведения о влиянии этой проблемы.
        см. input_data в доках к api
        '''
        return await self.post_data(f'problems/{problem_id}/impact_details', input_data)
    
    async def update_impact_details_for_problem(self, problem_id, impact_details_id, input_data):
        '''
        Эта операция позволяет редактировать сведения о влиянии этой проблемы.
        см. input_data в доках к api
        '''
        return await self.put_data(f'problems/{problem_id}/impact_details/{impact_details_id}', input_data)
    
    async def get_symptoms_for_problem(self, problem_id):
        '''
        Эта операция используется для получения симптомов данного problem_id.
        '''
        return await self.get_data(f'problems/{problem_id}/symptoms')
    
    async def add_symptoms_for_problem(self, problem_id, input_data):
        '''
        Эта операция позволяет добавить симптомы данной проблемы.
        см. input_data в доках к api
        '''
        return await self.post_data(f'problems/{problem_id}/symptoms', input_data)
    
    async def update_symptoms_for_problem(self, problem_id, symptoms_id, input_data):
        '''
        Эта операция позволяет редактировать симптомы этой проблемы.
        см. input_data в доках к api
        '''
        return await self.put_data(f'problems/{problem_id}/symptoms/{symptoms_id}', input_data)
    
    # problem note
    async def get_all_notes_for_problem_data(self, problem_id):
        '''
        Эта операция поможет вам получить все сведения о проблеме.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_note.html#get-list-problem-note
        '''
        return await self.get_data(f'problems/{problem_id}/notes')
    
    async def get_note_for_problem_data(self, problem_id, note_id):
        '''
        Эта операция поможет вам получить уведомление о проблеме.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_note.html#get-problem-note
        '''
        return await self.get_data(f'problems/{problem_id}/notes/{note_id}')
    
    async def add_note_for_problem(self, problem_id, input_data):
        '''
        Эта операция поможет вам добавить примечание к проблеме.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_note.html#add-problem-note
        '''
        return await self.post_data(f'problems/{problem_id}/notes', input_data)
    
    async def add_note_attachment_for_problem(self, problem_id, notes_id, file_path):
        '''
        Эта операция позволяет добавлять вложения к заметке с problem_id.
        '''
        return await self.send_file(file_path, f'problems/{problem_id}/notes/{notes_id}/upload', http_method='put')
    
    async def update_note_for_problem(self, problem_id, note_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить примечание к проблеме.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_note.html#edit-problem-note
        '''
        return await self.put_data(f'problems/{problem_id}/notes/{note_id}', input_data)
    
    async def delete_note_for_problem(self, problem_id, note_id):
        '''
        Эта операция поможет вам удалить примечание в проблеме.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_note.html#delete-problem-note
        '''
        return await self.delete_data(f'problems/{problem_id}/notes/{note_id}')
    
    #problem task
    async def get_all_tasks_for_problem_data(self, problem_id):
        '''
        Эта операция помогает получить все проблемные задачи.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task.html#get-list-problem-task
        '''
        return await self.get_data(f'problems/{problem_id}/tasks')

    async def get_task_for_problem_data(self, problem_id, task_id):
        '''
        Эта операция поможет вам получить проблемное задание.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task.html#get-problem-task
        '''
        return await self.get_data(f'problem/{problem_id}/tasks/{task_id}')
    
    async def add_task_for_problem(self, problem_id, input_data):
        '''
        Эта операция поможет вам добавить задачу к проблеме.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task.html#add-problem-task
        '''
        return await self.post_data(f'probles/{problem_id}/tasks', input_data)
    
    async def update_task_for_problem(self, problem_id, task_id, input_data):
        '''
        Эта операция поможет вам обновить задачу в проблеме.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task.html#edit-problem-task
        '''
        return await self.put_data(f'problems/{problem_id}/tasks/{task_id}', input_data)
    
    async def delete_task_for_problem(self, problem_id, task_id):
        '''
        Эта операция поможет вам удалить примечание в проблеме.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task.html#delete-problem-task
        '''
        return await self.delete_data(f'problem/{problem_id}/tasks/{task_id}')
    
    # worklog
    async def get_all_worklogs_for_problem_data(self, problem_id):
        '''
        Эта операция поможет вам получить все журналы работ в проблем.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_worklog.html#get-list-problem-worklog
        '''
        return await self.get_data(f'problem/{problem_id}/worklogs')
    
    async def get_worklog_for_problem_data(self, problem_id, worklog_id):
        '''
        Эта операция поможет вам получить журнал работ для проблемы.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_worklog.html#get-problem-worklog
        '''
        return await self.get_data(f'problems/{problem_id}/worklogs/{worklog_id}')
    
    async def add_worklog_for_problem(self, problem_id, input_data):
        '''
        Эта операция поможет вам добавить журнал работ для проблемы.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_worklog.html#add-problem-worklog
        '''
        return await self.post_data(f'problems/{problem_id}/worklogs', input_data)
    
    async def update_worklog_for_problem(self, problem_id, worklog_id, input_data):
        '''
        Эта операция поможет вам обновить журнал работ для проблемы.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_worklog.html#edit-problem-worklog
        '''
        return await self.put_data(f'problems/{problem_id}/worklogs/{worklog_id}', input_data)

    async def delete_worklog_for_problem(self, problem_id, worklog_id):
        '''
        Эта операция поможет вам удалить журнал работ для проблемы.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_worklog.html#delete-problem-worklog
        '''
        return await self.delete_data(f'problems/{problem_id}/worklogs/{worklog_id}')
    
    # task worklog
    async def get_all_task_worklogs_for_problem_data(self, problem_id, task_id):
        '''
        Эта операция поможет вам получить все рабочие журналы задачи lkz проблемы.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task_worklog.html#get-list-problem-task-worklog
        '''
        return await self.get_data(f'problems/{problem_id}/tasks/{task_id}/worklogs')
    
    async def get_task_worklogs_for_problem_data(self, problem_id, task_id, worklog_id):
        '''
        Эта операция поможет вам получить рабочий журнал задачи для проблемы.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task_worklog.html#get-problem-task-worklog
        '''
        return await self.get_data(f'problems/{problem_id}/tasks/{task_id}/worklogs/{worklog_id}')
    
    async def add_task_worklogs_for_problem(self, problem_id, task_id, input_data):
        '''
        Эта операция поможет вам добавить рабочий журнал задачи для проблемы
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task_worklog.html#add-problem-task-worklog
        '''
        return await self.post_data(f'problems/{problem_id}/tasks/{task_id}/worklogs', input_data)
    
    async def update_task_worklogs_for_problem(self, problem_id, task_id, worklog_id, input_data):
        '''
        Эта операция поможет вам обновить рабочий журнал задачи для проблемы.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task_worklog.html#edit-problem-task-worklog
        '''
        return await self.put_data(f'problems/{problem_id}/tasks/{task_id}/worklogs/{worklog_id}', input_data)
    
    async def delete_task_worklogs_for_problem(self, problem_id, task_id, worklog_id):
        '''
        Эта операция поможет вам удалить рабочий журнал задачи для проблемы.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem_task_worklog.html#delete-problem-task-worklog
        '''
        return await self.delete_data(f'problems/{problem_id}/tasks/{task_id}/worklogs/{worklog_id}')
    
    # problem associate
    async def problem_associate_many_requests(self, problem_id, requests_ids):
        '''
        Эта операция помогает связать множество заявок с проблемой, используя problem_id.
        '''
        input_data = {"associated_incidents": [{"request": {"id": req}} for req in requests_ids]}
        return await self.post_data(f'problems/{problem_id}/associated_incidents', input_data)

    async def problem_associate_request(self, problem_id, requests_id):
        '''
        Эта операция поможет вам связать заявку с проблемой, используя problem_id.
        '''
        input_data = {"associated_incident": {"request": {"id": requests_id}}}
        return await self.post_data(f'problems/{problem_id}/associated_incidents', input_data)
    
    async def problem_diassociate_many_requests(self, problem_id, requests_ids):
        '''
        Эта операция поможет вам отменить связь многих инцидентов с проблемой за счет использования problem_id.
        '''
        input_data = {"associated_incidents": [{"request": {"id": req}} for req in requests_ids]}
        return await self.delete_data(f'problems/{problem_id}/associated_incidents', input_data)
    
    async def problem_diassociate_request(self, problem_id, requests_id):
        '''
        Эта операция поможет вам отделить инцидент от проблемы с помощью problem_id.
        '''
        input_data = {"associated_incident": {"request": {"id": requests_id}}}
        return await self.delete_data(f'problems/{problem_id}/associated_incidents', input_data)
    
    async def get_problem_associate_request(self, problem_id):
        '''
        Эта операция поможет вам просмотреть существующие инциденты, связанные с проблемой, используя problem_id
        '''
        return await self.get_data(f'problems/{problem_id}/associated_incidents')

    async def problem_associate_change(self, problem_id, change_id):
        '''
        Эта операция поможет вам связать изменение с проблемой, используя problem_id.
        '''
        input_data = {"associated_change": {"change": {"id": change_id}}}
        return await self.post_data(f'problems/{problem_id}/associated_change', input_data)
    
    async def problem_diassociate_change(self, problem_id, change_id):
        '''
        Эта операция поможет вам связать изменение с проблемой, используя problem_id.
        '''
        input_data = {"associated_change": {"change": {"id": change_id}}}
        return await self.delete_data(f'problems/{problem_id}/associated_change', input_data)
    
    async def get_problem_associate_change(self, problem_id):
        '''
        Эта операция поможет вам просмотреть существующие изменения, связанные с проблемой, с помощью problem_id
        '''
        return await self.get_data(f'problems/{problem_id}/associated_change')
    
    # problem template
    async def get_all_problem_templates_data(self, input_data=None):
        '''
        Эта операция извлекает все шаблоны проблем, доступные в приложении.
        '''
        if not input_data:
            input_data = {"list_info": {"start_index": 1,
                                        "sort_field": "id",
                                        "sort_order": "asc",
                                        "get_total_count": True,
                                        "row_count": 10}}
        return await self.get_data(f'problem_templates', input_data)
    
    async def get_problem_templates_data(self, problem_template_id):
        '''
        Эта операция извлекает сведения о шаблоне проблемы.
        '''
        return await self.get_data(f'problem_templates/{problem_template_id}')
    
    async def add_problem_template(self, input_data):
        '''
        Эта операция позволяет добавить новый шаблон задачи.
        см. input_data в доках к api
        '''
        return await self.post_data(f'problem_templates', input_data)

    async def update_problem_template(self, problem_template_id, input_data):
        '''
        Эта операция позволяет обновить шаблон проблемы.
        см. input_data в доках к api
        '''
        return await self.post_data(f'problem_templates/{problem_template_id}', input_data)
    
    async def delete_problem_template(self, problem_template_id):
        '''
        Эта операция позволяет удалить шаблон проблемы
        '''
        return await self.delete_data(f'problem_templates/{problem_template_id}')
    

    # Тут закончились методы указанные в документациях