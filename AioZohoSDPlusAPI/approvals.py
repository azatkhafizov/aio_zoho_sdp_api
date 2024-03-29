from .sdp_aio_api_core import SDP

class Approvals(SDP):

    async def get_all_approvals_data(self, input_data):
        '''
        Получить все согласования
        см. input_data в доках к api
        '''
        return await self.get_data(f'approvals', input_data)
    
    # approve
    async def approve_request(self, request_id, approval_level_id, approval_id, comments):
        '''
        Согласовать заявку
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/approve', input_data)
    
    async def approve_purchase_requests(self, purchase_requests_id, approval_level_id, approval_id, comments):
        '''
        Согласовать заявку на закуп
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'purchase_requests/{purchase_requests_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/approve', input_data)
    
    async def approve_change(self, change_id, approval_level_id, approval_id, comments):
        '''
        Согласовать заявку
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'changes/{change_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/approve', input_data)
    
    async def approve_purchase_orders(self, purchase_orders_id, approval_level_id, approval_id, comments):
        '''
        Согласовать заказ на закуп
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'purchase_orders/{purchase_orders_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/approve', input_data)
    
    # reject
    async def approve_request(self, request_id, approval_level_id, approval_id, comments):
        '''
        Согласовать заявку
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'requests/{request_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/reject', input_data)
    
    async def approve_purchase_requests(self, purchase_requests_id, approval_level_id, approval_id, comments):
        '''
        Согласовать заявку на закуп
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'purchase_requests/{purchase_requests_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/reject', input_data)
    
    async def approve_change(self, change_id, approval_level_id, approval_id, comments):
        '''
        Согласовать заявку
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'changes/{change_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/reject', input_data)
    
    async def approve_purchase_orders(self, purchase_orders_id, approval_level_id, approval_id, comments):
        '''
        Согласовать заказ на закуп
        '''
        input_data = {"approval": {"comments": comments}}
        return await self.put_data(f'purchase_orders/{purchase_orders_id}/approval_levels/{approval_level_id}/approvals/{approval_id}/reject', input_data)
    
    # Тут закончились методы указанные в документациях