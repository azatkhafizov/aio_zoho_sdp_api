import os

from .sdp_aio_api_core import SDP

class Request(SDP):
           
    async def add_request(self, input_data):
        '''
        Эта операция используется для добавления новой заявки. 
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#add-request
        '''
        return await self.post_data(f'requests', input_data)
    
    async def update_request(self, request_id, input_data):
        '''
        Эта операция поможет обновить заявки, используя уникальный request_id.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#edit-request
        '''
        return await self.put_data(f'requests/{request_id}', input_data)
    
    async def get_request_data(self, request_id):
        '''
        Эта операция поможет вывести детали заявки по уникальному идентификатору запроса.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-request
        '''
        return await self.get_data(f'requests/{request_id}')
    
    async def get_all_requests_data(self, input_data=None):
        '''
        Эта операция позволяет просмотреть подробную информацию обо всех заявках.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-list-request
        '''
        if input_data:
            return await self.get_data(f'requests', input_data)
        else:
            return await self.get_data(f'requests')
    
    async def get_all_requests_filters(self, 
                                       input_data={"show_all": {"module": "request"},"list_info": {"row_count": "100","search_fields": {"module": "request"}}}):
        '''
        Эта операция позволяет просмотреть все фильтры заявок.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#view-all-request-filters
        '''
        return await self.get_data(f'list_view_filters/show_all', input_data)
    
    async def close_request(self, 
                            request_id: str(), 
                            requester_ack_resolution: bool(), 
                            requester_ack_comments: 
                            str(), closure_comments: 
                            str(), closure_code_name: str()):
        '''
        Эта операция позволяет закрыть заявку. Статус: Close.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#close-request
        '''
        input_data = {
                        "request": {
                            "closure_info": {
                                "requester_ack_resolution": requester_ack_resolution,
                                "requester_ack_comments": requester_ack_comments,
                                "closure_comments": closure_comments,
                                "closure_code": {
                                    "name": closure_code_name
                                }
                            }
                        }
                    }
        return await self.put_data(f'requests/{request_id}/close', input_data)
    
    async def assign_request(self, request_id, input_data):
        '''
        Эта операция позволяет назначить заявку техническому специалисту.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#assign-request
        '''
        return await self.put_data(f'requests/{request_id}/assign', input_data)
    
    async def get_request_resolution(self, request_id):
        '''
        Эта операция позволяет получить разрешение заявки.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-resolution
        '''
        return await self.get_data(f'requests/{request_id}/resolutions')
    
    async def add_request_resolution(self, request_id, resolution_content):
        '''
        Эта операция позволяет вам добавить/обновить решение заявки.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#add-resolution
        '''
        input_data = {"resolution": {"content": resolution_content}}
        return await self.post_data(f'requests/{request_id}/resolutions', input_data)
    
    async def merge_requests(self, request_id, merge_requests_list: list()):
        '''
        Эта опция позволяет объединить несколько заявки. 
        request_id должен быть предполагаемым родительским запросом после слияния.
        '''
        input_data = {"merge_requests": [{'id': req} for req in merge_requests_list]}
        return await self.put_data(f'requests/{request_id}/merge_requests', input_data)
    
    async def get_request_summary(self, request_id):
        '''
        Эта операция позволяет получить сводку заявки.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-request-summary
        '''
        return await self.get_data(f'requests/{request_id}/summary')
    
    async def request_associate_problem(self, request_id, problem_id):
        '''
        Эта операция позволяет связать проблему с заявкой об инциденте.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#associate-problem
        '''
        input_data = {"request_problem_association": {"problem": {"id": str(problem_id)}}}
        return await self.post_data(f'requests/{request_id}/problem', input_data)
    
    async def get_request_associated_problem(self, request_id):
        '''
        Эта операция позволяет получить связанную с заявкой проблемы.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-associated-problem
        '''
        return await self.get_data(f'requests/{request_id}/problem')
    
    async def request_dissociate_problem(self, request_id, problem_id):
        '''
        Эта операция позволяет отделить (уже прикрепленную) проблему от заявки.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#dissociate-problem
        '''
        input_data = {"request_problem_association": {"problem": {"id": str(problem_id)}}}
        return await self.delete_data(f'requests/{request_id}/problem', input_data)
    
    async def request_associate_project(self, request_id, project_id):
        '''
        Эта операция позволяет связать проект с заявкой.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#associate-project
        '''
        input_data = {"request_project_association": {"project": {"id": str(project_id)}}}
        return await self.post_data(f'requests/{request_id}/project', input_data)
    
    async def get_request_associated_project(self, request_id):
        '''
        Эта операция позволяет получить связанный заявки с проектом.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-associated-project
        '''
        return await self.get_data(f'requests/{request_id}/project')
    
    async def request_dissociate_project(self, request_id, project_id):
        '''
        Эта операция позволяет отсоединить (уже прикрепленный) проект от заявки.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#dissociate-project
        '''
        input_data = {"request_project_association": {"project": {"id": str(project_id)}}}
        return await self.delete_data(f'requests/{request_id}/project', input_data)
    
    async def associate_request_initiated_change(self, request_id, change_id):
        '''
        Эта операция позволяет связать изменение, инициированное этой заявкой.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#associate-change-initiated-by-request
        '''
        input_data = {"request_initiated_change": {"project": {"id": str(change_id)}}}
        return await self.post_data(f'requests/{request_id}/request_initiated_change', input_data)
    
    async def get_request_associated_initiated_change(self, request_id):
        '''
        Эта операция позволяет получить связанное изменение, инициированное этой заявкой.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-associated-change-initiated-by-request
        '''
        return await self.get_data(f'requests/{request_id}/request_initiated_change')
    
    async def dissociate_request_initiated_change(self, request_id, change_id):
        '''
        Эта операция позволяет отсоединить (уже прикрепленное) изменение, инициированное запросом, от заявки.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#dissociate-request-initiated-change
        '''
        input_data = {"request_initiated_change": {"project": {"id": str(change_id)}}}
        return await self.delete_data(f'requests/{request_id}/request_initiated_change', input_data)
    
    async def associate_request_caused_by_change(self, request_id, change_id):
        '''
        Эта операция позволяет прикрепить изменение к заявке.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#associate-request-caused-by-change
        '''
        input_data = {"request_caused_by_change": {"project": {"id": str(change_id)}}}
        return await self.post_data(f'requests/{request_id}/request_caused_by_change', input_data)
    
    async def get_request_associated_caused_by_change(self, request_id):
        '''
        Эта операция позволяет получить соответствующее изменение к заявке.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-associated-request-caused-by-change
        '''
        return await self.get_data(f'requests/{request_id}/request_caused_by_change')
    
    async def dissociate_request_caused_by_change(self, request_id, change_id):
        '''
        Эта операция позволяет отсоединить (уже прикрепленный) запрос, вызванный изменением заявкой
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#dissociate-request-caused-by-change
        '''
        input_data = {"request_caused_by_change": {"project": {"id": str(change_id)}}}
        return await self.delete_data(f'requests/{request_id}/request_caused_by_change', input_data)
    
    async def delete_request_to_trash(self, request_id):
        '''
        Эта операция позволяет удалить (переместить в корзину) заявку.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#delete-request
        '''
        return await self.delete_data(f'requests/{request_id}/move_to_trash')
    
    async def delete_request_from_trash(self, request_id):
        '''
        Эта операция позволяет удалить заявку навсегда (из корзины).
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#delete-request-from-trash
        '''
        return await self.delete_data(f'requests/{request_id}')
    
    async def restore_request_from_trash(self, request_id):
        '''
        Эта операция позволяет восстановить заявку из корзины.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#restore-request-from-trash
        '''
        return await self.put_data(f'requests/{request_id}/restore_from_trash')
    
    async def add_tags_in_request(self, request_id, tags_ids: list()):
        '''
        Эта операция позволяет связать теги с заявкой.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#add-tags-in-request
        '''
        input_data = {"tags": [{'id': tid} for tid in tags_ids]}
        return await self.put_data(f'requests/{request_id}/tag', input_data)

    async def add_request_attachment(self, file_path):
        '''
        Эта операция используется для загрузки вложения к заявке.        
        '''
        return await self.send_file(file_path, f'requests/upload', http_method='post')
    
    async def add_request_attachment_and_associate(self, request_id, file_path):
        '''
        Эта операция используется для добавления и связывания вложения с заявкой.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html#add-attachment-to-a-request
        '''
        return await self.send_file(file_path, f'requests/{request_id}/upload', http_method='put')
    
    async def get_request_attachments_list(self, request_id):
        '''
        Эта операция используется для получения всех вложений, присутствующих в заявке.
        '''
        return await self.get_data(f'requests/{request_id}/attachments')

    async def download_request_attachment(self, request_id, attachment_id, saved_file_patch=os.getcwd()):
        '''
        Эта операция используется для скачивания определенного вложения, присутствующего в заявке.
        '''
        attachment_file_list = await self.get_request_attachments_list(request_id)
        file_name = 'file'
        for at in attachment_file_list['attachments']:
            if at['id'] == str(attachment_id):
                file_name = at['name']
        content_data = await self.get_content_data(f'requests/{request_id}/attachments/{attachment_id}/download')
        with open(os.path.join(saved_file_patch, file_name), 'wb') as file:
            file.write(content_data)
        return {"saved_in": saved_file_patch}

    async def delete_request_attachment(self, request_id, attachment_id):
        '''
        Эта операция используется для удаления вложения в заявке.
        '''
        return await self.delete_data(f'requests/{request_id}/attachments/{attachment_id}')

    async def link_requests(self, request_id, input_data):
        '''
        Привязывает к request_id заявки из input_data
        Пример для input_data:
            {link_requests": [{"linked_request": {"id": "1","comments": "Какой то коммент"}]}

        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#link-requests
        '''
        return await self.post_data(f'requests/{request_id}/link_requests', input_data)
    
    async def unlink_requests(self, request_id, input_data):
        '''
        Удаляет связб у request_id к заявкам из input_data
        Пример для input_data:
            {"link_requests": [{"linked_request": {"id": "1"}}]}

        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#unlink-requests
        '''
        return await self.delete_data(f'requests/{request_id}/link_requests', input_data)
    
    async def get_all_link_requests(self, request_id):
        '''
        Эта операция помогает получить все связанные заявки в рамках заявки.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/request.html#get-all-link-requests
        '''
        return await self.get_data(f'requests/{request_id}/link_requests')

    async  def add_note_attachment_for_request(self, request_id, file_path):
        '''
        Эта операция используется для загрузки вложения для примечания в заявке.
        '''
        return await self.send_file(file_path, f'requests/{request_id}/notes/upload')
    
    async  def add_note_attachment_for_request_and_associate(self, request_id, note_id, file_path):
        '''
        Эта операция используется для загрузки вложения к примечанию.
        '''
        return await self.send_file(file_path, f'requests/{request_id}/notes/{note_id}/upload')
    
    async def get_note_attachment_for_request(self, request_id, note_id):
        '''
        Эта операция используется для извлечения всех вложений, присутствующих в примечании.
        '''
        return await self.get_data(f'requests/{request_id}/notes/{note_id}/attachments')
    
    async def delete_note_attachment_for_request(self, request_id, note_id, attachment_id):
        '''
        Эта операция используется для удаления вложения в примечании.
        '''
        return await self.delete_data(f'requests/{request_id}/notes/{note_id}/attachments/{attachment_id}')

    async def download_note_attachment_for_request(self, request_id, note_id, attachment_id, saved_file_patch=os.getcwd()):
        '''
        Эта операция используется для скачивания определенного вложения, присутствующего в примечании.
        '''
        attachment_file_list = await self.get_note_attachment_for_request(request_id, note_id)
        file_name = 'file'
        for at in attachment_file_list['attachments']:
            if at['id'] == str(attachment_id):
                file_name = at['name']
        content_data = await self.get_content_data(f'requests/{request_id}/notes/{note_id}/attachments/{attachment_id}/download')
        with open(os.path.join(saved_file_patch, file_name), 'wb') as file:
            file.write(content_data)
        return {"saved_in": saved_file_patch}

    async def add_request_note(self, request_id, message, show_to_requester: bool, attachments_paths: list = None):
        '''
        Эта операция добавляет примечание.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_note.html#add-request-note
        '''
        attachments = list()
        if attachments_paths:
            for attachment_path in attachments_paths:
                send_file_res = await self.send_file(attachment_path, f'requests/{request_id}/notes/upload')
                if 'attachment' in send_file_res.keys():
                    attachments.append({'id': str(send_file_res['attachment']['id'])})
        input_data = {"note":{"description": message,
                              "notify_technician": True,
                              "show_to_requester": show_to_requester,
                              "mark_first_response": False,
                              "attachments": attachments}}
        return await self.post_data(f'requests/{request_id}/notes', input_data)
    
    async def update_request_note(self, request_id, note_id, message, show_to_requester: bool):
        '''
        Эта операция обновляет примечание.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_note.html#edit-request-note
        '''
        input_data = {"note": {"description": message,
                               "show_to_requester": show_to_requester}}
        return await self.put_data(f'requests/{request_id}/notes/{note_id}', input_data)
    
    async def get_request_note_data(self, request_id, note_id):
        '''
        Эта операция получает информацию о примечании.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_note.html#get-request-note
        '''
        return await self.get_data(f'requests/{request_id}/notes/{note_id}')
    
    async def get_request_all_notes_data(self, request_id, input_data=None):
        '''
        Эта операция получает все примечания.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_note.html#get-list-request-note
        '''
        if input_data:
            return await self.get_data(f'requests/{request_id}/notes', input_data)
        else:
            return await self.get_data(f'requests/{request_id}/notes')

    async def delete_request_note(self, request_id, note_id):
        '''
        Эта операция удаляет примечание.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_note.html#delete-request-note
        '''
        return await self.delete_data(f'requests/{request_id}/notes/{note_id}')

    async def request_draw_save_as_draft(self, request_id, input_data):
        '''
        Эта операция позволяет сохранить содержимое уведомления по электронной почте как черновик в заявке.
        '''
        return await self.post_data(f'requests/{request_id}/drafts', input_data)

    async def get_request_draw_data(self, request_id, draft_id):
        '''
        Эта операция позволяет получить содержимое существующего черновика заявки по электронной почте.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/draft.html#get-draft
        '''
        return await self.get_data(f'requests/{request_id}/drafts/{draft_id}')
    
    async def get_request_all_draw_data(self, request_id):
        '''
        Эта операция позволяет получить все черновики, имеющиеся по заявке.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/draft.html#get-list-draft
        '''
        return await self.get_data(f'requests/{request_id}/drafts')
    
    async def delete_request_draw_data(self, request_id, draft_id):
        '''
        Эта операция позволяет удалить черновик заявки.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/requests/draft.html#delete-draft
        '''
        return await self.delete_data(f'requests/{request_id}/drafts/{draft_id}')
    
    async def get_request_notification_data(self, request_id, notification_id):
        '''
        Эта операция позволяет просмотреть сведения об одном уведомлении в заявке.
        '''
        return await self.get_data(f'requests/{request_id}/notifications/{notification_id}')
    
    async def get_request_all_notification_data(self, request_id):
        '''
        Эта операция позволяет просмотреть подробную информацию обо всем уведомлении в заявке.
        '''
        return await self.get_data(f'requests/{request_id}/notifications')

    async def get_request_all_conversations_data(self, request_id, input_data=None):
        '''
        Эта операция позволяет просмотреть подробную информацию обо всех разговорах в заявке.
        '''
        if not input_data:
            input_data = {"list_info": {
                                        "start_index": 1,
                                        "sort_order": "desc",
                                        "row_count": 500},
                          "notes": True}
        return await self.get_data(f'requests/{request_id}/conversations')

    async  def add_notification_attachment_for_request(self, request_id, file_path):
        '''
        Эта операция используется для загрузки вложения для уведомления.
        '''
        return await self.send_file(file_path, f'requests/{request_id}/notifications/upload')

    async def download_notification_attachment_for_request(self, request_id, notification_id, attachment_id, saved_file_patch=os.getcwd()):
        '''
        Эта операция используется для скачивания определенного вложения, присутствующего в уведомлении.
        '''
        attachment_file_list = await self.get_request_notification_data(request_id, notification_id)
        file_name = 'file'
        for at in attachment_file_list['notification']['attachments']:
            if at['id'] == str(attachment_id):
                file_name = at['name']
        content_data = await self.get_content_data(f'requests/{request_id}/notifications/{notification_id}/attachments/{attachment_id}/download')
        with open(os.path.join(saved_file_patch, file_name), 'wb') as file:
            file.write(content_data)
        return {"saved_in": saved_file_patch}

    async def add_request_notification(self, request_id, message, attachments_paths: list = None):
        '''
        Эта операция позволяет добавить уведомление по заявке.
         С attachments_paths аботает, уведомление приходит на почту, в SDP не отображается, нужно разобраться
        '''
        input_data = {"notification":{"description":message,
                                      "subject":f"Re: [Request ID :##RE-{request_id}##] : {request_data['request']['subject']}",
                                      "content_type":"text/html",
                                      "type":"reply",
                                      "mode":"E-Mail",
                                      "to":[{"email_id": request_data['request']['requester']['email_id']}],
                                      "cc":[],
                                      "bcc":[],
                                      "copied_from":{"module":"request","id":str(request_id)}}}
        request_data = await self.get_request_data(request_id)
        attachments = list()
        if attachments_paths:
            input_data["attachments"] = attachments
            for attachment_path in attachments_paths:
                send_file_res = await self.add_notification_attachment_for_request(request_id, attachment_path)
                if 'attachment' in send_file_res.keys():
                    attachments.append({'id': str(send_file_res['attachment']['id'])})
        return await self.post_data(f'requests/{request_id}/notifications', input_data)

    async def get_request_template_data(self, template_id):
        '''
        Эта операция позволяет просмотреть подробную информацию о шаблоне заявки.
        '''
        return await self.get_data(f'request_templates/{template_id}')

    async def get_requests_template_data(self, input_data=None, is_incedent_template=False):
        '''
        Эта операция позволяет получить список всех шаблонов в приложении. 
        Это предоставит базовый набор информации о шаблоне. 
        Он не будет предоставлять поля, свойства полей и детали макета.
        Если указать is_incedent_template=True, то выдаст ифнфорацию о инцедентах, иначе о услугах
        '''
        if not input_data:
            input_data = {"list_info": {"sort_field": "name"}}
            input_data["list_info"]["search_fields"] = {"is_service_template": is_incedent_template}
        return await self.get_data(f'request_templates', input_data)
    
    async  def add_request_approval_level(self, request_id, approval_level: int()):
        '''
        Эта операция добавляет уровень утверждения заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval_level.html#add-request-approval-level
        '''
        input_data = {"approval_level": {"level": approval_level}}
        return await self.post_data(f'requests/{request_id}/approval_levels', input_data)
    
    async def get_request_approval_level_data(self, request_id, approval_level_id):
        '''
        Эта операция получает уровень одобрения заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval_level.html#get-request-approval-level
        '''
        return await self.get_data(f'requests/{request_id}/approval_levels/{approval_level_id}')

    async def get_all_request_approval_levels_data(self, request_id, input_data=None):
        '''
        Эта операция поможет вам получить все уровни утверждения заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval_level.html#get-list-request-approval-level
        '''
        if not input_data:
            input_data = {"list_info":{"row_count":"100","start_index":"1","sort_field":"created_time","sort_order":"desc"}}
        return await self.get_data(f'requests/{request_id}/approval_levels', input_data)
        
    async def delete_request_approval_level(self, request_id, approval_level_id):
        '''
        Эта операция поможет вам удалить уровень утверждения заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval_level.html#delete-request-approval-level
        '''
        return await self.delete_data(f'requests/{request_id}/approval_levels/{approval_level_id}')

    async  def add_request_approval(self, request_id, approval_level_id, input_data):
        '''
        Эта операция поможет вам добавить утверждение заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval_level.html#add-request-approval-level
        '''
        return await self.post_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals', input_data)
    
    async def get_request_all_approvals_data(self, request_id, approval_level_id):
        '''
        Эта операция поможет вам получить все утверждения заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval.html#get-list-request-approval
        '''
        return await self.get_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals')

    async def get_request_approval_data(self, request_id, approval_level_id, approval_id):
        '''
        Эта операция поможет вам получить одобрение заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval.html#get-request-approval
        '''
        return await self.get_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals/{approval_id}')
    
    async def delete_request_approval(self, request_id, approval_level_id, approval_id):
        '''
        Эта операция поможет вам получить одобрение заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval.html#get-request-approval
        '''
        return await self.delete_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals/{approval_id}')
    
    async def approve_request_approval(self, request_id, approval_level_id, approval_id, comments):
        '''
        Эта операция поможет вам утвердить утверждение заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval.html#approve-request-approval
        '''
        input_data={"approval": {"comments": comments}}
        return await self.put_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/approve', input_data)
    
    async def get_notification_content_for_sending_request_approva(self, request_id, approval_level_id, approval_id):
        '''
        Эта операция поможет вам получить содержимое уведомления для отправки утверждения заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval.html#get-notification-content-for-sending-request-approval
        '''
        return await self.get_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/send_notification')
    
    async def send_notification_for_request_approval(self,request_id, approval_level_id, approval_id, subject, description):
        '''
        Эта операция поможет вам отправить уведомление для утверждения заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval.html#send-notification-for-request-approval
        '''
        input_data = {"notification": {"subject": subject, "description": description}}
        return await self.put_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/send_notification', input_data)
    
    async def reject_request_approval(self, request_id, approval_level_id, approval_id, comments):
        '''
        Эта операция поможет вам отклонить утверждение заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_approval.html#reject-request-approval
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/reject', input_data)
    
    async def add_request_task(self, request_id, input_data):
        '''
        Эта операция поможет вам добавить задачу заявки. 
        Обязательные поля: - title
        см. документацию для input_data
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task.html#add-request-task
        '''
        return await self.post_data(f'requests/{request_id}/tasks', input_data)
    
    async def update_request_task(self, request_id, task_id, input_data):
        '''
        Эта операция поможет вам выполнить задачу для запроса.
        см. документацию для input_data
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task.html#add-request-task
        '''
        return await self.put_data(f'requests/{request_id}/tasks/{task_id}', input_data)

    async def get_request_task_data(self, request_id, task_id):
        '''
        Эта операция поможет вам получить задачу заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task.html#get-request-task
        '''
        return await self.get_data(f'requests/{request_id}/tasks/{task_id}')
    
    async def get_all_tequest_tasks_data(self, request_id, input_data=None):
        '''
        Эта операция поможет вам получить все задачи заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task.html#get-list-request-task
        '''
        if not input_data:
            input_data = {"list_info":{"row_count":"100","start_index":"1","sort_field":"created_time","sort_order":"desc"}}
        return await self.get_data(f'requests/{request_id}/tasks', input_data)
    
    async def delete_request_task(self, request_id, task_id):
        '''
        Эта операция поможет вам удалить задачу заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task.html#delete-request-task
        '''
        return await self.delete_data(f'requests/{request_id}/tasks/{task_id}')
    
    async def add_attachment_to_request_task(self, request_id, task_id, file_path):
        '''
        Эта операция поможет вам добавить вложение к задаче заявки. 
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task.html#add-attachment-to-a-request-task
        '''
        return await self.send_file(file_path, f'requests/{request_id}/tasks/{task_id}/uploads')

    async def add_request_worklog(self, request_id, input_data):
        '''
        Эта операция поможет вам добавить данные в журнал работ заявки.
        см. документацию для input_data
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_worklog.html#add-request-worklog
        '''
        return await self.post_data(f'requests/{request_id}/worklogs', input_data)

    async def update_request_worklog(self, request_id, worklog_id, input_data):
        '''
        Эта операция поможет вам обновить журнал работ для заявки.
        см. документацию для input_data
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_worklog.html#edit-request-worklog
        '''
        return await self.put_data(f'requests/{request_id}/worklogs/{worklog_id}', input_data)
    
    async def get_request_worklog(self, request_id, worklog_id):
        '''
        Эта операция поможет вам получить журнал работ для заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_worklog.html#get-request-worklog

        '''
        return await self.get_data(f'requests/{request_id}/worklogs/{worklog_id}')
    
    async def get_request_all_worklogs(self, request_id, input_data=None):
        '''
        Эта операция поможет вам получить все журналы работ для заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_worklog.html#get-list-request-worklog
        '''
        if not input_data:
            input_data = {"list_info":{"row_count":"100","start_index":"1","sort_field":"created_time","sort_order":"desc"}}
        return await self.get_data(f'requests/{request_id}/worklogs')
    
    async def delete_request_worklog(self, request_id, worklog_id):
        '''
        Эта операция поможет вам удалить журнал работ для заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_worklog.html#delete-request-worklog
        '''
        return await self.delete_data(f'requests/{request_id}/worklogs/{worklog_id}')
    
    async def add_request_task_worklog(self, request_id, task_id, input_data):
        '''
        Эта операция поможет вам добавить журнал работ для задачи заявки.
        см. документацию для input_data
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task_worklog.html#add-request-task-worklog
        '''
        return await self.post_data(f'requests/{request_id}/tasks/{task_id}/worklogs', input_data)
    
    async def update_request_task_worklog(self, request_id, task_id, worklog_id, input_data):
        '''
        Эта операция поможет вам обновить журнал работ для задачи заявки.
        см. документацию для input_data
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task_worklog.html#edit-request-task-worklog
        '''
        return await self.put_data(f'requests/{request_id}/tasks/{task_id}/worklogs/{worklog_id}', input_data)
    
    async def get_request_task_worklog_data(self, request_id, task_id, worklog_id):
        '''
        Эта операция поможет вам получить журнал работ для задачи заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task_worklog.html#get-request-task-worklog
        '''
        return await self.get_data(f'requests/{request_id}/tasks/{task_id}/worklogs/{worklog_id}')
    
    async def get_request_task_all_worklogs_data(self, request_id, task_id, input_data=None):
        '''
        Эта операция поможет вам получить все журналы работ для задачи заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task_worklog.html#get-list-request-task-worklog
        '''
        if not input_data:
            input_data = {"list_info":{"row_count":"100","start_index":"1","sort_field":"created_time","sort_order":"desc"}}
        return await self.get_data(f'requests/{request_id}/tasks/{task_id}/worklogs')

    async def delete_request_task_worklog(self, request_id, task_id, worklog_id):
        '''
        Эта операция поможет вам удалить журнал работ для задачи заявки.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request_task_worklog.html#delete-request-task-worklog
        '''
        return await self.delete_data(f'requests/{request_id}/tasks/{task_id}/worklogs/{worklog_id}')

    # Тут закончились методы указанные в документациях

    async def ropen_request(self, request_id):
        '''
        Предназначена для переоткрытия заявки
        '''
        input_data = {"request":{"status":{"id":"6"}}} # "In Progress"
        return await self.update_request(request_id, input_data)
    
        
    async def get_request_detail(self, request_id):
        '''
        Дает детальную информацию о заявке
        '''
        input_data = {"includes":["request_template",
                                  "metainfo",
                                  "self_service_portal",
                                  "status","_links",
                                  "priority_matrices",
                                  "csi_model",
                                  "get_connected_nodes",
                                  "status_mandatory_fields",
                                  "techs_on_leave"]}
        return await self.get_data(f'requests/{request_id}/request_detail', input_data)
