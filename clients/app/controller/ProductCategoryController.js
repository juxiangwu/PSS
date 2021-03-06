Ext.define('PSS.controller.ProductCategoryController',{
	add:function(datas,callback){
		var config = require('./config.json')

		Ext.Ajax.request({
			url:config.host+'/add_category',
			method:'POST',
			params:datas,
			success:function(response,opts){
				if(callback){
					callback(JSON.parse(response.responseText))
				}
			},
			failure:function(response,opts){
				Ext.Msg.alert('添加商品分类','网络错误')
			}
		});
	},
	remove:function(datas,callback){
		var config = require('./config.json');
		Ext.Ajax.request({
			url:config.host+'/remove_category',
			method:'POST',
			params:datas,
			success:function(response,opts){
				if(callback){
					callback(JSON.parse(response.responseText))
				}
			},
			failure:function(response,opts){
				Ext.Msg.alert('删除商品分类','网络错误');
			}
		});
	},
	update:function(datas,callback){
		var config = require('./config.json');
		Ext.Ajax.request({
			url:config.host+'/update_category',
			method:'POST',
			params:datas,
			success:function(response,opts){
				if(callback){
					callback(JSON.parse(response.responseText));
				}
			},
			failure:function(response,opts){
				Ext.Msg.alert('更新商品分类','网络错误');
			}
		});
	}
})