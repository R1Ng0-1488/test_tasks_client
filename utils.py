import requests




class TaskApiService:
	url = 'http://localhost:8000'

	@classmethod
	def create_task(cls, task_type, data_):
		try:
			data = {
				'task_type': task_type,
				'data': data_ 
			}
			res = requests.post(cls.url, data=data)
			return res.json()
		except Exception as e:
			return {'Result': False, 'errors': {'server':[str(e)]}}

	@classmethod
	def get_status(cls, task_id):
		try:
			data = {
				'task_id': task_id,
			}
			res = requests.post(f'{cls.url}/get_status/', data=data)
			return res.json()
		except Exception as e:
			return {'Result': False, 'errors': {'server':[str(e)]}}

	@classmethod
	def get_result(cls, task_id):
		try:
			data = {
				'task_id': task_id,
			}
			res = requests.post(f'{cls.url}/get_result/', data=data)
			return res.json()
		except Exception as e:
			return {'Result': False, 'errors': {'server':[str(e)]}}