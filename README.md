## Общие сведения

Этот модуль умеет работать с REST API Zoho SD Plus Manageengine через модуль aiohttp
Реализовано большая часть возможностей REST API у Zoho SD Plus, а именно:

- **Request**   -  Реализован полностью ✅
- **Problem**  -  Реализован полностью ✅
- **Change**  - Реализован полностью ✅
- **Project**  -  Реализован полностью ✅
- **Release**  -  Не реализован (в разработке) ❌
- **Solutions**  - Реализован полностью ✅
- **Space**  - Не реализован (в разработке) ❌
- **CMDB**  -  Не реализован (в разработке) ❌
- **Contract**  - Реализован полностью ✅
- **Admin**  - Реализован частично (в разработке) ☑️
- **Purchase**  - Не реализован (в разработке) ❌
- **Approvals**  - Реализован полностью ✅
- **Comments**  -  Не реализован (в разработке) ❌
- **Personalization** - Реализован полностью ✅
- **Task**  -  Не реализован (в разработке) ❌
- **Worklog**  -  Не реализован (в разработке) ❌
- **DeviceRegistration**  -  Реализован полностью ✅
- **Asset**  - Реализован полностью ✅
-  **Report**  - Реализован полностью ✅
- **Announcements**  -  Реализован полностью ✅

## Ипользование модуля
```python
import asyncio

from AioZohoSDPlusAPI import Request

sd_conn = Request('TokenKey', 'https://exemple.sd.ru/api/v3')

print(asyncio.run(sd_conn.get_request_data('1000')))
