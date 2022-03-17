from django.contrib import admin


class CustAdmin(admin.ModelAdmin):
    list_display = ('custno', 'id', 'password', 'name', 'address', 'email', 'regdate')


class CategoriAdmin(admin.ModelAdmin):
    list_display = ('cid', 'categoriname')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('foodid', 'name', 'price', 'regdate')


class MarketAdmin(admin.ModelAdmin):
    list_display = ('marketno', 'cid', 'foodid', 'marketname', 'marketaddress', 'regdate',
                    'open', 'close', 'holiday', 'hit')


class CeoAdmin(admin.ModelAdmin):
    list_display = ('ceoid', 'seochono', 'id', 'password', 'name')


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('replyid', 'reviewno', 'seochono','ceoid', 'pcontent', 'regdate')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewno', 'seochono', 'custno', 'content', 'star', 'regdate')


class SeochoAdmin(admin.ModelAdmin):
    list_display = ('marketno', 'marketname', 'ceoname', 'address', 'phone', 'categori', 'food', 'open', 'close')


class SeochofoodAdmin(admin.ModelAdmin):
    list_display = ('foodid', 'marketno', 'name', 'price')

