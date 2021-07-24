# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .Model import Model
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.
    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]
    This returns:
        [ x, y, message ]
    where message is a Python string and x and y are Python integers
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [int(entity['x']),int(entity['y']),entity['message']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cs430p-f20-caspar-chil-cchilds')

    # returns entries in GCP database
    def select(self):
        query = self.client.query(kind = 'Flags')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    # inserts a new entry into the GCP database
    def insert(self, x, y, message):
        """
        Inserts entry into database
        :param x: Int
        :param y: Int
        :param message: String
        :return: True
        """

        # generate GCP datastore entity
        key = self.client.key('Flags')
        rev = datastore.Entity(key)

        # fill entity with data from arguments
        rev.update( {
            'x': x,
            'y': y,
            'message': message
            })

        #insert entity into GCP datastore
        self.client.put(rev)
        return True
