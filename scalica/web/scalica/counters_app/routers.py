NUM_LOGICAL_SHARDS = 16
NUM_PHYSICAL_SHARDS = 2 

LOGICAL_TO_PHYSICAL = ( 
  'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2',
  'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2',
)


def logical_to_physical(logical):
  if logical >= NUM_LOGICAL_SHARDS or logical < 0:
    raise Exception("shard out of bounds %d" % logical)
  return LOGICAL_TO_PHYSICAL[logical] 


def logical_shard_for_user(url_hash):
  return url_hash % NUM_LOGICAL_SHARDS

class UserRouter(object):

  def _database_of(self, url_hash):
    return logical_to_physical(logical_shard_for_user(url_hash))

  def _db_for_read_write(self, model, **hints):
    db = None    
    try:
      instance = hints['instance']
      db = self._database_of(instance.url_hash)
    except AttributeError:
      # For the user model the key is id.
      db = self._database_of(instance.id)
    except KeyError:
    	try:
       	   db = self._database_of(int(hints['url_hash']))
        except KeyError:
       	   print "No instance in hints"
    print "Returning", db
    return db

  def db_for_read(self, model, **hints):
    """ """
    return self._db_for_read_write(model, **hints)

  def db_for_write(self, model, **hints):
    """ """
    return self._db_for_read_write(model, **hints)


  def allow_migrate(self, db, app_label, model=None, **hints):
    return True
