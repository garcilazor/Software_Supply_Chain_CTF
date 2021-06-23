model_backend = 'sqlite'
#model_backend = 'datastore'

# depending on the intended backend, import the corresponding model file
if model_backend == 'sqlite':
    from .model_sqlite3 import model
elif model_backend == 'datastore':
    from .model_datastore import model
else:
    raise ValueError("No such database backend set up. ")

# initialize the backend model
appmodel = model()

# return the backedend model
def get_model():
	return appmodel

