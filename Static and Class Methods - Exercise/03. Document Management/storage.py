from project.topic import Topic
from project.category import Category
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for el in self.categories:
            if el.id == category_id:
                el.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for el in self.topics:
            if el.id == topic_id:
                el.topic = new_topic
                el.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        for el in self.documents:
            if el.id == document_id:
                el.file_name = new_file_name

    def delete_category(self, category_id):
        for el in self.categories:
            if el.id == category_id:
                self.categories.remove(el)

    def delete_topic(self, topic_id):
        for el in self.topics:
            if el.id == topic_id:
                self.topics.remove(el)

    def delete_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                self.documents.remove(el)

    def get_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                return el.__repr__()

    def __repr__(self):
        result = []
        for el in self.documents:
            result.append(el.__repr__())
        return "\n".join(result)


from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)


