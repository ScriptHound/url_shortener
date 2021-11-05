import tarantool

connection = tarantool.connect('localhost', 3301, password='pass', user='admin')
connection.call('box.schema.space.create', ("urls",))

space_format = {
    {"name": 'id', "type": 'unsigned'},
    {"name": 'link', "type": 'string'}}
connection.call("my_space:format", {"format": space_format})
connection.call(
    "box.schema.sequence.create",
    ('id_seq', {"start": 1, "min": 1}))
connection.call("box.space.urls:create_index", ('id_idx', {"sequence": 'id_seq'}))

