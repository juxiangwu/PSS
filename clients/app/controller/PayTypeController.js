Ext.define('PSS.controller.PayTypeController',{
	add:function(datas,callback){
		Ext.Ajax.request({
			url:require('./config.json').host + '/add_paytype',
			method:'POST',
			params:datas,
			success:function(response,opts){
				if(callback){
					callback(JSON.parse(response.responseText));
				}
			},
			failure:function(response,opts){
				Ext.Msg.alert('添加支付方式','网络错误');
			}
		});
	},
	remove:function(datas,callback){
		Ext.Ajax.request({
			url:require('./config.json').host + '/remove_paytype',
			method:'POST',
			params:datas,
			success:function(response,opts){
				if(callback){
					callback(JSON.parse(response.responseText));
				}
			},
			failure:function(response,opts){
				Ext.Msg.alert('删除支付方式','网络错误');
			}
		});
	},
	update:function(datas,callback){
		Ext.Ajax.request({
			url:require('./config.json').host + '/update_paytype',
			method:'POST',
			params:datas,
			success:function(response,opts){
				if(callback){
					callback(JSON.parse(response.responseText));
				}
			},
			failure:function(response,opts){
				Ext.Msg.alert('更新支付方式','网络错误');
			}
		});
	}
});