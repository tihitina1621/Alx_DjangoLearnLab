from django.shortcuts import render
from django.contrib.auth.models import User, Permission
from .forms import ExampleForm


"book_list",  "books"
@permission_required('bookshelf.can_edit', raise_exception=True)
@permission_required('bookshelf.can_create', raise_exception=True)