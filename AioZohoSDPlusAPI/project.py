import os

from .sdp_aio_api_core import SDP

class Project(SDP):

    # project
    async def get_all_poject_data(self, input_data=None):
        '''
        Просмотреть все проекты
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return await self.get_data(f'projects', input_data)
    
    async def get_project_data(self, project_id):
        '''
        Просмотреть данные об проектке
        '''
        return await self.get_data(f'projects/{project_id}')
    
    async def add_project(self, input_data):
        '''
        Добвить проект
        input_data см. в доках к API
        '''
        return await self.post_data(f'projects', input_data)
    
    async def update_project(self, project_id, input_data):
        '''
        Изменить проект
        input_data см. в доках к API
        '''
        return await self.put_data(f'projects/{project_id}', input_data)
    
    async def delete_project(self, project_id):
        '''
        Удалить проект
        '''
        return await self.put_data(f'projects/{project_id}')
    
    # milestone
    async def get_all_milestones_data(self, project_id, input_data=None):
        '''
        Просмотреть все ключевые этапы проекта
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return await self.get_data(f'projects/{project_id}/milestones', input_data)
    
    async def get_milestone_data(self, project_id, milestone_id):
        '''
        Просмотреть данные об ключевом этапе проекта
        '''
        return await self.get_data(f'projects/{project_id}/milestones/{milestone_id}')
    
    async def add_milestone(self, project_id, input_data):
        '''
        Добвить ключевой этап для проекта
        input_data см. в доках к API
        '''
        return await self.post_data(f'projects/{project_id}/milestones/', input_data)
    
    async def update_milestone(self, project_id, milestone_id, input_data):
        '''
        Изменить ключевой этап проекта
        input_data см. в доках к API
        '''
        return await self.put_data(f'projects/{project_id}/milestones/{milestone_id}', input_data)
    
    async def delete_milestone(self, project_id, milestone_id):
        '''
        Удалить ключевой этап проекта
        '''
        return await self.put_data(f'projects/{project_id}/milestones/{milestone_id}')
    
    async def milestone_assign_owner_for_project(self, project_id, milestone_id, owner_id):
        '''
        Эта операция назначает владельца для ключевого этапа
        '''
        input_data = {"milestone": {"owner": {"id": str(owner_id)}}}
        return await self.put_data(f'projects/{project_id}/milestones/{milestone_id}', input_data)
    
    async def get_project_milestone_attachments_data(self, project_id, milestone_id):
        '''
        Эта операция используется для извлечения всех вложений, присутствующих в ключевом этапе
        '''
        return await self.get_data(f'projects/{project_id}/milestones/{milestone_id}/attachments')
    
    async def download_project_milestone_attachments(self, project_id, milestone_id, attachment_id, saved_file_patch=os.getcwd()):
        '''
        Эта операция используется для загрузки определенного вложения, присутствующего в ключевом этапе. 
        '''
        attachment_file_list = await self.get_project_milestone_attachments_data(project_id, milestone_id)
        file_name = 'file'
        for at in attachment_file_list['attachments']:
            if at['id'] == str(attachment_id):
                file_name = at['name']
        content_data = await self.get_content_data(f'requests/{project_id}/notes/{milestone_id}/attachments/{attachment_id}/download')
        with open(os.path.join(saved_file_patch, file_name), 'wb') as file:
            file.write(content_data)
        return {"saved_in": saved_file_patch}

    async def add_project_milestone_attachments_and_associate(self, project_id, milestone_id, file_path):
        '''
        Эта операция используется для загрузки вложения к проекту и ассациировать
        '''
        return await self.send_file(file_path, f'projects/{project_id}/milestones/{milestone_id}/_upload')
    
    async def add_project_milestone_attachments(self, project_id, file_path):
        '''
        Эта операция используется для загрузки вложения к ключевому этапу.
        '''
        return await self.send_file(file_path, f'projects/{project_id}/milestones/upload')
    
    async def add_and_associate_project_milestone_attachments(self, project_id, milestone_id, file_path):
        '''
        Эта операция используется для добавления и связывания вложения с ключевым этапом
        '''
        return await self.send_file(file_path, f'projects/{project_id}/milestones/{milestone_id}/_upload', 'put')
    
    async def delete_project_milestone_attachments(self, project_id, milestone_id, attachment_id):
        '''
        Эта операция используется для удаления вложения в ключевом этапе
        '''
        return await self.delete_data(f'projects/{project_id}/milestones/{milestone_id}/attachments/{attachment_id}')
    
    # project members   
    async def get_all_project_members(self, project_id):
        '''
        Эта операция позволяет просмотреть всех участников, связанных с проектом.
        '''
        return await self.get_data(f'projects/{project_id}/members')

    async def add_project_members(self, project_id, user_id, role_id, is_active:bool=True):
        '''
        Добвить участников в проект
        '''
        input_data = {"member": {"user": {"id": str(user_id)},
                      "role": {"id": str(role_id)},
                      "is_active": is_active}}
        return await self.post_data(f'projects/{project_id}/members', input_data)
    
    async def update_project_member(self, project_id, member_id, input_data):
        '''
        Эта операция позволяет обновить сведения об участнике проекта. 
        input_data см. в доках к API
        '''
        return await self.put_data(f'projects/{project_id}/members/{member_id}', input_data)
    
    async def delete_project_member(self, project_id, member_id):
        '''
        Эта операция удаляет/отсоединяет участника от проекта.
        '''
        return await self.put_data(f'projects/{project_id}/members/{member_id}')
    
    # project attachment
    async def get_project_attachment_data(self, project_id):
        '''
        Эта операция используется для извлечения всех вложений, присутствующих в проекте.
        '''
        return await self.put_data(f'projects/{project_id}/attachments')

    async def add_project_attachment(self, file_path):
        '''
        Эта операция используется для загрузки вложения в проект.
        '''
        return await self.send_file(file_path, f'projects/_upload')
    
    async def add_project_attachment(self, project_id, file_path):
        '''
        Эта операция используется для загрузки вложения в проект и асациировать
        '''
        return await self.send_file(file_path, f'projects/{project_id}/_upload')
    
    async def download_project_attachment(self, project_id, attachment_id, saved_file_patch=os.getcwd()):
        '''
        Эта операция используется для загрузки определенного вложения, присутствующего в ключевом этапе. 
        '''
        attachment_file_list = await self.get_project_attachment_data(project_id)
        file_name = 'file'
        for at in attachment_file_list['attachments']:
            if at['id'] == str(attachment_id):
                file_name = at['name']
        content_data = await self.get_content_data(f'projects/{project_id}/attachments/{attachment_id}/_download')
        with open(os.path.join(saved_file_patch, file_name), 'wb') as file:
            file.write(content_data)
        return {"saved_in": saved_file_patch}
    
    async def delete_project_attachment(self, project_id, attachment_id):
        '''
        Эта операция используется для удаления вложения в проекте
        '''
        return await self.delete_data(f'projects/{project_id}/attachments/{attachment_id}')\
    
    # Тут закончились методы указанные в документациях