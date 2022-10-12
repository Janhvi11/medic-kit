from django.urls import path
from ..views import *

chat_url = [
    path("viewChat/",chatView,name="view-chat"),
    path("addChat/",chatAdd,name="add-chat"),
    path("deleteChat/<int:id>",chatDelete,name="delete-chat"),
    path("editChat/<int:id>",chatEdit,name="edit-chat"),
]