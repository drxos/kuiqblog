# -*- coding: utf-8 -*-

#=============================================================================
# 
# File : admin.py                                                                         
# Author : Hodonou SOUNTON                            
# Team : drxos, kiah, fall, geolov, sadj
# Site : http://reysh.com                                                       
# Date : 2016-01-07T12:02:38+01:00
# Licence : © Reysh Tech, All Right Reserved.
#                                                                            
#=============================================================================



# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals


# ============================================================================





# Core Django imports
# ----------------------------------------------------------------------------
from django.contrib import admin
from django.contrib.auth.models import Group


# ============================================================================





# Third-party app imports
# ----------------------------------------------------------------------------
from ckeditor.widgets import CKEditorWidget

# ============================================================================





# Imports from our apps
# ----------------------------------------------------------------------------

from .models import Category, Post # Author, Editor



# ============================================================================

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'
	exclude = ['author']	
	prepopulated_fields = {'slug': ('title',)}
	
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()

	def get_queryset(self, request):
		qs = super(PostAdmin, self).get_queryset(request)
		groups = []


		if request.user.is_superuser or request.user.has_perm('is_editor'):
			print(request.user.permissions)			
			return qs


		return qs.filter(author=request.user)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

